"""AttributeCreateAction — split from attribute_action.py."""

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, List, cast

from rhapsody_cli.actions.attribute.base import AbstractAttributeAction
from rhapsody_cli.actions.support import load_json_data
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class AttributeCreateAction(AbstractAttributeAction):
    """Create one or multiple attributes.

    SWR_ATTR_00001: Attribute Create Command
    SWR_ATTR_00007: External JSON File Support
    SWR_ATTR_00011: Type Resolution
    SWR_ATTR_00012: IsStatic Flag Support
    SWR_ATTR_00013: Bulk Creation Support
    """

    VALID_ATTRIBUTES = {
        "name",
        "type",
        "defaultValue",
        "multiplicity",
        "isStatic",
        "visibility",
        "declaration",
        "description",
    }

    def __init__(self) -> None:
        """Initialize the 'create' action."""
        super().__init__(command_id="create")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'create' subcommand and its arguments."""
        parser = sub_parser.add_parser("create", help="Create an attribute")
        self.add_path_argument(parser, required=True, help_text="Parent classifier path")
        parser.add_argument("--input", default=None, help="JSON file with attribute attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute attribute creation."""
        super().execute(args)
        input_data = args.input if args.input else args.attributes
        if not input_data:
            raise CliExecutionError("Either --input or attributes argument must be provided")

        data = self._load_json_data(input_data)
        attrs_data = data if isinstance(data, list) else [data]

        classifier = self._resolve_classifier(args.path)

        created: List[str] = []
        errors: List[str] = []
        for attr_attrs in attrs_data:
            try:
                name = self._create_single_attribute(classifier, attr_attrs, args.path)
                created.append(name)
            except CliExecutionError:
                raise
            except Exception as e:
                attr_name = attr_attrs.get("name", "unknown")
                self.logger.error("Failed to create attribute '%s': %s", attr_name, e)
                errors.append(cast(str, attr_name))

        self._report_results(created, errors, len(attrs_data))

    def _create_single_attribute(self, classifier: IRPModelElement, attr_attrs: Dict[str, object], parent_path: str) -> str:
        """Create a single attribute and set its attributes. Returns the attribute name."""
        name = str(attr_attrs.get("name", ""))
        if not name:
            raise CliExecutionError("'name' is required in attributes")

        unknown = set(attr_attrs.keys()) - self.VALID_ATTRIBUTES
        if unknown:
            self.logger.warning("Skipping unknown attributes: %s", unknown)

        attribute = classifier.add_attribute(name)  # type: ignore[attr-defined]
        self._set_attributes(classifier, attribute, attr_attrs)

        full_path = f"{parent_path}/{name}"
        self.logger.info("Created attribute: %s", full_path)
        return name

    def _report_results(self, created: List[str], errors: List[str], total: int) -> None:
        """Log summary of creation results."""
        if errors and not created:
            raise CliExecutionError(f"Created 0/{total} attributes; all failed")
        if errors:
            self.logger.info("Created %d/%d attributes with %d error(s)", len(created), total, len(errors))

    def _load_json_data(self, attributes_input: str) -> Dict[str, object]:
        """Load JSON data from inline string or external file.

        SWR_ATTR_00007: External JSON File Support
        """
        if attributes_input.startswith("{") or attributes_input.startswith("["):
            try:
                return cast(Dict[str, object], json.loads(attributes_input))
            except json.JSONDecodeError as e:
                raise CliExecutionError(f"Invalid JSON: {e}") from e

        if not Path(attributes_input).exists():
            raise CliExecutionError(f"File not found: {attributes_input}")

        try:
            with open(attributes_input, encoding="utf-8") as f:
                return cast(Dict[str, object], json.load(f))
        except json.JSONDecodeError as e:
            raise CliExecutionError(f"Invalid JSON in file: {e}") from e
        except OSError as e:
            raise CliExecutionError(f"Failed to read file: {e}") from e

    def _load_json_data(self, attributes_input: str) -> Dict[str, object]:
        """Load JSON data via the shared helper (see actions.support)."""
        return cast(Dict[str, object], load_json_data(attributes_input))

    def _set_attributes(self, classifier: IRPModelElement, attribute: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set validated attributes on attribute."""
        if "name" in attrs:
            attribute.name = cast(str, attrs["name"])
        if "defaultValue" in attrs:
            attribute.set_default_value(cast(str, attrs["defaultValue"]))  # type: ignore[attr-defined]
        if "multiplicity" in attrs:
            attribute.multiplicity = cast(str, attrs["multiplicity"])  # type: ignore[attr-defined]
        if "visibility" in attrs:
            attribute.visibility = cast(str, attrs["visibility"])  # type: ignore[attr-defined]
        if "declaration" in attrs:
            attribute.set_declaration(cast(str, attrs["declaration"]))  # type: ignore[attr-defined]
        if "description" in attrs:
            attribute.description = cast(str, attrs["description"])
        self._set_boolean_flags(attribute, attrs)
        self._set_type(classifier, attribute, attrs)

    def _set_boolean_flags(self, attribute: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set boolean flag isStatic.

        SWR_ATTR_00012: IsStatic Flag Support
        """
        if "isStatic" in attrs:
            attribute.is_static = bool(attrs["isStatic"])  # type: ignore[attr-defined]

    def _set_type(self, classifier: IRPModelElement, attribute: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Resolve and set the attribute type.

        SWR_ATTR_00011: Type Resolution
        """
        if "type" in attrs:
            type_name = cast(str, attrs["type"])
            owner = classifier.owner
            target = owner.find_nested_classifier_recursive(type_name)  # type: ignore[attr-defined]
            if target is None:
                raise CliExecutionError(f"Type '{type_name}' not found")
            attribute.set_type(target)  # type: ignore[attr-defined]
