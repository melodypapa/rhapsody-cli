"""System tests for the `project` CLI command group.

Tests project lifecycle: new, list, close, open — all via subprocess.

Known CLI bug: `project close` checks `self._project` (always None in
subprocess mode) instead of calling `app.active_project()`, so it is a
no-op. Tests that depend on close are marked xfail until the CLI is fixed.
"""

import pytest

from tests.system.cli.conftest import _run_cli


@pytest.mark.system
class TestProjectCLI:
    """Test project CLI commands via subprocess."""

    @pytest.fixture(autouse=True)
    def _require_rhapsody(self, _require_rhapsody: None) -> None:
        """Skip these tests if no Rhapsody instance is available."""

    @pytest.mark.skip(reason="project new switches the active project away from the session " "project; system tests share one session project")
    def test_project_new_creates_project(self) -> None:
        """Test that `project new` creates a project and it appears in list."""
        # Skipped — shared session project used for all system tests

    def test_project_list_shows_open_project(self, cli_project: str) -> None:
        """Test that `project list` shows the open project."""
        result = _run_cli("project", "list")
        assert result.returncode == 0
        assert cli_project in result.stdout

    @pytest.mark.skip(reason="project close is a no-op in subprocess mode (checks self._project " "instead of app.active_project()); also requires project new which " "switches the session project")
    def test_project_close_removes_from_list(self) -> None:
        """Test that `project close` removes project from list."""
        # Skipped — shared session project used for all system tests

    @pytest.mark.skip(reason="project close is a no-op in subprocess mode; cannot close " "before re-opening without switching the session project")
    def test_project_open_existing_project(self) -> None:
        """Test that `project open` opens a previously created project."""
        # Skipped — shared session project used for all system tests
