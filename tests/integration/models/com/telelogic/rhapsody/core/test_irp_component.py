"""Integration tests for IRPComponent with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit import IRPUnit


@pytest.mark.integration
class TestIRPComponentIntegration:
    """Integration tests for IRPComponent with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _component(pkg: IRPPackage) -> tuple[IRPPackage, IRPComponent]:
        element = pkg.add_new_aggr("Component", f"Component_{uuid.uuid4().hex[:8]}")
        component = IRPComponent(element._com)
        assert isinstance(component, IRPComponent)
        return pkg, component

    def test_additional_sources(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("SourcesPkg"))
        try:
            _, component = self._component(pkg)
            component.additional_sources = "src/a.cpp"
            assert component.additional_sources == "src/a.cpp"
        finally:
            pkg.delete_from_project()

    def test_build_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("BuildTypePkg"))
        try:
            _, component = self._component(pkg)
            component.build_type = "Standard"
            assert component.build_type == "Standard"
        finally:
            pkg.delete_from_project()

    def test_configurations(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ConfigurationsPkg"))
        try:
            _, component = self._component(pkg)
            configuration = component.add_configuration(self._unique("Config"))
            assert configuration in list(component.configurations)
        finally:
            pkg.delete_from_project()

    def test_files(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("FilesPkg"))
        try:
            _, component = self._component(pkg)
            file = component.add_file(self._unique("File"))
            assert file in list(component.files)
        finally:
            pkg.delete_from_project()

    def test_include_path(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("IncludePkg"))
        try:
            _, component = self._component(pkg)
            component.include_path = "include"
            assert component.include_path == "include"
        finally:
            pkg.delete_from_project()

    def test_libraries(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("LibrariesPkg"))
        try:
            _, component = self._component(pkg)
            component.libraries = "libm"
            assert component.libraries == "libm"
        finally:
            pkg.delete_from_project()

    def test_nested_components(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("NestedPkg"))
        try:
            _, component = self._component(pkg)
            nested = component.add_nested_component(self._unique("NestedComponent"))
            assert nested in list(component.nested_components)
        finally:
            pkg.delete_from_project()

    def test_panel_diagrams_empty_state(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("PanelPkg"))
        try:
            _, component = self._component(pkg)
            # No documented API attaches a panel diagram to a component.
            assert len(list(component.panel_diagrams)) == 0
        finally:
            pkg.delete_from_project()

    def test_scope_by_selected_elements(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = test_project.add_package(self._unique("ScopePkg"))
        try:
            _, component = self._component(pkg)
            element = component.add_file(self._unique("ScopeFile"))
            selection = rhapsody_app.create_new_collection()
            selection.add_item(element)
            component.scope_by_selected_elements = selection
            assert element in list(component.scope_by_selected_elements)
        finally:
            pkg.delete_from_project()

    def test_scope_elements(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ScopeElementsPkg"))
        try:
            _, component = self._component(pkg)
            element = component.add_file(self._unique("ScopedFile"))
            component.add_scope_element(IRPUnit(element._com))
            assert element in list(component.scope_elements)
        finally:
            pkg.delete_from_project()

    def test_standard_headers(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("HeadersPkg"))
        try:
            _, component = self._component(pkg)
            component.standard_headers = "types.h"
            assert component.standard_headers == "types.h"
        finally:
            pkg.delete_from_project()

    def test_variation_points_empty_state(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("VariationPkg"))
        try:
            _, component = self._component(pkg)
            # No documented API creates a variation point on a component.
            assert len(list(component.variation_points)) == 0
        finally:
            pkg.delete_from_project()

    def test_unavailable_members_raise_before_dispatch(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("UnavailablePkg"))
        try:
            _, component = self._component(pkg)
            with pytest.raises(NotImplementedError):
                component.get_path()
            with pytest.raises(NotImplementedError):
                component.set_path("path")
            with pytest.raises(NotImplementedError):
                component.update_contained_diagrams_on_server()
        finally:
            pkg.delete_from_project()
