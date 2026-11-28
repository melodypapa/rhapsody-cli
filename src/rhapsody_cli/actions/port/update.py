"""PortUpdateAction — split from port_action.py."""

import argparse
import json
import logging
from pathlib import Path
from typing import Dict, Union, cast

from rhapsody_cli.actions.port.base import AbstractPortAction
from rhapsody_cli.actions.support import load_json_data
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class PortUpdateAction(AbstractPortAction):
    """Update attributes of an existing port.

    SWR_PORT_00005: Port Update Command
    SWR_PORT_00007: External JSON File Support
    SWR_PORT_00010: GUID Lookup Support
    SWR_PORT_00011: PortContract Resolution
    SWR_PORT_00012: IsBehavioral and IsReversed Support
    """

    VALID_ATTRIBUTES = {
        "name",
        "isBehavioral",
        "isReversed",
        "portContract",
        "description",
    }

    def __init__(self) -> None:
        """Initialize the 'update' action."""
        super().__init__(command_id="update")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'update' subcommand and its arguments."""
        parser = sub_parser.add_parser("update", help="Update attributes of an existing port")
        self.add_path_argument(parser, required=False, help_text="Parent classifier path")
        parser.add_argument("--guid", default=None, help="Port GUID to update")
        parser.add_argument("--name", default=None, help="Port name within classifier")
        parser.add_argument("--input", default=None, help="JSON file with port attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port update."""
        super().execute(args)
        has_path_name = args.path and args.name
        has_guid = args.guid is not None

        if has_path_name and has_guid:
            raise CliExecutionError("Only one of --path + --name or --guid may be specified")
        if not has_path_name and not has_guid:
            raise CliExecutionError("Either --path + --name or --guid must be specified")

        if has_guid:
            port = self._resolve_port_by_guid(args.guid)
            classifier = port.owner
        else:
            classifier = self._resolve_classifier(args.path)
            port = self._resolve_port(classifier, args.name)

        input_data = args.input if args.input else args.attributes
        if not input_data:
            raise CliExecutionError("Either --input or attributes argument must be provided")

        data = self._load_json_data(input_data)

        unknown = set(data.keys()) - self.VALID_ATTRIBUTES
        if unknown:
            self.logger.warning("Skipping unknown attributes: %s", unknown)

        self._set_attributes(classifier, port, data)

        self.logger.info("Successfully updated port: %s", port.name)

    def _load_json_data(self, attributes_input: str) -> Dict[str, object]:
        """Load JSON data from inline string or external file.

        SWR_PORT_00007: External JSON File Support
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

    def _set_attributes(self, classifier: IRPModelElement, port: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set validated attributes on port (partial update)."""
        if "name" in attrs:
            port.name = cast(str, attrs["name"])
        if "description" in attrs:
            port.description = cast(str, attrs["description"])
        if "isBehavioral" in attrs:
            port.is_behavioral = int(cast(Union[str, int], attrs["isBehavioral"]))  # type: ignore[attr-defined]
        if "isReversed" in attrs:
            port.is_reversed = int(cast(Union[str, int], attrs["isReversed"]))  # type: ignore[attr-defined]
        if "portContract" in attrs:
            contract_name = cast(str, attrs["portContract"])
            owner = classifier.owner
            target = owner.find_nested_classifier_recursive(contract_name)  # type: ignore[attr-defined]
            if target is None:
                raise CliExecutionError(f"PortContract '{contract_name}' not found")
            port.port_contract = target  # type: ignore[attr-defined]
