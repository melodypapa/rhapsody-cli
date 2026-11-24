"""Integration test configuration."""

import os
import shutil
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Generator, Optional
from unittest.mock import patch

import pytest
from pytest import Config, FixtureRequest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject

# Add unit directory to Python path so imports from unit tests work
sys.path.insert(0, str(Path(__file__).parent.parent / "unit"))

TEST_PROJECT_DIR = Path(__file__).parent.parent.parent / "demos" / "test_project"
TEST_PROJECT_NAME = "TestProject"


def pytest_addoption(parser: Config) -> None:
    """Add custom command line options for integration tests."""
    parser.addoption(
        "--keep-test-artifacts",
        action="store_true",
        default=False,
        help="Keep test artifacts after integration test run for debugging",
    )


def _safe_cleanup_test_project(app: RhapsodyApplication, project_dir: Path) -> None:
    """Safely clean up test project with proper file handle management.

    This function implements proper cleanup sequence to avoid file lock issues:
    1. Close all projects to release COM file handles
    2. Wait for Windows file system to release locks
    3. Delete the project directory

    Note: Auto-save is now enabled when projects are created/opened,
    so saves are handled automatically without explicit save calls.

    Args:
        app: The Rhapsody application instance
        project_dir: Path to the project directory to clean up
    """
    try:
        # Close all open projects first to release COM file handles.
        # IRPApplication exposes no closeAllProjects COM member, so close each
        # project individually through its exposed close() member.
        for project in app.projects:
            try:
                project.close()
            except Exception as exc:
                print(f"Warning: could not close project {project.name!r}: {exc}")

        # Wait a moment for file handles to be released (Windows file system latency)
        time.sleep(0.5)

        # Now safe to delete directory
        if project_dir.exists():
            shutil.rmtree(project_dir)

    except Exception as e:
        print(f"Warning: Could not fully clean up test project: {e}")
        # Try to at least remove files we can individually
        if project_dir.exists():
            try:
                for item in project_dir.iterdir():
                    if item.is_file():
                        try:
                            item.unlink()
                        except Exception:
                            # Skip files that are still locked
                            pass
            except Exception:
                # If we can't clean up files, at least we tried
                pass


@pytest.fixture(scope="session")
def rhapsody_app(rhapsody_instance: Optional[RhapsodyApplication], request: FixtureRequest) -> Optional[RhapsodyApplication]:
    """Session-scoped Rhapsody application fixture.

    Uses the shared ``rhapsody_instance`` owner (see ``tests/conftest.py``) rather
    than launching its own, so the Rhapsody lifecycle is owned in exactly one
    place. Returns ``None`` when Rhapsody is unavailable; the ``_require_rhapsody``
    autouse fixture then skips the session.
    """
    app = rhapsody_instance
    if app is None:
        return None
    if not request.config.getoption("--rhapsody-hidden-ui", default=False):
        # Bring window to foreground when a test needs visual rendering.
        try:
            app.bring_window_to_top()
        except Exception:
            pass  # If bring_window_to_top fails, continue anyway
    return app


@pytest.fixture(scope="session", autouse=True)
def rhapsody_session(rhapsody_app: RhapsodyApplication) -> Generator[RhapsodyApplication, None, None]:
    """Connect once for entire test session, disconnect at end.

    Creates a session file that persists across all integration tests,
    improving performance by avoiding repeated connect/disconnect cycles.

    A new Rhapsody instance is launched with the GUI visible by default to ensure
    proper rendering and display of model elements. Non-visual runs can use the
    ``--rhapsody-hidden-ui`` pytest option.

    The session file is stored in the user's home directory and has a
    long timeout (30 minutes) to accommodate slow test runs.

    Yields:
        RhapsodyApplication: The connected application instance.
    """
    from rhapsody_cli.session import Session, SessionManager

    session_manager = SessionManager()

    # Create session file with long timeout for integration tests
    now = datetime.now()
    session: Session = {
        "connected": True,
        "instance_type": "launched",  # We're launching a new instance
        "connected_at": now.isoformat(),
        "last_activity": now.isoformat(),
        "timeout_minutes": 30,  # Long timeout for test session
    }
    session_manager.save(session)

    yield rhapsody_app

    # Cleanup: clear session file at end
    session_manager.clear()


@pytest.fixture(scope="session", autouse=True)
def _require_rhapsody(rhapsody_app: RhapsodyApplication) -> None:
    """Skip the entire integration session if no Rhapsody instance is available."""
    try:
        _ = rhapsody_app.is_hidden_ui
    except Exception as exc:
        pytest.skip(f"No running Rhapsody available: {exc}", allow_module_level=False)


@pytest.fixture(scope="session")
def _test_project_directory(rhapsody_app: RhapsodyApplication, request: FixtureRequest) -> Generator[Path, None, None]:
    """Create and clean up the shared test-project files once per integration session."""
    if TEST_PROJECT_DIR.exists():
        _safe_cleanup_test_project(rhapsody_app, TEST_PROJECT_DIR)

    TEST_PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    project = rhapsody_app.create_new_project(str(TEST_PROJECT_DIR), TEST_PROJECT_NAME)
    if project is None:
        raise RuntimeError("Rhapsody did not report an active project after project creation")

    project.allow_auto_save(1)
    yield TEST_PROJECT_DIR

    keep = request.config.getoption("--keep-test-artifacts", default=False)
    if not keep and not os.getenv("RHAPSODY_KEEP_ARTIFACTS"):
        _safe_cleanup_test_project(rhapsody_app, TEST_PROJECT_DIR)


@pytest.fixture(scope="function")
def test_project(rhapsody_app: RhapsodyApplication, _test_project_directory: Path) -> IRPProject:
    """Return a fresh wrapper for the active shared test project for each test.

    Other integration tests may switch or reopen projects. Reacquire the COM
    wrapper at each function boundary instead of reusing a stale session object.
    """
    project = rhapsody_app.active_project()
    if project is None or project.name != TEST_PROJECT_NAME:
        project = rhapsody_app.open_project(str(_test_project_directory / f"{TEST_PROJECT_NAME}.rpyx"))

    project.allow_auto_save(1)
    return project


@pytest.fixture(scope="function")
def test_stereotypes(test_project: IRPProject) -> None:
    """Set up test stereotypes with tag definitions for integration tests.

    This fixture creates a stereotype with tag definitions that are required
    for various stereotype-related tests. It runs once per test session.

    The fixture will skip tests that require stereotypes if the setup fails,
    allowing the test suite to continue gracefully.

    Note: The test_project fixture already has auto-save enabled, so changes
    are automatically persisted.
    """
    try:
        # Create a stereotype with tag definition for testing
        stereo = test_project.add_stereotype("TestStereotype", "Class")
        if stereo is not None:
            # Save the project to persist the stereotype setup
            test_project.save(with_subs=1)
    except Exception as e:
        # If stereotype setup fails, tests that require it will be skipped
        print(f"Warning: Could not set up test stereotypes: {e}")


@pytest.fixture(scope="function")
def second_test_project(rhapsody_app: RhapsodyApplication, request: FixtureRequest) -> Generator[IRPProject, None, None]:
    """Function-scoped second test project for cross-project testing.

    This fixture creates a temporary second project for testing cross-project
    operations like copy, move, and reference functionality.

    The project is created with auto-save enabled to ensure automatic persistence
    during cleanup operations without explicit save calls.

    The project is automatically cleaned up after each test using the safe
    cleanup logic to avoid file lock issues.

    Args:
        rhapsody_app: The Rhapsody application instance
        request: pytest request object for accessing test configuration

    Returns:
        IRPProject: A temporary second test project
    """
    import tempfile

    # Create a temporary directory for the second project
    with tempfile.TemporaryDirectory() as temp_dir:
        project_path = Path(temp_dir) / "SecondTestProject"
        project_path.mkdir(parents=True, exist_ok=True)

        # Create the second test project
        second_project = rhapsody_app.create_new_project(str(project_path), "SecondTestProject")
        if second_project is None:
            raise RuntimeError("Rhapsody did not report an active project after project creation")

        try:
            # Enable auto-save on the project at creation to ensure automatic persistence
            second_project.allow_auto_save(1)

            yield second_project

        finally:
            # Clean up the second project
            try:
                # Live close() raises a modal "Projects can only be removed from
                # project lists" dialog; assert the COM binding instead.
                with patch.object(IRPModelElement, "call_com") as com_call:
                    second_project.close()
                    com_call.assert_called_once()
            except Exception:
                pass  # Don't let cleanup failures break tests
