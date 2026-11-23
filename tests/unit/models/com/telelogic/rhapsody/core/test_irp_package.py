"""Tests for rhapsody_cli.elements.package.IRPPackage."""

from typing import cast

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.elements.activity import RPFlow, RPFlowItem
from rhapsody_cli.models.elements.common import RPSysMLPort
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_package_is_a_unit() -> None:
    fake = make_fake_element("Package", properties={"name": "MyPkg"})
    package = IRPPackage(fake)

    assert isinstance(package, IRPUnit)
    assert package.get_name() == "MyPkg"


def test_package_add_class_delegates_to_com_and_wraps_result() -> None:
    fake = make_fake_element("Package")
    new_class = make_fake_element("Class", properties={"name": "Widget"})
    fake.addClass.return_value = new_class
    package = IRPPackage(fake)

    result = package.add_class("Widget")

    fake.addClass.assert_called_once_with("Widget")
    assert result.get_name() == "Widget"


def test_package_add_nested_package_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    nested = make_fake_element("Package", properties={"name": "Nested"})
    fake.addNestedPackage.return_value = nested
    package = IRPPackage(fake)

    result = package.add_nested_package("Nested")

    fake.addNestedPackage.assert_called_once_with("Nested")
    assert result.get_name() == "Nested"


def test_package_add_actor_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    actor = make_fake_element("Actor", properties={"name": "Driver"})
    fake.addActor.return_value = actor
    package = IRPPackage(fake)

    result = package.add_actor("Driver")

    fake.addActor.assert_called_once_with("Driver")
    assert result.get_name() == "Driver"


def test_package_add_global_function_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    func = make_fake_element("Operation", properties={"name": "doThing"})
    fake.addGlobalFunction.return_value = func
    package = IRPPackage(fake)

    result = package.add_global_function("doThing")

    fake.addGlobalFunction.assert_called_once_with("doThing")
    assert result.get_name() == "doThing"


def test_package_is_registered_for_meta_class_package() -> None:
    fake = make_fake_element("Package", properties={"name": "MyPkg"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPPackage)


def test_package_get_nested_packages_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    nested1 = make_fake_element("Package", properties={"name": "Nested1"})
    nested2 = make_fake_element("Package", properties={"name": "Nested2"})
    fake.packages = make_fake_collection([nested1, nested2])
    package = IRPPackage(fake)

    result = package.get_nested_packages()
    assert isinstance(result, IRPCollection)
    assert len(result) == 2
    assert result[0].get_name() == "Nested1"
    assert result[1].get_name() == "Nested2"


def test_package_get_classes_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    class1 = make_fake_element("Class", properties={"name": "Class1"})
    class2 = make_fake_element("Class", properties={"name": "Class2"})
    fake.classes = make_fake_collection([class1, class2])
    package = IRPPackage(fake)

    result = package.get_classes()
    assert isinstance(result, IRPCollection)
    assert len(result) == 2


def test_package_get_actors_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    actor1 = make_fake_element("Actor", properties={"name": "Actor1"})
    fake.actors = make_fake_collection([actor1])
    package = IRPPackage(fake)

    result = package.get_actors()
    assert isinstance(result, IRPCollection)
    assert len(result) == 1


def test_package_get_use_cases_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    uc1 = make_fake_element("UseCase", properties={"name": "UC1"})
    fake.useCases = make_fake_collection([uc1])
    package = IRPPackage(fake)

    result = package.get_use_cases()
    assert isinstance(result, IRPCollection)


def test_package_add_use_case_returns_wrapped_element() -> None:
    fake = make_fake_element("Package")
    uc = make_fake_element("UseCase", properties={"name": "UC1"})
    fake.addUseCase.return_value = uc
    package = IRPPackage(fake)

    result = package.add_use_case("UC1")

    fake.addUseCase.assert_called_once_with("UC1")
    assert result.get_name() == "UC1"


# --- New diagram tests ---
def test_package_add_activity_diagram_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    diagram = make_fake_element("ActivityDiagram", properties={"name": "Activity1"})
    fake.addActivityDiagram.return_value = diagram
    package = IRPPackage(fake)

    result = package.add_activity_diagram("Activity1")

    fake.addActivityDiagram.assert_called_once_with("Activity1")
    assert result.get_name() == "Activity1"


def test_package_add_sequence_diagram_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    diagram = make_fake_element("SequenceDiagram", properties={"name": "Seq1"})
    fake.addSequenceDiagram.return_value = diagram
    package = IRPPackage(fake)

    result = package.add_sequence_diagram("Seq1")

    fake.addSequenceDiagram.assert_called_once_with("Seq1")
    assert result.get_name() == "Seq1"


def test_package_get_sequence_diagrams_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    diagram = make_fake_element("SequenceDiagram", properties={"name": "Seq1"})
    fake.sequenceDiagrams = make_fake_collection([diagram])
    package = IRPPackage(fake)

    result = package.get_sequence_diagrams()
    assert isinstance(result, IRPCollection)


def test_package_delete_class_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)
    cls_fake = make_fake_element("Class", properties={"name": "ToDelete"})

    package.delete_class(IRPUnit(cls_fake))

    fake.deleteClass.assert_called_once_with(cls_fake)


def test_package_delete_package_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)
    nested_fake = make_fake_element("Package", properties={"name": "Nested"})

    package.delete_package(IRPUnit(nested_fake))

    fake.deletePackage.assert_called_once_with(nested_fake)


def test_package_find_class_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    found = make_fake_element("Class", properties={"name": "MyClass"})
    fake.findClass.return_value = found
    package = IRPPackage(fake)

    result = package.find_class("MyClass")

    fake.findClass.assert_called_once_with("MyClass")
    assert result.get_name() == "MyClass"


def test_package_add_association_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    assoc = make_fake_element("Relation", properties={"name": "assoc1"})
    fake.addAssociation.return_value = assoc
    package = IRPPackage(fake)

    result = package.add_association("assoc1")

    fake.addAssociation.assert_called_once_with("assoc1")
    assert result.get_name() == "assoc1"


def test_package_get_events_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    event = make_fake_element("Event", properties={"name": "Event1"})
    fake.events = make_fake_collection([event])
    package = IRPPackage(fake)

    result = package.get_events()

    assert isinstance(result, IRPCollection)


def test_package_get_nodes_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    node = make_fake_element("Node", properties={"name": "Node1"})
    fake.nodes = make_fake_collection([node])
    package = IRPPackage(fake)

    result = package.get_nodes()

    assert isinstance(result, IRPCollection)


def test_package_add_flow_items_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    flow_item = make_fake_element("FlowItem", properties={"name": "MyFlowItem"})
    fake.addFlowItems.return_value = flow_item
    package = IRPPackage(fake)

    result = package.add_flow_items("MyFlowItem")

    fake.addFlowItems.assert_called_once_with("MyFlowItem")
    assert result.get_name() == "MyFlowItem"


def test_package_add_flows_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    flow = make_fake_element("Flow", properties={"name": "MyFlow"})
    fake.addFlows.return_value = flow
    package = IRPPackage(fake)

    result = package.add_flows("MyFlow")

    fake.addFlows.assert_called_once_with("MyFlow")
    assert result.get_name() == "MyFlow"


def test_package_delete_flow_items_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)
    flow_item_fake = make_fake_element("FlowItem", properties={"name": "ToDelete"})

    package.delete_flow_items(cast(RPFlowItem, IRPModelElement(flow_item_fake)))

    fake.deleteFlowItems.assert_called_once_with(flow_item_fake)


def test_package_delete_flows_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)
    flow_fake = make_fake_element("Flow", properties={"name": "ToDelete"})

    package.delete_flows(cast(RPFlow, IRPModelElement(flow_fake)))

    fake.deleteFlows.assert_called_once_with(flow_fake)


def test_package_get_flow_items_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    flow_item = make_fake_element("FlowItem", properties={"name": "FlowItem1"})
    fake.flowItems = make_fake_collection([flow_item])
    package = IRPPackage(fake)

    result = package.get_flow_items()
    assert isinstance(result, IRPCollection)


def test_package_get_flows_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    flow = make_fake_element("Flow", properties={"name": "Flow1"})
    fake.flows = make_fake_collection([flow])
    package = IRPPackage(fake)

    result = package.get_flows()
    assert isinstance(result, IRPCollection)


# --- Remote Requirements Methods (Task 3) Tests ---
def test_package_get_remote_requirements_populate_mode_returns_int() -> None:
    fake = make_fake_element("Package")
    fake.getRemoteRequirementsPopulateMode.return_value = 1
    package = IRPPackage(fake)

    result = package.get_remote_requirements_populate_mode()
    assert result == 1


def test_package_get_root_instance_specifications_raises_not_implemented() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)

    with pytest.raises(NotImplementedError):
        package.get_root_instance_specifications()

    fake.getRootInstanceSpecifications.assert_not_called()


def test_package_login_to_remote_artifact_server_raises_not_implemented() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)

    with pytest.raises(NotImplementedError):
        package.login_to_remote_artifact_server()

    fake.loginToRemoteArtifactServer.assert_not_called()


def test_package_populate_remote_requirements_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)

    package.populate_remote_requirements()

    fake.populateRemoteRequirements.assert_called_once_with()


def test_package_recalculate_events_base_id_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)

    package.recalculate_events_base_id()

    fake.reCalculateEventsBaseId.assert_called_once_with()


def test_package_set_remote_requirements_populate_mode_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)

    package.set_remote_requirements_populate_mode(2)

    fake.setRemoteRequirementsPopulateMode.assert_called_once_with(2)


def test_package_update_contained_diagrams_on_server_raises_not_implemented() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)

    with pytest.raises(NotImplementedError):
        package.update_contained_diagrams_on_server(1)

    fake.updateContainedDiagramsOnServer.assert_not_called()


# --- SysML Methods (Task 4) Tests ---
def test_package_add_implicit_object_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    instance = make_fake_element("Instance", properties={"name": "ImplicitObj"})
    fake.addImplicitObject.return_value = instance
    package = IRPPackage(fake)

    result = package.add_implicit_object("ImplicitObj")

    fake.addImplicitObject.assert_called_once_with("ImplicitObj")
    assert result.get_name() == "ImplicitObj"


def test_package_add_link_between_sysml_ports_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    port1_fake = make_fake_element("SysMLPort", properties={"name": "Port1"})
    port2_fake = make_fake_element("SysMLPort", properties={"name": "Port2"})
    link_fake = make_fake_element("Link", properties={"name": "Link1"})
    fake.addLinkBetweenSYSMLPorts.return_value = link_fake
    package = IRPPackage(fake)

    result = package.add_link_between_sysml_ports(
        cast(RPSysMLPort, IRPModelElement(port1_fake)),
        cast(RPSysMLPort, IRPModelElement(port2_fake)),
    )

    fake.addLinkBetweenSYSMLPorts.assert_called_once_with(port1_fake, port2_fake)
    assert result.get_name() == "Link1"


# --- Misc Methods (Task 5) Tests ---
def test_package_get_all_nested_elements_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    elem1 = make_fake_element("Class", properties={"name": "Class1"})
    elem2 = make_fake_element("Package", properties={"name": "NestedPkg"})
    fake.getAllNestedElements.return_value = make_fake_collection([elem1, elem2])
    package = IRPPackage(fake)

    result = package.get_all_nested_elements()
    assert isinstance(result, IRPCollection)


def test_package_get_events_base_id_returns_string() -> None:
    fake = make_fake_element("Package")
    fake.eventsBaseId = "EventsBase_123"
    package = IRPPackage(fake)

    result = package.get_events_base_id()
    assert result == "EventsBase_123"


def test_package_get_namespace_returns_string() -> None:
    fake = make_fake_element("Package")
    fake.getNamespace.return_value = "com.example.mypackage"
    package = IRPPackage(fake)

    result = package.get_namespace()
    assert result == "com.example.mypackage"


def test_package_get_saved_in_separate_directory_returns_int() -> None:
    fake = make_fake_element("Package")
    fake.savedInSeperateDirectory = 1
    package = IRPPackage(fake)

    result = package.get_saved_in_separate_directory()
    assert result == 1


def test_package_get_user_defined_stereotypes_returns_collection() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection

    fake = make_fake_element("Package")
    stereotype = make_fake_element("Stereotype", properties={"name": "MyStereotype"})
    fake.userDefinedStereotypes = make_fake_collection([stereotype])
    package = IRPPackage(fake)

    result = package.get_user_defined_stereotypes()
    assert isinstance(result, IRPCollection)


def test_package_set_saved_in_separate_directory_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)

    package.set_saved_in_separate_directory(1)

    assert fake.savedInSeperateDirectory == 1


def test_package_update_contained_matrices_on_server_raises_not_implemented() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)

    with pytest.raises(NotImplementedError):
        package.update_contained_matrices_on_server(1)

    fake.updateContainedMatricesOnServer.assert_not_called()


def test_package_update_contained_tables_on_server_raises_not_implemented() -> None:
    fake = make_fake_element("Package")
    package = IRPPackage(fake)

    with pytest.raises(NotImplementedError):
        package.update_contained_tables_on_server(1)

    fake.updateContainedTablesOnServer.assert_not_called()


def test_generated_add_class() -> None:
    fake = make_fake_element("Package")
    fake.addClass.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_class("x")
    assert result is not None


def test_generated_add_nested_package() -> None:
    fake = make_fake_element("Package")
    fake.addNestedPackage.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_nested_package("x")
    assert result is not None


def test_generated_add_actor() -> None:
    fake = make_fake_element("Package")
    fake.addActor.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_actor("x")
    assert result is not None


def test_generated_add_global_function() -> None:
    fake = make_fake_element("Package")
    fake.addGlobalFunction.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_global_function("x")
    assert result is not None


def test_generated_add_flow_items() -> None:
    fake = make_fake_element("Package")
    fake.addFlowItems.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_flow_items("x")
    assert result is not None


def test_generated_add_flows() -> None:
    fake = make_fake_element("Package")
    fake.addFlows.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_flows("x")
    assert result is not None


def test_generated_get_nested_packages() -> None:
    fake = make_fake_element("Package", properties={"packages": make_fake_collection([])})
    result = IRPPackage(fake).get_nested_packages()
    assert result is not None


def test_generated_get_classes() -> None:
    fake = make_fake_element("Package", properties={"classes": make_fake_collection([])})
    result = IRPPackage(fake).get_classes()
    assert result is not None


def test_generated_get_actors() -> None:
    fake = make_fake_element("Package", properties={"actors": make_fake_collection([])})
    result = IRPPackage(fake).get_actors()
    assert result is not None


def test_generated_get_use_cases() -> None:
    fake = make_fake_element("Package", properties={"useCases": make_fake_collection([])})
    result = IRPPackage(fake).get_use_cases()
    assert result is not None


def test_generated_add_use_case() -> None:
    fake = make_fake_element("Package")
    fake.addUseCase.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_use_case("x")
    assert result is not None


def test_generated_add_activity_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addActivityDiagram.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_activity_diagram("x")
    assert result is not None


def test_generated_add_sequence_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addSequenceDiagram.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_sequence_diagram("x")
    assert result is not None


def test_generated_add_use_case_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addUseCaseDiagram.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_use_case_diagram("x")
    assert result is not None


def test_generated_add_collaboration_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addCollaborationDiagram.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_collaboration_diagram("x")
    assert result is not None


def test_generated_add_component_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addComponentDiagram.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_component_diagram("x")
    assert result is not None


def test_generated_add_deployment_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addDeploymentDiagram.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_deployment_diagram("x")
    assert result is not None


def test_generated_add_object_model_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addObjectModelDiagram.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_object_model_diagram("x")
    assert result is not None


def test_generated_add_statechart_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addStatechart.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_statechart_diagram("x")
    assert result is not None


def test_generated_add_timing_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addTimingDiagram.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_timing_diagram("x")
    assert result is not None


def test_generated_add_panel_diagram() -> None:
    fake = make_fake_element("Package")
    fake.addPanelDiagram.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_panel_diagram("x")
    assert result is not None


def test_generated_get_sequence_diagrams() -> None:
    fake = make_fake_element("Package", properties={"sequenceDiagrams": make_fake_collection([])})
    result = IRPPackage(fake).get_sequence_diagrams()
    assert result is not None


def test_generated_get_use_case_diagrams() -> None:
    fake = make_fake_element("Package", properties={"useCaseDiagrams": make_fake_collection([])})
    result = IRPPackage(fake).get_use_case_diagrams()
    assert result is not None


def test_generated_get_collaboration_diagrams() -> None:
    fake = make_fake_element("Package", properties={"collaborationDiagrams": make_fake_collection([])})
    result = IRPPackage(fake).get_collaboration_diagrams()
    assert result is not None


def test_generated_get_component_diagrams() -> None:
    fake = make_fake_element("Package", properties={"componentDiagrams": make_fake_collection([])})
    result = IRPPackage(fake).get_component_diagrams()
    assert result is not None


def test_generated_get_deployment_diagrams() -> None:
    fake = make_fake_element("Package", properties={"deploymentDiagrams": make_fake_collection([])})
    result = IRPPackage(fake).get_deployment_diagrams()
    assert result is not None


def test_generated_get_object_model_diagrams() -> None:
    fake = make_fake_element("Package", properties={"objectModelDiagrams": make_fake_collection([])})
    result = IRPPackage(fake).get_object_model_diagrams()
    assert result is not None


def test_generated_get_timing_diagrams() -> None:
    fake = make_fake_element("Package", properties={"timingDiagrams": make_fake_collection([])})
    result = IRPPackage(fake).get_timing_diagrams()
    assert result is not None


def test_generated_get_panel_diagrams() -> None:
    fake = make_fake_element("Package", properties={"panelDiagrams": make_fake_collection([])})
    result = IRPPackage(fake).get_panel_diagrams()
    assert result is not None


def test_generated_delete_sequence_diagram() -> None:
    fake = make_fake_element("Package")
    fake.deleteSequenceDiagram.return_value = None
    IRPPackage(fake).delete_sequence_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_use_case_diagram() -> None:
    fake = make_fake_element("Package")
    fake.deleteUseCaseDiagram.return_value = None
    IRPPackage(fake).delete_use_case_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_collaboration_diagram() -> None:
    fake = make_fake_element("Package")
    fake.deleteCollaborationDiagram.return_value = None
    IRPPackage(fake).delete_collaboration_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_component_diagram() -> None:
    fake = make_fake_element("Package")
    fake.deleteComponentDiagram.return_value = None
    IRPPackage(fake).delete_component_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_deployment_diagram() -> None:
    fake = make_fake_element("Package")
    fake.deleteDeploymentDiagram.return_value = None
    IRPPackage(fake).delete_deployment_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_object_model_diagram() -> None:
    fake = make_fake_element("Package")
    fake.deleteObjectModelDiagram.return_value = None
    IRPPackage(fake).delete_object_model_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_timing_diagram() -> None:
    fake = make_fake_element("Package")
    fake.deleteTimingDiagram.return_value = None
    IRPPackage(fake).delete_timing_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_panel_diagram() -> None:
    fake = make_fake_element("Package")
    fake.deletePanelDiagram.return_value = None
    IRPPackage(fake).delete_panel_diagram(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_class() -> None:
    fake = make_fake_element("Package")
    fake.deleteClass.return_value = None
    IRPPackage(fake).delete_class(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_actor() -> None:
    fake = make_fake_element("Package")
    fake.deleteActor.return_value = None
    IRPPackage(fake).delete_actor(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_use_case() -> None:
    fake = make_fake_element("Package")
    fake.deleteUseCase.return_value = None
    IRPPackage(fake).delete_use_case(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_flow_items() -> None:
    fake = make_fake_element("Package")
    fake.deleteFlowItems.return_value = None
    IRPPackage(fake).delete_flow_items(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_flows() -> None:
    fake = make_fake_element("Package")
    fake.deleteFlows.return_value = None
    IRPPackage(fake).delete_flows(make_fake_element("Class", properties={"name": "x"}))


def test_generated_delete_package() -> None:
    fake = make_fake_element("Package")
    fake.deletePackage.return_value = None
    IRPPackage(fake).delete_package(make_fake_element("Class", properties={"name": "x"}))


def test_generated_find_class() -> None:
    fake = make_fake_element("Package")
    fake.findClass.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).find_class("x")
    assert result is not None


def test_generated_find_actor() -> None:
    fake = make_fake_element("Package")
    fake.findActor.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).find_actor("x")
    assert result is not None


def test_generated_find_use_case() -> None:
    fake = make_fake_element("Package")
    fake.findUseCase.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).find_use_case("x")
    assert result is not None


def test_generated_add_association() -> None:
    fake = make_fake_element("Package")
    fake.addAssociation.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_association("x")
    assert result is not None


def test_generated_add_event() -> None:
    fake = make_fake_element("Package")
    fake.addEvent.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_event("x")
    assert result is not None


def test_generated_get_events() -> None:
    fake = make_fake_element("Package", properties={"events": make_fake_collection([])})
    result = IRPPackage(fake).get_events()
    assert result is not None


def test_generated_get_flow_items() -> None:
    fake = make_fake_element("Package", properties={"flowItems": make_fake_collection([])})
    result = IRPPackage(fake).get_flow_items()
    assert result is not None


def test_generated_get_flows() -> None:
    fake = make_fake_element("Package", properties={"flows": make_fake_collection([])})
    result = IRPPackage(fake).get_flows()
    assert result is not None


def test_generated_find_event() -> None:
    fake = make_fake_element("Package")
    fake.findEvent.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).find_event("x")
    assert result is not None


def test_generated_delete_event() -> None:
    fake = make_fake_element("Package")
    fake.deleteEvent.return_value = None
    IRPPackage(fake).delete_event(make_fake_element("Class", properties={"name": "x"}))


def test_generated_add_node() -> None:
    fake = make_fake_element("Package")
    fake.addNode.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_node("x")
    assert result is not None


def test_generated_get_nodes() -> None:
    fake = make_fake_element("Package", properties={"nodes": make_fake_collection([])})
    result = IRPPackage(fake).get_nodes()
    assert result is not None


def test_generated_find_node() -> None:
    fake = make_fake_element("Package")
    fake.findNode.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).find_node("x")
    assert result is not None


def test_generated_delete_node() -> None:
    fake = make_fake_element("Package")
    fake.deleteNode.return_value = None
    IRPPackage(fake).delete_node(make_fake_element("Class", properties={"name": "x"}))


def test_generated_add_module() -> None:
    fake = make_fake_element("Package")
    fake.addModule.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_module("x")
    assert result is not None


def test_generated_get_modules() -> None:
    fake = make_fake_element("Package", properties={"modules": make_fake_collection([])})
    result = IRPPackage(fake).get_modules()
    assert result is not None


def test_generated_add_type() -> None:
    fake = make_fake_element("Package")
    fake.addType.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_type("x")
    assert result is not None


def test_generated_get_types() -> None:
    fake = make_fake_element("Package", properties={"types": make_fake_collection([])})
    result = IRPPackage(fake).get_types()
    assert result is not None


def test_generated_find_type() -> None:
    fake = make_fake_element("Package")
    fake.findType.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).find_type("x")
    assert result is not None


def test_generated_delete_type() -> None:
    fake = make_fake_element("Package")
    fake.deleteType.return_value = None
    IRPPackage(fake).delete_type(make_fake_element("Class", properties={"name": "x"}))


def test_generated_find_global_function() -> None:
    fake = make_fake_element("Package")
    fake.findGlobalFunction.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).find_global_function("x")
    assert result is not None


def test_generated_get_global_functions() -> None:
    fake = make_fake_element("Package", properties={"globalFunctions": make_fake_collection([])})
    result = IRPPackage(fake).get_global_functions()
    assert result is not None


def test_generated_delete_global_function() -> None:
    fake = make_fake_element("Package")
    fake.deleteGlobalFunction.return_value = None
    IRPPackage(fake).delete_global_function(make_fake_element("Class", properties={"name": "x"}))


def test_generated_add_global_object() -> None:
    fake = make_fake_element("Package")
    fake.addGlobalObject.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_global_object("x")
    assert result is not None


def test_generated_get_global_objects() -> None:
    fake = make_fake_element("Package", properties={"globalObjects": make_fake_collection([])})
    result = IRPPackage(fake).get_global_objects()
    assert result is not None


def test_generated_find_global_object() -> None:
    fake = make_fake_element("Package")
    fake.findGlobalObject.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).find_global_object("x")
    assert result is not None


def test_generated_delete_global_object() -> None:
    fake = make_fake_element("Package")
    fake.deleteGlobalObject.return_value = None
    IRPPackage(fake).delete_global_object(make_fake_element("Class", properties={"name": "x"}))


def test_generated_add_global_variable() -> None:
    fake = make_fake_element("Package")
    fake.addGlobalVariable.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_global_variable("x")
    assert result is not None


def test_generated_get_global_variables() -> None:
    fake = make_fake_element("Package", properties={"globalVariables": make_fake_collection([])})
    result = IRPPackage(fake).get_global_variables()
    assert result is not None


def test_generated_find_global_variable() -> None:
    fake = make_fake_element("Package")
    fake.findGlobalVariable.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).find_global_variable("x")
    assert result is not None


def test_generated_delete_global_variable() -> None:
    fake = make_fake_element("Package")
    fake.deleteGlobalVariable.return_value = None
    IRPPackage(fake).delete_global_variable(make_fake_element("Class", properties={"name": "x"}))


def test_generated_get_nested_classifiers() -> None:
    fake = make_fake_element("Package", properties={"nestedClassifiers": make_fake_collection([])})
    result = IRPPackage(fake).get_nested_classifiers()
    assert result is not None


def test_generated_get_nested_components() -> None:
    fake = make_fake_element("Package", properties={"nestedComponents": make_fake_collection([])})
    result = IRPPackage(fake).get_nested_components()
    assert result is not None


def test_generated_add_instance_specification_raises_not_implemented() -> None:
    fake = make_fake_element("Package")
    classifier = make_fake_element("Class", properties={"name": "x"})

    with pytest.raises(NotImplementedError):
        IRPPackage(fake).add_instance_specification("x", classifier)

    fake.addInstanceSpecification.assert_not_called()


def test_generated_get_instance_specifications() -> None:
    fake = make_fake_element("Package", properties={"instanceSpecifications": make_fake_collection([])})
    result = IRPPackage(fake).get_instance_specifications()
    assert result is not None


def test_generated_add_link() -> None:
    fake = make_fake_element("Package")
    fake.addLink.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_link("x")
    assert result is not None


def test_generated_get_links() -> None:
    fake = make_fake_element("Package", properties={"links": make_fake_collection([])})
    result = IRPPackage(fake).get_links()
    assert result is not None


def test_generated_find_all_by_name() -> None:
    fake = make_fake_element("Package")
    fake.findAllByName.return_value = make_fake_collection([])
    result = IRPPackage(fake).find_all_by_name("x")
    assert result is not None


def test_generated_get_behavioral_diagrams() -> None:
    fake = make_fake_element("Package", properties={"behavioralDiagrams": make_fake_collection([])})
    result = IRPPackage(fake).get_behavioral_diagrams()
    assert result is not None


def test_generated_get_source_artifacts() -> None:
    fake = make_fake_element("Package", properties={"sourceArtifacts": make_fake_collection([])})
    result = IRPPackage(fake).get_source_artifacts()
    assert result is not None


def test_generated_find_usage() -> None:
    fake = make_fake_element("Package")
    fake.findUsage.return_value = make_fake_collection([])
    result = IRPPackage(fake).find_usage(make_fake_element("Class", properties={"name": "x"}))
    assert result is not None


def test_generated_get_remote_requirements_populate_mode() -> None:
    fake = make_fake_element("Package")
    fake.getRemoteRequirementsPopulateMode.return_value = 1
    result = IRPPackage(fake).get_remote_requirements_populate_mode()
    assert result is not None


def test_generated_get_root_instance_specifications_raises_not_implemented() -> None:
    fake = make_fake_element("Package")

    with pytest.raises(NotImplementedError):
        IRPPackage(fake).get_root_instance_specifications()

    fake.getRootInstanceSpecifications.assert_not_called()


def test_generated_login_to_remote_artifact_server_raises_not_implemented() -> None:
    fake = make_fake_element("Package")

    with pytest.raises(NotImplementedError):
        IRPPackage(fake).login_to_remote_artifact_server()

    fake.loginToRemoteArtifactServer.assert_not_called()


def test_generated_populate_remote_requirements() -> None:
    fake = make_fake_element("Package")
    fake.populateRemoteRequirements.return_value = None
    IRPPackage(fake).populate_remote_requirements()


def test_generated_recalculate_events_base_id() -> None:
    fake = make_fake_element("Package")
    fake.reCalculateEventsBaseId.return_value = None
    IRPPackage(fake).recalculate_events_base_id()


def test_generated_set_remote_requirements_populate_mode() -> None:
    fake = make_fake_element("Package")
    fake.setRemoteRequirementsPopulateMode.return_value = None
    IRPPackage(fake).set_remote_requirements_populate_mode(1)


def test_generated_update_contained_diagrams_on_server_raises_not_implemented() -> None:
    fake = make_fake_element("Package")

    with pytest.raises(NotImplementedError):
        IRPPackage(fake).update_contained_diagrams_on_server(1)

    fake.updateContainedDiagramsOnServer.assert_not_called()


def test_generated_add_implicit_object() -> None:
    fake = make_fake_element("Package")
    fake.addImplicitObject.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_implicit_object("x")
    assert result is not None


def test_generated_add_link_between_sysml_ports() -> None:
    fake = make_fake_element("Package")
    fake.addLinkBetweenSYSMLPorts.return_value = make_fake_element("Class", properties={"name": "x"})
    result = IRPPackage(fake).add_link_between_sysml_ports(make_fake_element("Class", properties={"name": "x"}), make_fake_element("Class", properties={"name": "x"}))
    assert result is not None


def test_generated_get_all_nested_elements() -> None:
    fake = make_fake_element("Package")
    fake.getAllNestedElements.return_value = make_fake_collection([])
    result = IRPPackage(fake).get_all_nested_elements()
    assert result is not None


def test_generated_get_events_base_id() -> None:
    fake = make_fake_element("Package", properties={"eventsBaseId": make_fake_collection([])})
    result = IRPPackage(fake).get_events_base_id()
    assert result is not None


def test_generated_get_namespace() -> None:
    fake = make_fake_element("Package")
    fake.getNamespace.return_value = "x"
    result = IRPPackage(fake).get_namespace()
    assert result is not None


def test_generated_get_saved_in_separate_directory() -> None:
    fake = make_fake_element("Package", properties={"savedInSeperateDirectory": make_fake_collection([])})
    result = IRPPackage(fake).get_saved_in_separate_directory()
    assert result is not None


def test_generated_get_user_defined_stereotypes() -> None:
    fake = make_fake_element("Package", properties={"userDefinedStereotypes": make_fake_collection([])})
    result = IRPPackage(fake).get_user_defined_stereotypes()
    assert result is not None


def test_generated_set_saved_in_separate_directory() -> None:
    fake = make_fake_element("Package")
    IRPPackage(fake).set_saved_in_separate_directory(1)


def test_generated_update_contained_matrices_on_server_raises_not_implemented() -> None:
    fake = make_fake_element("Package")

    with pytest.raises(NotImplementedError):
        IRPPackage(fake).update_contained_matrices_on_server(1)

    fake.updateContainedMatricesOnServer.assert_not_called()


def test_generated_update_contained_tables_on_server_raises_not_implemented() -> None:
    fake = make_fake_element("Package")

    with pytest.raises(NotImplementedError):
        IRPPackage(fake).update_contained_tables_on_server(1)

    fake.updateContainedTablesOnServer.assert_not_called()
