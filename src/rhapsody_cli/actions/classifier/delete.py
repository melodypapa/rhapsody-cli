"""ClassDeleteAction — split from class_action.py."""

import argparse
import logging

from rhapsody_cli.actions.classifier.base import AbstractClassAction
from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)


class ClassDeleteAction(AbstractClassAction):
    """Delete a class.

    SWR_CLS_00002: Class Delete Command
    SWR_CLS_00013: GUID Lookup Support
    """

    def __init__(self) -> None:
        """Initialize the 'delete' action."""
        super().__init__(command_id="delete")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'delete' subcommand and its arguments."""
        parser = sub_parser.add_parser("delete", help="Delete a class")
        self.add_path_argument(parser, required=False, help_text="Class path to delete")
        parser.add_argument("--guid", default=None, help="Class GUID to delete")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute class deletion."""
        super().execute(args)
        if args.path and args.guid:
            raise CliExecutionError("Only one of --path or --guid may be specified")
        if not args.path and not args.guid:
            raise CliExecutionError("Either --path or --guid must be specified")

        if args.guid:
            cls = self._resolve_class_by_guid(args.guid)
            label = f"GUID '{args.guid}'"
        else:
            cls = self._resolve_and_validate_class(args.path)
            label = args.path

        try:
            cls.delete_from_project()
            self.logger.info("Deleted class: %s", label)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to delete class '{label}'")
