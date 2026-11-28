"""ClassViewAction — split from class_action.py."""

import argparse
import logging
from typing import Dict, List, cast

from rhapsody_cli.actions.classifier.base import AbstractClassAction
from rhapsody_cli.actions.support import write_text_file
from rhapsody_cli.cli.formatters import OutputFormatter
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class ClassViewAction(AbstractClassAction):
    """View class details.

    SWR_CLS_00003: Class View Command
    SWR_CLS_00008: Multi-Format Output
    SWR_CLS_00013: GUID Lookup Support
    """

    _VIEW_HEADERS = [
        "Name",
        "GUID",
        "Description",
        "IsAbstract",
        "IsActive",
        "IsFinal",
        "IsComposite",
        "IsReactive",
        "MetaClass",
        "FullPath",
        "Operations",
        "Attributes",
    ]
    _VIEW_KEYS = [
        "name",
        "guid",
        "description",
        "isAbstract",
        "isActive",
        "isFinal",
        "isComposite",
        "isReactive",
        "metaClass",
        "fullPath",
        "operations",
        "attributes",
    ]

    def __init__(self) -> None:
        """Initialize the 'view' action."""
        super().__init__(command_id="view")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'view' subcommand and its arguments."""
        parser = sub_parser.add_parser("view", help="View class details")
        self.add_path_argument(parser, required=False, help_text="Class path to view")
        parser.add_argument("--guid", default=None, help="Class GUID to view")
        parser.add_argument("--output", default=None, help="Write output to file")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute class view."""
        super().execute(args)
        if args.path and args.guid:
            raise CliExecutionError("Only one of --path or --guid may be specified")
        if not args.path and not args.guid:
            raise CliExecutionError("Either --path or --guid must be specified")

        if args.guid:
            cls = self._resolve_class_by_guid(args.guid)
        else:
            cls = self._resolve_and_validate_class(args.path)

        try:
            data = self._collect_class_data(cls)
            output = self._format_output(data, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Wrote class details to: %s", args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to view class '{args.path or args.guid}'")

    def _collect_class_data(self, cls: IRPModelElement) -> Dict[str, object]:
        """Collect class details into a data dictionary.

        Normalizes IsAbstract (bool) to int for clean JSON round-trip.
        """
        operations = cls.operations  # type: ignore[attr-defined]
        attributes = cls.attributes  # type: ignore[attr-defined]
        return {
            "name": cls.name,
            "guid": cls.guid,
            "description": cls.description,
            "isAbstract": int(cls.is_abstract),  # type: ignore[attr-defined]
            "isActive": int(cls.is_active),  # type: ignore[attr-defined]
            "isFinal": int(cls.get_is_final()),  # type: ignore[attr-defined]
            "isComposite": int(cls.is_composite),  # type: ignore[attr-defined]
            "isReactive": int(cls.is_reactive),  # type: ignore[attr-defined]
            "metaClass": cls.meta_class,
            "fullPath": cls.get_full_path_name(),
            "operations": [cast(IRPModelElement, op).name for op in operations],
            "attributes": [cast(IRPModelElement, attr).name for attr in attributes],
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
                ["IsAbstract", str(data["isAbstract"])],
                ["IsActive", str(data["isActive"])],
                ["IsFinal", str(data["isFinal"])],
                ["IsComposite", str(data["isComposite"])],
                ["IsReactive", str(data["isReactive"])],
                ["MetaClass", str(data["metaClass"])],
                ["FullPath", str(data["fullPath"])],
                ["Operations", ", ".join(cast(List[str], data["operations"]))],
                ["Attributes", ", ".join(cast(List[str], data["attributes"]))],
            ]
            return OutputFormatter.table(["Property", "Value"], table_rows)

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content via the shared helper (see actions.support)."""
        write_text_file(file_path, content)
