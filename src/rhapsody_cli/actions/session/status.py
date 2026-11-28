"""StatusAction — split from session_action.py."""

"""Session actions - connect, disconnect, status, version."""

import argparse
import logging
from datetime import datetime, timedelta

from rhapsody_cli.actions.abstract_action import RootCommandAction
from rhapsody_cli.application import RhapsodyApplication
from rhapsody_cli.exceptions import RhapsodyConnectionError
from rhapsody_cli.session import SessionManager

logger = logging.getLogger(__name__)


class StatusAction(RootCommandAction):
    """Action for `rhapsody-cli status` — show connection status."""

    def __init__(self) -> None:
        super().__init__(command_id="status")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'status' subcommand and its arguments."""
        parser = sub_parser.add_parser(self.command_id, help="Show connection status")

    def execute(self, args: argparse.Namespace) -> None:
        """Show connection status."""
        # NOTE: All output below is the command's result data (not status/log
        # messages), written to stdout via print() so it stays safe for piping.
        session_manager = SessionManager()
        session = session_manager.load()

        if not session:
            print("Not connected")
            return

        if not session_manager.is_valid(session):
            print("Session timed out. Please connect again.")
            return

        # Show connection info
        print(f"Connected to Rhapsody (instance type: {session['instance_type']})")

        connected_at = datetime.fromisoformat(session["connected_at"])
        print(f"Connected at: {connected_at.strftime('%Y-%m-%d %H:%M:%S')}")

        last_activity = datetime.fromisoformat(session["last_activity"])
        print(f"Last activity: {last_activity.strftime('%Y-%m-%d %H:%M:%S')}")

        timeout_minutes = session["timeout_minutes"]
        if timeout_minutes == 0:
            print("Timeout: No timeout")
        else:
            elapsed = datetime.now() - last_activity
            remaining = timedelta(minutes=timeout_minutes) - elapsed
            if remaining.total_seconds() > 0:
                print(f"Timeout: {remaining.seconds // 60} minutes remaining")
            else:
                print("Timeout: Session expired")

        # Show Rhapsody version
        try:
            app = RhapsodyApplication.connect(attach_only=True)
            version = app.version()
            print(f"Rhapsody version: {version}")
        except RhapsodyConnectionError:
            print("Warning: Rhapsody not running")
