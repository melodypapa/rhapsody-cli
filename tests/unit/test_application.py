"""Tests for rhapsody_cli.application.RhapsodyApplication (connection lifecycle).

Every COM member of the ``IRPApplication`` surface is owned — and tested — by
the canonical wrapper: ``tests/unit/models/com/telelogic/rhapsody/core/
test_irp_application.py``. This file covers only the facade's own
orchestration: attach/launch/connect/disconnect.
"""

from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.application import RhapsodyApplication
from rhapsody_cli.exceptions import RhapsodyConnectionError, RhapsodyRuntimeException


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_uses_attach_when_running(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    app = RhapsodyApplication.connect()

    mock_attach.assert_called_once_with()
    mock_launch.assert_not_called()
    assert app is mock_attach.return_value


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_uses_launch_when_attach_fails(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("No running Rhapsody instance found")

    RhapsodyApplication.connect()

    mock_attach.assert_called_once_with()
    mock_launch.assert_called_once_with()


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_raises_when_both_fail(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("No running Rhapsody instance found")
    mock_launch.side_effect = RhapsodyConnectionError("Failed to launch Rhapsody")

    with pytest.raises(RhapsodyConnectionError, match="Failed to launch"):
        RhapsodyApplication.connect()


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_attach_only_raises_when_not_running(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("No running Rhapsody instance found")

    with pytest.raises(RhapsodyConnectionError, match="No running Rhapsody"):
        RhapsodyApplication.connect(attach_only=True)

    mock_launch.assert_not_called()


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_launch_shows_gui_by_default(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("No running Rhapsody instance found")
    launched = MagicMock(name="LaunchedApp")
    mock_launch.return_value = launched

    RhapsodyApplication.connect()

    launched.set_hidden_ui.assert_called_once_with(False)


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_launch_hides_gui_when_specified(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("No running Rhapsody instance found")
    launched = MagicMock(name="LaunchedApp")
    mock_launch.return_value = launched

    RhapsodyApplication.connect(show_gui=False)

    launched.set_hidden_ui.assert_not_called()


def test_disconnect_calls_quit() -> None:
    with patch.object(RhapsodyApplication, "quit") as mock_quit:
        app = RhapsodyApplication(MagicMock(name="FakeApplication"))
        app.disconnect()

    mock_quit.assert_called_once_with()


def test_attach_raises_when_pywin32_unavailable(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("rhapsody_cli.application.win32_client", None)
    with pytest.raises(RhapsodyConnectionError, match="pywin32 is not available"):
        RhapsodyApplication._attach()


def test_attach_wraps_com_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_client = MagicMock()
    fake_client.GetActiveObject.side_effect = RhapsodyRuntimeException("no active object")
    monkeypatch.setattr("rhapsody_cli.application.win32_client", fake_client)
    with pytest.raises(RhapsodyConnectionError, match="No running Rhapsody"):
        RhapsodyApplication._attach()


def test_launch_raises_when_pywin32_unavailable(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("rhapsody_cli.application.win32_client", None)
    with pytest.raises(RhapsodyConnectionError, match="pywin32 is not available"):
        RhapsodyApplication._launch()


def test_launch_wraps_com_failure(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_client = MagicMock()
    fake_client.Dispatch.side_effect = RhapsodyRuntimeException("dispatch failed")
    monkeypatch.setattr("rhapsody_cli.application.win32_client", fake_client)
    with pytest.raises(RhapsodyConnectionError, match="Failed to launch"):
        RhapsodyApplication._launch()


def test_attach_returns_wrapped_application(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_com = MagicMock(name="ActiveApplication")
    fake_client = MagicMock()
    fake_client.GetActiveObject.return_value = fake_com
    monkeypatch.setattr("rhapsody_cli.application.win32_client", fake_client)
    app = RhapsodyApplication._attach()
    assert app._com is fake_com


def test_launch_returns_wrapped_application(monkeypatch: pytest.MonkeyPatch) -> None:
    fake_com = MagicMock(name="LaunchedApplication")
    fake_client = MagicMock()
    fake_client.Dispatch.return_value = fake_com
    monkeypatch.setattr("rhapsody_cli.application.win32_client", fake_client)
    app = RhapsodyApplication._launch()
    assert app._com is fake_com


def test_facade_is_irp_application_subclass() -> None:
    """The facade inherits the whole COM surface from the canonical wrapper."""
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPApplication

    assert issubclass(RhapsodyApplication, IRPApplication)
    app = RhapsodyApplication(MagicMock(name="FakeApplication"))
    assert isinstance(app, IRPApplication)
