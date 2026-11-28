"""ClassListAction — split from class_action.py."""

import argparse
import logging
from typing import List, cast

from rhapsody_cli.actions.classifier.base import AbstractClassAction
from rhapsody_cli.actions.support import write_text_file
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class ClassListAction(AbstractClassAction):
    """List classes in a package.

    SWR_CLS_00004: Class List Command
    SWR_CLS_00008: Multi-Format Output
    """

    def __init__(self) -> None:
        """Initialize the 'list' action."""
        super().__init__(command_id="list")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'list' subcommand and its arguments."""
        parser = sub_parser.add_parser("list", help="List classes in a package")
        self.add_path_argument(parser, required=True, help_text="Package path")
        parser.add_argument("--output", default=None, help="Write output to file")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute class list."""
        super().execute(args)
        package = self._resolve_and_validate_package(args.path)

        try:
            class_names = self._collect_class_names(package)
            output = self._format_output(class_names, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Wrote %d classes to: %s", len(class_names), args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to list classes in '{args.path}'")

    def _collect_class_names(self, package: IRPModelElement) -> List[str]:
        """Collect names of classes in package."""
        classes = package.classes  # type: ignore[attr-defined]
        return [cast(IRPModelElement, cls).name for cls in classes]

    def _format_output(self, class_names: List[str], format_type: str) -> str:
        """Format output via the shared renderer (see _render_output)."""
        self.output_format = format_type
        return self._render_output(class_names, ["Name"], [[name] for name in class_names])

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content via the shared helper (see actions.support)."""
        write_text_file(file_path, content)
