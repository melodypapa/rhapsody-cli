"""PackageUpdateAction — split from package_action.py."""

import argparse
import json
import logging
from typing import Dict, List, cast

from rhapsody_cli.actions.package.base import AbstractPackageAction
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class PackageUpdateAction(AbstractPackageAction):
    """Update attributes of an existing package.

    SWR_PKG_0016: Package Update Command
    SWR_PKG_0006: External JSON File Support
    SWR_PKG_0007: Stereotype and Tag Support
    """

    VALID_ATTRIBUTES = {
        "name",
        "description",
        "display_name",
        "stereotypes",
        "tags",
        "properties",
    }

    def __init__(self) -> None:
        """Initialize the 'update' action."""
        super().__init__(command_id="update")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'update' subcommand and its arguments."""
        parser = sub_parser.add_parser("update", help="Update attributes of an existing package")
        self.add_path_argument(parser, required=False, help_text="Package path to update")
        parser.add_argument("--guid", default=None, help="GUID of the package to update")
        parser.add_argument("--input", default=None, help="JSON file with package attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")

    def _resolve_element_by_guid(self, guid: str) -> IRPModelElement:
        """Resolve element by GUID and validate it's a Package.

        Args:
            guid: GUID of the element to resolve.

        Returns:
            Package COM object.

        Raises:
            CliExecutionError: If GUID not found or element is not a Package.
        """
        project = self._get_active_root()
        element = project.find_element_by_guid(guid)  # type: ignore[attr-defined]
        if element is None:
            raise CliExecutionError(f"GUID '{guid}' not found")
        meta_class = element.meta_class
        if meta_class != "Package":
            raise CliExecutionError(f"GUID '{guid}' does not resolve to a Package (found {meta_class})")
        return cast(IRPModelElement, element)

    def _load_json_data(self, args: argparse.Namespace) -> Dict[str, object]:
        """Load JSON data from inline string or file.

        SWR_PKG_0006: External JSON File Support

        Args:
            args: Parsed argparse.Namespace with `input` and `attributes`.

        Returns:
            Dictionary of package attributes (empty if neither provided).
        """
        if args.input:
            try:
                with open(args.input, encoding="utf-8") as f:
                    return cast(Dict[str, object], json.load(f))
            except FileNotFoundError:
                raise CliExecutionError(f"File not found: {args.input}") from None
            except json.JSONDecodeError as e:
                raise CliExecutionError(f"Invalid JSON: {e}") from e
        elif args.attributes:
            data_str = args.attributes.strip()
            if data_str.startswith("{"):
                try:
                    return cast(Dict[str, object], json.loads(data_str))
                except json.JSONDecodeError as e:
                    raise CliExecutionError(f"Invalid JSON: {e}") from e
            else:
                try:
                    with open(data_str, encoding="utf-8") as f:
                        return cast(Dict[str, object], json.load(f))
                except FileNotFoundError:
                    raise CliExecutionError(f"File not found: {data_str}") from None
                except json.JSONDecodeError as e:
                    raise CliExecutionError(f"Invalid JSON: {e}") from e
        return {}

    def _set_attributes(self, package: IRPModelElement, data: Dict[str, object]) -> None:
        """Set validated attributes on package (partial update).

        Only fields present in `data` are modified; unknown fields are
        skipped with a warning log.

        Args:
            package: Package COM object to update.
            data: Dictionary of attributes to apply.
        """
        for key, value in data.items():
            if key not in self.VALID_ATTRIBUTES:
                self.logger.warning("Skipping unknown attribute: %s", key)
                continue
            if key == "name":
                package.name = cast(str, value)
            elif key == "description":
                package.description = cast(str, value)
            elif key == "display_name":
                package.display_name = cast(str, value)
            elif key == "stereotypes":
                for stereotype in cast(List[str], value):
                    package.add_stereotype(stereotype, "Package")
            elif key == "tags":
                for tag_key, tag_value in cast(Dict[str, str], value).items():
                    package.set_property_value(tag_key, tag_value)
            elif key == "properties":
                for prop_key, prop_value in cast(Dict[str, str], value).items():
                    package.set_property_value(prop_key, prop_value)

    def execute(self, args: argparse.Namespace) -> None:
        """Execute package update.

        Args:
            args: Parsed argparse.Namespace with path/guid and attribute data.
        """
        super().execute(args)
        self.logger.info("Starting package update...")
        if not args.path and not args.guid:
            raise CliExecutionError("Either --path or --guid is required")
        if args.guid:
            self.logger.info("Resolving package by GUID '%s'...", args.guid)
            package = self._resolve_element_by_guid(args.guid)
        else:
            self.logger.info("Resolving package path '%s'...", args.path)
            package = self._resolve_and_validate_package(args.path)
        data = self._load_json_data(args)
        self._set_attributes(package, data)
        self.logger.info("Successfully updated package: %s", package.name)
