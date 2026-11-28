"""ConnectAction — split from session_action.py."""

import argparse
import json
import logging
import os
from datetime import datetime

from rhapsody_cli.actions.abstract_action import RootCommandAction
from rhapsody_cli.application import RhapsodyApplication
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.session import Session, SessionManager

logger = logging.getLogger(__name__)


class ConnectAction(RootCommandAction):
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
            return int(args.timeout)

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
