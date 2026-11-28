"""OperationListAction — split from operation_action.py."""

import argparse
import logging
from typing import List, cast

from rhapsody_cli.actions.operation.base import AbstractOperationAction
from rhapsody_cli.actions.support import write_text_file
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class OperationListAction(AbstractOperationAction):
    """List operations on a classifier.

    SWR_OP_00004: Operation List Command
    SWR_OP_00008: Multi-Format Output
    """

    def __init__(self) -> None:
        """Initialize the 'list' action."""
        super().__init__(command_id="list")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'list' subcommand and its arguments."""
        parser = sub_parser.add_parser("list", help="List operations on a classifier")
        self.add_path_argument(parser, required=True, help_text="Classifier path")
        parser.add_argument("--output", default=None, help="Write output to file")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute operation list."""
        super().execute(args)
        classifier = self._resolve_classifier(args.path)

        try:
            op_names = self._collect_operation_names(classifier)
            output = self._format_output(op_names, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Wrote %d operations to: %s", len(op_names), args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to list operations in '{args.path}'")

    def _collect_operation_names(self, classifier: IRPModelElement) -> List[str]:
        """Collect names of operations on a classifier."""
        operations = classifier.operations  # type: ignore[attr-defined]
        return [cast(IRPModelElement, op).name for op in operations]

    def _format_output(self, op_names: List[str], format_type: str) -> str:
        """Format output via the shared renderer (see _render_output)."""
        self.output_format = format_type
        return self._render_output(op_names, ["Name"], [[name] for name in op_names])

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
