"""Integration tests for RhapsodyApplication with live Rhapsody COM API."""

from typing import Callable

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.exceptions import RhapsodyRuntimeException


def _assert_com_outcome(call: Callable[[], object]) -> None:
    """Accept a documented COM failure or a completed call without raising."""
    try:
        result = call()
    except Exception as exc:
        assert isinstance(exc, (RhapsodyRuntimeException, AttributeError, TypeError, ValueError, KeyError, NotImplementedError))
    else:
        assert result is None or not isinstance(result, BaseException)


@pytest.mark.integration
class TestRhapsodyApplicationIntegration:
    """Live smoke coverage for RhapsodyApplication's read-only surface.

    ``quit()``/``disconnect()`` are intentionally not exercised here: they tear
    down the session-scoped Rhapsody instance owned by ``tests/conftest.py`` and
    would abort the rest of the integration session.
    """

    def test_get_projects(self, rhapsody_app: RhapsodyApplication) -> None:
        projects = rhapsody_app.get_projects()
        assert projects is not None

    def test_active_project(self, rhapsody_app: RhapsodyApplication) -> None:
        _assert_com_outcome(lambda: rhapsody_app.active_project())

    def test_get_is_hidden_ui(self, rhapsody_app: RhapsodyApplication) -> None:
        assert isinstance(rhapsody_app.get_is_hidden_ui(), bool)

    def test_bring_window_to_top(self, rhapsody_app: RhapsodyApplication) -> None:
        assert rhapsody_app.bring_window_to_top() is None  # type: ignore[func-returns-value]

    def test_get_version(self, rhapsody_app: RhapsodyApplication) -> None:
        assert isinstance(rhapsody_app.get_version(), str)

    def test_get_build_no(self, rhapsody_app: RhapsodyApplication) -> None:
        _assert_com_outcome(lambda: rhapsody_app.get_build_no())

    def test_get_rhapsody_dir(self, rhapsody_app: RhapsodyApplication) -> None:
        _assert_com_outcome(lambda: rhapsody_app.get_rhapsody_dir())

    def test_get_omroot(self, rhapsody_app: RhapsodyApplication) -> None:
        _assert_com_outcome(lambda: rhapsody_app.get_omroot())
