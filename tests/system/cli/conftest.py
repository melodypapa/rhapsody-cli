"""CLI system test helpers and fixtures.

Provides subprocess CLI invocation helpers and a session-scoped
test project created via the Python API directly (not subprocess)
to avoid UI dialog and timeout issues.
"""

import json
import subprocess
import sys
import uuid
from pathlib import Path
from typing import Any, Generator

import pytest

from rhapsody_cli import RhapsodyApplication


def _run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    """Run the CLI as a subprocess.

    Args:
        *args: CLI arguments (e.g., "class", "create", "--path", "Pkg")

    Returns:
        CompletedProcess with stdout, stderr, returncode.
    """
    cmd = [sys.executable, "-m", "rhapsody_cli.cli.main", *args]
    return subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=30,
    )


def _run_cli_json(*args: str) -> Any:
    """Run the CLI with --format json and parse the JSON output.

    Args:
        *args: CLI arguments (without --format json, which is added automatically)

    Returns:
        Parsed JSON data from stdout.

    Raises:
        AssertionError: If the process exits non-zero or JSON parsing fails.
    """
    result = _run_cli(*args, "--format", "json")
    assert result.returncode == 0, f"CLI failed: {result.stderr}"
    return json.loads(result.stdout)


def _unique_name(prefix: str = "Test") -> str:
    """Generate a unique element name with UUID suffix.

    Args:
        prefix: Prefix for the name (e.g., "Cls", "Pkg")

    Returns:
        A unique name like "TestCls_a1b2c3d4".
    """
    return f"{prefix}_{uuid.uuid4().hex[:8]}"


@pytest.fixture(scope="session")
def cli_connection() -> Generator[None, None, None]:
    """Establish a CLI session connection via the subprocess.

    Establishes a single session that all CLI commands in the session will use.
    This avoids creating a new COM connection for each subprocess call.

    Cleans up the session file after tests complete to prevent unit tests
    from detecting it and trying to connect to Rhapsody.

    Yields:
        None — the session is established as a side effect.
    """
    result = _run_cli("connect")
    assert result.returncode == 0, f"Failed to connect via CLI: {result.stderr}"
    yield
    # Clean up: disconnect to clear session file
    _run_cli("disconnect")


@pytest.fixture(scope="session")
def cli_project(test_project_dir: Path, cli_connection: None) -> Generator[str, None, None]:
    """Session-scoped test project created via Python API.

    Uses the Python API directly (not the subprocess CLI) to avoid
    UI dialogs and timeout issues with `project new`. The project
    is properly closed on teardown.

    Attaches to the existing Rhapsody instance that was launched by cli_connection.
    Does not kill or restart Rhapsody to preserve the CLI session.

    Depends on cli_connection to ensure a session is established first.

    Returns:
        The project name string.
    """
    project_name = "SystemTestProject"

    # Attach to existing Rhapsody instance (launched by cli_connection)
    app = RhapsodyApplication.connect(attach_only=True)
    app.create_new_project(str(test_project_dir), project_name)

    yield project_name

    # Close project via Python API
    try:
        app = RhapsodyApplication.connect(attach_only=True)
        for proj in app.get_projects():
            if proj.get_name() == project_name:
                proj.close()
                break
    except Exception:
        pass  # If connection fails, instance may already be closed
