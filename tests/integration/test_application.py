"""Integration tests for RhapsodyApplication with live Rhapsody COM API."""

import pytest

from rhapsody_cli import RhapsodyApplication


@pytest.mark.integration
class TestRhapsodyApplicationIntegration:
    """Live smoke coverage for RhapsodyApplication's read-only surface.

    ``quit()``/``disconnect()`` are intentionally not exercised here: they tear
    down the session-scoped Rhapsody instance owned by ``tests/conftest.py`` and
    would abort the rest of the integration session.
    """

    def test_get_projects(self, rhapsody_app: RhapsodyApplication) -> None:
        projects = rhapsody_app.projects
        assert projects is not None

    def test_active_project(self, rhapsody_app: RhapsodyApplication) -> None:
        assert rhapsody_app.active_project() is not None

    def test_get_is_hidden_ui(self, rhapsody_app: RhapsodyApplication) -> None:
        assert isinstance(rhapsody_app.is_hidden_ui, bool)

    def test_bring_window_to_top(self, rhapsody_app: RhapsodyApplication) -> None:
        assert rhapsody_app.bring_window_to_top() is None  # type: ignore[func-returns-value]

    def test_version(self, rhapsody_app: RhapsodyApplication) -> None:
        assert isinstance(rhapsody_app.version(), str)

    def test_get_build_no(self, rhapsody_app: RhapsodyApplication) -> None:
        # The getBuildNo() method does not exist on the COM object, but the
        # exposed BuildNo property is readable.
        assert isinstance(rhapsody_app.build_no, str)

    def test_get_omroot(self, rhapsody_app: RhapsodyApplication) -> None:
        # The getOMROOT() method does not exist on the COM object, but the
        # exposed OMROOT property is readable.
        assert isinstance(rhapsody_app.omroot, str)
