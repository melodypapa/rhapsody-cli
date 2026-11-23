"""Unit tests for IRPApplication (fake COM — no live Rhapsody).

Covers every owned member of
``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application``; the
connection lifecycle (connect/attach/launch/disconnect) is owned by the
``RhapsodyApplication`` facade and tested in ``tests/unit/test_application.py``.
"""

from __future__ import annotations

from unittest.mock import MagicMock

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


def test_create_new_project_propagates_missing_active_project() -> None:
    fake_app = make_fake_element("Application")
    fake_app.activeProject.return_value = None
    app = _app(fake_app)

    assert app.create_new_project("C:/models", "NewProject") is None


def test_active_project_wraps_result_as_irp_project() -> None:
    fake_app = make_fake_element("Application")
    fake_project = make_fake_element("Project", properties={"name": "ActiveOne"})
    fake_app.activeProject.return_value = fake_project
    app = _app(fake_app)

    project = app.active_project()

    assert isinstance(project, IRPProject)
    assert project.get_name() == "ActiveOne"


def test_active_project_returns_none_when_no_project_is_open() -> None:
    fake_app = make_fake_element("Application")
    fake_app.activeProject.return_value = None
    app = _app(fake_app)

    assert app.active_project() is None
    fake_app.activeProject.assert_called_once_with()


def test_get_projects_reads_projects_property() -> None:
    fake_app = make_fake_element("Application")
    fake_project = make_fake_element("Project", properties={"name": "P1"})
    fake_app.projects = make_fake_collection([fake_project])
    app = _app(fake_app)

    projects = app.projects

    assert isinstance(projects, IRPCollection)
    assert len(projects) == 1


def test_quit_delegates_to_com() -> None:
    fake_app = make_fake_element("Application")
    app = _app(fake_app)

    app.quit()
    fake_app.quit.assert_called_once_with()


def test_get_is_hidden_ui_reads_ishiddenui_property() -> None:
    fake = make_fake_element("Application", properties={"isHiddenUI": 0})
    app = _app(fake)

    assert app.is_hidden_ui is False


def test_set_hidden_ui_calls_sethiddenui_method() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    app.set_hidden_ui(False)
    fake.setHiddenUI.assert_called_once_with(False)


def test_bring_window_to_top_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    app.bring_window_to_top()
    fake.bringWindowToTop.assert_called_once_with()


def test_save_all_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    app.save_all()
    fake.saveAll.assert_called_once_with()


def test_version_returns_version_method_result() -> None:
    fake = make_fake_element("Application")
    fake.version.return_value = "8.3.1"
    app = _app(fake)

    assert app.version() == "8.3.1"


def test_get_build_no_reads_buildno_property() -> None:
    fake = make_fake_element("Application", properties={"BuildNo": "20231012"})
    app = _app(fake)

    assert app.build_no == "20231012"


def test_get_omroot_reads_omroot_property() -> None:
    fake = make_fake_element("Application", properties={"OMROOT": "C:/OMROOT"})
    app = _app(fake)

    assert app.omroot == "C:/OMROOT"


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

    app.generate()
    fake.generate.assert_called_once_with()


def test_generate_elements_passes_collection_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    collection = IRPCollection(make_fake_collection([]))

    app.generate_elements(collection)
    fake.generateElements.assert_called_once_with(collection._com)


def test_generate_entire_project_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    app.generate_entire_project()
    fake.generateEntireProject.assert_called_once_with()


def test_regenerate_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    app.regenerate()
    fake.regenerate.assert_called_once_with()


def test_add_to_model_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    app.add_to_model("C:/models/Unit.sbs", 1)
    fake.addToModel.assert_called_once_with("C:/models/Unit.sbs", 1)


def test_add_to_model_ex_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    app.add_to_model_ex("C:/models/Unit.sbs", 0, 1, 0)
    fake.addToModelEx.assert_called_once_with("C:/models/Unit.sbs", 0, 1, 0)


def test_set_log_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    app.set_log("C:/logs/rhapsody.log")
    fake.setLog.assert_called_once_with("C:/logs/rhapsody.log")


def test_check_model_delegates_to_com() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)

    app.check_model()
    fake.checkModel.assert_called_once_with()


def test_add_profile_to_model() -> None:
    fake = make_fake_element("Application")
    fake.addProfileToModel.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.add_profile_to_model("value")
    fake.addProfileToModel.assert_called_once_with("value")
    assert result is not None


def test_add_selected_to_favorites() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.add_selected_to_favorites()
    fake.addSelectedToFavorites.assert_called_once_with()


def test_add_to_model_by_reference() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.add_to_model_by_reference("value")
    fake.addToModelByReference.assert_called_once_with("value")


def test_add_to_model_from_url() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.add_to_model_from_url("value")
    fake.addToModelFromURL.assert_called_once_with("value")


def test_add_units_to_model() -> None:
    fake = make_fake_element("Application")
    fake.addUnitsToModel.return_value = make_fake_collection([])
    arg_0 = make_fake_collection([])
    app = _app(fake)
    result = app.add_units_to_model(arg_0, 3, 3, 3)
    fake.addUnitsToModel.assert_called_once_with(arg_0._com, 3, 3, 3)
    assert result is not None


def test_allow_browser_refresh() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.allow_browser_refresh(3)
    fake.allowBrowserRefresh.assert_called_once_with(3)


def test_allow_ge_refresh() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.allow_ge_refresh(3)
    fake.allowGERefresh.assert_called_once_with(3)


def test_allow_rmm_remote_oslc_links_load() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.allow_rmm_remote_oslc_links_load(3)
    fake.allowRmmRemoteOslcLinksLoad.assert_called_once_with(3)


def test_get_application_connection_string() -> None:
    fake = make_fake_element("Application")
    fake.getApplicationConnectionString.return_value = "result"
    app = _app(fake)
    result = app.get_application_connection_string()
    fake.getApplicationConnectionString.assert_called_once_with()
    assert isinstance(result, str)


def test_get_application_name() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.get_application_name("value", "value")
    fake.getApplicationName.assert_called_once_with("value", "value")


def test_get_application_root() -> None:
    fake = make_fake_element("Application")
    fake.ApplicationRoot = "value"
    app = _app(fake)
    result = app.application_root
    assert isinstance(result, str)


def test_get_application_status() -> None:
    fake = make_fake_element("Application")
    fake.getApplicationStatus.return_value = 7
    app = _app(fake)
    result = app.get_application_status()
    fake.getApplicationStatus.assert_called_once_with()
    assert isinstance(result, int)


def test_set_application_status() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.set_application_status(3)
    fake.setApplicationStatus.assert_called_once_with(3)


def test_apply_new_terms_profile() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.apply_new_terms_profile("value")
    fake.applyNewTermsProfile.assert_called_once_with("value")


def test_apply_window_layout() -> None:
    fake = make_fake_element("Application")
    fake.applyWindowLayout.return_value = 7
    app = _app(fake)
    result = app.apply_window_layout("value")
    fake.applyWindowLayout.assert_called_once_with("value")
    assert isinstance(result, int)


def test_arc_check_out() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.arc_check_out("value", "value", 3, 3)
    fake.arcCheckOut.assert_called_once_with("value", "value", 3, 3)


def test_build() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.build()
    fake.build.assert_called_once_with()


def test_build_entire_project() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.build_entire_project()
    fake.buildEntireProject.assert_called_once_with()


def test_build_with_dependencies() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.build_with_dependencies()
    fake.buildWithDependencies.assert_called_once_with()


def test_can_redo() -> None:
    fake = make_fake_element("Application")
    fake.canRedo.return_value = 7
    app = _app(fake)
    result = app.can_redo()
    fake.canRedo.assert_called_once_with()
    assert isinstance(result, int)


def test_can_undo() -> None:
    fake = make_fake_element("Application")
    fake.canUndo.return_value = 7
    app = _app(fake)
    result = app.can_undo()
    fake.canUndo.assert_called_once_with()
    assert isinstance(result, int)


def test_check_in() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.check_in("value", "value", 3, 3, "value")
    fake.checkIn.assert_called_once_with("value", "value", 3, 3, "value")


def test_check_out() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.check_out("value", "value", 3, 3)
    fake.checkOut.assert_called_once_with("value", "value", 3, 3)


def test_clean() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.clean()
    fake.clean.assert_called_once_with()


def test_clear_output_window() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.clear_output_window("value")
    fake.clearOutputWindow.assert_called_once_with("value")


def test_close_all_animated_sequence_diagrams() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.close_all_animated_sequence_diagrams(3)
    fake.closeAllAnimatedSequenceDiagrams.assert_called_once_with(3)


def test_compare_sequence_diagram() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_element("Element")
    arg_1 = make_fake_element("Element")
    app = _app(fake)
    app.compare_sequence_diagram(arg_0, arg_1)
    fake.compareSequenceDiagram.assert_called_once_with(arg_0._com, arg_1._com)


def test_set_component() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.set_component("value")
    fake.setComponent.assert_called_once_with("value")


def test_set_configuration() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.set_configuration("value")
    fake.setConfiguration.assert_called_once_with("value")


def test_connect_to_archive() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.connect_to_archive("value")
    fake.connectToArchive.assert_called_once_with("value")


def test_connect_to_imported_model() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.connect_to_imported_model("value", "value", "value")
    fake.connectToImportedModel.assert_called_once_with("value", "value", "value")


def test_connect_to_target() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.connect_to_target("value")
    fake.connectToTarget.assert_called_once_with("value")


def test_create_and_insert_project() -> None:
    fake = make_fake_element("Application")
    fake.createAndInsertProject.return_value = 7
    app = _app(fake)
    result = app.create_and_insert_project("value", "value")
    fake.createAndInsertProject.assert_called_once_with("value", "value")
    assert isinstance(result, int)


def test_create_domain_from_profile() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_element("Element")
    app = _app(fake)
    app.create_domain_from_profile(arg_0, "value")
    fake.createDomainFromProfile.assert_called_once_with(arg_0._com, "value")


def test_create_embedded_web_view_window() -> None:
    fake = make_fake_element("Application")
    fake.createEmbeddedWebViewWindow.return_value = 7
    app = _app(fake)
    result = app.create_embedded_web_view_window("value", "value", "value")
    fake.createEmbeddedWebViewWindow.assert_called_once_with("value", "value", "value")
    assert isinstance(result, int)


def test_create_progress_bar() -> None:
    fake = make_fake_element("Application")
    fake.createProgressBar.return_value = object()
    app = _app(fake)
    result = app.create_progress_bar("value")
    fake.createProgressBar.assert_called_once_with("value")
    assert result is not None


def test_get_dm_bool_property() -> None:
    fake = make_fake_element("Application")
    fake.getDMBoolProperty.return_value = 7
    app = _app(fake)
    result = app.get_dm_bool_property("value")
    fake.getDMBoolProperty.assert_called_once_with("value")
    assert isinstance(result, int)


def test_set_dm_bool_property() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.set_dm_bool_property("value", 3)
    fake.setDMBoolProperty.assert_called_once_with("value", 3)


def test_get_dm_model_workspace_folder() -> None:
    fake = make_fake_element("Application")
    fake.getDMModelWorkspaceFolder.return_value = "result"
    app = _app(fake)
    result = app.get_dm_model_workspace_folder()
    fake.getDMModelWorkspaceFolder.assert_called_once_with()
    assert isinstance(result, str)


def test_get_dm_property() -> None:
    fake = make_fake_element("Application")
    fake.getDMProperty.return_value = "result"
    app = _app(fake)
    result = app.get_dm_property("value")
    fake.getDMProperty.assert_called_once_with("value")
    assert isinstance(result, str)


def test_set_dm_property() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.set_dm_property("value", "value")
    fake.setDMProperty.assert_called_once_with("value", "value")


def test_d_m_refresh_recursive() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_element("Element")
    app = _app(fake)
    app.d_m_refresh_recursive(arg_0)
    fake.dMRefreshRecursive.assert_called_once_with(arg_0._com)


def test_d_m_sync_and_refresh() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_element("Element")
    app = _app(fake)
    app.d_m_sync_and_refresh(arg_0, 3, 3)
    fake.dMSyncAndRefresh.assert_called_once_with(arg_0._com, 3, 3)


def test_dbg_check_com_in() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.dbg_check_com_in(3)
    fake.dbgCheckComIn.assert_called_once_with(3)


def test_dbg_check_com_out() -> None:
    fake = make_fake_element("Application")
    fake.dbgCheckComOut.return_value = 7
    app = _app(fake)
    result = app.dbg_check_com_out()
    fake.dbgCheckComOut.assert_called_once_with()
    assert isinstance(result, int)


def test_deferred_add_to_model() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.deferred_add_to_model("value", 3, "value", 3)
    fake.deferredAddToModel.assert_called_once_with("value", 3, "value", 3)


def test_delete_project_from_list() -> None:
    fake = make_fake_element("Application")
    fake.deleteProjectFromList.return_value = 7
    app = _app(fake)
    result = app.delete_project_from_list("value")
    fake.deleteProjectFromList.assert_called_once_with("value")
    assert isinstance(result, int)


def test_delete_window_layout() -> None:
    fake = make_fake_element("Application")
    fake.deleteWindowLayout.return_value = 7
    app = _app(fake)
    result = app.delete_window_layout("value")
    fake.deleteWindowLayout.assert_called_once_with("value")
    assert isinstance(result, int)


def test_get_diagram_of_selected_element() -> None:
    fake = make_fake_element("Application")
    fake.getDiagramOfSelectedElement.return_value = object()
    app = _app(fake)
    result = app.get_diagram_of_selected_element()
    fake.getDiagramOfSelectedElement.assert_called_once_with()
    assert result is not None


def test_disconnect_from_target() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.disconnect_from_target()
    fake.disconnectFromTarget.assert_called_once_with()


def test_download_to_target() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.download_to_target("value")
    fake.downloadToTarget.assert_called_once_with("value")


def test_end_undo_transaction() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.end_undo_transaction()
    fake.endUndoTransaction.assert_called_once_with()


def test_enter_animation_command() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.enter_animation_command("value")
    fake.enterAnimationCommand.assert_called_once_with("value")


def test_error_message() -> None:
    fake = make_fake_element("Application")
    fake.errorMessage.return_value = "result"
    app = _app(fake)
    result = app.error_message()
    fake.errorMessage.assert_called_once_with()
    assert isinstance(result, str)


def test_get_error_message() -> None:
    fake = make_fake_element("Application")
    fake.getErrorMessage.return_value = "result"
    app = _app(fake)
    result = app.get_error_message("value")
    fake.getErrorMessage.assert_called_once_with("value")
    assert isinstance(result, str)


def test_get_executable_folder() -> None:
    fake = make_fake_element("Application")
    fake.getExecutableFolder.return_value = "result"
    app = _app(fake)
    result = app.get_executable_folder()
    fake.getExecutableFolder.assert_called_once_with()
    assert isinstance(result, str)


def test_execute_command() -> None:
    fake = make_fake_element("Application")
    arg_1 = make_fake_collection([])
    arg_2 = make_fake_collection([])
    app = _app(fake)
    app.execute_command("value", arg_1, arg_2)
    fake.ExecuteCommand.assert_called_once_with("value", arg_1._com, arg_2._com)


def test_execute_command_line() -> None:
    fake = make_fake_element("Application")
    fake.executeCommandLine.return_value = 7
    app = _app(fake)
    result = app.execute_command_line("value")
    fake.executeCommandLine.assert_called_once_with("value")
    assert isinstance(result, int)


def test_execute_transformation_sequence() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.execute_transformation_sequence("value", 3)
    fake.executeTransformationSequence.assert_called_once_with("value", 3)


def test_expand_string_keywords() -> None:
    fake = make_fake_element("Application")
    fake.expandStringKeywords.return_value = "result"
    app = _app(fake)
    result = app.expand_string_keywords("value")
    fake.expandStringKeywords.assert_called_once_with("value")
    assert isinstance(result, str)


def test_export_window_layout() -> None:
    fake = make_fake_element("Application")
    fake.exportWindowLayout.return_value = 7
    app = _app(fake)
    result = app.export_window_layout("value", "value", 3)
    fake.exportWindowLayout.assert_called_once_with("value", "value", 3)
    assert isinstance(result, int)


def test_fixpack() -> None:
    fake = make_fake_element("Application")
    fake.fixpack.return_value = "result"
    app = _app(fake)
    result = app.fixpack()
    fake.fixpack.assert_called_once_with()
    assert isinstance(result, str)


def test_force_output2_console() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.force_output2_console(3)
    fake.forceOutput2Console.assert_called_once_with(3)


def test_force_roundtrip() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.force_roundtrip()
    fake.forceRoundtrip.assert_called_once_with()


def test_force_roundtrip_elements() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_collection([])
    app = _app(fake)
    app.force_roundtrip_elements(arg_0)
    fake.forceRoundtripElements.assert_called_once_with(arg_0._com)


def test_generate_main_and_make_files() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.generate_main_and_make_files()
    fake.generateMainAndMakeFiles.assert_called_once_with()


def test_generate_with_dependencies() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.generate_with_dependencies()
    fake.generateWithDependencies.assert_called_once_with()


def test_get_helper_status() -> None:
    fake = make_fake_element("Application")
    fake.getHelperStatus.return_value = 7
    app = _app(fake)
    result = app.get_helper_status("value")
    fake.getHelperStatus.assert_called_once_with("value")
    assert isinstance(result, int)


def test_set_helper_status() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.set_helper_status("value", 3)
    fake.setHelperStatus.assert_called_once_with("value", 3)


def test_high_light_element() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_element("Element")
    app = _app(fake)
    app.high_light_element(arg_0)
    fake.highLightElement.assert_called_once_with(arg_0._com)


def test_highlight_by_handle() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.highlight_by_handle("value")
    fake.highlightByHandle.assert_called_once_with("value")


def test_import_classes() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.import_classes()
    fake.importClasses.assert_called_once_with()


def test_import_design_manager_model() -> None:
    fake = make_fake_element("Application")
    fake.importDesignManagerModel.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.import_design_manager_model("value", "value", "value", "value", "value", 3)
    fake.importDesignManagerModel.assert_called_once_with("value", "value", "value", "value", "value", 3)
    assert result is not None


def test_import_sync_simulink_block2() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_element("Element")
    app = _app(fake)
    app.import_sync_simulink_block2(arg_0, "value", "value", "value", "value")
    fake.importSyncSimulinkBlock2.assert_called_once_with(arg_0._com, "value", "value", "value", "value")


def test_import_tlb() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.import_tlb("value")
    fake.importTlb.assert_called_once_with("value")


def test_import_window_layout() -> None:
    fake = make_fake_element("Application")
    fake.importWindowLayout.return_value = 7
    app = _app(fake)
    result = app.import_window_layout("value", 3)
    fake.importWindowLayout.assert_called_once_with("value", 3)
    assert isinstance(result, int)


def test_get_ini_file_parameter_value() -> None:
    fake = make_fake_element("Application")
    fake.getIniFileParameterValue.return_value = "result"
    app = _app(fake)
    result = app.get_ini_file_parameter_value("value", "value")
    fake.getIniFileParameterValue.assert_called_once_with("value", "value")
    assert isinstance(result, str)


def test_insert_project() -> None:
    fake = make_fake_element("Application")
    fake.insertProject.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.insert_project("value")
    fake.insertProject.assert_called_once_with("value")
    assert result is not None


def test_insert_project_from_design_manager() -> None:
    fake = make_fake_element("Application")
    fake.insertProjectFromDesignManager.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.insert_project_from_design_manager("value", "value", "value", "value", "value", "value")
    fake.insertProjectFromDesignManager.assert_called_once_with("value", "value", "value", "value", "value", "value")
    assert result is not None


def test_get_interface_name() -> None:
    fake = make_fake_element("Application")
    fake.interfaceName = "value"
    app = _app(fake)
    result = app.interface_name
    assert isinstance(result, str)


def test_invoke_plugins_method() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.invoke_plugins_method("value")
    fake.invokePluginsMethod.assert_called_once_with("value")


def test_invoke_rpe() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.invoke_rpe()
    fake.invokeRPE.assert_called_once_with()


def test_get_is_load_on_demand() -> None:
    fake = make_fake_element("Application")
    fake.isLoadOnDemand = 3
    app = _app(fake)
    result = app.is_load_on_demand
    assert isinstance(result, int)


def test_set_is_load_on_demand() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.is_load_on_demand = 3


def test_is_rhapsody_cl() -> None:
    fake = make_fake_element("Application")
    fake.isRhapsodyCL.return_value = 7
    app = _app(fake)
    result = app.is_rhapsody_cl()
    fake.isRhapsodyCL.assert_called_once_with()
    assert isinstance(result, int)


def test_is_rhapsody_file_type() -> None:
    fake = make_fake_element("Application")
    fake.isRhapsodyFileType.return_value = 7
    app = _app(fake)
    result = app.is_rhapsody_file_type("value")
    fake.isRhapsodyFileType.assert_called_once_with("value")
    assert isinstance(result, int)


def test_is_valid_web_view() -> None:
    fake = make_fake_element("Application")
    fake.isValidWebView.return_value = 7
    app = _app(fake)
    result = app.is_valid_web_view(3)
    fake.isValidWebView.assert_called_once_with(3)
    assert isinstance(result, int)


def test_get_language() -> None:
    fake = make_fake_element("Application")
    fake.Language = "value"
    app = _app(fake)
    result = app.language
    assert isinstance(result, str)


def test_set_language() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.language = "value"


def test_get_list_of_factory_properties() -> None:
    fake = make_fake_element("Application")
    fake.getListOfFactoryProperties.return_value = make_fake_collection([])
    app = _app(fake)
    result = app.get_list_of_factory_properties()
    fake.getListOfFactoryProperties.assert_called_once_with()
    assert result is not None


def test_get_list_of_selected_elements() -> None:
    fake = make_fake_element("Application")
    fake.getListOfSelectedElements.return_value = make_fake_collection([])
    app = _app(fake)
    result = app.get_list_of_selected_elements()
    fake.getListOfSelectedElements.assert_called_once_with()
    assert result is not None


def test_get_list_of_site_properties() -> None:
    fake = make_fake_element("Application")
    fake.getListOfSiteProperties.return_value = make_fake_collection([])
    app = _app(fake)
    result = app.get_list_of_site_properties()
    fake.getListOfSiteProperties.assert_called_once_with()
    assert result is not None


def test_get_locale_name() -> None:
    fake = make_fake_element("Application")
    fake.getLocaleName.return_value = "result"
    app = _app(fake)
    result = app.get_locale_name()
    fake.getLocaleName.assert_called_once_with()
    assert isinstance(result, str)


def test_get_log_root() -> None:
    fake = make_fake_element("Application")
    fake.LogRoot = "value"
    app = _app(fake)
    result = app.log_root
    assert isinstance(result, str)


def test_login_to_design_manager_with_alias() -> None:
    fake = make_fake_element("Application")
    fake.loginToDesignManagerWithAlias.return_value = 7
    app = _app(fake)
    result = app.login_to_design_manager_with_alias("value", "value")
    fake.loginToDesignManagerWithAlias.assert_called_once_with("value", "value")
    assert isinstance(result, int)


def test_login_to_design_manager_with_certificate() -> None:
    fake = make_fake_element("Application")
    fake.loginToDesignManagerWithCertificate.return_value = 7
    app = _app(fake)
    result = app.login_to_design_manager_with_certificate("value", "value", "value")
    fake.loginToDesignManagerWithCertificate.assert_called_once_with("value", "value", "value")
    assert isinstance(result, int)


def test_login_to_design_manager_with_username() -> None:
    fake = make_fake_element("Application")
    fake.loginToDesignManagerWithUsername.return_value = 7
    app = _app(fake)
    result = app.login_to_design_manager_with_username("value", "value", "value")
    fake.loginToDesignManagerWithUsername.assert_called_once_with("value", "value", "value")
    assert isinstance(result, int)


def test_make() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.make()
    fake.make.assert_called_once_with()


def test_merge_elements() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_element("Element")
    arg_1 = make_fake_element("Element")
    app = _app(fake)
    app.merge_elements(arg_0, arg_1)
    fake.mergeElements.assert_called_once_with(arg_0._com, arg_1._com)


def test_get_model_element_from_source() -> None:
    fake = make_fake_element("Application")
    fake.getModelElementFromSource.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.get_model_element_from_source("value", 3, 3)
    fake.getModelElementFromSource.assert_called_once_with("value", 3, 3)
    assert result is not None


def test_new_project_on_design_manager() -> None:
    fake = make_fake_element("Application")
    fake.newProjectOnDesignManager.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.new_project_on_design_manager("value", "value", "value", "value", "value", "value")
    fake.newProjectOnDesignManager.assert_called_once_with("value", "value", "value", "value", "value", "value")
    assert result is not None


def test_notify_file_changed() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.notify_file_changed("value", 3)
    fake.notifyFileChanged.assert_called_once_with("value", 3)


def test_open_active_x_view() -> None:
    fake = make_fake_element("Application")
    fake.OpenActiveXView.return_value = object()
    arg_1 = make_fake_collection([])
    arg_2 = make_fake_collection([])
    app = _app(fake)
    result = app.open_active_x_view("value", arg_1, arg_2)
    fake.OpenActiveXView.assert_called_once_with("value", arg_1._com, arg_2._com)
    assert result is not None


def test_open_advanced_search_and_replace_dialog() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.open_advanced_search_and_replace_dialog()
    fake.openAdvancedSearchAndReplaceDialog.assert_called_once_with()


def test_open_diagram_view() -> None:
    fake = make_fake_element("Application")
    fake.OpenDiagramView.return_value = object()
    arg_0 = make_fake_element("Element")
    app = _app(fake)
    result = app.open_diagram_view(arg_0)
    fake.OpenDiagramView.assert_called_once_with(arg_0._com)
    assert result is not None


def test_open_file_list() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.open_file_list("value")
    fake.openFileList.assert_called_once_with("value")


def test_open_project_from_design_manager() -> None:
    fake = make_fake_element("Application")
    fake.openProjectFromDesignManager.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.open_project_from_design_manager("value", "value", "value", "value", "value", "value")
    fake.openProjectFromDesignManager.assert_called_once_with("value", "value", "value", "value", "value", "value")
    assert result is not None


def test_open_project_from_design_manager_after_login() -> None:
    fake = make_fake_element("Application")
    fake.openProjectFromDesignManagerAfterLogin.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.open_project_from_design_manager_after_login("value", "value", "value", "value")
    fake.openProjectFromDesignManagerAfterLogin.assert_called_once_with("value", "value", "value", "value")
    assert result is not None


def test_open_project_from_url() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.open_project_from_url("value")
    fake.openProjectFromURL.assert_called_once_with("value")


def test_open_project_with_last_session() -> None:
    fake = make_fake_element("Application")
    fake.openProjectWithLastSession.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.open_project_with_last_session("value")
    fake.openProjectWithLastSession.assert_called_once_with("value")
    assert result is not None


def test_open_project_without_sub_units() -> None:
    fake = make_fake_element("Application")
    fake.openProjectWithoutSubUnits.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.open_project_without_sub_units("value")
    fake.openProjectWithoutSubUnits.assert_called_once_with("value")
    assert result is not None


def test_get_output_window_text() -> None:
    fake = make_fake_element("Application")
    fake.getOutputWindowText.return_value = "result"
    app = _app(fake)
    result = app.get_output_window_text()
    fake.getOutputWindowText.assert_called_once_with()
    assert isinstance(result, str)


def test_get_progress_bar() -> None:
    fake = make_fake_element("Application")
    fake.getProgressBar.return_value = object()
    app = _app(fake)
    result = app.get_progress_bar("value")
    fake.getProgressBar.assert_called_once_with("value")
    assert result is not None


def test_rebuild() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.rebuild()
    fake.rebuild.assert_called_once_with()


def test_rebuild_entire_project() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.rebuild_entire_project()
    fake.rebuildEntireProject.assert_called_once_with()


def test_rebuild_with_dependencies() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.rebuild_with_dependencies()
    fake.rebuildWithDependencies.assert_called_once_with()


def test_redo() -> None:
    fake = make_fake_element("Application")
    fake.redo.return_value = 7
    app = _app(fake)
    result = app.redo()
    fake.redo.assert_called_once_with()
    assert isinstance(result, int)


def test_refactor_selected_operation() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.refactor_selected_operation("value")
    fake.refactorSelectedOperation.assert_called_once_with("value")


def test_refresh_all_views() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.refresh_all_views()
    fake.refreshAllViews.assert_called_once_with()


def test_regenerate_elements() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_collection([])
    app = _app(fake)
    app.regenerate_elements(arg_0)
    fake.regenerateElements.assert_called_once_with(arg_0._com)


def test_regenerate_entire_project() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.regenerate_entire_project()
    fake.regenerateEntireProject.assert_called_once_with()


def test_regenerate_with_dependencies() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.regenerate_with_dependencies()
    fake.regenerateWithDependencies.assert_called_once_with()


def test_register_com_client() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.register_com_client(3, "value", 3)
    fake.registerCOMClient.assert_called_once_with(3, "value", 3)


def test_remove_progress_bar() -> None:
    fake = make_fake_element("Application")
    fake.removeProgressBar.return_value = 7
    arg_0 = make_fake_element("Element")
    app = _app(fake)
    result = app.remove_progress_bar(arg_0)
    fake.removeProgressBar.assert_called_once_with(arg_0._com)
    assert isinstance(result, int)


def test_rename_window_layout() -> None:
    fake = make_fake_element("Application")
    fake.renameWindowLayout.return_value = 7
    app = _app(fake)
    result = app.rename_window_layout("value", "value")
    fake.renameWindowLayout.assert_called_once_with("value", "value")
    assert isinstance(result, int)


def test_report() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.report("value", "value")
    fake.report.assert_called_once_with("value", "value")


def test_reset_window_layout() -> None:
    fake = make_fake_element("Application")
    fake.resetWindowLayout.return_value = 7
    app = _app(fake)
    result = app.reset_window_layout()
    fake.resetWindowLayout.assert_called_once_with()
    assert isinstance(result, int)


def test_get_rhapsody_handle_error_function() -> None:
    fake = make_fake_element("Application")
    fake.getRhapsodyHandleErrorFunction.return_value = 7
    app = _app(fake)
    result = app.get_rhapsody_handle_error_function()
    fake.getRhapsodyHandleErrorFunction.assert_called_once_with()
    assert isinstance(result, int)


def test_get_rhapsody_handle_error_function_long() -> None:
    fake = make_fake_element("Application")
    fake.getRhapsodyHandleErrorFunctionLong.return_value = 7
    app = _app(fake)
    result = app.get_rhapsody_handle_error_function_long()
    fake.getRhapsodyHandleErrorFunctionLong.assert_called_once_with()
    assert isinstance(result, int)


def test_rhp_checkin_license() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.rhp_checkin_license("value")
    fake.RhpCheckinLicense.assert_called_once_with("value")


def test_rhp_checkout_license() -> None:
    fake = make_fake_element("Application")
    fake.RhpCheckoutLicense.return_value = "result"
    app = _app(fake)
    result = app.rhp_checkout_license("value")
    fake.RhpCheckoutLicense.assert_called_once_with("value")
    assert isinstance(result, str)


def test_roundtrip() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.roundtrip()
    fake.roundtrip.assert_called_once_with()


def test_roundtrip_elements() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_collection([])
    app = _app(fake)
    app.roundtrip_elements(arg_0)
    fake.roundtripElements.assert_called_once_with(arg_0._com)


def test_run_application() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.run_application()
    fake.runApplication.assert_called_once_with()


def test_run_helper() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.run_helper("value")
    fake.runHelper.assert_called_once_with("value")


def test_run_helper_with_parameters() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.run_helper_with_parameters("value", "value")
    fake.runHelperWithParameters.assert_called_once_with("value", "value")


def test_save_check_model_result() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.save_check_model_result("value", 3, 3)
    fake.saveCheckModelResult.assert_called_once_with("value", 3, 3)


def test_save_window_layout() -> None:
    fake = make_fake_element("Application")
    fake.saveWindowLayout.return_value = 7
    app = _app(fake)
    result = app.save_window_layout("value", 3)
    fake.saveWindowLayout.assert_called_once_with("value", 3)
    assert isinstance(result, int)


def test_select_graph_elements() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_collection([])
    app = _app(fake)
    app.select_graph_elements(arg_0)
    fake.selectGraphElements.assert_called_once_with(arg_0._com)


def test_select_model_elements() -> None:
    fake = make_fake_element("Application")
    arg_0 = make_fake_collection([])
    app = _app(fake)
    app.select_model_elements(arg_0)
    fake.selectModelElements.assert_called_once_with(arg_0._com)


def test_get_selected_element() -> None:
    fake = make_fake_element("Application")
    fake.getSelectedElement.return_value = make_fake_element("Element")
    app = _app(fake)
    result = app.get_selected_element()
    fake.getSelectedElement.assert_called_once_with()
    assert result is not None


def test_get_selected_graph_elements() -> None:
    fake = make_fake_element("Application")
    fake.getSelectedGraphElements.return_value = make_fake_collection([])
    app = _app(fake)
    result = app.get_selected_graph_elements()
    fake.getSelectedGraphElements.assert_called_once_with()
    assert result is not None


def test_get_serial_no() -> None:
    fake = make_fake_element("Application")
    fake.SerialNo = "value"
    app = _app(fake)
    result = app.serial_no
    assert isinstance(result, str)


def test_start_undo_transaction() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.start_undo_transaction()
    fake.startUndoTransaction.assert_called_once_with()


def test_sync_build() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.sync_build()
    fake.syncBuild.assert_called_once_with()


def test_terminate_application() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.terminate_application()
    fake.terminateApplication.assert_called_once_with()


def test_get_the_code_generator_interface() -> None:
    fake = make_fake_element("Application")
    fake.getTheCodeGeneratorInterface.return_value = object()
    app = _app(fake)
    result = app.get_the_code_generator_interface()
    fake.getTheCodeGeneratorInterface.assert_called_once_with()
    assert result is not None


def test_get_the_external_code_generator_invoker() -> None:
    fake = make_fake_element("Application")
    fake.getTheExternalCodeGeneratorInvoker.return_value = object()
    app = _app(fake)
    result = app.get_the_external_code_generator_invoker()
    fake.getTheExternalCodeGeneratorInvoker.assert_called_once_with()
    assert result is not None


def test_get_the_integrator_interface() -> None:
    fake = make_fake_element("Application")
    fake.getTheIntegratorInterface.return_value = object()
    app = _app(fake)
    result = app.get_the_integrator_interface()
    fake.getTheIntegratorInterface.assert_called_once_with()
    assert result is not None


def test_get_the_java_plugins_interface() -> None:
    fake = make_fake_element("Application")
    fake.getTheJavaPluginsInterface.return_value = object()
    app = _app(fake)
    result = app.get_the_java_plugins_interface()
    fake.getTheJavaPluginsInterface.assert_called_once_with()
    assert result is not None


def test_get_the_roundtrip_interface() -> None:
    fake = make_fake_element("Application")
    fake.getTheRoundtripInterface.return_value = object()
    app = _app(fake)
    result = app.get_the_roundtrip_interface()
    fake.getTheRoundtripInterface.assert_called_once_with()
    assert result is not None


def test_get_tool_set() -> None:
    fake = make_fake_element("Application")
    fake.ToolSet = "value"
    app = _app(fake)
    result = app.tool_set
    assert isinstance(result, str)


def test_set_tool_set() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.tool_set = "value"


def test_undo() -> None:
    fake = make_fake_element("Application")
    fake.undo.return_value = 7
    app = _app(fake)
    result = app.undo()
    fake.undo.assert_called_once_with()
    assert isinstance(result, int)


def test_unload_from_target() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.unload_from_target()
    fake.unloadFromTarget.assert_called_once_with()


def test_unregister_com_client() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.unregister_com_client(3, "value", 3)
    fake.unregisterCOMClient.assert_called_once_with(3, "value", 3)


def test_set_update_recent_file_list() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.set_update_recent_file_list(3)
    fake.setUpdateRecentFileList.assert_called_once_with(3)


def test_update_rmm_data_to_new_version() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.update_rmm_data_to_new_version()
    fake.updateRmmDataToNewVersion.assert_called_once_with()


def test_get_user_data_root() -> None:
    fake = make_fake_element("Application")
    fake.UserDataRoot = "value"
    app = _app(fake)
    result = app.user_data_root
    assert isinstance(result, str)


def test_get_user_omroot() -> None:
    fake = make_fake_element("Application")
    fake.UserOMROOT = "value"
    app = _app(fake)
    result = app.user_omroot
    assert isinstance(result, str)


def test_version_number_long() -> None:
    fake = make_fake_element("Application")
    fake.versionNumberLong.return_value = "result"
    app = _app(fake)
    result = app.version_number_long()
    fake.versionNumberLong.assert_called_once_with()
    assert isinstance(result, str)


def test_get_web_view_url() -> None:
    fake = make_fake_element("Application")
    fake.getWebViewURL.return_value = "result"
    app = _app(fake)
    result = app.get_web_view_url(3)
    fake.getWebViewURL.assert_called_once_with(3)
    assert isinstance(result, str)


def test_set_web_view_url() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.set_web_view_url(3, "value")
    fake.setWebViewURL.assert_called_once_with(3, "value")


def test_get_window_layout_list() -> None:
    fake = make_fake_element("Application")
    fake.getWindowLayoutList.return_value = make_fake_collection([])
    app = _app(fake)
    result = app.get_window_layout_list()
    fake.getWindowLayoutList.assert_called_once_with()
    assert result is not None


def test_write_to_output_window() -> None:
    fake = make_fake_element("Application")
    app = _app(fake)
    app.write_to_output_window("value", "value")
    fake.writeToOutputWindow.assert_called_once_with("value", "value")


def test_get_plug_in_window() -> None:
    fake = make_fake_element("Application")
    fake.GetPlugInWindow.return_value = object()
    app = _app(fake)

    result = app.get_plug_in_window(1, 2, 1)

    fake.GetPlugInWindow.assert_called_once_with(1, 2, 1)
    assert result is not None
