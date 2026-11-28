"""OperationViewAction — split from operation_action.py."""

import argparse
import logging
from typing import Callable, Dict, List, cast

from rhapsody_cli.actions.operation.base import AbstractOperationAction
from rhapsody_cli.actions.support import write_text_file
from rhapsody_cli.cli.formatters import OutputFormatter
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class OperationViewAction(AbstractOperationAction):
    """View operation details.

    SWR_OP_00003: Operation View Command
    SWR_OP_00008: Multi-Format Output
    SWR_OP_00010: GUID Lookup Support
    """

    _VIEW_HEADERS = [
        "Name",
        "GUID",
        "Description",
        "Body",
        "IsAbstract",
        "IsStatic",
        "IsVirtual",
        "Returns",
        "Visibility",
        "Arguments",
        "MetaClass",
        "FullPath",
    ]
    _VIEW_KEYS = [
        "name",
        "guid",
        "description",
        "body",
        "isAbstract",
        "isStatic",
        "isVirtual",
        "returns",
        "visibility",
        "arguments",
        "metaClass",
        "fullPath",
    ]

    def __init__(self) -> None:
        """Initialize the 'view' action."""
        super().__init__(command_id="view")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'view' subcommand and its arguments."""
        parser = sub_parser.add_parser("view", help="View operation details")
        self.add_path_argument(parser, required=False, help_text="Parent classifier path")
        parser.add_argument("--guid", default=None, help="Operation GUID to view")
        parser.add_argument("--name", default=None, help="Operation name within classifier")
        parser.add_argument("--output", default=None, help="Write output to file")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute operation view."""
        super().execute(args)
        has_path_name = args.path and args.name
        has_guid = args.guid is not None

        if has_path_name and has_guid:
            raise CliExecutionError("Only one of --path + --name or --guid may be specified")
        if not has_path_name and not has_guid:
            raise CliExecutionError("Either --path + --name or --guid must be specified")

        if has_guid:
            operation = self._resolve_operation_by_guid(args.guid)
        else:
            classifier = self._resolve_classifier(args.path)
            operation = self._resolve_operation(classifier, args.name)

        try:
            data = self._collect_operation_data(operation)
            output = self._format_output(data, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Wrote operation details to: %s", args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to view operation '{args.name or args.guid}'")

    def _collect_operation_data(self, operation: IRPModelElement) -> Dict[str, object]:
        """Collect operation details into a data dictionary.

        Normalizes boolean flags to int for clean JSON round-trip.
        """

        def safe(getter: Callable[[], object], default: object) -> object:
            # Some Rhapsody builds return IRPInterfaceItem COM objects for
            # operations; those lack several IRPOperation-only members.
            try:
                return getter()
            except (AttributeError, RuntimeError):
                return default

        returns = safe(lambda: operation.returns, None)  # type: ignore[attr-defined]
        returns_name = cast(IRPModelElement, returns).name if returns is not None else ""
        arguments = safe(lambda: operation.arguments, [])  # type: ignore[attr-defined]
        return {
            "name": operation.name,
            "guid": operation.guid,
            "description": safe(lambda: operation.description, ""),
            "body": safe(lambda: operation.body, ""),  # type: ignore[attr-defined]
            "isAbstract": int(safe(lambda: operation.is_abstract, 0)),  # type: ignore[attr-defined,call-overload]
            "isStatic": int(safe(lambda: operation.is_static, 0)),  # type: ignore[attr-defined,call-overload]
            "isVirtual": int(safe(lambda: operation.is_virtual, 0)),  # type: ignore[attr-defined,call-overload]
            "returns": returns_name,
            "visibility": safe(lambda: operation.visibility, ""),  # type: ignore[attr-defined]
            "arguments": [cast(IRPModelElement, arg).name for arg in arguments],  # type: ignore[attr-defined]
            "metaClass": operation.meta_class,
            "fullPath": operation.get_full_path_name(),
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
                ["Body", str(data["body"])],
                ["IsAbstract", str(data["isAbstract"])],
                ["IsStatic", str(data["isStatic"])],
                ["IsVirtual", str(data["isVirtual"])],
                ["Returns", str(data["returns"])],
                ["Visibility", str(data["visibility"])],
                ["Arguments", ", ".join(cast(List[str], data["arguments"]))],
                ["MetaClass", str(data["metaClass"])],
                ["FullPath", str(data["fullPath"])],
            ]
            return OutputFormatter.table(["Property", "Value"], table_rows)

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content via the shared helper (see actions.support)."""
        write_text_file(file_path, content)
