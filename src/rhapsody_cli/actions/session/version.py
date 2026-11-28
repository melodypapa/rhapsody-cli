"""VersionAction — split from session_action.py."""

import argparse
import logging

from rhapsody_cli import __version__
from rhapsody_cli.actions.abstract_action import RootCommandAction
from rhapsody_cli.application import RhapsodyApplication
from rhapsody_cli.exceptions import RhapsodyConnectionError
from rhapsody_cli.session import SessionManager

logger = logging.getLogger(__name__)


class VersionAction(RootCommandAction):
    """Action for `rhapsody-cli version` — show CLI version."""

    def __init__(self) -> None:
        super().__init__(command_id="version")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'version' subcommand and its arguments."""
        parser = sub_parser.add_parser(self.command_id, help="Show CLI version")

    def execute(self, args: argparse.Namespace) -> None:
        """Show CLI version and optionally Rhapsody version."""
        # NOTE: Version output is the command's result data, written to stdout
        # via print() so it stays safe for piping (e.g. `rhapsody-cli version`).
        print(f"rhapsody-cli version: {__version__}")

        # Try to show Rhapsody version if connected
        session_manager = SessionManager()
        session = session_manager.load()

        if session and session_manager.is_valid(session):
            try:
                app = RhapsodyApplication.connect(attach_only=True)
                version = app.version()
                print(f"Rhapsody version: {version}")
            except RhapsodyConnectionError:
                pass  # Not running, that's OK
