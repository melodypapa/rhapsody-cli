"""PortDeleteAction — split from port_action.py."""

import argparse
import logging

from rhapsody_cli.actions.port.base import AbstractPortAction
from rhapsody_cli.exceptions import CliExecutionError

logger = logging.getLogger(__name__)


class PortDeleteAction(AbstractPortAction):
    """Delete a port.

    SWR_PORT_00002: Port Delete Command
    SWR_PORT_00010: GUID Lookup Support
    """

    def __init__(self) -> None:
        """Initialize the 'delete' action."""
        super().__init__(command_id="delete")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'delete' subcommand and its arguments."""
        parser = sub_parser.add_parser("delete", help="Delete a port")
        self.add_path_argument(parser, required=False, help_text="Parent classifier path")
        parser.add_argument("--guid", default=None, help="Port GUID to delete")
        parser.add_argument("--name", default=None, help="Port name within classifier")

    def execute(self, args: argparse.Namespace) -> None:
        """Execute port deletion."""
        super().execute(args)
        has_path_name = args.path and args.name
        has_guid = args.guid is not None

        if has_path_name and has_guid:
            raise CliExecutionError("Only one of --path + --name or --guid may be specified")
        if not has_path_name and not has_guid:
            raise CliExecutionError("Either --path + --name or --guid must be specified")

        if has_guid:
            port = self._resolve_port_by_guid(args.guid)
            label = f"GUID '{args.guid}'"
        else:
            classifier = self._resolve_classifier(args.path)
            port = self._resolve_port(classifier, args.name)
            label = args.name

        try:
            port.delete_from_project()
            self.logger.info("Deleted port: %s", label)
        except Exception as e:
            self._handle_execution_error(e, f"Failed to delete port '{label}'")
