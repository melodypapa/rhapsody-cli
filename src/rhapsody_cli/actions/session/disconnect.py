"""DisconnectAction — split from session_action.py."""

import argparse
import logging

from rhapsody_cli.actions.abstract_action import RootCommandAction
from rhapsody_cli.application import RhapsodyApplication
from rhapsody_cli.exceptions import RhapsodyConnectionError
from rhapsody_cli.session import SessionManager

logger = logging.getLogger(__name__)


class DisconnectAction(RootCommandAction):
    """Action for `rhapsody-cli disconnect` — disconnect from Rhapsody."""

    def __init__(self) -> None:
        super().__init__(command_id="disconnect")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'disconnect' subcommand and its arguments."""
        parser = sub_parser.add_parser(self.command_id, help="Disconnect from Rhapsody")

    def execute(self, args: argparse.Namespace) -> None:
        """Disconnect from Rhapsody and clear session."""
        session_manager = SessionManager()
        session = session_manager.load()

        if not session:
            logger.info("Not connected")
            return

        # If instance was launched, quit Rhapsody
        if session.get("instance_type") == "launched":
            try:
                app = RhapsodyApplication.connect(attach_only=True)
                app.quit()
                logger.info("Closed Rhapsody instance")
            except RhapsodyConnectionError:
                logger.warning("Could not quit Rhapsody (may already be closed)")

        # Clear session file
        session_manager.clear()
        logger.info("Disconnected from Rhapsody")
