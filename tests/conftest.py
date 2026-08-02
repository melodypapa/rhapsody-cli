"""Shared test configuration for integration and system tests.

This module owns the single Rhapsody process lifecycle. Both the integration
and system layers attach to the instance managed here; neither launches or
quits Rhapsody on its own.

Because every Rhapsody-using fixture (integration ``rhapsody_app``, system
``rhapsody_available``) depends on ``rhapsody_instance``, pytest sets it up
first and finalizes it LAST -- after all other teardown such as
``close_all_projects``. Quitting last avoids COM calls against an
already-terminated server, which previously surfaced as Windows fatal
exceptions (RPC_E_DISCONNECTED / RPC_S_SERVER_UNAVAILABLE) during session
teardown when the system layer's ``disconnect`` quit Rhapsody before the
integration layer's ``close_all_projects`` ran.

Unit tests do not request ``rhapsody_instance``, so it is never created for
unit-only runs.
"""

import time
from typing import Generator, Optional

import pytest

from rhapsody_cli import RhapsodyApplication


@pytest.fixture(scope="session")
def rhapsody_instance() -> Generator[Optional[RhapsodyApplication], None, None]:
    """Single owner of the Rhapsody process lifecycle.

    Launches (or attaches to) one Rhapsody instance for the whole test session
    and quits it on teardown. Yields ``None`` when Rhapsody cannot be reached so
    dependent fixtures can skip gracefully rather than error.

    Finalized last because it is the root dependency of every Rhapsody fixture,
    so ``app.quit()`` runs only after all other teardown has finished.
    """
    try:
        app = RhapsodyApplication.connect(attach_only=False, show_gui=True)
    except Exception:
        yield None
        return
    # Give the GUI time to initialize before any layer uses the instance.
    time.sleep(2)
    yield app
    try:
        app.quit()
    except Exception:
        # Best-effort: the instance may have been closed externally. A COM fault
        # here would be a C-level crash (uncatchable), which is exactly why this
        # fixture must finalize LAST -- by then nothing else needs the server.
        pass
