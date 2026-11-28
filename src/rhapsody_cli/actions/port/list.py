"""PortListAction — split from port_action.py."""

import argparse
import logging
from typing import List, cast

from rhapsody_cli.actions.port.base import AbstractPortAction
from rhapsody_cli.actions.support import write_text_file
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class PortListAction(AbstractPortAction):
    """List ports on a classifier.

    SWR_PORT_00004: Port List Command
    SWR_PORT_00008: Multi-Format Output
    """

    def __init__(self) -> None:
        """Initialize the 'list' action."""
        super().__init__(command_id="list")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'list' subcommand and its arguments."""
        parser = sub_parser.add_parser("list", help="List ports on a classifier")
        self.add_path_argument(parser, required=True, help_text="Classifier path")
        parser.add_argument("--output", default=None, help="Write output to file")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port list."""
        super().execute(args)
        classifier = self._resolve_classifier(args.path)

        try:
            port_names = self._collect_port_names(classifier)
            output = self._format_output(port_names, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Wrote %d ports to: %s", len(port_names), args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to list ports in '{args.path}'")

    def _collect_port_names(self, classifier: IRPModelElement) -> List[str]:
        """Collect names of ports on a classifier."""
        ports = classifier.ports  # type: ignore[attr-defined]
        return [cast(IRPModelElement, port).name for port in ports]

    def _format_output(self, port_names: List[str], format_type: str) -> str:
        """Format output via the shared renderer (see _render_output)."""
        self.output_format = format_type
        return self._render_output(port_names, ["Name"], [[name] for name in port_names])

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content via the shared helper (see actions.support)."""
        write_text_file(file_path, content)
