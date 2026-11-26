"""Integration tests for IRPPackage with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation


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
            created_name = self._unique("AddClass")
            created = pkg.add_class(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_nested_package(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddNestedPackage")
            created = pkg.add_nested_package(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_actor(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddActor")
            created = pkg.add_actor(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_global_function(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddGlobalFunction")
            created = pkg.add_global_function(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_flow_items(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddFlowItems")
            created = pkg.add_flow_items(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_flows(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddFlows")
            created = pkg.add_flows(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_get_nested_packages(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            nested_package = pkg.add_nested_package(self._unique("NestedPkg"))

            assert nested_package in list(pkg.packages)
        finally:
            pkg.delete_from_project()

    def test_get_classes(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_class = pkg.add_class(self._unique("CollectionClass"))

            assert created_class in list(pkg.classes)
        finally:
            pkg.delete_from_project()

    def test_get_actors(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_actor = pkg.add_actor(self._unique("CollectionActor"))

            assert created_actor in list(pkg.actors)
        finally:
            pkg.delete_from_project()

    def test_get_use_cases(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_use_case = pkg.add_use_case(self._unique("CollectionUseCase"))

            assert created_use_case in list(pkg.use_cases)
        finally:
            pkg.delete_from_project()

    def test_add_use_case(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddUseCase")
            created = pkg.add_use_case(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_activity_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            diagram = pkg.add_activity_diagram()
            assert diagram in list(pkg.behavioral_diagrams)
        finally:
            pkg.delete_from_project()

    def test_add_sequence_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddSequenceDiagram")
            created = pkg.add_sequence_diagram(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_use_case_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddUseCaseDiagram")
            created = pkg.add_use_case_diagram(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_collaboration_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddCollaborationDiagram")
            created = pkg.add_collaboration_diagram(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_component_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddComponentDiagram")
            created = pkg.add_component_diagram(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_deployment_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddDeploymentDiagram")
            created = pkg.add_deployment_diagram(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_object_model_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddObjectModelDiagram")
            created = pkg.add_object_model_diagram(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_statechart(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            statechart = pkg.add_statechart()
            assert statechart in list(pkg.behavioral_diagrams)
        finally:
            pkg.delete_from_project()

    def test_add_timing_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddTimingDiagram")
            created = pkg.add_timing_diagram(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_add_panel_diagram(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddPanelDiagram")
            created = pkg.add_panel_diagram(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_get_sequence_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_diagram = pkg.add_sequence_diagram(self._unique("CollectionSequence"))

            assert created_diagram in list(pkg.sequence_diagrams)
        finally:
            pkg.delete_from_project()

    def test_get_use_case_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_diagram = pkg.add_use_case_diagram(self._unique("CollectionUseCaseDiagram"))

            assert created_diagram in list(pkg.use_case_diagrams)
        finally:
            pkg.delete_from_project()

    def test_get_collaboration_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_diagram = pkg.add_collaboration_diagram(self._unique("CollectionCollaboration"))

            assert created_diagram in list(pkg.collaboration_diagrams)
        finally:
            pkg.delete_from_project()

    def test_get_component_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_diagram = pkg.add_component_diagram(self._unique("CollectionComponent"))

            assert created_diagram in list(pkg.component_diagrams)
        finally:
            pkg.delete_from_project()

    def test_get_deployment_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_diagram = pkg.add_deployment_diagram(self._unique("CollectionDeployment"))

            assert created_diagram in list(pkg.deployment_diagrams)
        finally:
            pkg.delete_from_project()

    def test_get_object_model_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_diagram = pkg.add_object_model_diagram(self._unique("CollectionObjectModel"))

            assert created_diagram in list(pkg.object_model_diagrams)
        finally:
            pkg.delete_from_project()

    def test_get_timing_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_diagram = pkg.add_timing_diagram(self._unique("CollectionTiming"))

            assert created_diagram in list(pkg.timing_diagrams)
        finally:
            pkg.delete_from_project()

    def test_get_panel_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_diagram = pkg.add_panel_diagram(self._unique("CollectionPanel"))

            assert created_diagram in list(pkg.panel_diagrams)
        finally:
            pkg.delete_from_project()

    def test_delete_sequence_diagram_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        diagram_name = self._unique("DeleteSequence")
        try:
            element = pkg.add_sequence_diagram(diagram_name)
            assert element in list(pkg.sequence_diagrams)

            pkg.delete_sequence_diagram(diagram_name)

            assert element not in list(pkg.sequence_diagrams)
        finally:
            pkg.delete_from_project()

    def test_delete_use_case_diagram_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        diagram_name = self._unique("DeleteUseCase")
        try:
            element = pkg.add_use_case_diagram(diagram_name)
            assert element in list(pkg.use_case_diagrams)

            pkg.delete_use_case_diagram(diagram_name)

            assert element not in list(pkg.use_case_diagrams)
        finally:
            pkg.delete_from_project()

    def test_delete_collaboration_diagram_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        diagram_name = self._unique("DeleteCollaboration")
        try:
            element = pkg.add_collaboration_diagram(diagram_name)
            assert element in list(pkg.collaboration_diagrams)

            pkg.delete_collaboration_diagram(diagram_name)

            assert element not in list(pkg.collaboration_diagrams)
        finally:
            pkg.delete_from_project()

    def test_delete_component_diagram_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        diagram_name = self._unique("DeleteComponent")
        try:
            element = pkg.add_component_diagram(diagram_name)
            assert element in list(pkg.component_diagrams)

            pkg.delete_component_diagram(diagram_name)

            assert element not in list(pkg.component_diagrams)
        finally:
            pkg.delete_from_project()

    def test_delete_deployment_diagram_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        diagram_name = self._unique("DeleteDeployment")
        try:
            element = pkg.add_deployment_diagram(diagram_name)
            assert element in list(pkg.deployment_diagrams)

            pkg.delete_deployment_diagram(diagram_name)

            assert element not in list(pkg.deployment_diagrams)
        finally:
            pkg.delete_from_project()

    def test_delete_object_model_diagram_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        diagram_name = self._unique("DeleteObjectModel")
        try:
            element = pkg.add_object_model_diagram(diagram_name)
            assert element in list(pkg.object_model_diagrams)

            pkg.delete_object_model_diagram(diagram_name)

            assert element not in list(pkg.object_model_diagrams)
        finally:
            pkg.delete_from_project()

    def test_delete_timing_diagram_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        diagram_name = self._unique("DeleteTiming")
        try:
            element = pkg.add_timing_diagram(diagram_name)
            assert element in list(pkg.timing_diagrams)

            pkg.delete_timing_diagram(diagram_name)

            assert element not in list(pkg.timing_diagrams)
        finally:
            pkg.delete_from_project()

    def test_delete_panel_diagram_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        diagram_name = self._unique("DeletePanel")
        try:
            element = pkg.add_panel_diagram(diagram_name)
            assert element in list(pkg.panel_diagrams)

            pkg.delete_panel_diagram(diagram_name)

            assert element not in list(pkg.panel_diagrams)
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

    def test_delete_package_deletes_this_nested_package(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        child_name = self._unique("DelPkg")
        try:
            child_package = pkg.add_nested_package(child_name)

            child_package.delete_package()

            assert all(item.name != child_name for item in pkg.packages)
        finally:
            pkg.delete_from_project()

    def test_find_class(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_class(self._unique("missing_arg")) is None
        finally:
            pkg.delete_from_project()

    def test_find_actor(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_actor(self._unique("missing_arg")) is None
        finally:
            pkg.delete_from_project()

    def test_find_use_case(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_use_case(self._unique("missing_arg")) is None
        finally:
            pkg.delete_from_project()

    def test_add_association_with_real_relation_ends(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            class_a = pkg.add_class(self._unique("AssocClassA"))
            class_b = pkg.add_class(self._unique("AssocClassB"))
            relation_name = self._unique("AssocRelation")
            end1 = class_a.add_relation_to(class_b, self._unique("roleA"), "Association", "1", self._unique("roleB"), "Association", "1", relation_name)
            end2 = IRPRelation(end1._com).inverse
            assert end2 is not None
            association_name = self._unique("PackageAssociation")

            association = pkg.add_association(end1, end2, association_name)

            assert isinstance(association, IRPAssociationClass)
        finally:
            pkg.delete_from_project()

    def test_add_event(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddEvent")
            created = pkg.add_event(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_get_events(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_event = pkg.add_event(self._unique("CollectionEvent"))

            assert created_event in list(pkg.events)
        finally:
            pkg.delete_from_project()

    def test_get_flow_items(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_flow_item = pkg.add_flow_items(self._unique("CollectionFlowItem"))

            assert created_flow_item in list(pkg.flow_items)
        finally:
            pkg.delete_from_project()

    def test_get_flows(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_flow = pkg.add_flows(self._unique("CollectionFlow"))

            assert created_flow in list(pkg.flows)
        finally:
            pkg.delete_from_project()

    def test_find_event(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_event(self._unique("missing_arg")) is None
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
            created_name = self._unique("AddNode")
            created = pkg.add_node(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_get_nodes(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_node = pkg.add_node(self._unique("CollectionNode"))

            assert created_node in list(pkg.nodes)
        finally:
            pkg.delete_from_project()

    def test_find_node(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_node(self._unique("missing_arg")) is None
        finally:
            pkg.delete_from_project()

    def test_delete_node_by_name(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        node_name = self._unique("DeleteNode")
        try:
            element = pkg.add_node(node_name)
            assert element in list(pkg.nodes)

            pkg.delete_node(node_name)

            assert pkg.find_node(node_name) is None
        finally:
            pkg.delete_from_project()

    def test_add_module(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddModule")
            created = pkg.add_module(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_get_modules(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_module = pkg.add_module(self._unique("CollectionModule"))

            assert created_module in list(pkg.modules)
        finally:
            pkg.delete_from_project()

    def test_add_type(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddType")
            created = pkg.add_type(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_get_types(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_type = pkg.add_type(self._unique("CollectionType"))

            assert created_type in list(pkg.types)
        finally:
            pkg.delete_from_project()

    def test_find_type(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_type(self._unique("missing_arg")) is None
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
            assert pkg.find_global_function(self._unique("missing_arg")) is None
        finally:
            pkg.delete_from_project()

    def test_get_global_functions(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_function = pkg.add_global_function(self._unique("CollectionGlobalFunction"))

            assert created_function in list(pkg.global_functions)
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

    def test_add_global_object_from_real_class(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            class_name = self._unique("GlobalObjectClass")
            object_name = self._unique("GlobalObject")
            created_class = pkg.add_class(class_name)

            instance = pkg.add_global_object(object_name, created_class.name, pkg.name)

            assert instance in list(pkg.global_objects)
        finally:
            pkg.delete_from_project()

    def test_get_global_objects(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_class = pkg.add_class(self._unique("CollectionGlobalClass"))
            object_name = self._unique("CollectionGlobalObject")
            pkg.add_global_object(object_name, created_class.name, pkg.name)

            assert object_name in [global_object.name for global_object in pkg.global_objects]
        finally:
            pkg.delete_from_project()

    def test_find_global_object(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_global_object(self._unique("missing_arg")) is None
        finally:
            pkg.delete_from_project()

    def test_delete_global_object(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            class_name = self._unique("DeleteGlobalClass")
            object_name = self._unique("DeleteGlobalObject")
            pkg.add_class(class_name)
            element = pkg.add_global_object(object_name, class_name, pkg.name)

            pkg.delete_global_object(element)

            assert pkg.find_global_object(object_name) is None
        finally:
            pkg.delete_from_project()

    def test_add_global_variable(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddGlobalVariable")
            created = pkg.add_global_variable(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_get_global_variables(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_variable = pkg.add_global_variable(self._unique("CollectionGlobalVariable"))

            assert created_variable in list(pkg.global_variables)
        finally:
            pkg.delete_from_project()

    def test_find_global_variable(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.find_global_variable(self._unique("missing_arg")) is None
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
            created_class = pkg.add_class(self._unique("CollectionNestedClassifier"))

            assert created_class in list(pkg.nested_classifiers)
        finally:
            pkg.delete_from_project()

    def test_add_instance_specification(self, test_project: IRPProject) -> None:
        """JavaDoc IRPPackage.addInstanceSpecification exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        pkg = self._pkg(test_project)
        try:
            classifier = pkg.add_class(self._unique("InstCls"))
            with pytest.raises(NotImplementedError):
                pkg.add_instance_specification(self._unique("InstSpec"), classifier)
        finally:
            pkg.delete_from_project()

    def test_find_all_by_name_returns_matching_class(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        class_name = self._unique("FindAllByName")
        try:
            created_class = pkg.add_class(class_name)

            found = pkg.find_all_by_name(class_name, "Class")

            assert found == created_class
        finally:
            pkg.delete_from_project()

    def test_get_behavioral_diagrams(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_diagram = pkg.add_activity_diagram()

            assert created_diagram in list(pkg.behavioral_diagrams)
        finally:
            pkg.delete_from_project()

    def test_find_usage(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            element = pkg.add_class(self._unique("UsageCls"))
            assert isinstance(pkg.find_usage(element), IRPCollection)
        finally:
            pkg.delete_from_project()

    def test_get_root_instance_specifications(self, test_project: IRPProject) -> None:
        """JavaDoc IRPPackage.getRootInstanceSpecifications exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(NotImplementedError):
                pkg.get_root_instance_specifications()
        finally:
            pkg.delete_from_project()

    def test_login_to_remote_artifact_server(self, test_project: IRPProject) -> None:
        """JavaDoc IRPPackage.loginToRemoteArtifactServer exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
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

    def test_re_calculate_events_base_id(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.re_calculate_events_base_id() is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_set_remote_requirements_populate_mode(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            assert pkg.set_remote_requirements_populate_mode("All") is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_update_contained_diagrams_on_server(self, test_project: IRPProject) -> None:
        """JavaDoc IRPPackage.updateContainedDiagramsOnServer exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(NotImplementedError):
                pkg.update_contained_diagrams_on_server(1)
        finally:
            pkg.delete_from_project()

    def test_add_implicit_object(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_name = self._unique("AddImplicitObject")
            created = pkg.add_implicit_object(created_name)
            assert created.name == created_name
        finally:
            pkg.delete_from_project()

    def test_get_all_nested_elements(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            created_class = pkg.add_class(self._unique("NestedElementClass"))

            assert created_class in list(pkg.get_all_nested_elements())
        finally:
            pkg.delete_from_project()

    def test_get_events_base_id(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            pkg.add_event(self._unique("EventsBaseIdEvent"))
            pkg.re_calculate_events_base_id()

            base_id = pkg.events_base_id

            assert base_id == str(int(base_id))
        finally:
            pkg.delete_from_project()

    def test_get_namespace(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            namespace = pkg.get_namespace()
            # JavaDoc documents no return contract; this Rhapsody build returns
            # an empty namespace string for a package created at project root.
            assert namespace == ""
        finally:
            pkg.delete_from_project()

    def test_get_saved_in_separate_directory(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            current_value = pkg.saved_in_seperate_directory

            pkg.saved_in_seperate_directory = current_value

            assert pkg.saved_in_seperate_directory == current_value
        finally:
            pkg.delete_from_project()

    def test_set_saved_in_separate_directory(self, test_project: IRPProject) -> None:
        pkg = self._pkg(test_project)
        try:
            pkg.saved_in_seperate_directory = 0
            assert pkg.saved_in_seperate_directory == 0
        finally:
            pkg.delete_from_project()

    def test_update_contained_matrices_on_server(self, test_project: IRPProject) -> None:
        """JavaDoc IRPPackage.updateContainedMatricesOnServer exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(NotImplementedError):
                pkg.update_contained_matrices_on_server(1)
        finally:
            pkg.delete_from_project()

    def test_update_contained_tables_on_server(self, test_project: IRPProject) -> None:
        """JavaDoc IRPPackage.updateContainedTablesOnServer exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        pkg = self._pkg(test_project)
        try:
            with pytest.raises(NotImplementedError):
                pkg.update_contained_tables_on_server(1)
        finally:
            pkg.delete_from_project()
