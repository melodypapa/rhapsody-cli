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

    def test_project_new_creates_project(self, test_project_dir) -> None:
        """Test that `project new` creates a project and it appears in list."""
        import shutil

        project_dir = test_project_dir / "new_test"
        project_dir.mkdir(parents=True, exist_ok=True)
        project_name = f"ProjNew_{__import__('uuid').uuid4().hex[:8]}"

        try:
            result = _run_cli("project", "new", str(project_dir), project_name)
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify project appears in list
            list_result = _run_cli("project", "list")
            assert list_result.returncode == 0
            assert project_name in list_result.stdout
        finally:
            shutil.rmtree(project_dir, ignore_errors=True)

    def test_project_list_shows_open_project(self, cli_project: str) -> None:
        """Test that `project list` shows the open project."""
        result = _run_cli("project", "list")
        assert result.returncode == 0
        assert cli_project in result.stdout

    @pytest.mark.xfail(
        reason="CLI bug: project close checks self._project (always None in "
        "subprocess mode) instead of app.active_project(); no-op until fixed"
    )
    def test_project_close_removes_from_list(self, test_project_dir) -> None:
        """Test that `project close` removes project from list."""
        import shutil

        project_dir = test_project_dir / "close_test"
        project_dir.mkdir(parents=True, exist_ok=True)
        project_name = f"ProjClose_{__import__('uuid').uuid4().hex[:8]}"

        try:
            _run_cli("project", "new", str(project_dir), project_name)
            _run_cli("project", "close")

            result = _run_cli("project", "list")
            assert result.returncode == 0
            assert project_name not in result.stdout
        finally:
            shutil.rmtree(project_dir, ignore_errors=True)

    @pytest.mark.xfail(
        reason="CLI bug: project close is a no-op in subprocess mode; cannot "
        "close before re-opening"
    )
    def test_project_open_existing_project(self, test_project_dir) -> None:
        """Test that `project open` opens a previously created project."""
        import shutil

        project_dir = test_project_dir / "open_test"
        project_dir.mkdir(parents=True, exist_ok=True)
        project_name = f"ProjOpen_{__import__('uuid').uuid4().hex[:8]}"

        try:
            # Create and close
            _run_cli("project", "new", str(project_dir), project_name)
            _run_cli("project", "close")

            # Re-open
            project_file = project_dir / f"{project_name}.rpy"
            result = _run_cli("project", "open", str(project_file))
            assert result.returncode == 0, f"Failed: {result.stderr}"

            # Verify in list
            list_result = _run_cli("project", "list")
            assert list_result.returncode == 0
            assert project_name in list_result.stdout
        finally:
            shutil.rmtree(project_dir, ignore_errors=True)
