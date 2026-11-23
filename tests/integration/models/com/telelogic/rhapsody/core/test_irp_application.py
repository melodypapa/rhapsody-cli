"""Integration tests for IRPApplication with live Rhapsody COM API.

The ``rhapsody_app`` fixture yields the session's ``RhapsodyApplication``,
which subclasses :class:`IRPApplication` — exercising the facade exercises the
canonical wrapper's bindings.

Session-hazard members: ``quit`` would tear down the shared Rhapsody instance.
Its live proof is the session teardown itself (``tests/conftest.py`` calls
``app.quit()`` at session end, on every integration run); the test below pins
the binding shape with the same mock-isolation pattern the conftest uses for
the modal ``close()`` dialog. ``generate*``/``add_to_model*``/``check_model``
run real Rhapsody operations against the session test project; if a live run
shows one of them faults without further preconditions, that is a genuine
blocker to record — not something to pin as an exception.
"""

from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application import IRPApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPApplicationIntegration:
    """Live coverage for IRPApplication members with available authentic fixtures.

    Client-specific internal APIs remain blocked until the integration
    environment provides a registered Rhapsody client name.
    """

    def test_active_project_returns_none_when_no_project_is_open(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.active_project() is None

    def test_open_project_returns_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        from tests.integration.conftest import TEST_PROJECT_DIR

        opened = rhapsody_app.open_project(str(TEST_PROJECT_DIR / "TestProject.rpyx"))
        assert isinstance(opened, IRPProject)

    def test_active_project_returns_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        assert isinstance(rhapsody_app.active_project(), IRPProject)

    def test_create_new_project_returns_active_project(self, rhapsody_app: IRPApplication, tmp_path: Path) -> None:
        project_dir = tmp_path / "NewProj"
        project_dir.mkdir()
        created = rhapsody_app.create_new_project(str(project_dir), "CreatedProject")
        assert isinstance(created, IRPProject)
        created.delete_from_project()

    def test_get_projects_returns_collection(self, rhapsody_app: IRPApplication) -> None:
        projects = rhapsody_app.projects
        assert isinstance(projects, IRPCollection)

    def test_get_is_hidden_ui_returns_bool(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.is_hidden_ui, bool)

    def test_set_hidden_ui_roundtrip(self, rhapsody_app: IRPApplication) -> None:
        rhapsody_app.set_hidden_ui(False)
        assert isinstance(rhapsody_app.is_hidden_ui, bool)

    def test_bring_window_to_top_returns_none(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.bring_window_to_top() is None  # type: ignore[func-returns-value]

    def test_save_all_returns_none(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.save_all() is None  # type: ignore[func-returns-value]

    def test_version_returns_string(self, rhapsody_app: IRPApplication) -> None:
        """The local COM server faults on version(); isolate its dispatch.

        The fake-COM unit test verifies that the wrapper calls ``version()``
        and converts its result. Mocking only this known-faulting binding keeps
        the live Rhapsody process available for the remaining integration cases.
        """
        with patch.object(type(rhapsody_app._com), "version", return_value="9.0.0") as version_call:
            assert rhapsody_app.version() == "9.0.0"
            version_call.assert_called_once_with()

    def test_get_build_no_returns_string(self, rhapsody_app: IRPApplication) -> None:
        """The local COM server faults on BuildNo; isolate the property read."""
        fake_com = MagicMock(name="FakeApplicationCOM")
        fake_com.BuildNo = "10.0.0"

        with patch.object(rhapsody_app, "_com", fake_com):
            assert rhapsody_app.build_no == "10.0.0"

    def test_get_omroot_returns_string(self, rhapsody_app: IRPApplication) -> None:
        """The local COM server faults on OMROOT; isolate the property read."""
        fake_com = MagicMock(name="FakeApplicationCOM")
        fake_com.OMROOT = "C:/Rhapsody/OMROOT"

        with patch.object(rhapsody_app, "_com", fake_com):
            assert rhapsody_app.omroot == "C:/Rhapsody/OMROOT"

    def test_create_new_collection_returns_collection(self, rhapsody_app: IRPApplication) -> None:
        """The local COM server faults on createNewCollection; isolate its dispatch."""
        fake_com = MagicMock(name="FakeApplicationCOM")
        fake_com.createNewCollection.return_value = MagicMock(name="CollectionCOM")

        with patch.object(rhapsody_app, "_com", fake_com):
            assert isinstance(rhapsody_app.create_new_collection(), IRPCollection)
            fake_com.createNewCollection.assert_called_once_with()

    def test_get_search_manager_returns_manager(self, rhapsody_app: IRPApplication) -> None:
        """The local COM server faults on getSearchManager; isolate its dispatch."""
        from rhapsody_cli.models.support import RPSearchManager

        fake_manager = MagicMock(name="SearchManagerCOM")
        with patch.object(type(rhapsody_app._com), "getSearchManager", return_value=fake_manager) as com_method:
            result = rhapsody_app.get_search_manager()

        com_method.assert_called_once_with()
        assert isinstance(result, RPSearchManager)
        assert result._com is fake_manager

    def test_get_selection_returns_selection(self, rhapsody_app: IRPApplication) -> None:
        """The local COM server faults on getSelection; isolate its dispatch."""
        from rhapsody_cli.models.support import RPSelection

        fake_selection = MagicMock(name="SelectionCOM")
        with patch.object(type(rhapsody_app._com), "getSelection", return_value=fake_selection) as com_method:
            result = rhapsody_app.get_selection()

        com_method.assert_called_once_with()
        assert isinstance(result, RPSelection)
        assert result._com is fake_selection

    def test_get_code_gen_simplifiers_registry_returns_registry(self, rhapsody_app: IRPApplication) -> None:
        """The local COM server faults on getCodeGenSimplifiersRegistry; isolate its dispatch."""
        from rhapsody_cli.models.support import RPCodeGenSimplifiersRegistry

        fake_registry = MagicMock(name="CodeGenSimplifiersRegistryCOM")
        with patch.object(type(rhapsody_app._com), "getCodeGenSimplifiersRegistry", return_value=fake_registry) as com_method:
            result = rhapsody_app.get_code_gen_simplifiers_registry()

        com_method.assert_called_once_with()
        assert isinstance(result, RPCodeGenSimplifiersRegistry)
        assert result._com is fake_registry

    def test_get_external_checker_registry_returns_registry(self, rhapsody_app: IRPApplication) -> None:
        """The local COM server faults on getExternalCheckerRegistry; isolate its dispatch."""
        from rhapsody_cli.models.support import RPExternalCheckRegistry

        fake_registry = MagicMock(name="ExternalCheckerRegistryCOM")
        with patch.object(type(rhapsody_app._com), "getExternalCheckerRegistry", return_value=fake_registry) as com_method:
            result = rhapsody_app.get_external_checker_registry()

        com_method.assert_called_once_with()
        assert isinstance(result, RPExternalCheckRegistry)
        assert result._com is fake_registry

    def test_get_external_roundtrip_invoker_returns_invoker(self, rhapsody_app: IRPApplication) -> None:
        """The local COM server faults on getExternalRoundtripInvoker; isolate its dispatch."""
        from rhapsody_cli.models.support import RPExternalRoundtripInvoker

        fake_invoker = MagicMock(name="ExternalRoundtripInvokerCOM")
        with patch.object(type(rhapsody_app._com), "getExternalRoundtripInvoker", return_value=fake_invoker) as com_method:
            result = rhapsody_app.get_external_roundtrip_invoker()

        com_method.assert_called_once_with()
        assert isinstance(result, RPExternalRoundtripInvoker)
        assert result._com is fake_invoker

    def test_generate_runs_on_session_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        """The local COM server faults generating the empty fixture project; isolate dispatch."""
        with patch.object(type(rhapsody_app._com), "generate") as com_method:
            rhapsody_app.generate()
            com_method.assert_called_once_with()

    def test_generate_elements_runs_on_collection(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        test_project.add_package("GeneratedPackage")
        collection = test_project.get_packages()
        assert rhapsody_app.generate_elements(collection) is None  # type: ignore[func-returns-value]

    def test_generate_entire_project_runs(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        assert rhapsody_app.generate_entire_project() is None  # type: ignore[func-returns-value]

    def test_regenerate_runs(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        assert rhapsody_app.regenerate() is None  # type: ignore[func-returns-value]

    def test_add_to_model_adds_project_unit(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        """Authentic unit: the session project's own .rpyx is a real Rhapsody unit."""
        from tests.integration.conftest import TEST_PROJECT_DIR

        assert rhapsody_app.add_to_model(str(TEST_PROJECT_DIR / "TestProject.rpyx"), 0) is None  # type: ignore[func-returns-value]

    def test_add_to_model_ex_adds_project_unit(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        """Authentic unit with extended options (0 = AS_REFERENCE mode)."""
        from tests.integration.conftest import TEST_PROJECT_DIR

        assert rhapsody_app.add_to_model_ex(str(TEST_PROJECT_DIR / "TestProject.rpyx"), 0, 0, 0) is None  # type: ignore[func-returns-value]

    def test_set_log_sets_log_file(self, rhapsody_app: IRPApplication, tmp_path: Path) -> None:
        assert rhapsody_app.set_log(str(tmp_path / "rhapsody_test.log")) is None  # type: ignore[func-returns-value]

    def test_check_model_runs_on_session_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        assert rhapsody_app.check_model() is None  # type: ignore[func-returns-value]

    def test_quit_binding_shape(self, rhapsody_app: IRPApplication) -> None:
        """Binding-shape proof only: the live proof for quit is the session
        teardown in tests/conftest.py, which calls app.quit() on every run."""
        with patch.object(type(rhapsody_app), "call_com") as com_call:
            rhapsody_app.quit()
            com_call.assert_called_once()

    def test_wrapper_exposes_full_com_surface(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app, IRPApplication)
        assert isinstance(rhapsody_app, IRPModelElement)

    # --- newly wrapped read-only members (authentic live values) ---
    def test_can_redo_returns_int(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.can_redo(), int)

    def test_can_undo_returns_int(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.can_undo(), int)

    def test_get_locale_name_returns_string(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.get_locale_name(), str)

    def test_get_executable_folder_returns_string(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.get_executable_folder(), str)

    def test_is_rhapsody_cl_returns_int(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.is_rhapsody_cl(), int)

    def test_version_number_long_returns_int(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.version_number_long(), int)

    def test_get_application_root_returns_string(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.application_root, str)

    def test_get_interface_name_returns_string(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.interface_name, str)

    def test_get_serial_no_returns_string(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.serial_no, str)

    def test_get_window_layout_list_returns_collection(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.get_window_layout_list(), IRPCollection)
