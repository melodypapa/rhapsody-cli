"""AttributeListAction — split from attribute_action.py."""

import argparse
import logging
from typing import List, cast

from rhapsody_cli.actions.attribute.base import AbstractAttributeAction
from rhapsody_cli.actions.support import write_text_file
from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

logger = logging.getLogger(__name__)


class AttributeListAction(AbstractAttributeAction):
    """List attributes on a classifier.

    SWR_ATTR_00004: Attribute List Command
    SWR_ATTR_00008: Multi-Format Output
    """

    def __init__(self) -> None:
        """Initialize the 'list' action."""
        super().__init__(command_id="list")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'list' subcommand and its arguments."""
        parser = sub_parser.add_parser("list", help="List attributes on a classifier")
        self.add_path_argument(parser, required=True, help_text="Classifier path")
        parser.add_argument("--output", default=None, help="Write output to file")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute attribute list."""
        super().execute(args)
        classifier = self._resolve_classifier(args.path)

        try:
            attr_names = self._collect_attribute_names(classifier)
            output = self._format_output(attr_names, args.format)

            if args.output:
                self._write_to_file(args.output, output)
                self.logger.info("Wrote %d attributes to: %s", len(attr_names), args.output)
            else:
                # NOTE: Result data to stdout (not logger) so it stays safe for piping/redirection.
                print(output)
        except CliExecutionError:
            raise
        except Exception as e:
            self._handle_execution_error(e, f"Failed to list attributes in '{args.path}'")

    def _collect_attribute_names(self, classifier: IRPModelElement) -> List[str]:
        """Collect names of attributes on a classifier."""
        attributes = classifier.attributes  # type: ignore[attr-defined]
        return [cast(IRPModelElement, attr).name for attr in attributes]

    def _format_output(self, attr_names: List[str], format_type: str) -> str:
        """Format output via the shared renderer (see _render_output)."""
        self.output_format = format_type
        return self._render_output(attr_names, ["Name"], [[name] for name in attr_names])

    def _write_to_file(self, file_path: str, content: str) -> None:
        """Write content via the shared helper (see actions.support)."""
        write_text_file(file_path, content)
