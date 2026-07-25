"""Tests for session actions (connect, disconnect, status, version)."""

import argparse
import json
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.actions.session_action import ConnectAction, DisconnectAction, StatusAction, VersionAction
from rhapsody_cli.exceptions import CliExecutionError, RhapsodyConnectionError
from rhapsody_cli.session import SessionManager


@pytest.mark.no_session
class TestConnectAction:
    """Tests for ConnectAction."""

    def test_connect_new_session(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect creates new session when none exists."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = ConnectAction()
            args = argparse.Namespace(timeout=None, attach_only=False, no_gui=False)

            action.execute(args)

        # Verify session file was created
        session_file = session_dir / "session.json"
        assert session_file.exists()

        session_data = json.loads(session_file.read_text())
        assert session_data["connected"] is True
        assert session_data["timeout_minutes"] == 5  # Default

    def test_connect_already_connected(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect informs user if already connected."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        session_data = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "timeout_minutes": 5,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        action = ConnectAction()
        args = argparse.Namespace(timeout=None, attach_only=False, no_gui=False)

        # Should not raise, just inform user
        action.execute(args)

    def test_connect_with_custom_timeout(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect uses custom timeout when provided."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = ConnectAction()
            args = argparse.Namespace(timeout=10, attach_only=False, no_gui=False)

            action.execute(args)

        session_file = session_dir / "session.json"
        session_data = json.loads(session_file.read_text())
        assert session_data["timeout_minutes"] == 10

    def test_connect_attach_only_success(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect with --attach-only attaches to existing instance."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app) as mock_connect:
            action = ConnectAction()
            args = argparse.Namespace(timeout=None, attach_only=True, no_gui=False)

            action.execute(args)

            # Verify connect was called with attach_only=True
            mock_connect.assert_called_once_with(attach_only=True, show_gui=True)

    def test_connect_attach_only_no_instance(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect with --attach-only fails when no instance running."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        with patch(
            "rhapsody_cli.actions.session_action.RhapsodyApplication.connect",
            side_effect=RhapsodyConnectionError("No running instance"),
        ):
            action = ConnectAction()
            args = argparse.Namespace(timeout=None, attach_only=True, no_gui=False)

            with pytest.raises(CliExecutionError, match="Failed to connect"):
                action.execute(args)

    def test_connect_with_no_gui(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect with --no-gui passes show_gui=False."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app) as mock_connect:
            action = ConnectAction()
            args = argparse.Namespace(timeout=None, attach_only=False, no_gui=True)

            action.execute(args)

            # Verify connect was called with show_gui=False
            mock_connect.assert_called_once_with(attach_only=False, show_gui=False)

    def test_connect_timeout_from_config(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect uses timeout from config file when not specified on CLI."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        config_file = session_dir / "config.json"
        config_file.write_text(json.dumps({"timeout_minutes": 15}))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = ConnectAction()
            args = argparse.Namespace(timeout=None, attach_only=False, no_gui=False)

            action.execute(args)

        session_file = session_dir / "session.json"
        session_data = json.loads(session_file.read_text())
        assert session_data["timeout_minutes"] == 15

    def test_connect_timeout_from_env(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect uses timeout from environment variable."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)
        monkeypatch.setenv("RHAPSODY_CLI_TIMEOUT", "20")

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = ConnectAction()
            args = argparse.Namespace(timeout=None, attach_only=False, no_gui=False)

            action.execute(args)

        session_file = session_dir / "session.json"
        session_data = json.loads(session_file.read_text())
        assert session_data["timeout_minutes"] == 20

    def test_connect_invalid_negative_timeout(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect handles negative timeout by using default."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = ConnectAction()
            args = argparse.Namespace(timeout=-5, attach_only=False, no_gui=False)

            action.execute(args)

        session_file = session_dir / "session.json"
        session_data = json.loads(session_file.read_text())
        assert session_data["timeout_minutes"] == 5  # Default

    def test_connect_zero_timeout(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Connect allows zero timeout (no timeout)."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = ConnectAction()
            args = argparse.Namespace(timeout=0, attach_only=False, no_gui=False)

            action.execute(args)

        session_file = session_dir / "session.json"
        session_data = json.loads(session_file.read_text())
        assert session_data["timeout_minutes"] == 0


@pytest.mark.no_session
class TestDisconnectAction:
    """Tests for DisconnectAction."""

    def test_disconnect_launched_instance(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Disconnect calls quit() for launched instances."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        session_data = {
            "connected": True,
            "instance_type": "launched",
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "timeout_minutes": 5,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = DisconnectAction()
            args = argparse.Namespace()

            action.execute(args)

        # Verify quit was called
        mock_app.quit.assert_called_once()

        # Verify session file was cleared
        assert not session_file.exists()

    def test_disconnect_attached_instance(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Disconnect clears session for attached instances without quitting."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        session_data = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "timeout_minutes": 5,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = DisconnectAction()
            args = argparse.Namespace()

            action.execute(args)

        # Verify quit was NOT called
        mock_app.quit.assert_not_called()

        # Verify session file was cleared
        assert not session_file.exists()

    def test_disconnect_not_connected(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Disconnect informs user when not connected."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        action = DisconnectAction()
        args = argparse.Namespace()

        # Should not raise, just inform user
        action.execute(args)

    def test_disconnect_launched_but_already_closed(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
        """Disconnect handles the case where launched instance was already closed."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        session_data = {
            "connected": True,
            "instance_type": "launched",
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "timeout_minutes": 5,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        with patch(
            "rhapsody_cli.actions.session_action.RhapsodyApplication.connect",
            side_effect=RhapsodyConnectionError("No instance"),
        ):
            action = DisconnectAction()
            args = argparse.Namespace()

            # Should not raise, just log warning and clear session
            action.execute(args)

        # Verify session file was cleared
        assert not session_file.exists()


@pytest.mark.no_session
class TestStatusAction:
    """Tests for StatusAction."""

    def test_status_connected(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
        """Status shows connection info when connected."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        session_data = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "timeout_minutes": 10,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = StatusAction()
            args = argparse.Namespace()

            action.execute(args)

        captured = capsys.readouterr()
        assert "Connected to Rhapsody" in captured.out
        assert "instance type: attached" in captured.out
        assert "Rhapsody version: 9.0.0" in captured.out

    def test_status_not_connected(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
        """Status shows 'Not connected' when no session."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        action = StatusAction()
        args = argparse.Namespace()

        action.execute(args)

        captured = capsys.readouterr()
        assert "Not connected" in captured.out

    def test_status_timed_out(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
        """Status shows timed out message when session expired."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        old_time = datetime.now() - timedelta(minutes=10)
        session_data = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": old_time.isoformat(),
            "last_activity": old_time.isoformat(),
            "timeout_minutes": 5,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        action = StatusAction()
        args = argparse.Namespace()

        action.execute(args)

        captured = capsys.readouterr()
        assert "Session timed out" in captured.out

    def test_status_zero_timeout(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
        """Status shows 'No timeout' when timeout is 0."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        session_data = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "timeout_minutes": 0,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = StatusAction()
            args = argparse.Namespace()

            action.execute(args)

        captured = capsys.readouterr()
        assert "Timeout: No timeout" in captured.out

    def test_status_rhapsody_not_running(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
        """Status handles Rhapsody not running gracefully."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        session_data = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "timeout_minutes": 10,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        with patch(
            "rhapsody_cli.actions.session_action.RhapsodyApplication.connect",
            side_effect=RhapsodyConnectionError("No instance"),
        ):
            action = StatusAction()
            args = argparse.Namespace()

            action.execute(args)

        captured = capsys.readouterr()
        assert "Warning: Rhapsody not running" in captured.out


@pytest.mark.no_session
class TestVersionAction:
    """Tests for VersionAction."""

    def test_version_shows_cli_version(self, capsys: pytest.CaptureFixture) -> None:
        """Version shows CLI version."""
        action = VersionAction()
        args = argparse.Namespace()

        action.execute(args)

        captured = capsys.readouterr()
        assert "rhapsody-cli version:" in captured.out

    def test_version_shows_rhapsody_version_when_connected(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
        """Version shows Rhapsody version when connected."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        session_data = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "timeout_minutes": 5,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        mock_app = MagicMock()
        mock_app.get_version.return_value = "9.0.0"

        with patch("rhapsody_cli.actions.session_action.RhapsodyApplication.connect", return_value=mock_app):
            action = VersionAction()
            args = argparse.Namespace()

            action.execute(args)

        captured = capsys.readouterr()
        assert "rhapsody-cli version:" in captured.out
        assert "Rhapsody version: 9.0.0" in captured.out

    def test_version_no_rhapsody_when_not_connected(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
        """Version shows only CLI version when not connected."""
        session_dir = tmp_path / ".rhapsody-cli"
        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        action = VersionAction()
        args = argparse.Namespace()

        action.execute(args)

        captured = capsys.readouterr()
        assert "rhapsody-cli version:" in captured.out
        assert "Rhapsody version" not in captured.out

    def test_version_handles_rhapsody_not_running(self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture) -> None:
        """Version handles Rhapsody not running gracefully when connected."""
        session_dir = tmp_path / ".rhapsody-cli"
        session_dir.mkdir(parents=True)
        session_file = session_dir / "session.json"

        session_data = {
            "connected": True,
            "instance_type": "attached",
            "connected_at": datetime.now().isoformat(),
            "last_activity": datetime.now().isoformat(),
            "timeout_minutes": 5,
        }
        session_file.write_text(json.dumps(session_data))

        monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)

        with patch(
            "rhapsody_cli.actions.session_action.RhapsodyApplication.connect",
            side_effect=RhapsodyConnectionError("No instance"),
        ):
            action = VersionAction()
            args = argparse.Namespace()

            action.execute(args)

        captured = capsys.readouterr()
        assert "rhapsody-cli version:" in captured.out
        # Should not crash, just not show Rhapsody version
        assert "Rhapsody version" not in captured.out
