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
        try:
            assert isinstance(new_pkg, IRPPackage)
            pkgs = test_project.packages
            names = [p.name for p in pkgs]
            assert name in names
        finally:
            new_pkg.delete_from_project()

    def test_project_packages_returns_collection(self, test_project: IRPProject) -> None:
        pkgs = test_project.packages
        assert pkgs is not None

    def test_add_node_and_get_nodes(self, test_project: IRPProject) -> None:
        node = test_project.add_node(self._unique("Node"))
        try:
            assert node in list(test_project.nodes)
        finally:
            node.delete_from_project()

    def test_use_unique_stereotype_and_ref_cache_is_boolean(self, test_project: IRPProject) -> None:
        assert test_project.use_unique_stereotype_and_ref_cache in (0, 1)

    def test_all_stereotypes_contains_created_stereotype(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("StereoPkg"))
        try:
            stereotype = pkg.add_stereotype(self._unique("ProjectStereo"), "Class")
            assert stereotype in list(test_project.all_stereotypes)
        finally:
            pkg.delete_from_project()

    def test_create_component_in_project(self, test_project: IRPProject) -> None:
        comp_name = self._unique("MyComponent")
        comp = test_project.add_component(comp_name)
        try:
            assert comp is not None
        finally:
            comp.delete_from_project()


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
        try:
            child_pkg = parent_pkg.add_nested_package(child_name)
            assert isinstance(child_pkg, IRPPackage)
            assert child_pkg in list(parent_pkg.packages)
        finally:
            parent_pkg.delete_from_project()

    def test_package_navigation(self, test_project: IRPProject) -> None:
        parent_name = self._unique("NavParent")
        child_name = self._unique("NavChild")
        parent_pkg = self._create_package(test_project, parent_name)
        try:
            child_pkg = parent_pkg.add_nested_package(child_name)
            owner = child_pkg.owner
            assert owner == parent_pkg
            assert isinstance(owner, IRPPackage)
        finally:
            parent_pkg.delete_from_project()

    def test_add_class_to_package(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("ClassPkg")
        class_name = self._unique("TestClass")
        pkg = self._create_package(test_project, pkg_name)
        try:
            new_class = pkg.add_class(class_name)
            assert isinstance(new_class, IRPClass)
            class_names = [c.name for c in pkg.classes]
            assert class_name in class_names
        finally:
            pkg.delete_from_project()

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
            pkg = test_project.add_package(self._unique("arg"))
            assert pkg is not None
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
            pkg = test_project.add_component(self._unique("arg"))
            assert pkg is not None
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
            assert isinstance(collaboration, IRPClass)
        finally:
            collaboration.delete_from_project()

    def test_add_profile(self, test_project: IRPProject) -> None:
        profile = None
        try:
            profile = test_project.add_profile(self._unique("Profile"))
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
        assert test_project.open_csv_file(self._unique("arg"), 0) is None  # type: ignore[func-returns-value]

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
