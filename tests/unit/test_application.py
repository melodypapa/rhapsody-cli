"""Tests for rhapsody_cli.application.RhapsodyApplication."""

from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.application import RhapsodyApplication
from rhapsody_cli.exceptions import RhapsodyConnectionError, RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from tests.unit.models.fakes import make_fake_collection, make_fake_element

# --- connect() lifecycle tests ---


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_uses_attach_when_running(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    fake_com = MagicMock(name="FakeApplication")
    mock_attach.return_value = RhapsodyApplication(fake_com)

    app = RhapsodyApplication.connect()

    mock_attach.assert_called_once()
    mock_launch.assert_not_called()
    assert app._com is fake_com


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_uses_launch_when_attach_fails(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")
    fake_com = MagicMock(name="FakeApplication")
    mock_launch.return_value = RhapsodyApplication(fake_com)

    app = RhapsodyApplication.connect()

    mock_attach.assert_called_once()
    mock_launch.assert_called_once()
    assert app._com is fake_com


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_raises_when_both_fail(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")
    mock_launch.side_effect = RhapsodyConnectionError("launch failed")

    with pytest.raises(RhapsodyConnectionError):
        RhapsodyApplication.connect()

    mock_attach.assert_called_once()
    mock_launch.assert_called_once()


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_attach_only_raises_when_not_running(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")

    with pytest.raises(RhapsodyConnectionError):
        RhapsodyApplication.connect(attach_only=True)

    mock_attach.assert_called_once()
    mock_launch.assert_not_called()


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_launch_shows_gui_by_default(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")
    fake_com = MagicMock(name="FakeApplication")
    mock_launch.return_value = RhapsodyApplication(fake_com)

    RhapsodyApplication.connect()

    fake_com.setHiddenUI.assert_called_once_with(False)


@patch.object(RhapsodyApplication, "_launch")
@patch.object(RhapsodyApplication, "_attach")
def test_connect_launch_hides_gui_when_specified(mock_attach: MagicMock, mock_launch: MagicMock) -> None:
    mock_attach.side_effect = RhapsodyConnectionError("no instance")
    fake_com = MagicMock(name="FakeApplication")
    mock_launch.return_value = RhapsodyApplication(fake_com)

    RhapsodyApplication.connect(show_gui=False)

    fake_com.setHiddenUI.assert_not_called()


def test_open_project_wraps_result_as_rpproject() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_project = make_fake_element("Project", properties={"name": "MyProject"})
    fake_app.openProject.return_value = fake_project
    app = RhapsodyApplication(fake_app)

    project = app.open_project("C:/models/MyProject.rpy")

    fake_app.openProject.assert_called_once_with("C:/models/MyProject.rpy")
    assert isinstance(project, IRPProject)
    assert project.get_name() == "MyProject"


def test_active_project_wraps_result_as_rpproject() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_project = make_fake_element("Project", properties={"name": "ActiveOne"})
    fake_app.activeProject.return_value = fake_project
    app = RhapsodyApplication(fake_app)

    project = app.active_project()

    assert isinstance(project, IRPProject)
    assert project.get_name() == "ActiveOne"


def test_active_project_raises_when_no_project_open() -> None:
    """activeProject() must not silently return an IRPProject wrapping None."""
    fake_app = MagicMock(name="FakeApplication")
    fake_app.activeProject.return_value = None
    app = RhapsodyApplication(fake_app)

    with pytest.raises(RhapsodyRuntimeException, match="No active project is open"):
        app.active_project()


def test_get_projects_returns_collection_of_rpproject() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_project = make_fake_element("Project", properties={"name": "P1"})
    fake_app.projects = make_fake_collection([fake_project])
    app = RhapsodyApplication(fake_app)

    projects = app.get_projects()

    assert len(projects) == 1
    assert isinstance(projects[0], IRPProject)
    assert projects[0].get_name() == "P1"


def test_get_projects_falls_back_to_projects_property_when_method_missing() -> None:
    """Some Rhapsody COM Prog IDs (e.g. Rhapsody2.Application.1) expose the
    projects collection via the bare 'projects' property instead of a
    getProjects() method."""
    fake_project = make_fake_element("Project", properties={"name": "P1"})
    fake_app = MagicMock(spec=["projects"])
    fake_app.projects = make_fake_collection([fake_project])
    app = RhapsodyApplication(fake_app)

    projects = app.get_projects()

    assert len(projects) == 1
    assert isinstance(projects[0], IRPProject)
    assert projects[0].get_name() == "P1"


def test_create_new_project_calls_com_and_returns_active_project() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_project = make_fake_element("Project", properties={"name": "NewProject"})
    fake_app.activeProject.return_value = fake_project
    app = RhapsodyApplication(fake_app)

    project = app.create_new_project("C:/models", "NewProject")

    fake_app.createNewProject.assert_called_once_with("C:/models", "NewProject")
    fake_app.activeProject.assert_called_once_with()
    assert isinstance(project, IRPProject)
    assert project.get_name() == "NewProject"


def test_quit_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.quit()

    fake_app.quit.assert_called_once_with()


def test_disconnect_calls_quit() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.disconnect()

    fake_app.quit.assert_called_once_with()


def test_get_is_hidden_ui_calls_method_when_present() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_app.getIsHiddenUI.return_value = 1
    app = RhapsodyApplication(fake_app)

    result = app.get_is_hidden_ui()
    assert result is True


def test_get_is_hidden_ui_falls_back_to_property_when_method_missing() -> None:
    fake_app = MagicMock(spec=["isHiddenUI"])
    fake_app.isHiddenUI = 0
    app = RhapsodyApplication(fake_app)

    result = app.get_is_hidden_ui()

    assert result is False


def test_set_hidden_ui_calls_method_when_present() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.set_hidden_ui(False)

    fake_app.setHiddenUI.assert_called_once_with(False)


def test_set_hidden_ui_hides_when_requested() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)
    app.set_hidden_ui(True)
    fake_app.setHiddenUI.assert_called_once_with(True)


def test_bring_window_to_top_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.bring_window_to_top()

    fake_app.bringWindowToTop.assert_called_once_with()


# --- Project lifecycle ---


def test_save_all_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.save_all()

    fake_app.saveAll.assert_called_once_with()


# --- Version info ---


def test_get_version_returns_string() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_app.version.return_value = "8.3.1"
    app = RhapsodyApplication(fake_app)

    assert app.get_version() == "8.3.1"
    fake_app.version.assert_called_once_with()


def test_get_build_no_returns_string() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_app.BuildNo = "12345"
    app = RhapsodyApplication(fake_app)

    assert app.get_build_no() == "12345"


def test_get_omroot_returns_string() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_app.OMROOT = "C:/Rhapsody/OMROOT"
    app = RhapsodyApplication(fake_app)

    assert app.get_omroot() == "C:/Rhapsody/OMROOT"


# --- Code generation ---


def test_generate_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.generate()

    fake_app.generate.assert_called_once_with()


def test_generate_elements_passes_collection_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    fake_collection = make_fake_collection([])
    app = RhapsodyApplication(fake_app)

    app.generate_elements(IRPCollection(fake_collection))

    fake_app.generateElements.assert_called_once_with(fake_collection)


def test_generate_entire_project_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.generate_entire_project()

    fake_app.generateEntireProject.assert_called_once_with()


def test_regenerate_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.regenerate()

    fake_app.regenerate.assert_called_once_with()


# --- Model import ---


def test_add_to_model_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.add_to_model("myfile.rpy", 1)

    fake_app.addToModel.assert_called_once_with("myfile.rpy", 1)


def test_add_to_model_ex_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.add_to_model_ex("myfile.rpy", 1, 1, 1)

    fake_app.addToModelEx.assert_called_once_with("myfile.rpy", 1, 1, 1)


# --- Model checking ---


def test_set_log_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.set_log("C:/log.txt")

    fake_app.setLog.assert_called_once_with("C:/log.txt")


def test_check_model_delegates_to_com() -> None:
    fake_app = MagicMock(name="FakeApplication")
    app = RhapsodyApplication(fake_app)

    app.check_model()

    fake_app.checkModel.assert_called_once_with()


def test_create_new_collection_returns_rpcollection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake_app = make_fake_element("Application")
    fake_app.createNewCollection.return_value = make_fake_collection([])
    app = RhapsodyApplication(fake_app)

    result = app.create_new_collection()

    fake_app.createNewCollection.assert_called_once_with()
    assert isinstance(result, IRPCollection)


def test_get_search_manager_returns_wrapped_element() -> None:
    from rhapsody_cli.models.support import RPSearchManager

    fake_app = make_fake_element("Application")
    fake_search = make_fake_element("SearchManager")
    fake_app.getSearchManager.return_value = fake_search
    app = RhapsodyApplication(fake_app)

    result = app.get_search_manager()
    assert isinstance(result, RPSearchManager)


def test_get_selection_returns_wrapped_element() -> None:
    from rhapsody_cli.models.support import RPSelection

    fake_app = make_fake_element("Application")
    fake_selection = make_fake_element("Selection")
    fake_app.getSelection.return_value = fake_selection
    app = RhapsodyApplication(fake_app)

    result = app.get_selection()
    assert isinstance(result, RPSelection)


def test_get_code_gen_simplifiers_registry_returns_wrapped_element() -> None:
    from rhapsody_cli.models.support import RPCodeGenSimplifiersRegistry

    fake_app = make_fake_element("Application")
    fake_registry = make_fake_element("CodeGenSimplifiersRegistry")
    fake_app.getCodeGenSimplifiersRegistry.return_value = fake_registry
    app = RhapsodyApplication(fake_app)

    result = app.get_code_gen_simplifiers_registry()
    assert isinstance(result, RPCodeGenSimplifiersRegistry)


def test_get_diag_synth_api_returns_wrapped_element() -> None:
    from rhapsody_cli.models.support import RPDiagSynthAPI

    fake_app = make_fake_element("Application")
    fake_api = make_fake_element("DiagSynthAPI")
    fake_app.getDiagSynthAPI.return_value = fake_api
    app = RhapsodyApplication(fake_app)

    result = app.get_diag_synth_api("MyClient")

    fake_app.getDiagSynthAPI.assert_called_once_with("MyClient")
    assert isinstance(result, RPDiagSynthAPI)


def test_get_external_checker_registry_returns_wrapped_element() -> None:
    from rhapsody_cli.models.support import RPExternalCheckRegistry

    fake_app = make_fake_element("Application")
    fake_registry = make_fake_element("ExternalCheckRegistry")
    fake_app.getExternalCheckerRegistry.return_value = fake_registry
    app = RhapsodyApplication(fake_app)

    result = app.get_external_checker_registry()
    assert isinstance(result, RPExternalCheckRegistry)


def test_get_external_ide_registry_returns_wrapped_element() -> None:
    from rhapsody_cli.models.support import RPExternalIDERegistry

    fake_app = make_fake_element("Application")
    fake_registry = make_fake_element("ExternalIDERegistry")
    fake_app.getExternalIDERegistry.return_value = fake_registry
    app = RhapsodyApplication(fake_app)

    result = app.get_external_ide_registry("MyClient")

    fake_app.getExternalIDERegistry.assert_called_once_with("MyClient")
    assert isinstance(result, RPExternalIDERegistry)


def test_get_external_roundtrip_invoker_returns_wrapped_element() -> None:
    from rhapsody_cli.models.support import RPExternalRoundtripInvoker

    fake_app = make_fake_element("Application")
    fake_invoker = make_fake_element("ExternalRoundtripInvoker")
    fake_app.getExternalRoundtripInvoker.return_value = fake_invoker
    app = RhapsodyApplication(fake_app)

    result = app.get_external_roundtrip_invoker()
    assert isinstance(result, RPExternalRoundtripInvoker)


def test_get_ow_pane_mgr_returns_wrapped_element() -> None:
    from rhapsody_cli.models.support import RPowPaneMgr

    fake_app = make_fake_element("Application")
    fake_pane = make_fake_element("OWPaneMgr")
    fake_app.getOWPaneMgr.return_value = fake_pane
    app = RhapsodyApplication(fake_app)

    result = app.get_ow_pane_mgr("MyClient")

    fake_app.getOWPaneMgr.assert_called_once_with("MyClient")
    assert isinstance(result, RPowPaneMgr)


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
