"""System test configuration.

System tests invoke the CLI as a real subprocess. Tests requiring
Rhapsody auto-skip when no instance is available.
"""

import shutil
import sys
import tempfile
import time
from pathlib import Path

import pytest

from rhapsody_cli import RhapsodyApplication

# Add unit directory to Python path so imports from unit tests work
sys.path.insert(0, str(Path(__file__).parent.parent / "unit"))

TEST_PROJECT_DIR = Path(tempfile.gettempdir()) / "rhapsody_cli_system_test"
TEST_PROJECT_NAME = "SystemTestProject"


@pytest.fixture(scope="session")
def rhapsody_available() -> bool:
    """Check if Rhapsody is available, launching a new instance if needed.

    Attempts to launch a new Rhapsody instance with the GUI visible.
    If an instance is already running, attaches to it instead.
    The GUI visibility is important for proper rendering and display of model elements.
    """
    try:
        app = RhapsodyApplication.connect(attach_only=False, show_gui=True)
        # Give the GUI time to initialize and render
        time.sleep(2)
        # Bring window to foreground to make GUI visible
        try:
            app.bring_window_to_top()
        except Exception:
            pass  # If bring_window_to_top fails, continue anyway
        app.get_is_hidden_ui()
        return True
    except Exception:
        return False


@pytest.fixture(scope="session")
def _require_rhapsody(rhapsody_available: bool) -> None:
    """Skip tests that require Rhapsody when no instance is available.

    Not autouse — test classes that need Rhapsody must request this fixture
    explicitly (typically via an autouse=True wrapper in the class). This allows
    CLI parsing tests to run without Rhapsody.
    """
    if not rhapsody_available:
        pytest.skip("No running Rhapsody available — skipping system tests", allow_module_level=False)


@pytest.fixture(scope="session")
def test_project_dir() -> Path:
    """Session-scoped test project directory."""
    if TEST_PROJECT_DIR.exists():
        shutil.rmtree(TEST_PROJECT_DIR)
    TEST_PROJECT_DIR.mkdir(parents=True, exist_ok=True)
    return TEST_PROJECT_DIR
