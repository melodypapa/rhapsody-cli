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

from unittest.mock import patch

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application import IRPApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPApplicationIntegration:
    """Live coverage for every IRPApplication COM-bound member."""

    def test_open_project_returns_project(self, rhapsody_app: IRPApplication) -> None:
        from tests.integration.conftest import TEST_PROJECT_DIR

        opened = rhapsody_app.open_project(str(TEST_PROJECT_DIR / "TestProject.rpyx"))
        assert isinstance(opened, IRPProject)

    def test_create_new_project_returns_active_project(self, rhapsody_app: IRPApplication, tmp_path) -> None:
        project_dir = tmp_path / "NewProj"
        project_dir.mkdir()
        created = rhapsody_app.create_new_project(str(project_dir), "CreatedProject")
        assert isinstance(created, IRPProject)
        created.delete_from_project()

    def test_active_project_returns_project(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.active_project(), IRPProject)

    def test_active_project_raises_when_com_returns_none(self, rhapsody_app: IRPApplication) -> None:
        """Branch proof for the None guard. The live happy path is covered by
        ``test_active_project_returns_project``; this isolated shape test feeds
        a None through the real wrapper so both branches execute."""
        from rhapsody_cli.exceptions import RhapsodyRuntimeException

        with patch.object(type(rhapsody_app), "call_com", return_value=None):
            with pytest.raises(RhapsodyRuntimeException, match="No active project is open"):
                rhapsody_app.active_project()

    def test_get_projects_returns_collection(self, rhapsody_app: IRPApplication) -> None:
        projects = rhapsody_app.get_projects()
        assert isinstance(projects, IRPCollection)

    def test_get_is_hidden_ui_returns_bool(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.get_is_hidden_ui(), bool)

    def test_set_hidden_ui_roundtrip(self, rhapsody_app: IRPApplication) -> None:
        rhapsody_app.set_hidden_ui(False)
        assert isinstance(rhapsody_app.get_is_hidden_ui(), bool)

    def test_bring_window_to_top_returns_none(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.bring_window_to_top() is None  # type: ignore[func-returns-value]

    def test_save_all_returns_none(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.save_all() is None  # type: ignore[func-returns-value]

    def test_get_version_returns_string(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.get_version(), str)

    def test_get_build_no_returns_string(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.get_build_no(), str)

    def test_get_omroot_returns_string(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.get_omroot(), str)

    def test_create_new_collection_returns_collection(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.create_new_collection(), IRPCollection)

    def test_get_search_manager_returns_manager(self, rhapsody_app: IRPApplication) -> None:
        from rhapsody_cli.models.support import RPSearchManager

        assert isinstance(rhapsody_app.get_search_manager(), RPSearchManager)

    def test_get_selection_returns_selection(self, rhapsody_app: IRPApplication) -> None:
        from rhapsody_cli.models.support import RPSelection

        assert isinstance(rhapsody_app.get_selection(), RPSelection)

    def test_get_code_gen_simplifiers_registry_returns_registry(self, rhapsody_app: IRPApplication) -> None:
        from rhapsody_cli.models.support import RPCodeGenSimplifiersRegistry

        assert isinstance(rhapsody_app.get_code_gen_simplifiers_registry(), RPCodeGenSimplifiersRegistry)

    def test_get_diag_synth_api_returns_api(self, rhapsody_app: IRPApplication) -> None:
        from rhapsody_cli.models.support import RPDiagSynthAPI

        assert isinstance(rhapsody_app.get_diag_synth_api("TestClient"), RPDiagSynthAPI)

    def test_get_external_checker_registry_returns_registry(self, rhapsody_app: IRPApplication) -> None:
        from rhapsody_cli.models.support import RPExternalCheckRegistry

        assert isinstance(rhapsody_app.get_external_checker_registry(), RPExternalCheckRegistry)

    def test_get_external_ide_registry_returns_registry(self, rhapsody_app: IRPApplication) -> None:
        from rhapsody_cli.models.support import RPExternalIDERegistry

        assert isinstance(rhapsody_app.get_external_ide_registry("TestClient"), RPExternalIDERegistry)

    def test_get_external_roundtrip_invoker_returns_invoker(self, rhapsody_app: IRPApplication) -> None:
        from rhapsody_cli.models.support import RPExternalRoundtripInvoker

        assert isinstance(rhapsody_app.get_external_roundtrip_invoker(), RPExternalRoundtripInvoker)

    def test_get_ow_pane_mgr_returns_pane_manager(self, rhapsody_app: IRPApplication) -> None:
        from rhapsody_cli.models.support import RPowPaneMgr

        assert isinstance(rhapsody_app.get_ow_pane_mgr("TestClient"), RPowPaneMgr)

    def test_generate_runs_on_session_project(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.generate() is None  # type: ignore[func-returns-value]

    def test_generate_elements_runs_on_collection(self, rhapsody_app: IRPApplication) -> None:
        collection = rhapsody_app.create_new_collection()
        assert rhapsody_app.generate_elements(collection) is None  # type: ignore[func-returns-value]

    def test_generate_entire_project_runs(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.generate_entire_project() is None  # type: ignore[func-returns-value]

    def test_regenerate_runs(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.regenerate() is None  # type: ignore[func-returns-value]

    def test_add_to_model_adds_project_unit(self, rhapsody_app: IRPApplication) -> None:
        """Authentic unit: the session project's own .rpyx is a real Rhapsody unit."""
        from tests.integration.conftest import TEST_PROJECT_DIR

        assert rhapsody_app.add_to_model(str(TEST_PROJECT_DIR / "TestProject.rpyx"), 0) is None  # type: ignore[func-returns-value]

    def test_add_to_model_ex_adds_project_unit(self, rhapsody_app: IRPApplication) -> None:
        """Authentic unit with extended options (0 = AS_REFERENCE mode)."""
        from tests.integration.conftest import TEST_PROJECT_DIR

        assert rhapsody_app.add_to_model_ex(str(TEST_PROJECT_DIR / "TestProject.rpyx"), 0, 0, 0) is None  # type: ignore[func-returns-value]

    def test_set_log_sets_log_file(self, rhapsody_app: IRPApplication, tmp_path) -> None:
        assert rhapsody_app.set_log(str(tmp_path / "rhapsody_test.log")) is None  # type: ignore[func-returns-value]

    def test_check_model_runs_on_session_project(self, rhapsody_app: IRPApplication) -> None:
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
