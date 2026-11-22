"""Integration tests for IRPPackage with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.elements.common import RPSysMLPort


@pytest.mark.integration
class TestIRPPackageIntegration:
    """Integration tests for IRPPackage with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def _pkg(self, test_project: IRPProject) -> IRPPackage:
        pkg = test_project.add_package(self._unique("Pkg"))
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_add_class(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_class(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_nested_package(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_nested_package(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_actor(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_actor(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_global_function(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_global_function(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_flow_items(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_flow_items(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_flows(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_flows(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_get_nested_packages(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_nested_packages() is not None
        finally:
            pkg.delete_from_project()

    def test_get_classes(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_classes() is not None
        finally:
            pkg.delete_from_project()

    def test_get_actors(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_actors() is not None
        finally:
            pkg.delete_from_project()

    def test_get_use_cases(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_use_cases() is not None
        finally:
            pkg.delete_from_project()

    def test_add_use_case(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_use_case(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_activity_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(TypeError):
                pkg.add_activity_diagram(self._unique("arg"))
        finally:
            pkg.delete_from_project()

    def test_add_sequence_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_sequence_diagram(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_use_case_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_use_case_diagram(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_collaboration_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_collaboration_diagram(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_component_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_component_diagram(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_deployment_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_deployment_diagram(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_object_model_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_object_model_diagram(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_statechart_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(TypeError):
                pkg.add_statechart_diagram(self._unique("arg"))
        finally:
            pkg.delete_from_project()

    def test_add_timing_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_timing_diagram(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_panel_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_panel_diagram(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_get_sequence_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_sequence_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_get_use_case_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_use_case_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_get_collaboration_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_collaboration_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_get_component_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_component_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_get_deployment_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_deployment_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_get_object_model_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_object_model_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_get_timing_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_timing_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_get_panel_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_panel_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_delete_sequence_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_sequence_diagram(self._unique("DelElem"))
            assert element is not None
            pkg.delete_sequence_diagram(element)
        finally:
            pkg.delete_from_project()

    def test_delete_use_case_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_use_case_diagram(self._unique("DelElem"))
            assert element is not None
            pkg.delete_use_case_diagram(element)
        finally:
            pkg.delete_from_project()

    def test_delete_collaboration_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_collaboration_diagram(self._unique("DelElem"))
            assert element is not None
            pkg.delete_collaboration_diagram(element)
        finally:
            pkg.delete_from_project()

    def test_delete_component_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_component_diagram(self._unique("DelElem"))
            assert element is not None
            pkg.delete_component_diagram(element)
        finally:
            pkg.delete_from_project()

    def test_delete_deployment_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_deployment_diagram(self._unique("DelElem"))
            assert element is not None
            pkg.delete_deployment_diagram(element)
        finally:
            pkg.delete_from_project()

    def test_delete_object_model_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_object_model_diagram(self._unique("DelElem"))
            assert element is not None
            pkg.delete_object_model_diagram(element)
        finally:
            pkg.delete_from_project()

    def test_delete_timing_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_timing_diagram(self._unique("DelElem"))
            assert element is not None
            pkg.delete_timing_diagram(element)
        finally:
            pkg.delete_from_project()

    def test_delete_panel_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_panel_diagram(self._unique("DelElem"))
            assert element is not None
            pkg.delete_panel_diagram(element)
        finally:
            pkg.delete_from_project()

    def test_delete_class(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_class(self._unique("DelElem"))
            assert element is not None
            pkg.delete_class(element)
        finally:
            pkg.delete_from_project()

    def test_delete_actor(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_actor(self._unique("DelElem"))
            assert element is not None
            pkg.delete_actor(element)
        finally:
            pkg.delete_from_project()

    def test_delete_use_case(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_use_case(self._unique("DelElem"))
            assert element is not None
            pkg.delete_use_case(element)
        finally:
            pkg.delete_from_project()

    def test_delete_flow_items(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_flow_items(self._unique("DelElem"))
            assert element is not None
            pkg.delete_flow_items(element)
        finally:
            pkg.delete_from_project()

    def test_delete_flows(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_flows(self._unique("DelElem"))
            assert element is not None
            pkg.delete_flows(element)
        finally:
            pkg.delete_from_project()

    def test_delete_package(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_nested_package(self._unique("DelElem"))
            assert element is not None
            pkg.delete_package(element)
        finally:
            pkg.delete_from_project()

    def test_find_class(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_class(self._unique("arg")) is None
        finally:
            pkg.delete_from_project()

    def test_find_actor(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_actor(self._unique("arg")) is None
        finally:
            pkg.delete_from_project()

    def test_find_use_case(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_use_case(self._unique("arg")) is None
        finally:
            pkg.delete_from_project()

    def test_add_association(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(TypeError):
                pkg.add_association(self._unique("arg"))
        finally:
            pkg.delete_from_project()

    def test_add_event(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_event(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_get_events(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_events() is not None
        finally:
            pkg.delete_from_project()

    def test_get_flow_items(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_flow_items() is not None
        finally:
            pkg.delete_from_project()

    def test_get_flows(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_flows() is not None
        finally:
            pkg.delete_from_project()

    def test_find_event(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_event(self._unique("arg")) is None
        finally:
            pkg.delete_from_project()

    def test_delete_event(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_event(self._unique("DelElem"))
            assert element is not None
            pkg.delete_event(element)
        finally:
            pkg.delete_from_project()

    def test_add_node(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_node(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_get_nodes(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_nodes() is not None
        finally:
            pkg.delete_from_project()

    def test_find_node(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_node(self._unique("arg")) is None
        finally:
            pkg.delete_from_project()

    def test_delete_node(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_node(self._unique("DelElem"))
            assert element is not None
            pkg.delete_node(element)
        finally:
            pkg.delete_from_project()

    def test_add_module(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_module(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_get_modules(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_modules() is not None
        finally:
            pkg.delete_from_project()

    def test_add_type(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_type(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_get_types(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_types() is not None
        finally:
            pkg.delete_from_project()

    def test_find_type(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_type(self._unique("arg")) is None
        finally:
            pkg.delete_from_project()

    def test_delete_type(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_type(self._unique("DelElem"))
            assert element is not None
            pkg.delete_type(element)
        finally:
            pkg.delete_from_project()

    def test_find_global_function(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_global_function(self._unique("arg")) is None
        finally:
            pkg.delete_from_project()

    def test_get_global_functions(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_global_functions() is not None
        finally:
            pkg.delete_from_project()

    def test_delete_global_function(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_global_function(self._unique("DelElem"))
            assert element is not None
            pkg.delete_global_function(element)
        finally:
            pkg.delete_from_project()

    def test_add_global_object(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(RhapsodyRuntimeException):
                pkg.add_global_object(self._unique("arg"))
        finally:
            pkg.delete_from_project()

    def test_get_global_objects(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_global_objects() is not None
        finally:
            pkg.delete_from_project()

    def test_find_global_object(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_global_object(self._unique("arg")) is None
        finally:
            pkg.delete_from_project()

    def test_delete_global_object(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_global_object(self._unique("DelElem"))
            assert element is not None
            pkg.delete_global_object(element)
        finally:
            pkg.delete_from_project()

    def test_add_global_variable(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_global_variable(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_get_global_variables(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_global_variables() is not None
        finally:
            pkg.delete_from_project()

    def test_find_global_variable(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_global_variable(self._unique("arg")) is None
        finally:
            pkg.delete_from_project()

    def test_delete_global_variable(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_global_variable(self._unique("DelElem"))
            assert element is not None
            pkg.delete_global_variable(element)
        finally:
            pkg.delete_from_project()

    def test_get_nested_classifiers(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_nested_classifiers() is not None
        finally:
            pkg.delete_from_project()

    def test_get_nested_components(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_nested_components() is not None
        finally:
            pkg.delete_from_project()

    def test_add_instance_specification(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            classifier = pkg.add_class(self._unique("InstCls"))
            with pytest.raises(NotImplementedError):
                pkg.add_instance_specification(self._unique("InstSpec"), classifier)
        finally:
            pkg.delete_from_project()

    def test_get_instance_specifications(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_instance_specifications() is not None
        finally:
            pkg.delete_from_project()

    def test_add_link(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(TypeError):
                pkg.add_link(self._unique("arg"))
        finally:
            pkg.delete_from_project()

    def test_get_links(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_links() is not None
        finally:
            pkg.delete_from_project()

    def test_find_all_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(RhapsodyRuntimeException):
                pkg.find_all_by_name(self._unique("arg"))
        finally:
            pkg.delete_from_project()

    def test_get_behavioral_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_behavioral_diagrams() is not None
        finally:
            pkg.delete_from_project()

    def test_get_source_artifacts(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_source_artifacts() is not None
        finally:
            pkg.delete_from_project()

    def test_find_usage(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_class(self._unique("UsageCls"))
            assert isinstance(pkg.find_usage(element), IRPCollection)
        finally:
            pkg.delete_from_project()

    def test_get_remote_requirements_populate_mode(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(ValueError):
                pkg.get_remote_requirements_populate_mode()
        finally:
            pkg.delete_from_project()

    def test_get_root_instance_specifications(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(NotImplementedError):
                pkg.get_root_instance_specifications()
        finally:
            pkg.delete_from_project()

    def test_login_to_remote_artifact_server(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(NotImplementedError):
                pkg.login_to_remote_artifact_server()
        finally:
            pkg.delete_from_project()

    def test_populate_remote_requirements(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.populate_remote_requirements() is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_recalculate_events_base_id(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.recalculate_events_base_id() is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_set_remote_requirements_populate_mode(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.set_remote_requirements_populate_mode(0) is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_update_contained_diagrams_on_server(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises((TypeError, NotImplementedError)):
                pkg.update_contained_diagrams_on_server(1)
        finally:
            pkg.delete_from_project()

    def test_add_implicit_object(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.add_implicit_object(self._unique("arg")) is not None
        finally:
            pkg.delete_from_project()

    def test_add_link_between_sysml_ports(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            cls_a = pkg.add_class(self._unique("SysMLClsA"))
            cls_b = pkg.add_class(self._unique("SysMLClsB"))
            port_a = cls_a.add_new_aggr("Port", self._unique("portA"))
            port_b = cls_b.add_new_aggr("Port", self._unique("portB"))
            assert isinstance(port_a, RPSysMLPort) and isinstance(port_b, RPSysMLPort)
            assert pkg.add_link_between_sysml_ports(port_a, port_b) is not None
        finally:
            pkg.delete_from_project()

    def test_get_all_nested_elements(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_all_nested_elements() is not None
        finally:
            pkg.delete_from_project()

    def test_get_events_base_id(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_events_base_id() is not None
        finally:
            pkg.delete_from_project()

    def test_get_namespace(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_namespace() is not None
        finally:
            pkg.delete_from_project()

    def test_get_saved_in_separate_directory(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_saved_in_separate_directory() is not None
        finally:
            pkg.delete_from_project()

    def test_get_user_defined_stereotypes(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.get_user_defined_stereotypes() is not None
        finally:
            pkg.delete_from_project()

    def test_set_saved_in_separate_directory(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.set_saved_in_separate_directory(0) is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_update_contained_matrices_on_server(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(NotImplementedError):
                pkg.update_contained_matrices_on_server(1)
        finally:
            pkg.delete_from_project()

    def test_update_contained_tables_on_server(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(NotImplementedError):
                pkg.update_contained_tables_on_server(1)
        finally:
            pkg.delete_from_project()
