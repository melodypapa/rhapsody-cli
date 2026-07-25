"""Session management for rhapsody-cli."""

import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional, TypedDict, cast

logger = logging.getLogger(__name__)


class Session(TypedDict):
    """Session state stored in session.json.

    Attributes:
        connected: True if session is active.
        instance_type: "attached" (existing instance) or "launched" (new instance).
        connected_at: ISO 8601 timestamp when connection was established.
        last_activity: ISO 8601 timestamp of last command execution.
        timeout_minutes: Session timeout duration in minutes (0 = no timeout).
    """

    connected: bool
    instance_type: str
    connected_at: str
    last_activity: str
    timeout_minutes: int


class SessionManager:
    """Manages session file I/O and validation."""

    SESSION_DIR: Path = Path.home() / ".rhapsody-cli"
    SESSION_FILE: str = "session.json"

    def _session_path(self) -> Path:
        """Return the path to the session file."""
        return self.SESSION_DIR / self.SESSION_FILE

    def load(self) -> Optional[Session]:
        """Load session from file, return None if not exists or malformed.

        Returns:
            Session dict if valid file exists, None otherwise.
        """
        session_file = self._session_path()
        if not session_file.exists():
            return None

        try:
            data = json.loads(session_file.read_text())
            # Validate required fields
            required = ["connected", "instance_type", "connected_at", "last_activity", "timeout_minutes"]
            if not all(key in data for key in required):
                logger.warning("Session file missing required fields")
                return None
            return cast(Session, data)
        except json.JSONDecodeError:
            logger.warning("Session file contains invalid JSON")
            return None
        except Exception as e:
            logger.warning("Failed to load session file: %s", e)
            return None

    def save(self, session: Session) -> None:
        """Save session to file, creating directory if needed.

        Args:
            session: The session dict to save.
        """
        self.SESSION_DIR.mkdir(parents=True, exist_ok=True)
        session_file = self._session_path()
        session_file.write_text(json.dumps(session, indent=2))
        logger.debug("Saved session to %s", session_file)

    def clear(self) -> None:
        """Clear session file if it exists."""
        session_file = self._session_path()
        if session_file.exists():
            session_file.unlink()
            logger.debug("Cleared session file")

    def is_valid(self, session: Session) -> bool:
        """Check if session is valid (connected and not timed out).

        Args:
            session: The session to validate.

        Returns:
            True if session is connected and within timeout, False otherwise.
        """
        if not session.get("connected", False):
            return False

        timeout_minutes = session.get("timeout_minutes", 5)
        if timeout_minutes < 0:
            timeout_minutes = 5  # Use default for invalid values

        # timeout_minutes == 0 means no timeout
        if timeout_minutes == 0:
            return True

        try:
            last_activity = datetime.fromisoformat(session["last_activity"])
            now = datetime.now()
            elapsed = now - last_activity
            return elapsed < timedelta(minutes=timeout_minutes)
        except (KeyError, ValueError) as e:
            logger.warning("Failed to parse session timestamps: %s", e)
            return False

    def update_activity(self, session: Session) -> None:
        """Update last_activity timestamp to current time.

        Args:
            session: The session to update (modified in place).
        """
        session["last_activity"] = datetime.now().isoformat()
        self.save(session)
