"""Unit test configuration."""

import json
import sys
from datetime import datetime
from pathlib import Path

import pytest

# Add unit directory to Python path so imports work
sys.path.insert(0, str(Path(__file__).parent))


@pytest.fixture(autouse=True)
def mock_session(request: pytest.FixtureRequest, tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """Auto-use fixture: provide valid session for all tests.

    Creates a valid session.json in a temp directory and patches
    SessionManager.SESSION_DIR to use that path. This ensures
    existing tests don't break when session requirement is added.

    Skip for tests marked with @pytest.mark.no_session (tests that
    explicitly test session absence).
    """
    # Skip this fixture for tests that test session absence
    if "no_session" in request.keywords:
        return

    from rhapsody_cli.session import SessionManager

    session_dir = tmp_path / ".rhapsody-cli"
    session_dir.mkdir(parents=True, exist_ok=True)

    session_file = session_dir / "session.json"
    session_data = {
        "connected": True,
        "instance_type": "attached",
        "connected_at": datetime.now().isoformat(),
        "last_activity": datetime.now().isoformat(),
        "timeout_minutes": 30,  # Long timeout for tests
    }
    session_file.write_text(json.dumps(session_data))

    monkeypatch.setattr(SessionManager, "SESSION_DIR", session_dir)
