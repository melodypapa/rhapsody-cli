"""PackageListAction — split from package_action.py."""

import argparse
import logging
from typing import List, cast

from rhapsody_cli.actions.package.base import AbstractPackageAction
from rhapsody_cli.actions.support import write_text_file
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class PackageListAction(AbstractPackageAction):
    """List nested packages.

    SWR_PKG_0004: Package List Command
    SWR_PKG_0008: Multi-Format Output
    """

    def __init__(self) -> None:
        """Initialize the 'list' action."""
        super().__init__(command_id="list")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'list' subcommand and its arguments."""
        parser = sub_parser.add_parser("list", help="List nested packages")
        self.add_path_argument(parser, required=True, help_text="Package path")
        parser.add_argument("--output", default=None, help="Write output to file")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute package list."""
        super().execute(args)
        self.logger.info("Starting package list operation...")
        self.logger.info("Resolving package path '%s'...", args.path)
        package = self._resolve_and_validate_package(args.path)

        try:
            self.logger.info("Listing nested packages...")
            package_names = self._collect_nested_package_names(package)
            if package_names:
                self.logger.info("Found %d nested package%s", len(package_names), "s" if len(package_names) != 1 else "")
            else:
                self.logger.info("No nested packages found")
            output = self._format_output(package_names, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Writing output to file '%s'", args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to list packages in '{args.path}'")

    def _collect_nested_package_names(self, package: IRPModelElement) -> List[str]:
        """Collect names of nested packages."""
        nested_packages = package.packages  # type: ignore[attr-defined]
        return [cast(IRPModelElement, pkg).name for pkg in nested_packages]

    def _format_output(self, package_names: List[str], format_type: str) -> str:
        """Format output via the shared renderer (see _render_output)."""
        self.output_format = format_type
        return self._render_output(package_names, ["Name"], [[name] for name in package_names])

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content to file."""
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        except OSError as e:
            raise CliExecutionError(f"Failed to write file '{file_path}': {e}") from e

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content via the shared helper (see actions.support)."""
        write_text_file(file_path, content)
