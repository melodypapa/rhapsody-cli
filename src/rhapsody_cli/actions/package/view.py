"""PackageViewAction — split from package_action.py."""

import argparse
import logging
from typing import Dict

from rhapsody_cli.actions.package.base import AbstractPackageAction
from rhapsody_cli.actions.support import write_text_file
from rhapsody_cli.cli.formatters import OutputFormatter
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class PackageViewAction(AbstractPackageAction):
    """View package details.

    SWR_PKG_0003: Package View Command
    SWR_PKG_0008: Multi-Format Output
    """

    _VIEW_HEADERS = ["Name", "GUID", "Description", "MetaClass", "FullPath"]
    _VIEW_KEYS = ["name", "guid", "description", "metaClass", "fullPath"]

    def __init__(self) -> None:
        """Initialize the 'view' action."""
        super().__init__(command_id="view")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'view' subcommand and its arguments."""
        parser = sub_parser.add_parser("view", help="View package details")
        self.add_path_argument(parser, required=True, help_text="Package path to view")
        parser.add_argument("--output", default=None, help="Write output to file")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute package view."""
        super().execute(args)
        self.logger.info("Starting package view operation...")
        self.logger.info("Resolving package path '%s'...", args.path)
        package = self._resolve_and_validate_package(args.path)

        try:
            self.logger.info("Retrieving package details...")
            data = self._collect_package_data(package)
            output = self._format_output(data, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Writing output to file '%s'", args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to view package '{args.path}'")

    def _collect_package_data(self, package: IRPModelElement) -> Dict[str, str]:
        """Collect package details into a data dictionary."""
        return {
            "name": package.name,
            "guid": package.guid,
            "description": package.description,
            "metaClass": package.meta_class,
            "fullPath": package.get_full_path_name(),
        }

    def _format_output(self, data: Dict[str, str], format_type: str) -> str:
        """Format output based on format parameter."""
        if format_type == "json":
            return OutputFormatter.json_format(data)
        elif format_type == "csv":
            data_row = [data[key] for key in self._VIEW_KEYS]
            return OutputFormatter.csv_format(self._VIEW_HEADERS, [data_row])
        else:
            table_rows = [[k, v] for k, v in data.items()]
            return OutputFormatter.table(["Property", "Value"], table_rows)

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content via the shared helper (see actions.support)."""
        write_text_file(file_path, content)
