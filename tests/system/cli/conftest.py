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
from typing import Any

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
def cli_project(test_project_dir: Path) -> str:
    """Session-scoped test project created via Python API.

    Uses the Python API directly (not the subprocess CLI) to avoid
    UI dialogs and timeout issues with `project new`. The project
    is properly closed on teardown.

    Returns:
        The project name string.
    """
    project_name = "SystemTestProject"

    app = RhapsodyApplication.connect(attach_only=True)
    app.create_new_project(str(test_project_dir), project_name)

    yield project_name

    # Close project via Python API (not subprocess CLI, which is a no-op)
    app = RhapsodyApplication.connect(attach_only=True)
    for proj in app.get_projects():
        if proj.get_name() == project_name:
            proj.close()
            break
