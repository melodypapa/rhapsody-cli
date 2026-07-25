"""Tests for SessionManager and Session type."""

import json
from datetime import datetime, timedelta
from pathlib import Path
from typing import TypedDict

import pytest


class Session(TypedDict):
    """Session state stored in session.json."""

    connected: bool
    instance_type: str  # "attached" or "launched"
    connected_at: str  # ISO 8601
    last_activity: str  # ISO 8601
    timeout_minutes: int


@pytest.mark.no_session
class TestSessionType:
    """Tests for Session TypedDict."""

    def test_session_has_required_fields(self) -> None:
        """Session must have all required fields."""
        session: Session = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": "2026-07-25T10:00:00Z",
            "last_activity": "2026-07-25T10:30:00Z",
            "timeout_minutes": 5,
        }
        assert session["connected"] is True
        assert session["instance_type"] == "attached"
        assert session["timeout_minutes"] == 5


@pytest.mark.no_session
class TestSessionManagerLoad:
    """Tests for SessionManager.load()."""

    def test_load_no_session_file(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """load() returns None when session file doesn't exist."""
        from rhapsody_cli.session import SessionManager

        monkeypatch.setattr(SessionManager, "SESSION_DIR", tmp_path / ".rhapsody-cli")
        manager = SessionManager()
        result = manager.load()
        assert result is None

    def test_load_valid_session(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """load() returns Session dict when valid session file exists."""
        from rhapsody_cli.session import SessionManager

        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"
        session_data = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": "2026-07-25T10:00:00Z",
            "last_activity": "2026-07-25T10:30:00Z",
            "timeout_minutes": 5,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)
        manager = SessionManager()
        result = manager.load()

        assert result is not None
        assert result["connected"] is True
        assert result["instance_type"] == "attached"
        assert result["timeout_minutes"] == 5

    def test_load_corrupted_session(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """load() returns None and logs warning when session file is malformed."""
        from rhapsody_cli.session import SessionManager

        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"
        session_file.write_text("{ invalid json }")

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)
        manager = SessionManager()
        result = manager.load()

        assert result is None


@pytest.mark.no_session
class TestSessionManagerSave:
    """Tests for SessionManager.save()."""

    def test_save_creates_directory_and_file(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """save() creates .rhapsody-cli directory and session.json if needed."""
        from rhapsody_cli.session import Session, SessionManager

        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        session: Session = {
            "connected": True,
            "instance_type": "launched",
            "connected_at": "2026-07-25T11:00:00Z",
            "last_activity": "2026-07-25T11:00:00Z",
            "timeout_minutes": 10,
        }

        manager = SessionManager()
        manager.save(session)

        assert session_dir.exists()
        session_file = session_dir / "session.json"
        assert session_file.exists()

        loaded = json.loads(session_file.read_text())
        assert loaded["connected"] is True
        assert loaded["instance_type"] == "launched"
        assert loaded["timeout_minutes"] == 10


@pytest.mark.no_session
class TestSessionManagerClear:
    """Tests for SessionManager.clear()."""

    def test_clear_removes_session_file(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """clear() removes session.json file."""
        from rhapsody_cli.session import SessionManager

        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"
        session_file.write_text(json.dumps({"connected": True}))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)
        manager = SessionManager()
        manager.clear()

        assert not session_file.exists()


@pytest.mark.no_session
class TestSessionManagerIsValid:
    """Tests for SessionManager.is_valid()."""

    def test_is_valid_connected_not_timed_out(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """is_valid() returns True for connected session within timeout."""
        from rhapsody_cli.session import Session, SessionManager

        now = datetime.now()
        session: Session = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": now.isoformat(),
            "last_activity": now.isoformat(),
            "timeout_minutes": 5,
        }

        manager = SessionManager()
        result = manager.is_valid(session)
        assert result is True

    def test_is_valid_timed_out(self, monkeypatch: pytest.MonkeyPatch) -> None:
        """is_valid() returns False for session past timeout."""
        from rhapsody_cli.session import Session, SessionManager

        old_activity = datetime.now() - timedelta(minutes=10)
        session: Session = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": old_activity.isoformat(),
            "last_activity": old_activity.isoformat(),
            "timeout_minutes": 5,
        }

        manager = SessionManager()
        result = manager.is_valid(session)
        assert result is False

    def test_is_valid_disconnected(self) -> None:
        """is_valid() returns False for disconnected session."""
        from rhapsody_cli.session import Session, SessionManager

        now = datetime.now()
        session: Session = {
            "connected": False,
            "instance_type": "attached",
            "connected_at": now.isoformat(),
            "last_activity": now.isoformat(),
            "timeout_minutes": 5,
        }

        manager = SessionManager()
        result = manager.is_valid(session)
        assert result is False

    def test_is_valid_zero_timeout(self) -> None:
        """is_valid() returns True for timeout=0 (no timeout)."""
        from rhapsody_cli.session import Session, SessionManager

        old_activity = datetime.now() - timedelta(minutes=100)
        session: Session = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": old_activity.isoformat(),
            "last_activity": old_activity.isoformat(),
            "timeout_minutes": 0,
        }

        manager = SessionManager()
        result = manager.is_valid(session)
        assert result is True


@pytest.mark.no_session
class TestSessionManagerUpdateActivity:
    """Tests for SessionManager.update_activity()."""

    def test_update_activity_updates_timestamp(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """update_activity() updates last_activity to current time."""
        from rhapsody_cli.session import Session, SessionManager

        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        old_time = datetime.now() - timedelta(minutes=5)
        session: Session = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": old_time.isoformat(),
            "last_activity": old_time.isoformat(),
            "timeout_minutes": 5,
        }

        manager = SessionManager()
        manager.update_activity(session)

        # Check that last_activity was updated
        assert session["last_activity"] != old_time.isoformat()

        # Verify it's recent (within 1 second)
        last_activity = datetime.fromisoformat(session["last_activity"])
        now = datetime.now()
        assert (now - last_activity).total_seconds() < 1.0
