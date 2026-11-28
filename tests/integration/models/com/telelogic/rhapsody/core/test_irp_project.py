"""Integration tests for IRPProject with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import time
import uuid
from pathlib import Path

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collaboration import IRPCollaboration
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPProjectIntegration:
    """Integration tests for IRPProject with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{int(time.time() * 1000) % 1000000}"

    def test_project_is_rp_project(self, test_project: IRPProject) -> None:
        assert isinstance(test_project, IRPProject)
        assert isinstance(test_project, IRPPackage)
        assert isinstance(test_project, IRPModelElement)

    def test_add_package_to_project(self, test_project: IRPProject) -> None:
        name = self._unique("TopLevelPkg")
        new_pkg = test_project.add_package(name)
        try:
            assert isinstance(new_pkg, IRPPackage)
        finally:
            new_pkg.delete_from_project()

    def test_save_returns_none(self, test_project: IRPProject) -> None:
        assert test_project.save() is None  # type: ignore[func-returns-value]

    def test_use_unique_stereotype_and_ref_cache_write_only_setter(self, test_project: IRPProject) -> None:
        # The pywin32 property is write-only; this disposable project ends with the cache disabled.
        test_project.use_unique_stereotype_and_ref_cache = 1
        test_project.use_unique_stereotype_and_ref_cache = 0

    def test_all_stereotypes(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("StereoPkg"))
        try:
            stereotype = pkg.add_new_aggr("Stereotype", self._unique("ProjectStereo"))
            assert stereotype in list(test_project.all_stereotypes)
        finally:
            pkg.delete_from_project()

    def test_create_component_in_project(self, test_project: IRPProject) -> None:
        comp_name = self._unique("MyComponent")
        comp = test_project.add_component(comp_name)
        try:
            assert comp in list(test_project.components)
        finally:
            comp.delete_from_project()

    def test_find_element_by_binary_id_finds_created_class(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("BinIdPkg"))
        try:
            created = pkg.add_class(self._unique("BinIdCls"))

            found = test_project.find_element_by_binary_id(created.binary_id)

            assert found == created
        finally:
            pkg.delete_from_project()

    def test_default_directory_scheme_roundtrip(self, test_project: IRPProject) -> None:
        original = test_project.default_directory_scheme
        try:
            assert isinstance(original, str)
            test_project.default_directory_scheme = "Flat"
            assert test_project.default_directory_scheme == "Flat"
        finally:
            test_project.default_directory_scheme = original

    def test_check_events_base_ids_solve_collisions_completes(self, test_project: IRPProject) -> None:
        assert test_project.check_events_base_ids_solve_collisions() is None  # type: ignore[func-returns-value]


@pytest.mark.integration
class TestIRPProjectGenerated:
    """Generated live coverage for IRPProject owned methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_package(self, test_project: IRPProject) -> None:
        pkg = None
        try:
            package_name = self._unique("AddPackage")
            pkg = test_project.add_package(package_name)
            assert isinstance(pkg, IRPPackage)
        finally:
            if pkg is not None:
                pkg.delete_from_project()

    def test_find_component(self, test_project: IRPProject) -> None:
        created = test_project.add_component(self._unique("FindableComp"))
        try:
            found = test_project.find_component(created.name)
            assert found is not None
            assert found == created
            assert test_project.find_component(self._unique("missing")) is None
        finally:
            created.delete_from_project()

    def test_components(self, test_project: IRPProject) -> None:
        created = test_project.add_component(self._unique("GetterComp"))
        try:
            assert created in list(test_project.components)
        finally:
            created.delete_from_project()

    def test_find_element_by_guid(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("GuidPkg"))
        try:
            created = pkg.add_class(self._unique("GuidCls"))
            found = test_project.find_element_by_guid(created.guid)
            assert found is not None
            assert found == created
            assert test_project.find_element_by_guid(self._unique("missing")) is None
        finally:
            pkg.delete_from_project()

    def test_add_component(self, test_project: IRPProject) -> None:
        pkg = None
        try:
            component_name = self._unique("AddComponent")
            pkg = test_project.add_component(component_name)
            assert pkg in list(test_project.components)
        finally:
            if pkg is not None:
                pkg.delete_from_project()

    def test_delete_component(self, test_project: IRPProject) -> None:
        name = self._unique("DelComp")
        component = test_project.add_component(name)
        assert component in list(test_project.components)
        test_project.delete_component(component)
        assert test_project.find_component(name) is None

    def test_get_new_collaboration(self, test_project: IRPProject) -> None:
        collaboration = test_project.get_new_collaboration()
        try:
            assert isinstance(collaboration, IRPCollaboration)
        finally:
            collaboration.delete_from_project()

    def test_add_profile(self, test_project: IRPProject) -> None:
        profile = None
        try:
            profile_name = self._unique("AddProfile")
            profile = test_project.add_profile(profile_name)
            assert profile in list(test_project.profiles)
        finally:
            if profile is not None:
                profile.delete_from_project()

    def test_profiles(self, test_project: IRPProject) -> None:
        created = test_project.add_profile(self._unique("GetterProfile"))
        try:
            assert created in list(test_project.profiles)
        finally:
            created.delete_from_project()

    def test_allow_auto_save(self, test_project: IRPProject) -> None:
        assert test_project.allow_auto_save(0) is None  # type: ignore[func-returns-value]

    def test_allow_non_unique_names(self, test_project: IRPProject) -> None:
        assert test_project.allow_non_unique_names(0) is None  # type: ignore[func-returns-value]

    def test_cg_simplified_model_package(self, test_project: IRPProject) -> None:
        assert test_project.cg_simplified_model_package is None

    def test_highlight_from_code(self, test_project: IRPProject) -> None:
        # A real on-disk source file and a real line number from it.
        source_file = Path(__file__).resolve()
        line_number = 1
        assert source_file.is_file()
        assert test_project.highlight_from_code(source_file.as_posix(), line_number) is None  # type: ignore[func-returns-value]

    def test_add_custom_view_on_browser(self, test_project: IRPProject) -> None:
        view = test_project.add_package(self._unique("ViewElem"))
        try:
            assert test_project.add_custom_view_on_browser(view) is None  # type: ignore[func-returns-value]
            assert view in list(test_project.get_active_custom_views_on_browser())
            assert test_project.remove_custom_view_on_browser(view) is None  # type: ignore[func-returns-value]
        finally:
            view.delete_from_project()

    def test_add_custom_view_on_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ViewPkg"))
        try:
            diagram = pkg.add_object_model_diagram(self._unique("ViewDiagram"))
            assert test_project.add_custom_view_on_diagram(diagram, pkg) is None  # type: ignore[func-returns-value]
            assert pkg in list(test_project.get_active_custom_views_on_diagram(diagram))
            assert test_project.remove_custom_view_on_diagram(diagram, pkg) is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_open_csv_file(self, test_project: IRPProject) -> None:
        assert test_project.open_csv_file(self._unique("MissingCsv"), 0) is None  # type: ignore[func-returns-value]

    def test_enable_rhapsody_model_manager(self, test_project: IRPProject) -> None:
        """JavaDoc IRPProject.enableRhapsodyModelManager exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        with pytest.raises(NotImplementedError):
            test_project.enable_rhapsody_model_manager()

    def test_migrate_design_manager_links(self, test_project: IRPProject) -> None:
        """JavaDoc IRPProject.migrateDesignManagerLinks exists, but pywin32 does not expose it, so the stub raises before dispatch."""
        with pytest.raises(NotImplementedError):
            test_project.migrate_design_manager_links()

    def test_is_resolve_on_demand(self, test_project: IRPProject) -> None:
        """JavaDoc declares the getter, but pywin32 does not expose it."""
        with pytest.raises(NotImplementedError):
            test_project.is_resolve_on_demand()

    def test_set_resolve_on_demand(self, test_project: IRPProject) -> None:
        """JavaDoc declares the setter, but pywin32 does not expose it."""
        with pytest.raises(NotImplementedError):
            test_project.set_resolve_on_demand(1)

    def test_recalculate_events_base_ids(self, test_project: IRPProject) -> None:
        assert test_project.recalculate_events_base_ids() is None  # type: ignore[func-returns-value]

    def test_end_transaction_of_no_cg_interest(self, test_project: IRPProject) -> None:
        assert test_project.end_transaction_of_no_cg_interest() is None  # type: ignore[func-returns-value]

    def test_get_notify_plugin_on_elements_changed(self, test_project: IRPProject) -> None:
        original = test_project.get_notify_plugin_on_elements_changed()
        try:
            test_project.set_notify_plugin_on_elements_changed(1 - original)
            assert test_project.get_notify_plugin_on_elements_changed() == 1 - original
        finally:
            test_project.set_notify_plugin_on_elements_changed(original)

    def test_set_global_configuration(self, test_project: IRPProject) -> None:
        """JavaDoc IRPProject.setGlobalConfiguration exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        with pytest.raises(NotImplementedError):
            test_project.set_global_configuration(self._unique("gc"), self._unique("name"))

    def test_set_notify_plugin_on_elements_changed(self, test_project: IRPProject) -> None:
        assert test_project.set_notify_plugin_on_elements_changed(0) is None  # type: ignore[func-returns-value]

    def test_set_wait_dialog_watchdog_value(self, test_project: IRPProject) -> None:
        assert test_project.set_wait_dialog_watchdog_value("") is None  # type: ignore[func-returns-value]

    def test_start_transaction_of_no_cg_interest(self, test_project: IRPProject) -> None:
        assert test_project.start_transaction_of_no_cg_interest() is None  # type: ignore[func-returns-value]
