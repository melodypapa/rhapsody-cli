"""PackageCreateAction — split from package_action.py."""

import argparse
import logging
from typing import Dict, List, cast

from rhapsody_cli.actions.package.base import AbstractPackageAction
from rhapsody_cli.actions.support import apply_stereotypes, apply_tags, load_json_data
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class PackageCreateAction(AbstractPackageAction):
    """Create one or multiple packages.

    SWR_PKG_0001: Package Create Command
    SWR_PKG_0006: External JSON File Support
    SWR_PKG_0007: Stereotype and Tag Support
    SWR_PKG_0009: View-to-Create Workflow
    """

    VALID_ATTRIBUTES = {
        "name",
        "description",
        "description_html",
        "description_rtf",
        "display_name",
        "display_name_rtf",
        "properties",
        "stereotypes",
        "tags",
    }

    def __init__(self) -> None:
        """Initialize the 'create' action."""
        super().__init__(command_id="create")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'create' subcommand and its arguments."""
        parser = sub_parser.add_parser("create", help="Create a package")
        self.add_path_argument(parser, required=False, help_text="Parent package path (optional; defaults to project root)")
        parser.add_argument("--input", default=None, help="JSON file with package attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute package creation."""
        super().execute(args)
        self.logger.info("Starting package creation...")
        input_data = args.input if args.input else args.attributes
        if not input_data:
            raise CliExecutionError("Either --input or attributes argument must be provided")

        data = self._load_json_data(input_data)
        packages_data = data if isinstance(data, list) else [data]

        # Branch on whether path is provided (falsy = use project root)
        is_root = not args.path
        if is_root:
            self.logger.info("Creating packages at project root...")
            container = self._get_active_root()
        else:
            self.logger.info("Resolving parent path '%s'...", args.path)
            container = self._resolve_and_validate_package(args.path)

        created: List[str] = []
        errors: List[str] = []
        for pkg_attrs in packages_data:
            try:
                name = self._create_single_package(container, pkg_attrs, cast(str, args.path), is_root=is_root)
                created.append(name)
            except CliExecutionError:
                raise
            except Exception as e:
                pkg_name = pkg_attrs.get("name", "unknown")
                self.logger.error("Failed to create package '%s': %s", pkg_name, e)
                errors.append(cast(str, pkg_name))

        self._report_results(created, errors, len(packages_data))

    def _create_single_package(self, container: IRPModelElement, pkg_attrs: Dict[str, object], parent_path: str, *, is_root: bool = False) -> str:
        """Create a single package and set its attributes. Returns the package name.

        Args:
            container: The parent container (IRPProject for root, IRPPackage for nested).
            pkg_attrs: Dictionary of package attributes.
            parent_path: The parent path (for reporting; can be None/empty for root).
            is_root: Whether creating at project root (uses addPackage) vs nested (uses addNestedPackage).
        """
        name = str(pkg_attrs.get("name", ""))
        if not name:
            raise CliExecutionError("'name' is required in attributes")

        unknown = set(pkg_attrs.keys()) - self.VALID_ATTRIBUTES
        if unknown:
            self.logger.warning("Skipping unknown attributes: %s", unknown)

        self.logger.info("Creating package '%s'...", name)

        # Check for duplicates before attempting creation
        self._check_package_not_exists(container, name, is_root)

        try:
            # Call the appropriate creation method based on location
            if is_root:
                package = container.add_package(name)  # type: ignore[attr-defined]
            else:
                package = container.add_nested_package(name)  # type: ignore[attr-defined]
        except Exception as e:
            error_str = str(e)
            # Check if error indicates the package already exists
            # COM error code -2147221495 (0x80040005) means "DISP_E_EXCEPTION" but typically indicates duplicate
            # Also check for common duplicate/already exists keywords
            if "already" in error_str.lower() or "duplicate" in error_str.lower() or "-2147221495" in error_str or "2147221495" in error_str:
                container_desc = "project root" if is_root else "parent package"
                raise CliExecutionError(f"Package '{name}' already exists in {container_desc}") from e
            # Generic error
            raise CliExecutionError(f"Failed to create package '{name}': {e}") from e

        # Set attributes if any are provided
        if len(pkg_attrs) > 1:  # More than just 'name'
            self.logger.info("Setting attributes for package '%s'...", name)
            try:
                self._set_attributes(package, pkg_attrs)
            except Exception as e:
                # Log that attributes couldn't be set but don't fail - package was created
                self.logger.warning("Failed to set attributes for package '%s': %s", name, e)

        # Build full_path without leading artifacts for root-created packages
        if is_root or not parent_path:
            full_path = name
        else:
            full_path = f"{parent_path}/{name}"

        self.logger.info("Created package: %s", full_path)
        return name

    def _check_package_not_exists(self, container: IRPModelElement, name: str, is_root: bool) -> None:
        """Check if a package with the given name already exists in the container.

        Args:
            container: IRPProject (for root) or IRPPackage (for nested)
            name: Package name to check
            is_root: Whether checking at project root or nested

        Raises:
            CliExecutionError: If package with name already exists
        """
        self.logger.info("Checking if package '%s' already exists...", name)

        try:
            if is_root:
                from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject

                existing_packages = cast(IRPProject, container).packages
                container_desc = "project root"
            else:
                existing_packages = container.packages  # type: ignore[attr-defined]
                parent_name = container.name
                container_desc = f"package '{parent_name}'"

            # Search for duplicate by name
            for pkg in existing_packages:
                pkg_name = cast(IRPModelElement, pkg).name
                if pkg_name == name:
                    raise CliExecutionError(f"Package '{name}' already exists in {container_desc}")
        except CliExecutionError:
            raise
        except Exception as e:
            # If there's an error checking for duplicates, log it but continue
            # The creation attempt itself will fail more gracefully if package exists
            self.logger.debug("Could not enumerate existing packages to check for duplicates: %s", e)

    def _report_results(self, created: List[str], errors: List[str], total: int) -> None:
        """Log summary of creation results."""
        if errors and not created:
            raise CliExecutionError(f"Created 0/{total} packages; all failed")
        if created:
            self.logger.info("Successfully created %d package%s", len(created), "s" if len(created) != 1 else "")
        if errors:
            self.logger.info("Created %d/%d packages with %d error(s)", len(created), total, len(errors))

    def _load_json_data(self, attributes_input: str) -> Dict[str, object]:
        """Load JSON data via the shared helper (see actions.support)."""
        return cast(Dict[str, object], load_json_data(attributes_input))

    def _set_attributes(self, package: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set validated attributes on package."""
        self._set_basic_attributes(package, attrs)
        self._set_properties(package, attrs)
        self._set_stereotypes(package, attrs)
        self._set_tags(package, attrs)

    def _set_basic_attributes(self, package: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set basic attributes."""
        if "description" in attrs:
            package.description = cast(str, attrs["description"])
        if "description_html" in attrs:
            package.set_description_html(cast(str, attrs["description_html"]))
        if "description_rtf" in attrs:
            package.description_rtf = cast(str, attrs["description_rtf"])
        if "display_name" in attrs:
            package.display_name = cast(str, attrs["display_name"])
        if "display_name_rtf" in attrs:
            package.set_display_name_rtf(cast(str, attrs["display_name_rtf"]))

    def _set_properties(self, package: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set custom properties."""
        if "properties" in attrs:
            for key, val in cast(Dict[str, str], attrs["properties"]).items():
                package.set_property_value(key, val)

    def _set_stereotypes(self, package: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Apply stereotypes via the shared applier (see actions.support)."""
        apply_stereotypes(package, attrs, "Package")

    def _set_tags(self, package: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set tags via the shared applier (see actions.support)."""
        apply_tags(package, attrs)
