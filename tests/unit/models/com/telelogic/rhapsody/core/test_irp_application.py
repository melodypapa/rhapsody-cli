"""Unit tests for IRPApplication (fake COM — no live Rhapsody).

Covers every owned member of
``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application``; the
connection lifecycle (connect/attach/launch/disconnect) is owned by the
``RhapsodyApplication`` facade and tested in ``tests/unit/test_application.py``.
"""

import pytest
from unittest.mock import MagicMock

from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application import IRPApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def _app(com_obj: object | None = None) -> IRPApplication:
    return IRPApplication(com_obj if com_obj is not None else make_fake_element("Application"))


def test_open_project_wraps_result_as_irp_project() -> None:
    fake_app = make_fake_element("Application")
    fake_project = make_fake_element("Project", properties={"name": "MyProject"})
    fake_app.openProject.return_value = fake_project
    app = _app(fake_app)

    project = app.open_project("C:/models/MyProject.rpy")

    fake_app.openProject.assert_called_once_with("C:/models/MyProject.rpy")
    assert isinstance(project, IRPProject)
    assert project.get_name() == "MyProject"


def test_create_new_project_calls_com_and_returns_active_project() -> None:
    fake_app = make_fake_element("Application")
    fake_project = make_fake_element("Project", properties={"name": "NewProject"})
    fake_app.activeProject.return_value = fake_project
    app = _app(fake_app)

    project = app.create_new_project("C:/models", "NewProject")

    fake_app.createNewProject.assert_called_once_with("C:/models", "NewProject")
    assert isinstance(project, IRPProject)
    assert project.get_name() == "NewProject"


def test_active_project_wraps_result_as_irp_project() -> None:
    fake_app = make_fake_element("Application")
    fake_project = make_fake_element("Project", properties={"name": "ActiveOne"})
    fake_app.activeProject.return_value = fake_project
    app = _app(fake_app)

    project = app.active_project()

    assert isinstance(project, IRPProject)
    assert project.get_name() == "ActiveOne"


def test_active_project_raises_when_no_project_open() -> None:
    """activeProject() must not silently return an IRPProject wrapping None."""
    fake_app = make_fake_element("Application")
    fake_app.activeProject.return_value = None
    app = _app(fake_app)

    with pytest.raises(RhapsodyRuntimeException, match="No active project is open"):
        app.active_project()


def test_get_projects_reads_projects_property() -> None:
    fake_app = make_fake_element("Application")
    fake_project = make_fake_element("Project", properties={"name": "P1"})
    fake_app.projects = make_fake_collection([fake_project])
    app = _app(fake_app)

    projects = app.get_projects()

    assert isinstance(projects, IRPCollection)
    assert len(projects) == 1


def test_quit_delegates_to_com() -> None:
    fake_app = make_fake_element("Application")
    app = _app(fake_app)

    assert app.quit() is None
    fake_app.quit.assert_called_once_with()


def test_get_is_hidden_ui_reads_ishiddenui_property() -> None:
    fake = make_fake_element("Application", properties={"isHiddenUI": 0})
    app = _app(fake)

    assert app.get_is_hidden_ui() is False


def test_set_hidden_ui_calls_sethiddenui_method() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.set_hidden_ui(False) is None
    fake.setHiddenUI.assert_called_once_with(False)


def test_bring_window_to_top_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.bring_window_to_top() is None
    fake.bringWindowToTop.assert_called_once_with()


def test_save_all_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.save_all() is None
    fake.saveAll.assert_called_once_with()


def test_get_version_returns_version_method_result() -> None:
    fake = make_fake_element("Application")
    fake.version.return_value = "8.3.1"
    app = _app(fake)

    assert app.get_version() == "8.3.1"


def test_get_build_no_reads_buildno_property() -> None:
    fake = make_fake_element("Application", properties={"BuildNo": "20231012"})
    app = _app(fake)

    assert app.get_build_no() == "20231012"


def test_get_omroot_reads_omroot_property() -> None:
    fake = make_fake_element("Application", properties={"OMROOT": "C:/OMROOT"})
    app = _app(fake)

    assert app.get_omroot() == "C:/OMROOT"


def test_create_new_collection_wraps_result_as_irp_collection() -> None:
    fake = make_fake_element("Application")
    fake.createNewCollection.return_value = make_fake_collection([])
    app = _app(fake)

    collection = app.create_new_collection()

    fake.createNewCollection.assert_called_once_with()
    assert isinstance(collection, IRPCollection)


def test_get_search_manager_wraps_support_wrapper() -> None:
    from rhapsody_cli.models.support import RPSearchManager

    fake = make_fake_element("Application")
    manager = MagicMock(name="SearchManager")
    fake.getSearchManager.return_value = manager
    app = _app(fake)

    result = app.get_search_manager()

    fake.getSearchManager.assert_called_once_with()
    assert isinstance(result, RPSearchManager)
    assert result._com is manager


def test_get_selection_wraps_support_wrapper() -> None:
    from rhapsody_cli.models.support import RPSelection

    fake = make_fake_element("Application")
    selection = MagicMock(name="Selection")
    fake.getSelection.return_value = selection
    app = _app(fake)

    result = app.get_selection()

    fake.getSelection.assert_called_once_with()
    assert isinstance(result, RPSelection)
    assert result._com is selection


def test_get_code_gen_simplifiers_registry_wraps_support_wrapper() -> None:
    from rhapsody_cli.models.support import RPCodeGenSimplifiersRegistry

    fake = make_fake_element("Application")
    registry = MagicMock(name="CodeGenSimplifiersRegistry")
    fake.getCodeGenSimplifiersRegistry.return_value = registry
    app = _app(fake)

    result = app.get_code_gen_simplifiers_registry()

    fake.getCodeGenSimplifiersRegistry.assert_called_once_with()
    assert isinstance(result, RPCodeGenSimplifiersRegistry)
    assert result._com is registry


def test_get_diag_synth_api_wraps_support_wrapper() -> None:
    from rhapsody_cli.models.support import RPDiagSynthAPI

    fake = make_fake_element("Application")
    api = MagicMock(name="DiagSynthAPI")
    fake.getDiagSynthAPI.return_value = api
    app = _app(fake)

    result = app.get_diag_synth_api("MyClient")

    fake.getDiagSynthAPI.assert_called_once_with("MyClient")
    assert isinstance(result, RPDiagSynthAPI)
    assert result._com is api


def test_get_external_checker_registry_wraps_support_wrapper() -> None:
    from rhapsody_cli.models.support import RPExternalCheckRegistry

    fake = make_fake_element("Application")
    registry = MagicMock(name="ExternalCheckRegistry")
    fake.getExternalCheckerRegistry.return_value = registry
    app = _app(fake)

    result = app.get_external_checker_registry()

    fake.getExternalCheckerRegistry.assert_called_once_with()
    assert isinstance(result, RPExternalCheckRegistry)
    assert result._com is registry


def test_get_external_ide_registry_wraps_support_wrapper() -> None:
    from rhapsody_cli.models.support import RPExternalIDERegistry

    fake = make_fake_element("Application")
    registry = MagicMock(name="ExternalIDERegistry")
    fake.getExternalIDERegistry.return_value = registry
    app = _app(fake)

    result = app.get_external_ide_registry("MyClientID")

    fake.getExternalIDERegistry.assert_called_once_with("MyClientID")
    assert isinstance(result, RPExternalIDERegistry)
    assert result._com is registry


def test_get_external_roundtrip_invoker_wraps_support_wrapper() -> None:
    from rhapsody_cli.models.support import RPExternalRoundtripInvoker

    fake = make_fake_element("Application")
    invoker = MagicMock(name="ExternalRoundtripInvoker")
    fake.getExternalRoundtripInvoker.return_value = invoker
    app = _app(fake)

    result = app.get_external_roundtrip_invoker()

    fake.getExternalRoundtripInvoker.assert_called_once_with()
    assert isinstance(result, RPExternalRoundtripInvoker)
    assert result._com is invoker


def test_get_ow_pane_mgr_wraps_support_wrapper() -> None:
    from rhapsody_cli.models.support import RPowPaneMgr

    fake = make_fake_element("Application")
    pane_mgr = MagicMock(name="OWPaneMgr")
    fake.getOWPaneMgr.return_value = pane_mgr
    app = _app(fake)

    result = app.get_ow_pane_mgr("MyClientID")

    fake.getOWPaneMgr.assert_called_once_with("MyClientID")
    assert isinstance(result, RPowPaneMgr)
    assert result._com is pane_mgr


def test_generate_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.generate() is None
    fake.generate.assert_called_once_with()


def test_generate_elements_passes_collection_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    collection = IRPCollection(make_fake_collection([]))

    assert app.generate_elements(collection) is None
    fake.generateElements.assert_called_once_with(collection._com)


def test_generate_entire_project_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.generate_entire_project() is None
    fake.generateEntireProject.assert_called_once_with()


def test_regenerate_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.regenerate() is None
    fake.regenerate.assert_called_once_with()


def test_add_to_model_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.add_to_model("C:/models/Unit.sbs", 1) is None
    fake.addToModel.assert_called_once_with("C:/models/Unit.sbs", 1)


def test_add_to_model_ex_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.add_to_model_ex("C:/models/Unit.sbs", 0, 1, 0) is None
    fake.addToModelEx.assert_called_once_with("C:/models/Unit.sbs", 0, 1, 0)


def test_set_log_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.set_log("C:/logs/rhapsody.log") is None
    fake.setLog.assert_called_once_with("C:/logs/rhapsody.log")


def test_check_model_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    assert app.check_model() is None
    fake.checkModel.assert_called_once_with()
