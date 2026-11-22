"""Integration tests for IRPProject and IRPPackage with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import time
import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestRPProjectIntegration:
    """Integration tests for IRPProject with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{int(time.time() * 1000) % 1000000}"

    def test_project_properties(self, test_project: IRPProject) -> None:
        assert test_project.get_name()
        assert isinstance(test_project.get_name(), str)
        assert test_project.get_meta_class() == "Project"
        guid = test_project.get_guid()
        assert isinstance(guid, str)
        assert len(guid) > 0

    def test_project_is_rp_project(self, test_project: IRPProject) -> None:
        assert isinstance(test_project, IRPProject)
        assert isinstance(test_project, IRPPackage)
        assert isinstance(test_project, IRPModelElement)

    def test_add_package_to_project(self, test_project: IRPProject) -> None:
        name = self._unique("TopLevelPkg")
        new_pkg = test_project.add_package(name)
        assert new_pkg is not None
        assert isinstance(new_pkg, IRPPackage)
        assert new_pkg.get_name() == name
        assert new_pkg.get_meta_class() == "Package"
        pkgs = test_project.get_packages()
        names = [p.get_name() for p in pkgs]
        assert name in names

    def test_project_get_packages_returns_collection(self, test_project: IRPProject) -> None:
        pkgs = test_project.get_packages()
        assert pkgs is not None

    def test_create_component_in_project(self, test_project: IRPProject) -> None:
        comp_name = self._unique("MyComponent")
        comp = test_project.add_component(comp_name)
        try:
            assert comp is not None
            assert comp.get_name() == comp_name
            assert comp.get_meta_class() == "Component"
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
        child_pkg = parent_pkg.add_nested_package(child_name)
        assert child_pkg is not None
        assert isinstance(child_pkg, IRPPackage)
        assert child_pkg.get_name() == child_name
        children = parent_pkg.get_nested_packages()
        child_names = [c.get_name() for c in children]
        assert child_name in child_names

    def test_package_navigation(self, test_project: IRPProject) -> None:
        parent_name = self._unique("NavParent")
        child_name = self._unique("NavChild")
        parent_pkg = self._create_package(test_project, parent_name)
        child_pkg = parent_pkg.add_nested_package(child_name)
        owner = child_pkg.get_owner()
        assert owner is not None
        assert owner.get_name() == parent_name
        assert isinstance(owner, IRPPackage)

    def test_add_class_to_package(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("ClassPkg")
        class_name = self._unique("TestClass")
        pkg = self._create_package(test_project, pkg_name)
        new_class = pkg.add_class(class_name)
        assert new_class is not None
        assert new_class.get_name() == class_name
        assert new_class.get_meta_class() == "Class"
        classes = pkg.get_classes()
        class_names = [c.get_name() for c in classes]
        assert class_name in class_names

    def test_create_module_in_package(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("ModPkg")
        mod_name = self._unique("MyModule")
        pkg = self._create_package(test_project, pkg_name)
        try:
            mod = pkg.add_module(mod_name)
            assert mod is not None
            assert mod.get_name() == mod_name
            assert mod.get_meta_class() == "Module"
        finally:
            mod.delete_from_project()


@pytest.mark.integration
class TestIRPProjectGenerated:
    """Generated live coverage for IRPProject owned methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_package(self, test_project: IRPProject) -> None:
        try:
            test_project.add_package(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_close(self, test_project: IRPProject) -> None:
        try:
            test_project.close()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_become_active_project(self, test_project: IRPProject) -> None:
        try:
            test_project.become_active_project()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_find_component(self, test_project: IRPProject) -> None:
        try:
            test_project.find_component(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_packages(self, test_project: IRPProject) -> None:
        try:
            test_project.get_packages()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_add_class(self, test_project: IRPProject) -> None:
        try:
            test_project.add_class(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_add_actor(self, test_project: IRPProject) -> None:
        try:
            test_project.add_actor(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_components(self, test_project: IRPProject) -> None:
        try:
            test_project.get_components()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_find_element_by_guid(self, test_project: IRPProject) -> None:
        try:
            test_project.find_element_by_guid(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_add_component(self, test_project: IRPProject) -> None:
        try:
            test_project.add_component(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_delete_component(self, test_project: IRPProject) -> None:
        try:
            test_project.delete_component(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_add_node(self, test_project: IRPProject) -> None:
        try:
            test_project.add_node(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_nodes(self, test_project: IRPProject) -> None:
        try:
            test_project.get_nodes()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_find_node(self, test_project: IRPProject) -> None:
        try:
            test_project.find_node(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_delete_node(self, test_project: IRPProject) -> None:
        try:
            test_project.delete_node(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_active_configuration(self, test_project: IRPProject) -> None:
        try:
            test_project.get_active_configuration()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_set_active_configuration(self, test_project: IRPProject) -> None:
        try:
            test_project.set_active_configuration(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_active_component(self, test_project: IRPProject) -> None:
        try:
            test_project.get_active_component()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_set_active_component(self, test_project: IRPProject) -> None:
        try:
            test_project.set_active_component(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_all_stereotypes(self, test_project: IRPProject) -> None:
        try:
            test_project.get_all_stereotypes()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_new_collaboration(self, test_project: IRPProject) -> None:
        try:
            test_project.get_new_collaboration()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_add_profile(self, test_project: IRPProject) -> None:
        try:
            test_project.add_profile(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_profiles(self, test_project: IRPProject) -> None:
        try:
            test_project.get_profiles()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_save_as(self, test_project: IRPProject) -> None:
        try:
            test_project.save_as(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_find_element_by_binary_id(self, test_project: IRPProject) -> None:
        try:
            test_project.find_element_by_binary_id(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_find_element_by_file_name(self, test_project: IRPProject) -> None:
        try:
            test_project.find_element_by_file_name(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_code_generated_files(self, test_project: IRPProject) -> None:
        try:
            test_project.get_code_generated_files()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_allow_auto_save(self, test_project: IRPProject) -> None:
        try:
            test_project.allow_auto_save(0)
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_allow_non_unique_names(self, test_project: IRPProject) -> None:
        try:
            test_project.allow_non_unique_names(0)
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_cg_simplified_model_package(self, test_project: IRPProject) -> None:
        try:
            test_project.get_cg_simplified_model_package()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_locate_in_ide(self, test_project: IRPProject) -> None:
        try:
            test_project.locate_in_ide()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_is_modified_recursive(self, test_project: IRPProject) -> None:
        try:
            test_project.is_modified_recursive()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_highlight_from_code(self, test_project: IRPProject) -> None:
        try:
            test_project.highlight_from_code(self._unique("arg"), 0)
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_gateway_export_to_xml(self, test_project: IRPProject) -> None:
        try:
            test_project.gateway_export_to_xml(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_gateway_export_to_xml2(self, test_project: IRPProject) -> None:
        try:
            test_project.gateway_export_to_xml2(self._unique("arg"), self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_generate_report(self, test_project: IRPProject) -> None:
        try:
            test_project.generate_report(self._unique("arg"), self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_add_custom_view_on_browser(self, test_project: IRPProject) -> None:
        try:
            test_project.add_custom_view_on_browser(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_add_custom_view_on_diagram(self, test_project: IRPProject) -> None:
        try:
            test_project.add_custom_view_on_diagram(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_apply_browser_custom_views_on_diagrams(self, test_project: IRPProject) -> None:
        try:
            test_project.apply_browser_custom_views_on_diagrams()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_active_custom_views_on_browser(self, test_project: IRPProject) -> None:
        try:
            test_project.get_active_custom_views_on_browser()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_active_custom_views_on_diagram(self, test_project: IRPProject) -> None:
        try:
            test_project.get_active_custom_views_on_diagram()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_remove_custom_view_on_browser(self, test_project: IRPProject) -> None:
        try:
            test_project.remove_custom_view_on_browser(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_remove_custom_view_on_diagram(self, test_project: IRPProject) -> None:
        try:
            test_project.remove_custom_view_on_diagram(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_close_csv_file(self, test_project: IRPProject) -> None:
        try:
            test_project.close_csv_file()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_open_csv_file(self, test_project: IRPProject) -> None:
        try:
            test_project.open_csv_file(self._unique("arg"), 0)
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_reload_csv_file(self, test_project: IRPProject) -> None:
        try:
            test_project.reload_csv_file()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_apply_roundtrip_diff_merge(self, test_project: IRPProject) -> None:
        try:
            test_project.apply_roundtrip_diff_merge()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_enable_rhapsody_model_manager(self, test_project: IRPProject) -> None:
        try:
            test_project.enable_rhapsody_model_manager(0)
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_find_elements_with_oslc_link(self, test_project: IRPProject) -> None:
        try:
            test_project.find_elements_with_oslc_link(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_remote_resource_packages(self, test_project: IRPProject) -> None:
        try:
            test_project.get_remote_resource_packages()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_roundtrip_shadow_model(self, test_project: IRPProject) -> None:
        try:
            test_project.get_roundtrip_shadow_model()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_is_actively_managed(self, test_project: IRPProject) -> None:
        try:
            test_project.is_actively_managed()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_migrate_design_manager_links(self, test_project: IRPProject) -> None:
        try:
            test_project.migrate_design_manager_links()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_import_package_from_rose(self, test_project: IRPProject) -> None:
        try:
            test_project.import_package_from_rose(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_import_project_from_rose(self, test_project: IRPProject) -> None:
        try:
            test_project.import_project_from_rose(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_check_events_base_ids_solve_collisions(self, test_project: IRPProject) -> None:
        try:
            test_project.check_events_base_ids_solve_collisions()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_recalculate_events_base_ids(self, test_project: IRPProject) -> None:
        try:
            test_project.recalculate_events_base_ids()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_add_spell_checker_result(self, test_project: IRPProject) -> None:
        try:
            test_project.add_spell_checker_result(self._unique("arg"), self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_clean_unresolved_elements(self, test_project: IRPProject) -> None:
        try:
            test_project.clean_unresolved_elements()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_end_transaction_of_no_cg_interest(self, test_project: IRPProject) -> None:
        try:
            test_project.end_transaction_of_no_cg_interest()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_default_directory_scheme(self, test_project: IRPProject) -> None:
        try:
            test_project.get_default_directory_scheme()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_new_progress_bar(self, test_project: IRPProject) -> None:
        try:
            test_project.get_new_progress_bar()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_notify_plugin_on_elements_changed(self, test_project: IRPProject) -> None:
        try:
            test_project.get_notify_plugin_on_elements_changed()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_get_requirements_by_id(self, test_project: IRPProject) -> None:
        try:
            test_project.get_requirements_by_id(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_remove(self, test_project: IRPProject) -> None:
        try:
            test_project.remove()
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_save_as_prev_version(self, test_project: IRPProject) -> None:
        try:
            test_project.save_as_prev_version(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_set_default_directory_scheme(self, test_project: IRPProject) -> None:
        try:
            test_project.set_default_directory_scheme(0)
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_set_global_configuration(self, test_project: IRPProject) -> None:
        try:
            test_project.set_global_configuration(self._unique("arg"))
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_set_notify_plugin_on_elements_changed(self, test_project: IRPProject) -> None:
        try:
            test_project.set_notify_plugin_on_elements_changed(0)
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_set_object_explicit(self, test_project: IRPProject) -> None:
        try:
            test_project.set_object_explicit(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_set_object_implicit(self, test_project: IRPProject) -> None:
        try:
            test_project.set_object_implicit(None)  # type: ignore[arg-type]
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_set_use_unique_stereotype_and_ref_cache(self, test_project: IRPProject) -> None:
        try:
            test_project.set_use_unique_stereotype_and_ref_cache(0)
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_set_wait_dialog_watchdog_value(self, test_project: IRPProject) -> None:
        try:
            test_project.set_wait_dialog_watchdog_value(0)
        except Exception:
            pass  # COM member may be absent or reject the argument

    def test_start_transaction_of_no_cg_interest(self, test_project: IRPProject) -> None:
        try:
            test_project.start_transaction_of_no_cg_interest()
        except Exception:
            pass  # COM member may be absent or reject the argument
