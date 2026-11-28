"""PortCreateAction — split from port_action.py."""

import argparse
import logging
from typing import Dict, List, Union, cast

from rhapsody_cli.actions.port.base import AbstractPortAction
from rhapsody_cli.actions.support import load_json_data
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class PortCreateAction(AbstractPortAction):
    """Create one or multiple ports.

    SWR_PORT_00001: Port Create Command
    SWR_PORT_00007: External JSON File Support
    SWR_PORT_00011: PortContract Resolution
    SWR_PORT_00012: IsBehavioral and IsReversed Support
    SWR_PORT_00013: Bulk Creation Support
    """

    VALID_ATTRIBUTES = {
        "name",
        "isBehavioral",
        "isReversed",
        "portContract",
        "description",
    }

    def __init__(self) -> None:
        """Initialize the 'create' action."""
        super().__init__(command_id="create")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'create' subcommand and its arguments."""
        parser = sub_parser.add_parser("create", help="Create a port")
        self.add_path_argument(parser, required=True, help_text="Parent classifier path")
        parser.add_argument("--input", default=None, help="JSON file with port attributes")
        parser.add_argument("attributes", nargs="?", default=None, help="Inline JSON or JSON file path")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port creation."""
        super().execute(args)
        input_data = args.input if args.input else args.attributes
        if not input_data:
            raise CliExecutionError("Either --input or attributes argument must be provided")

        data = self._load_json_data(input_data)
        ports_data = data if isinstance(data, list) else [data]

        classifier = self._resolve_classifier(args.path)

        created: List[str] = []
        errors: List[str] = []
        for port_attrs in ports_data:
            try:
                name = self._create_single_port(classifier, port_attrs, args.path)
                created.append(name)
            except CliExecutionError:
                raise
            except Exception as e:
                port_name = port_attrs.get("name", "unknown")
                self.logger.error("Failed to create port '%s': %s", port_name, e)
                errors.append(cast(str, port_name))

        self._report_results(created, errors, len(ports_data))

    def _create_single_port(self, classifier: IRPModelElement, port_attrs: Dict[str, object], parent_path: str) -> str:
        """Create a single port and set its attributes. Returns the port name."""
        name = str(port_attrs.get("name", ""))
        if not name:
            raise CliExecutionError("'name' is required in attributes")

        unknown = set(port_attrs.keys()) - self.VALID_ATTRIBUTES
        if unknown:
            self.logger.warning("Skipping unknown attributes: %s", unknown)

        port = classifier.add_new_aggr("Port", name)
        self._set_attributes(classifier, port, port_attrs)

        full_path = f"{parent_path}/{name}"
        self.logger.info("Created port: %s", full_path)
        return name

    def _report_results(self, created: List[str], errors: List[str], total: int) -> None:
        """Log summary of creation results."""
        if errors and not created:
            raise CliExecutionError(f"Created 0/{total} ports; all failed")
        if errors:
            self.logger.info("Created %d/%d ports with %d error(s)", len(created), total, len(errors))

    def _load_json_data(self, attributes_input: str) -> Dict[str, object]:
        """Load JSON data via the shared helper (see actions.support)."""
        return cast(Dict[str, object], load_json_data(attributes_input))

    def _set_attributes(self, classifier: IRPModelElement, port: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set validated attributes on port."""
        if "name" in attrs:
            port.name = cast(str, attrs["name"])
        if "description" in attrs:
            port.description = cast(str, attrs["description"])
        self._set_boolean_flags(port, attrs)
        self._set_port_contract(classifier, port, attrs)

    def _set_boolean_flags(self, port: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Set boolean flags isBehavioral, isReversed.

        SWR_PORT_00012: IsBehavioral and IsReversed Support
        """
        if "isBehavioral" in attrs:
            port.is_behavioral = int(cast(Union[str, int], attrs["isBehavioral"]))  # type: ignore[attr-defined]
        if "isReversed" in attrs:
            port.is_reversed = int(cast(Union[str, int], attrs["isReversed"]))  # type: ignore[attr-defined]

    def _set_port_contract(self, classifier: IRPModelElement, port: IRPModelElement, attrs: Dict[str, object]) -> None:
        """Resolve and set the portContract.

        SWR_PORT_00011: PortContract Resolution
        """
        if "portContract" in attrs:
            contract_name = cast(str, attrs["portContract"])
            owner = classifier.owner
            target = owner.find_nested_classifier_recursive(contract_name)  # type: ignore[attr-defined]
            if target is None:
                raise CliExecutionError(f"PortContract '{contract_name}' not found")
            port.port_contract = target  # type: ignore[attr-defined]
