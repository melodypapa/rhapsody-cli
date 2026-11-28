"""Integration tests for IRPComponent with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPComponentIntegration:
    """Integration tests for IRPComponent with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _component(project: IRPProject) -> IRPComponent:
        component = project.add_component(f"Component_{uuid.uuid4().hex[:8]}")
        assert isinstance(component, IRPComponent)
        return component

    def test_additional_sources(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            component.additional_sources = "src/a.cpp"
            assert component.additional_sources == "src/a.cpp"
        finally:
            component.delete_from_project()

    def test_build_type(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            component.build_type = "Library"
            assert component.build_type.casefold() == "library"
        finally:
            component.delete_from_project()

    def test_configurations(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            configuration = component.add_configuration(self._unique("Config"))
            assert configuration in list(component.configurations)
        finally:
            component.delete_from_project()

    def test_files(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            file = component.add_file(self._unique("File"))
            assert file in list(component.files)
        finally:
            component.delete_from_project()

    def test_include_path(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            component.include_path = "include"
            assert component.include_path == "include"
        finally:
            component.delete_from_project()

    def test_libraries(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            component.libraries = "libm"
            assert component.libraries == "libm"
        finally:
            component.delete_from_project()

    def test_nested_components(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            nested = component.add_nested_component(self._unique("NestedComponent"))
            assert nested in list(component.nested_components)
        finally:
            component.delete_from_project()

    def test_panel_diagrams_empty_state(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            # No documented API attaches a panel diagram to a component.
            assert len(list(component.panel_diagrams)) == 0
        finally:
            component.delete_from_project()

    def test_scope_by_selected_elements(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            component.scope_by_selected_elements = 1
            assert component.scope_by_selected_elements == 1
        finally:
            component.delete_from_project()

    def test_scope_elements(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        package = test_project.add_package(self._unique("ScopeElementsPkg"))
        try:
            classifier = package.add_class(self._unique("ScopedClass"))
            component.add_scope_element(classifier)
            assert classifier in list(component.scope_elements)
        finally:
            component.delete_from_project()
            package.delete_from_project()

    def test_standard_headers(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            component.standard_headers = "types.h"
            assert component.standard_headers == "types.h"
        finally:
            component.delete_from_project()

    def test_variation_points_empty_state(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            # No documented API creates a variation point on a component.
            assert len(list(component.variation_points)) == 0
        finally:
            component.delete_from_project()

    def test_unavailable_members_raise_before_dispatch(self, test_project: IRPProject) -> None:
        component = self._component(test_project)
        try:
            with pytest.raises(NotImplementedError):
                component.get_path()
            with pytest.raises(NotImplementedError):
                component.set_path("path")
            with pytest.raises(NotImplementedError):
                component.update_contained_diagrams_on_server()
        finally:
            component.delete_from_project()
