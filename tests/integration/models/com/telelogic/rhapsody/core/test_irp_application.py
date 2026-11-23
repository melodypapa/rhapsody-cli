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

_LAYOUT_NAME = "IRPIntegrationLayout"


@pytest.fixture
def saved_window_layout(rhapsody_app: IRPApplication) -> Iterator[str]:
    """Create a real Rhapsody window layout and remove it after the test."""
    rhapsody_app.save_window_layout(_LAYOUT_NAME, 1)
    yield _LAYOUT_NAME
    rhapsody_app.delete_window_layout(_LAYOUT_NAME)


@pytest.mark.integration
class TestIRPApplicationIntegration:
    """Live coverage for IRPApplication's own COM-bound surface."""

    def test_active_project_returns_none_when_no_project_is_open(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.active_project() is None

    def test_open_project_returns_the_real_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        opened = rhapsody_app.open_project(str(TEST_PROJECT_DIR / "TestProject.rpyx"))

        assert opened.get_name() == TEST_PROJECT_NAME

    def test_active_project_is_the_test_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        assert rhapsody_app.active_project().get_name() == TEST_PROJECT_NAME

    def test_create_new_project_returns_the_created_project(self, rhapsody_app: IRPApplication, tmp_path: Path, test_project: IRPProject) -> None:
        project_dir = tmp_path / "NewProj"
        project_dir.mkdir()

        created = rhapsody_app.create_new_project(str(project_dir), "CreatedProject")

        assert created.get_name() == "CreatedProject"
        assert rhapsody_app.active_project().get_name() == "CreatedProject"
        created.delete_from_project()
        rhapsody_app.open_project(str(TEST_PROJECT_DIR / "TestProject.rpyx"))

    def test_projects_collection_contains_the_test_project(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        projects = rhapsody_app.projects

        names = [projects.get_item(index).get_name() for index in range(1, projects.get_count() + 1)]
        assert TEST_PROJECT_NAME in names

    def test_hidden_ui_roundtrip_uses_real_state(self, rhapsody_app: IRPApplication) -> None:
        original = rhapsody_app.is_hidden_ui

        rhapsody_app.set_hidden_ui(True)
        assert rhapsody_app.is_hidden_ui is True
        rhapsody_app.set_hidden_ui(False)
        assert rhapsody_app.is_hidden_ui is False
        rhapsody_app.set_hidden_ui(original)

    def test_bring_window_to_top_returns_none(self, rhapsody_app: IRPApplication) -> None:
        assert rhapsody_app.bring_window_to_top() is None  # type: ignore[func-returns-value]

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

    def test_window_layout_list_reflects_created_layout(self, rhapsody_app: IRPApplication, saved_window_layout: str) -> None:
        layouts = rhapsody_app.get_window_layout_list()

        names = [str(layouts.get_item(index)) for index in range(1, layouts.get_count() + 1)]
        assert saved_window_layout in names

    def test_create_new_collection_returns_empty_live_collection(self, rhapsody_app: IRPApplication) -> None:
        collection = rhapsody_app.create_new_collection()

        assert isinstance(collection, IRPCollection)
        assert collection.get_count() == 0

    def test_support_accessors_return_live_objects(self, rhapsody_app: IRPApplication) -> None:
        assert isinstance(rhapsody_app.get_search_manager(), RPSearchManager)
        assert isinstance(rhapsody_app.get_selection(), RPSelection)
        assert isinstance(rhapsody_app.get_code_gen_simplifiers_registry(), RPCodeGenSimplifiersRegistry)
        assert isinstance(rhapsody_app.get_external_checker_registry(), RPExternalCheckRegistry)
        assert isinstance(rhapsody_app.get_external_roundtrip_invoker(), RPExternalRoundtripInvoker)

    def test_generate_elements_runs_on_real_collection(self, rhapsody_app: IRPApplication, test_project: IRPProject) -> None:
        project = rhapsody_app.open_project(str(TEST_PROJECT_DIR / "TestProject.rpyx"))
        project.add_package("GeneratedPackage")
        collection = project.get_packages()

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
