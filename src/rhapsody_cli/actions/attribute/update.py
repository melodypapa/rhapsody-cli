"""AttributeUpdateAction — split from attribute_action.py."""

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, cast

from rhapsody_cli.actions.attribute.base import AbstractAttributeAction
from rhapsody_cli.actions.support import load_json_data
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class AttributeUpdateAction(AbstractAttributeAction):
    """Update attributes of an existing attribute.

    SWR_ATTR_00005: Attribute Update Command
    SWR_ATTR_00007: External JSON File Support
    SWR_ATTR_00010: GUID Lookup Support
    SWR_ATTR_00011: Type Resolution
    SWR_ATTR_00012: IsStatic Flag Support
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
        """Initialize the 'update' action."""
        super().__init__(command_id="update")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'update' subcommand and its arguments."""
        parser = sub_parser.add_parser("update", help="Update attributes of an existing attribute")
        self.add_path_argument(parser, required=False, help_text="Parent classifier path")
        parser.add_argument("--guid", default=None, help="Attribute GUID to update")
        parser.add_argument("--name", default=None, help="Attribute name within classifier")
        parser.add_argument("--input", default=None, help="JSON file with attribute attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute attribute update."""
        super().execute(args)
        has_path_name = args.path and args.name
        has_guid = args.guid is not None

        if has_path_name and has_guid:
            raise CliExecutionError("Only one of --path + --name or --guid may be specified")
        if not has_path_name and not has_guid:
            raise CliExecutionError("Either --path + --name or --guid must be specified")

        if has_guid:
            attribute = self._resolve_attribute_by_guid(args.guid)
            classifier = attribute.owner
        else:
            classifier = self._resolve_classifier(args.path)
            attribute = self._resolve_attribute(classifier, args.name)

        input_data = args.input if args.input else args.attributes
        if not input_data:
            raise CliExecutionError("Either --input or attributes argument must be provided")

        data = self._load_json_data(input_data)

        unknown = set(data.keys()) - self.VALID_ATTRIBUTES
        if unknown:
            self.logger.warning("Skipping unknown attributes: %s", unknown)

        self._set_attributes(classifier, attribute, data)

        self.logger.info("Successfully updated attribute: %s", attribute.name)

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
        """Set validated attributes on attribute (partial update)."""
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
        if "isStatic" in attrs:
            attribute.is_static = bool(attrs["isStatic"])  # type: ignore[attr-defined]
        if "type" in attrs:
            type_name = cast(str, attrs["type"])
            owner = classifier.owner
            target = owner.find_nested_classifier_recursive(type_name)  # type: ignore[attr-defined]
            if target is None:
                raise CliExecutionError(f"Type '{type_name}' not found")
            attribute.set_type(target)  # type: ignore[attr-defined]
