"""Session actions - connect, disconnect, status, version."""

import argparse
import json
import logging
import os
from datetime import datetime, timedelta

from rhapsody_cli.actions.abstract_action import AbstractAction
from rhapsody_cli.application import RhapsodyApplication
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.session import Session, SessionManager

logger = logging.getLogger(__name__)


class ConnectAction(AbstractAction):
    """Action for `rhapsody-cli connect` — connect to Rhapsody.

    Creates a session file if connection succeeds. Informs user if already connected.
    """

    def __init__(self) -> None:
        super().__init__(command_id="connect")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'connect' subcommand and its arguments."""
        parser = sub_parser.add_parser(self.command_id, help="Connect to Rhapsody")
        parser.add_argument("--timeout", type=int, help="Session timeout in minutes (default: 5, 0=no timeout)")
        parser.add_argument("--attach-only", action="store_true", help="Only attach to existing instance")
        parser.add_argument("--no-gui", action="store_true", help="Keep GUI hidden when launching new instance")
        self.add_verbose_argument(parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Connect to Rhapsody and create session."""
        session_manager = SessionManager()

        # Check if already connected
        existing_session = session_manager.load()
        if existing_session and session_manager.is_valid(existing_session):
            logger.info("Already connected to Rhapsody (instance type: %s)", existing_session["instance_type"])
            return

        # Get timeout from args, config, env, or default
        timeout = self._get_timeout(args)

        # Connect to Rhapsody
        try:
            show_gui = not args.no_gui
            RhapsodyApplication.connect(attach_only=args.attach_only, show_gui=show_gui)

            # Determine instance type
            # If attach_only succeeded, we attached; otherwise we launched
            instance_type = "attached" if args.attach_only else "launched"

            # If not attach_only, we need to check if we actually attached or launched
            # by checking if a session already existed before connect
            if not args.attach_only and existing_session is None:
                # First connection attempt - connect() tries attach first, then launches
                # We can't easily distinguish, but this is a reasonable heuristic
                instance_type = "launched"  # Assume launched if first connect

            # Create session
            now = datetime.now()
            session: Session = {
                "connected": True,
                "instance_type": instance_type,
                "connected_at": now.isoformat(),
                "last_activity": now.isoformat(),
                "timeout_minutes": timeout,
            }
            session_manager.save(session)

            logger.info("Connected to Rhapsody (instance type: %s, timeout: %d minutes)", instance_type, timeout)

        except RhapsodyConnectionError as e:
            raise CliExecutionError(f"Failed to connect to Rhapsody: {e}") from e

    def _get_timeout(self, args: argparse.Namespace) -> int:
        """Get timeout from args, config file, env var, or default.

        Priority: CLI flag > config file > env var > default (5).

        Args:
            args: Parsed command-line arguments.

        Returns:
            Timeout in minutes (0 = no timeout).
        """
        # 1. CLI flag
        if args.timeout is not None:
            if args.timeout < 0:
                logger.warning("Invalid timeout %d, using default (5 minutes)", args.timeout)
                return 5
            return args.timeout

        # 2. Config file
        config_file = SessionManager.SESSION_DIR / "config.json"
        if config_file.exists():
            try:
                config = json.loads(config_file.read_text())
                if "timeout_minutes" in config:
                    timeout = int(config["timeout_minutes"])
                    if timeout < 0:
                        logger.warning("Invalid timeout in config, using default")
                        return 5
                    return timeout
            except (json.JSONDecodeError, ValueError) as e:
                logger.warning("Failed to read config file: %s", e)

        # 3. Environment variable
        env_timeout = os.environ.get("RHAPSODY_CLI_TIMEOUT")
        if env_timeout:
            try:
                timeout = int(env_timeout)
                if timeout < 0:
                    logger.warning("Invalid RHAPSODY_CLI_TIMEOUT, using default")
                    return 5
                return timeout
            except ValueError as e:
                logger.warning("Invalid RHAPSODY_CLI_TIMEOUT: %s", e)

        # 4. Default
        return 5


class DisconnectAction(AbstractAction):
    """Action for `rhapsody-cli disconnect` — disconnect from Rhapsody."""

    def __init__(self) -> None:
        super().__init__(command_id="disconnect")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'disconnect' subcommand and its arguments."""
        parser = sub_parser.add_parser(self.command_id, help="Disconnect from Rhapsody")
        self.add_verbose_argument(parser)

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


class StatusAction(AbstractAction):
    """Action for `rhapsody-cli status` — show connection status."""

    def __init__(self) -> None:
        super().__init__(command_id="status")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'status' subcommand and its arguments."""
        parser = sub_parser.add_parser(self.command_id, help="Show connection status")
        self.add_verbose_argument(parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Show connection status."""
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
            version = app.get_version()
            print(f"Rhapsody version: {version}")
        except RhapsodyConnectionError:
            print("Warning: Rhapsody not running")


class VersionAction(AbstractAction):
    """Action for `rhapsody-cli version` — show CLI version."""

    def __init__(self) -> None:
        super().__init__(command_id="version")

    def init_arguments(self, sub_parser: "argparse._SubParsersAction[argparse.ArgumentParser]") -> None:
        """Register the 'version' subcommand and its arguments."""
        parser = sub_parser.add_parser(self.command_id, help="Show CLI version")
        self.add_verbose_argument(parser)

    def execute(self, args: argparse.Namespace) -> None:
        """Show CLI version and optionally Rhapsody version."""
        from rhapsody_cli import __version__

        print(f"rhapsody-cli version: {__version__}")

        # Try to show Rhapsody version if connected
        session_manager = SessionManager()
        session = session_manager.load()

        if session and session_manager.is_valid(session):
            try:
                app = RhapsodyApplication.connect(attach_only=True)
                version = app.get_version()
                print(f"Rhapsody version: {version}")
            except RhapsodyConnectionError:
                pass  # Not running, that's OK
