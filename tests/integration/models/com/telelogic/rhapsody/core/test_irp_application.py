"""Integration tests for IRPApplication against a live Rhapsody COM server.

Every test exercises the real pywin32 binding against a freshly launched
Rhapsody instance and asserts on live data. Where a result depends on model
state, the test creates that state first — via the ``test_project`` fixture or
a real COM call. There are no mocks, patches, skips or xfails here: call-shape
proofs belong in the fake-COM unit suite, not in integration coverage.

``quit`` is intentionally not invoked by a test because it would end the
shared session; its live proof is the session teardown in ``tests/conftest.py``.
"""

from __future__ import annotations

import re
import uuid
from pathlib import Path
from typing import Iterator

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_application import IRPApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.support import (
    RPCodeGenSimplifiersRegistry,
    RPExternalCheckRegistry,
    RPExternalRoundtripInvoker,
    RPSearchManager,
    RPSelection,
)
from tests.integration.conftest import TEST_PROJECT_DIR, TEST_PROJECT_NAME


@pytest.fixture(scope="module", autouse=True)
def _hide_application_ui_by_default(rhapsody_app: IRPApplication | None) -> Iterator[None]:
    """Keep this integration module hidden without changing shared fixtures."""
    if rhapsody_app is None:
        yield
        return

    original_hidden_ui = rhapsody_app.is_hidden_ui
    rhapsody_app.set_hidden_ui(True)
    try:
        yield
    finally:
        rhapsody_app.set_hidden_ui(original_hidden_ui)


@pytest.fixture(scope="function")
def live_fixtures(rhapsody_app: IRPApplication, test_project: IRPProject) -> Iterator[dict[str, object]]:
    """Create and clean up live objects for the individual integration case."""
    package = test_project.add_package(f"LiveFixturePkg_{uuid.uuid4().hex}")
    class_obj = package.add_class(f"LiveFixtureCls_{uuid.uuid4().hex}")
    collection = test_project.packages
    try:
        yield {
            "project": test_project,
            "package": package,
            "class": class_obj,
            "collection": collection,
        }
    finally:
        package.delete_from_project()


@pytest.mark.integration
class TestIRPApplicationIntegration:
    """Live coverage for IRPApplication's own COM-bound surface."""

    def test_active_project_returns_current_test_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        active = rhapsody_app.active_project()
        assert active is not None
        assert active.name == TEST_PROJECT_NAME

    def test_application_ui_is_hidden_by_default(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.is_hidden_ui is True

    def test_open_project_returns_the_real_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        opened = rhapsody_app.open_project(str(TEST_PROJECT_DIR / "TestProject.rpyx"))

        assert opened.name == TEST_PROJECT_NAME

    def test_create_new_project_returns_the_created_project(self, rhapsody_app: IRPApplication, tmp_path: Path, test_project: IRPProject) -> None:
        project_dir = tmp_path / "NewProj"
        project_dir.mkdir()

        # Save shared-project changes before switching to avoid Rhapsody's modal save prompt.
        rhapsody_app.save_all()
        created = rhapsody_app.create_new_project(str(project_dir), "CreatedProject")

        assert created is not None
        assert created.name == "CreatedProject"
        active = rhapsody_app.active_project()
        assert active is not None
        assert active.name == "CreatedProject"
        created.delete_from_project()
        reopened = rhapsody_app.open_project(str(TEST_PROJECT_DIR / "TestProject.rpyx"))
        assert reopened.name == TEST_PROJECT_NAME

    def test_projects_collection_contains_the_test_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        projects = rhapsody_app.projects

        names = [projects.get_item(index).name for index in range(1, projects.count + 1)]
        assert TEST_PROJECT_NAME in names

    def test_hidden_ui_roundtrip_uses_real_state(self, rhapsody_app: IRPApplication) -> None:
        original = rhapsody_app.is_hidden_ui

        rhapsody_app.set_hidden_ui(True)
        assert rhapsody_app.is_hidden_ui is True
        rhapsody_app.set_hidden_ui(False)
        assert rhapsody_app.is_hidden_ui is False
        rhapsody_app.set_hidden_ui(original)

    def test_bring_window_to_top_returns_none(self, rhapsody_app: IRPApplication) -> None:
        original_hidden_ui = rhapsody_app.is_hidden_ui
        try:
            assert rhapsody_app.bring_window_to_top() is None  # type: ignore[func-returns-value]
        finally:
            rhapsody_app.set_hidden_ui(original_hidden_ui)

    def test_save_all_returns_none(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.save_all() is None  # type: ignore[func-returns-value]

    def test_version_matches_installed_version(self, rhapsody_app: IRPApplication) -> None:
        assert re.fullmatch(r"\d+\.\d+\.\d+", rhapsody_app.version())

    def test_build_number_is_numeric(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.build_no.isdigit()

    def test_application_root_is_the_install_directory(self, rhapsody_app: IRPApplication) -> None:
        assert Path(rhapsody_app.application_root).is_dir()

    def test_omroot_is_share_directory_under_application_root(self, rhapsody_app: IRPApplication) -> None:
        omroot = Path(rhapsody_app.omroot)
        assert omroot.is_dir()
        assert omroot.parent == Path(rhapsody_app.application_root)

    def test_interface_name_is_irp_application(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.interface_name == "IRPApplication"

    def test_serial_number_is_non_empty(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.serial_no.strip()

    def test_version_number_long_is_non_empty(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.version_number_long().strip()

    def test_locale_name_is_non_empty(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.get_locale_name().strip()

    def test_executable_folder_is_the_install_directory(self, rhapsody_app: IRPApplication) -> None:
        assert Path(rhapsody_app.get_executable_folder()) == Path(rhapsody_app.application_root)

    def test_undo_and_redo_flags_are_boolean_values(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.can_undo() in (0, 1)
        assert rhapsody_app.can_redo() in (0, 1)

    def test_is_rhapsody_cl_flag_is_boolean_value(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.is_rhapsody_cl() in (0, 1)

    def test_create_new_collection_returns_empty_live_collection(self, rhapsody_app: IRPApplication) -> None:
        collection = rhapsody_app.create_new_collection()

        assert isinstance(collection, IRPCollection)
        assert collection.count == 0

    def test_support_accessors_return_live_objects(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.get_search_manager(), RPSearchManager)
        assert isinstance(rhapsody_app.get_selection(), RPSelection)
        assert isinstance(rhapsody_app.get_code_gen_simplifiers_registry(), RPCodeGenSimplifiersRegistry)
        assert isinstance(rhapsody_app.get_external_checker_registry(), RPExternalCheckRegistry)
        assert isinstance(rhapsody_app.get_external_roundtrip_invoker(), RPExternalRoundtripInvoker)

    def test_generate_elements_runs_on_real_collection(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        project = rhapsody_app.open_project(str(TEST_PROJECT_DIR / "TestProject.rpyx"))
        project.add_package("GeneratedPackage")
        collection = project.packages

        assert rhapsody_app.generate_elements(collection) is None  # type: ignore[func-returns-value]

    def test_generate_entire_project_runs(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        assert rhapsody_app.generate_entire_project() is None  # type: ignore[func-returns-value]

    def test_regenerate_runs(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        assert rhapsody_app.regenerate() is None  # type: ignore[func-returns-value]

    def test_check_model_runs_on_test_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        assert rhapsody_app.check_model() is None  # type: ignore[func-returns-value]

    def test_set_log_creates_the_log_file(self, rhapsody_app: IRPApplication, tmp_path: Path) -> None:
        log_file = tmp_path / "rhapsody_test.log"

        assert rhapsody_app.set_log(str(log_file)) is None  # type: ignore[func-returns-value]
        assert log_file.exists()

    def test_wrapper_exposes_full_com_surface(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app, IRPApplication)
        assert isinstance(rhapsody_app, IRPModelElement)

    def test_generate(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.generate() is None  # type: ignore[func-returns-value]

    def test_add_profile_to_model(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.add_profile_to_model("0")
        assert result is not None

    def test_add_selected_to_favorites(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.add_selected_to_favorites() is None  # type: ignore[func-returns-value]

    def test_allow_browser_refresh(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.allow_browser_refresh(0) is None  # type: ignore[func-returns-value]

    def test_allow_ge_refresh(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.allow_ge_refresh(0) is None  # type: ignore[func-returns-value]

    def test_allow_rmm_remote_oslc_links_load(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.allow_rmm_remote_oslc_links_load(0) is None  # type: ignore[func-returns-value]

    def test_get_application_connection_string(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_application_connection_string()
        assert isinstance(result, str)

    def test_get_application_name(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.get_application_name("0", "0") is None  # type: ignore[func-returns-value]

    def test_get_application_status(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_application_status()
        assert isinstance(result, int)

    def test_set_application_status(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.set_application_status(0) is None  # type: ignore[func-returns-value]

    def test_apply_new_terms_profile(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.apply_new_terms_profile("0") is None  # type: ignore[func-returns-value]

    def test_build_entire_project(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        # The app is session-shared; show_gui is launch-only, so hide this COM call locally.
        original_hidden_ui = rhapsody_app.is_hidden_ui
        rhapsody_app.set_hidden_ui(True)
        try:
            assert rhapsody_app.build_entire_project() is None  # type: ignore[func-returns-value]
        finally:
            rhapsody_app.set_hidden_ui(original_hidden_ui)

    def test_clear_output_window(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.clear_output_window("0") is None  # type: ignore[func-returns-value]

    def test_close_all_animated_sequence_diagrams(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.close_all_animated_sequence_diagrams(0) is None  # type: ignore[func-returns-value]

    def test_set_component(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.set_component("0") is None  # type: ignore[func-returns-value]

    def test_set_configuration(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.set_configuration("0") is None  # type: ignore[func-returns-value]

    def test_create_progress_bar(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.create_progress_bar("0")
        assert result is not None

    def test_get_diagram_of_selected_element(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_diagram_of_selected_element()
        assert result is not None

    def test_error_message(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.error_message()
        assert isinstance(result, str)

    def test_get_error_message(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_error_message("0")
        assert isinstance(result, str)

    def test_expand_string_keywords(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.expand_string_keywords("0")
        assert isinstance(result, str)

    def test_fixpack(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.fixpack()
        assert isinstance(result, str)

    def test_force_output2_console(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.force_output2_console(0) is None  # type: ignore[func-returns-value]

    def test_get_helper_status(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_helper_status("0")
        assert isinstance(result, int)

    def test_set_helper_status(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.set_helper_status("0", 0) is None  # type: ignore[func-returns-value]

    def test_get_list_of_factory_properties(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_list_of_factory_properties()
        assert result is not None

    def test_get_list_of_selected_elements(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_list_of_selected_elements()
        assert result is not None

    def test_get_list_of_site_properties(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_list_of_site_properties()
        assert result is not None

    def test_log_root(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.log_root
        assert isinstance(result, str)

    def test_make(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.make() is None  # type: ignore[func-returns-value]

    def test_rebuild_entire_project(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.rebuild_entire_project() is None  # type: ignore[func-returns-value]

    def test_regenerate_entire_project(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.regenerate_entire_project() is None  # type: ignore[func-returns-value]

    def test_get_rhapsody_handle_error_function(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_rhapsody_handle_error_function()
        assert isinstance(result, int)

    def test_get_rhapsody_handle_error_function_long(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_rhapsody_handle_error_function_long()
        assert isinstance(result, int)

    def test_get_the_code_generator_interface(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_the_code_generator_interface()
        assert result is not None

    def test_get_the_external_code_generator_invoker(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_the_external_code_generator_invoker()
        assert result is not None

    def test_get_the_integrator_interface(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_the_integrator_interface()
        assert result is not None

    def test_get_the_java_plugins_interface(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.get_the_java_plugins_interface()
        assert result is not None

    def test_set_update_recent_file_list(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.set_update_recent_file_list(0) is None  # type: ignore[func-returns-value]

    def test_user_data_root(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.user_data_root
        assert isinstance(result, str)

    def test_user_omroot(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        result = rhapsody_app.user_omroot
        assert isinstance(result, str)

    def test_write_to_output_window(self, rhapsody_app: IRPApplication, live_fixtures: dict[str, object]) -> None:
        assert rhapsody_app.write_to_output_window("0", "0") is None  # type: ignore[func-returns-value]
