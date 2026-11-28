"""PortViewAction — split from port_action.py."""

import argparse
import logging
from typing import Dict, List, cast

from rhapsody_cli.actions.port.base import AbstractPortAction
from rhapsody_cli.actions.support import write_text_file
from rhapsody_cli.cli.formatters import OutputFormatter
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class PortViewAction(AbstractPortAction):
    """View port details.

    SWR_PORT_00003: Port View Command
    SWR_PORT_00008: Multi-Format Output
    SWR_PORT_00010: GUID Lookup Support
    """

    _VIEW_HEADERS = [
        "Name",
        "GUID",
        "Description",
        "IsBehavioral",
        "IsReversed",
        "PortContract",
        "MetaClass",
        "FullPath",
    ]
    _VIEW_KEYS = [
        "name",
        "guid",
        "description",
        "isBehavioral",
        "isReversed",
        "portContract",
        "metaClass",
        "fullPath",
    ]

    def __init__(self) -> None:
        """Initialize the 'view' action."""
        super().__init__(command_id="view")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'view' subcommand and its arguments."""
        parser = sub_parser.add_parser("view", help="View port details")
        self.add_path_argument(parser, required=False, help_text="Parent classifier path")
        parser.add_argument("--guid", default=None, help="Port GUID to view")
        parser.add_argument("--name", default=None, help="Port name within classifier")
        parser.add_argument("--output", default=None, help="Write output to file")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port view."""
        super().execute(args)
        has_path_name = args.path and args.name
        has_guid = args.guid is not None

        if has_path_name and has_guid:
            raise CliExecutionError("Only one of --path + --name or --guid may be specified")
        if not has_path_name and not has_guid:
            raise CliExecutionError("Either --path + --name or --guid must be specified")

        if has_guid:
            port = self._resolve_port_by_guid(args.guid)
        else:
            classifier = self._resolve_classifier(args.path)
            port = self._resolve_port(classifier, args.name)

        try:
            data = self._collect_port_data(port)
            output = self._format_output(data, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Wrote port details to: %s", args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to view port '{args.name or args.guid}'")

    def _collect_port_data(self, port: IRPModelElement) -> Dict[str, object]:
        """Collect port details into a data dictionary.

        Normalizes boolean flags to int for clean JSON round-trip.
        """
        contract = port.port_contract  # type: ignore[attr-defined]
        contract_name = cast(IRPModelElement, contract).name if contract is not None else ""
        return {
            "name": port.name,
            "guid": port.guid,
            "description": port.description,
            "isBehavioral": int(port.is_behavioral),  # type: ignore[attr-defined]
            "isReversed": int(port.is_reversed),  # type: ignore[attr-defined]
            "portContract": contract_name,
            "metaClass": port.meta_class,
            "fullPath": port.get_full_path_name(),
        }

    def _format_output(self, data: Dict[str, object], format_type: str) -> str:
        """Format output based on format parameter."""
        if format_type == "json":
            return OutputFormatter.json_format(data)
        elif format_type == "csv":
            data_row = [str(data[key]) for key in self._VIEW_KEYS]
            return OutputFormatter.csv_format(self._VIEW_HEADERS, [data_row])
        else:
            table_rows: List[List[str]] = [
                ["Name", str(data["name"])],
                ["GUID", str(data["guid"])],
                ["Description", str(data["description"])],
                ["IsBehavioral", str(data["isBehavioral"])],
                ["IsReversed", str(data["isReversed"])],
                ["PortContract", str(data["portContract"])],
                ["MetaClass", str(data["metaClass"])],
                ["FullPath", str(data["fullPath"])],
            ]
            return OutputFormatter.table(["Property", "Value"], table_rows)

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content via the shared helper (see actions.support)."""
        write_text_file(file_path, content)
