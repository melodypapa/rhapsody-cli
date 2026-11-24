"""Shared test configuration for integration and system tests.

This module owns the single Rhapsody process lifecycle. Both the integration
and system layers attach to the instance managed here; neither launches or
quits Rhapsody on its own.

Because every Rhapsody-using fixture (integration ``rhapsody_app``, system
``rhapsody_available``) depends on ``rhapsody_instance``, pytest sets it up
first and finalizes it LAST -- after all other teardown such as the
integration layer's project-by-project close. Quitting last avoids COM calls
against an already-terminated server, which previously surfaced as Windows
fatal exceptions (RPC_E_DISCONNECTED / RPC_S_SERVER_UNAVAILABLE) during
session teardown when the system layer's ``disconnect`` quit Rhapsody before
the integration layer's project closing ran.

Unit tests do not request ``rhapsody_instance``, so it is never created for
unit-only runs.
"""

import time
from typing import Generator, Optional

import pytest
from _pytest.config.argparsing import Parser
from pytest import FixtureRequest

from rhapsody_cli import RhapsodyApplication


def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        "--rhapsody-hidden-ui",
        action="store_true",
        default=False,
        help="Run integration/system cases with the Rhapsody UI hidden",
    )


@pytest.fixture(scope="session")
def rhapsody_instance(request: FixtureRequest) -> Generator[Optional[RhapsodyApplication], None, None]:
    """Single owner of the Rhapsody process lifecycle.

    Launches (or attaches to) one Rhapsody instance for the whole test session
    and quits it on teardown. The opt-in ``--rhapsody-hidden-ui`` flag passes
    ``show_gui=False`` and explicitly hides the application. Yields ``None``
    when Rhapsody cannot be reached so dependent fixtures can skip gracefully.

    Finalized last because it is the root dependency of every Rhapsody fixture,
    so ``app.quit()`` runs only after all other teardown has finished.
    """
    hidden_ui = request.config.getoption("--rhapsody-hidden-ui", default=False)
    try:
        app = RhapsodyApplication.connect(attach_only=False, show_gui=not hidden_ui)
        if hidden_ui:
            app.set_hidden_ui(True)
    except Exception:
        yield None
        return
    # Give the GUI time to initialize before any layer uses the instance.
    time.sleep(2)
    yield app
    try:
        # Save all projects before quitting: otherwise Rhapsody shows a modal
        # "Save changes to <project>?" dialog (e.g. for TestProject.rpyx) that
        # blocks the COM automation thread. saveAll is a pywin32-exposed method.
        try:
            app.save_all()
        except Exception:
            pass  # best-effort: instance may already be closed
        app.quit()
    except Exception:
        # Best-effort: the instance may have been closed externally. A COM fault
        # here would be a C-level crash (uncatchable), which is exactly why this
        # fixture must finalize LAST -- by then nothing else needs the server.
        pass
