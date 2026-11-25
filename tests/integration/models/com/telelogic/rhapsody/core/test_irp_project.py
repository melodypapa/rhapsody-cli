"""Integration tests for IRPProject and IRPPackage with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import time
import uuid
from pathlib import Path

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestRPProjectIntegration:
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
        assert new_pkg is not None
        assert isinstance(new_pkg, IRPPackage)
        assert isinstance(new_pkg, IRPPackage)
        pkgs = test_project.packages
        names = [p.name for p in pkgs]
        assert name in names

    def test_project_packages_returns_collection(self, test_project: IRPProject) -> None:
        pkgs = test_project.packages
        assert pkgs is not None

    def test_create_component_in_project(self, test_project: IRPProject) -> None:
        comp_name = self._unique("MyComponent")
        comp = test_project.add_component(comp_name)
        try:
            assert comp is not None
        finally:
            comp.delete_from_project()

    def test_find_element_by_binary_id_finds_created_class(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("BinIdPkg"))
        try:
            created = pkg.add_class(self._unique("BinIdCls"))

            found = test_project.find_element_by_binary_id(created.binary_id)

            assert found is not None
            assert found.binary_id == created.binary_id
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
        assert test_project.check_events_base_ids_solve_collisions() is None


@pytest.mark.integration
class TestRPPackageIntegration:
    """Integration tests for IRPPackage with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{int(time.time() * 1000) % 1000000}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_create_nested_packages(self, test_project: IRPProject) -> None:
        parent_name = self._unique("ParentPkg")
        child_name = self._unique("ChildPkg")
        parent_pkg = self._create_package(test_project, parent_name)
        child_pkg = parent_pkg.add_nested_package(child_name)
        assert child_pkg is not None
        assert isinstance(child_pkg, IRPPackage)
        assert child_pkg in list(parent_pkg.packages)

    def test_package_navigation(self, test_project: IRPProject) -> None:
        parent_name = self._unique("NavParent")
        child_name = self._unique("NavChild")
        parent_pkg = self._create_package(test_project, parent_name)
        child_pkg = parent_pkg.add_nested_package(child_name)
        owner = child_pkg.owner
        assert owner is not None
        assert owner == parent_pkg
        assert isinstance(owner, IRPPackage)

    def test_add_class_to_package(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("ClassPkg")
        class_name = self._unique("TestClass")
        pkg = self._create_package(test_project, pkg_name)
        new_class = pkg.add_class(class_name)
        assert new_class is not None
        assert isinstance(new_class, IRPClass)
        classes = pkg.classes
        class_names = [c.name for c in classes]
        assert class_name in class_names

    def test_create_module_in_package(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("ModPkg")
        mod_name = self._unique("MyModule")
        pkg = self._create_package(test_project, pkg_name)
        try:
            mod = pkg.add_module(mod_name)
            assert mod is not None
        finally:
            mod.delete_from_project()


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
            assert pkg.name == package_name
        finally:
            if pkg is not None:
                pkg.delete_from_project()

    def test_find_component(self, test_project: IRPProject) -> None:
        assert test_project.find_component(self._unique("missing")) is None

    def test_packages(self, test_project: IRPProject) -> None:
        created = test_project.add_package(self._unique("GetterPkg"))
        try:
            assert created in list(test_project.packages)
        finally:
            created.delete_from_project()

    def test_components(self, test_project: IRPProject) -> None:
        created = test_project.add_component(self._unique("GetterComp"))
        try:
            assert created in list(test_project.components)
        finally:
            created.delete_from_project()

    def test_find_element_by_guid(self, test_project: IRPProject) -> None:
        assert test_project.find_element_by_guid(self._unique("missing")) is None

    def test_add_component(self, test_project: IRPProject) -> None:
        pkg = None
        try:
            component_name = self._unique("AddComponent")
            pkg = test_project.add_component(component_name)
            assert pkg.name == component_name
        finally:
            if pkg is not None:
                pkg.delete_from_project()

    def test_delete_component(self, test_project: IRPProject) -> None:
        name = self._unique("DelComp")
        component = test_project.add_component(name)
        assert component is not None
        test_project.delete_component(component)
        assert test_project.find_component(name) is None

    def test_find_node(self, test_project: IRPProject) -> None:
        assert test_project.find_node(self._unique("missing")) is None

    def test_get_new_collaboration(self, test_project: IRPProject) -> None:
        collaboration = test_project.get_new_collaboration()
        try:
            assert collaboration.meta_class == "Collaboration"
        finally:
            collaboration.delete_from_project()

    def test_add_profile(self, test_project: IRPProject) -> None:
        profile = None
        try:
            profile_name = self._unique("AddProfile")
            profile = test_project.add_profile(profile_name)
            assert profile.name == profile_name
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
            assert test_project.remove_custom_view_on_browser(view) is None  # type: ignore[func-returns-value]
        finally:
            view.delete_from_project()

    def test_add_custom_view_on_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ViewPkg"))
        try:
            diagram = pkg.add_object_model_diagram(self._unique("ViewDiagram"))
            assert test_project.add_custom_view_on_diagram(diagram, pkg) is None  # type: ignore[func-returns-value]
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
        """JavaDoc IRPProject.migrateDesignManagerLinks exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        with pytest.raises(NotImplementedError):
            test_project.migrate_design_manager_links()

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
        assert test_project.set_wait_dialog_watchdog_value(0) is None  # type: ignore[func-returns-value]

    def test_start_transaction_of_no_cg_interest(self, test_project: IRPProject) -> None:
        assert test_project.start_transaction_of_no_cg_interest() is None  # type: ignore[func-returns-value]
