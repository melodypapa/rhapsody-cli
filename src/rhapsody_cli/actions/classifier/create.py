"""ClassCreateAction — split from class_action.py."""

import argparse
import logging
from typing import Dict, List, cast

from rhapsody_cli.actions.classifier.base import AbstractClassAction
from rhapsody_cli.actions.support import apply_stereotypes, load_json_data
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class ClassCreateAction(AbstractClassAction):
    """Create one or multiple classes.

    SWR_CLS_00001: Class Create Command
    SWR_CLS_00006: External JSON File Support
    SWR_CLS_00007: Stereotype and Tag Support
    SWR_CLS_00009: View-to-Create Workflow
    SWR_CLS_00012: Boolean Flag Support
    """

    VALID_ATTRIBUTES = {
        "name",
        "description",
        "isAbstract",
        "isFinal",
        "isActive",
        "stereotypes",
        "tags",
        "operations",
        "attributes",
        "superclasses",
    }

    def __init__(self) -> None:
        """Initialize the 'create' action."""
        super().__init__(command_id="create")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'create' subcommand and its arguments."""
        parser = sub_parser.add_parser("create", help="Create a class")
        self.add_path_argument(parser, required=True, help_text="Parent package path")
        parser.add_argument("--input", default=None, help="JSON file with class attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute class creation."""
        super().execute(args)
        input_data = args.input if args.input else args.attributes
        if not input_data:
            raise CliExecutionError("Either --input or attributes argument must be provided")

        data = self._load_json_data(input_data)
        classes_data = data if isinstance(data, list) else [data]

        parent = self._resolve_and_validate_package(args.path)

        created: List[str] = []
        errors: List[str] = []
        for cls_attrs in classes_data:
            try:
                name = self._create_single_class(parent, cls_attrs, args.path)
                created.append(name)
            except CliExecutionError:
                raise
            except Exception as e:
                cls_name = cls_attrs.get("name", "unknown")
                self.logger.error("Failed to create class '%s': %s", cls_name, e)
                errors.append(cast(str, cls_name))

        self._report_results(created, errors, len(classes_data))

    def _create_single_class(self, parent: IRPModelElement, cls_attrs: Dict[str, object], parent_path: str) -> str:
        """Create a single class and set its attributes. Returns the class name."""
        name = str(cls_attrs.get("name", ""))
        if not name:
            raise CliExecutionError("'name' is required in attributes")

        unknown = set(cls_attrs.keys()) - self.VALID_ATTRIBUTES
        if unknown:
            self.logger.warning("Skipping unknown attributes: %s", unknown)

        cls = parent.add_class(name)  # type: ignore[attr-defined]
        self._set_attributes(parent, cls, cls_attrs)

        full_path = f"{parent_path}/{name}"
        self.logger.info("Created class: %s", full_path)
        return name

    def _report_results(self, created: List[str], errors: List[str], total: int) -> None:
        """Log summary of creation results."""
        if errors and not created:
            raise CliExecutionError(f"Created 0/{total} classes; all failed")
        if errors:
            self.logger.info("Created %d/%d classes with %d error(s)", len(created), total, len(errors))

    def _load_json_data(self, attributes_input: str) -> Dict[str, object]:
        """Load JSON data via the shared helper (see actions.support)."""
        return cast(Dict[str, object], load_json_data(attributes_input))

    def _set_attributes(self, parent: IRPModelElement, cls: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set validated attributes on class."""
        self._set_basic_attributes(cls, attrs)
        self._set_boolean_flags(cls, attrs)
        self._set_properties(cls, attrs)
        self._set_stereotypes(cls, attrs)
        self._set_operations(cls, attrs)
        self._set_attributes_list(cls, attrs)
        self._set_superclasses(parent, cls, attrs)

    def _set_basic_attributes(self, cls: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set basic attributes."""
        if "description" in attrs:
            cls.description = cast(str, attrs["description"])

    def _set_boolean_flags(self, cls: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set boolean flags isAbstract, isFinal, isActive.

        SWR_CLS_00012: Boolean Flag Support
        """
        if "isAbstract" in attrs:
            cls.is_abstract = bool(attrs["isAbstract"])  # type: ignore[attr-defined]
        if "isFinal" in attrs:
            cls.set_is_final(1 if attrs["isFinal"] else 0)  # type: ignore[attr-defined]
        if "isActive" in attrs:
            cls.is_active = 1 if attrs["isActive"] else 0  # type: ignore[attr-defined]

    def _set_properties(self, cls: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set custom properties (tags)."""
        if "tags" in attrs:
            for key, val in cast(Dict[str, str], attrs["tags"]).items():
                cls.set_property_value(key, val)

    def _set_stereotypes(self, cls: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Apply stereotypes via the shared applier (see actions.support)."""
        apply_stereotypes(cls, attrs, "Class")

    def _set_operations(self, cls: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Add operations."""
        if "operations" in attrs:
            for op_name in cast(List[str], attrs["operations"]):
                cls.add_operation(op_name)  # type: ignore[attr-defined]

    def _set_attributes_list(self, cls: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Add attributes."""
        if "attributes" in attrs:
            for attr_name in cast(List[str], attrs["attributes"]):
                cls.add_attribute(attr_name)  # type: ignore[attr-defined]

    def _set_superclasses(self, parent: IRPModelElement, cls: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Add generalization relationships to superclasses.

        SWR_CLS_00001: resolves superclass names via parent.findNestedClassifierRecursive(name).
        """
        if "superclasses" in attrs:
            for name in cast(List[str], attrs["superclasses"]):
                target = parent.find_nested_classifier_recursive(name)  # type: ignore[attr-defined]
                if target is None:
                    raise CliExecutionError(f"Superclass '{name}' not found in package")
                cls.add_generalization(target)  # type: ignore[attr-defined]
