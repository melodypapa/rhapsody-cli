"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_activity flowchart classes."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_activity import (
    IRPFlow,
    IRPFlowchart,
    IRPFlowItem,
    IRPObjectNode,
    IRPSwimlane,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart import IRPStatechart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from tests.unit.models.fakes import make_fake_collection, make_fake_element

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model import IRPSysMLPort
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort


class TestRPFlow:
    """Tests for IRPFlow (17 methods)."""

    def test_is_model_element(self) -> None:
        fake = make_fake_element("Flow", properties={"name": "MyFlow"})
        flow = IRPFlow(fake)
        assert isinstance(flow, IRPModelElement)
        assert flow.name == "MyFlow"

    def test_add_conveyed_delegates(self) -> None:
        fake = make_fake_element("Flow")
        element = make_fake_element("Class", properties={"name": "ConveyedClass"})
        flow = IRPFlow(fake)
        flow.add_conveyed(cast(IRPModelElement, IRPModelElement.wrap(element)))
        fake.addConveyed.assert_called_once_with(element)

    def test_get_conveyed_returns_collection(self) -> None:
        fake = make_fake_element("Flow")
        item1 = make_fake_element("Class", properties={"name": "Item1"})
        item2 = make_fake_element("Class", properties={"name": "Item2"})
        fake.getConveyed.return_value = make_fake_collection([item1, item2])
        flow = IRPFlow(fake)
        result = flow.get_conveyed()
        assert isinstance(result, IRPCollection)
        assert len(result) == 2

    def test_get_direction_returns_string(self) -> None:
        fake = make_fake_element("Flow", getDirection="toEnd2")
        flow = IRPFlow(fake)
        assert flow.get_direction() == "toEnd2"

    def test_get_end1_wraps_result(self) -> None:
        fake = make_fake_element("Flow")
        end1 = make_fake_element("State", properties={"name": "End1State"})
        fake.getEnd1.return_value = end1
        flow = IRPFlow(fake)
        result = flow.get_end1()
        assert cast(IRPModelElement, result).name == "End1State"

    def test_get_end1_port_wraps_result(self) -> None:
        fake = make_fake_element("Flow")
        port = make_fake_element("Port", properties={"name": "Port1"})
        fake.getEnd1Port.return_value = port
        flow = IRPFlow(fake)
        result = flow.get_end1_port()
        assert result.name == "Port1"

    def test_get_end1_sys_ml_port_wraps_result(self) -> None:
        fake = make_fake_element("Flow")
        sysml_port = make_fake_element("SysMLPort", properties={"name": "SysMLPort1"})
        fake.getEnd1SysMLPort.return_value = sysml_port
        flow = IRPFlow(fake)
        result = flow.get_end1_sys_ml_port()
        assert result.name == "SysMLPort1"

    def test_get_end2_wraps_result(self) -> None:
        fake = make_fake_element("Flow")
        end2 = make_fake_element("State", properties={"name": "End2State"})
        fake.getEnd2.return_value = end2
        flow = IRPFlow(fake)
        result = flow.get_end2()
        assert cast(IRPModelElement, result).name == "End2State"

    def test_get_end2_port_wraps_result(self) -> None:
        fake = make_fake_element("Flow")
        port = make_fake_element("Port", properties={"name": "Port2"})
        fake.getEnd2Port.return_value = port
        flow = IRPFlow(fake)
        result = flow.get_end2_port()
        assert result.name == "Port2"

    def test_get_end2_sys_ml_port_wraps_result(self) -> None:
        fake = make_fake_element("Flow")
        sysml_port = make_fake_element("SysMLPort", properties={"name": "SysMLPort2"})
        fake.getEnd2SysMLPort.return_value = sysml_port
        flow = IRPFlow(fake)
        result = flow.get_end2_sys_ml_port()
        assert result.name == "SysMLPort2"

    def test_remove_conveyed_delegates(self) -> None:
        fake = make_fake_element("Flow")
        element = make_fake_element("Class", properties={"name": "ConveyedClass"})
        flow = IRPFlow(fake)
        flow.remove_conveyed(cast(IRPModelElement, IRPModelElement.wrap(element)))
        fake.removeConveyed.assert_called_once_with(element)

    def test_set_direction_delegates(self) -> None:
        fake = make_fake_element("Flow")
        flow = IRPFlow(fake)
        flow.set_direction("bidirectional")
        fake.setDirection.assert_called_once_with("bidirectional")

    def test_set_end1_delegates(self) -> None:
        fake = make_fake_element("Flow")
        end1 = make_fake_element("State", properties={"name": "End1State"})
        flow = IRPFlow(fake)
        flow.set_end1(cast(IRPModelElement, IRPModelElement.wrap(end1)))
        fake.setEnd1.assert_called_once_with(end1)

    def test_set_end1_via_port_delegates(self) -> None:
        fake = make_fake_element("Flow")
        instance = make_fake_element("Instance", properties={"name": "MyInstance"})
        port = make_fake_element("Port", properties={"name": "MyPort"})
        flow = IRPFlow(fake)
        flow.set_end1_via_port(
            cast("IRPInstance", IRPModelElement.wrap(instance)),
            cast("IRPPort", IRPModelElement.wrap(port)),
        )
        fake.setEnd1ViaPort.assert_called_once_with(instance, port)

    def test_set_end1_via_sys_ml_port_delegates(self) -> None:
        fake = make_fake_element("Flow")
        instance = make_fake_element("Instance", properties={"name": "MyInstance"})
        sysml_port = make_fake_element("SysMLPort", properties={"name": "MySysMLPort"})
        flow = IRPFlow(fake)
        flow.set_end1_via_sys_ml_port(
            cast("IRPInstance", IRPModelElement.wrap(instance)),
            cast("IRPSysMLPort", IRPModelElement.wrap(sysml_port)),
        )
        fake.setEnd1ViaSysMLPort.assert_called_once_with(instance, sysml_port)

    def test_set_end2_delegates(self) -> None:
        fake = make_fake_element("Flow")
        end2 = make_fake_element("State", properties={"name": "End2State"})
        flow = IRPFlow(fake)
        flow.set_end2(cast(IRPModelElement, IRPModelElement.wrap(end2)))
        fake.setEnd2.assert_called_once_with(end2)

    def test_set_end2_via_port_delegates(self) -> None:
        fake = make_fake_element("Flow")
        instance = make_fake_element("Instance", properties={"name": "MyInstance"})
        port = make_fake_element("Port", properties={"name": "MyPort"})
        flow = IRPFlow(fake)
        flow.set_end2_via_port(
            cast("IRPInstance", IRPModelElement.wrap(instance)),
            cast("IRPPort", IRPModelElement.wrap(port)),
        )
        fake.setEnd2ViaPort.assert_called_once_with(instance, port)

    def test_set_end2_via_sys_ml_port_delegates(self) -> None:
        fake = make_fake_element("Flow")
        instance = make_fake_element("Instance", properties={"name": "MyInstance"})
        sysml_port = make_fake_element("SysMLPort", properties={"name": "MySysMLPort"})
        flow = IRPFlow(fake)
        flow.set_end2_via_sys_ml_port(
            cast("IRPInstance", IRPModelElement.wrap(instance)),
            cast("IRPSysMLPort", IRPModelElement.wrap(sysml_port)),
        )
        fake.setEnd2ViaSysMLPort.assert_called_once_with(instance, sysml_port)

    def test_is_registered_for_meta_class_flow(self) -> None:
        fake = make_fake_element("Flow", properties={"name": "MyFlow"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPFlow)


class TestRPFlowItem:
    """Tests for IRPFlowItem (3 methods)."""

    def test_is_classifier(self) -> None:
        fake = make_fake_element("FlowItem", properties={"name": "MyFlowItem"})
        flow_item = IRPFlowItem(fake)
        assert isinstance(flow_item, IRPModelElement)
        assert flow_item.name == "MyFlowItem"

    def test_add_represented_delegates(self) -> None:
        fake = make_fake_element("FlowItem")
        element = make_fake_element("Class", properties={"name": "RepresentedClass"})
        flow_item = IRPFlowItem(fake)
        flow_item.add_represented(cast(IRPModelElement, IRPModelElement.wrap(element)))
        fake.addRepresented.assert_called_once_with(element)

    def test_get_represented_returns_collection(self) -> None:
        fake = make_fake_element("FlowItem")
        item1 = make_fake_element("Class", properties={"name": "Rep1"})
        item2 = make_fake_element("Class", properties={"name": "Rep2"})
        fake.getRepresented.return_value = make_fake_collection([item1, item2])
        flow_item = IRPFlowItem(fake)
        result = flow_item.get_represented()
        assert isinstance(result, IRPCollection)
        assert len(result) == 2

    def test_remove_represented_delegates(self) -> None:
        fake = make_fake_element("FlowItem")
        element = make_fake_element("Class", properties={"name": "RepresentedClass"})
        flow_item = IRPFlowItem(fake)
        flow_item.remove_represented(cast(IRPModelElement, IRPModelElement.wrap(element)))
        fake.removeRepresented.assert_called_once_with(element)

    def test_is_registered_for_meta_class_flow_item(self) -> None:
        fake = make_fake_element("FlowItem", properties={"name": "MyFlowItem"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPFlowItem)


class TestRPFlowchart:
    """Tests for IRPFlowchart (15 methods)."""

    def test_is_statechart(self) -> None:
        fake = make_fake_element("Flowchart", properties={"name": "MyActivity"})
        flowchart = IRPFlowchart(fake)
        assert isinstance(flowchart, IRPStatechart)
        assert flowchart.name == "MyActivity"

    def test_add_accept_event_action_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        parent = make_fake_element("State", properties={"name": "RootState"})
        aea = make_fake_element("AcceptEventAction", properties={"name": "AEA1"})
        fake.addAcceptEventAction.return_value = aea
        flowchart = IRPFlowchart(fake)
        result = flowchart.add_accept_event_action("AEA1", IRPState(parent))
        assert result.name == "AEA1"
        fake.addAcceptEventAction.assert_called_once_with("AEA1", parent)

    def test_add_accept_time_event_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        parent = make_fake_element("State", properties={"name": "RootState"})
        ate = make_fake_element("AcceptTimeEvent", properties={"name": "ATE1"})
        fake.addAcceptTimeEvent.return_value = ate
        flowchart = IRPFlowchart(fake)
        result = flowchart.add_accept_time_event("ATE1", IRPState(parent))
        assert result.name == "ATE1"
        fake.addAcceptTimeEvent.assert_called_once_with("ATE1", parent)

    def test_add_activity_parameter_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        pin = make_fake_element("Pin", properties={"name": "Param1"})
        fake.addActivityParameter.return_value = pin
        flowchart = IRPFlowchart(fake)
        result = flowchart.add_activity_parameter("Param1")
        assert result.name == "Param1"
        fake.addActivityParameter.assert_called_once_with("Param1")

    def test_add_call_behavior_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        referenced = make_fake_element("Flowchart", properties={"name": "ReferencedActivity"})
        state = make_fake_element("State", properties={"name": "CallBehaviorState"})
        fake.addCallBehavior.return_value = state
        flowchart = IRPFlowchart(fake)
        result = flowchart.add_call_behavior(cast(IRPModelElement, IRPModelElement.wrap(referenced)))
        assert result.name == "CallBehaviorState"
        fake.addCallBehavior.assert_called_once_with(referenced)

    def test_add_call_operation_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        parent = make_fake_element("State", properties={"name": "RootState"})
        co = make_fake_element("CallOperation", properties={"name": "CO1"})
        fake.addCallOperation.return_value = co
        flowchart = IRPFlowchart(fake)
        result = flowchart.add_call_operation("CO1", IRPState(parent))
        assert result.name == "CO1"
        fake.addCallOperation.assert_called_once_with("CO1", parent)

    def test_add_object_node_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        parent = make_fake_element("State", properties={"name": "RootState"})
        node = make_fake_element("ObjectNode", properties={"name": "ObjectNode1"})
        fake.addObjectNode.return_value = node
        flowchart = IRPFlowchart(fake)
        result = flowchart.add_object_node("ObjectNode1", IRPState(parent))
        assert result.name == "ObjectNode1"
        fake.addObjectNode.assert_called_once_with("ObjectNode1", parent)

    def test_add_reference_activity_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        referenced = make_fake_element("Flowchart", properties={"name": "ReferencedActivity"})
        state = make_fake_element("State", properties={"name": "RefActivityState"})
        fake.addReferenceActivity.return_value = state
        flowchart = IRPFlowchart(fake)
        result = flowchart.add_reference_activity(cast(IRPModelElement, IRPModelElement.wrap(referenced)))
        assert result.name == "RefActivityState"
        fake.addReferenceActivity.assert_called_once_with(referenced)

    def test_add_swimlane_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        swimlane = make_fake_element("Swimlane", properties={"name": "Lane1"})
        fake.addSwimlane.return_value = swimlane
        flowchart = IRPFlowchart(fake)
        result = flowchart.add_swimlane("Lane1")
        assert result.name == "Lane1"
        fake.addSwimlane.assert_called_once_with("Lane1")

    def test_get_flowchart_diagram_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        diagram = make_fake_element("ActivityDiagram", properties={"name": "ActivityDiagram1"})
        fake.getFlowchartDiagram.return_value = diagram
        flowchart = IRPFlowchart(fake)
        result = flowchart.get_flowchart_diagram()
        assert result.name == "ActivityDiagram1"

    def test_get_is_analysis_only_returns_int(self) -> None:
        fake = make_fake_element("Flowchart", getIsAnalysisOnly=1)
        flowchart = IRPFlowchart(fake)
        assert flowchart.get_is_analysis_only() == 1

    def test_get_its_owner_wraps_result(self) -> None:
        fake = make_fake_element("Flowchart")
        owner = make_fake_element("Operation", properties={"name": "myOperation"})
        fake.getItsOwner.return_value = owner
        flowchart = IRPFlowchart(fake)
        result = flowchart.get_its_owner()
        assert result.name == "myOperation"

    def test_get_swimlanes_returns_collection(self) -> None:
        fake = make_fake_element("Flowchart")
        lane1 = make_fake_element("Swimlane", properties={"name": "Lane1"})
        lane2 = make_fake_element("Swimlane", properties={"name": "Lane2"})
        fake.getSwimlanes.return_value = make_fake_collection([lane1, lane2])
        flowchart = IRPFlowchart(fake)
        result = flowchart.get_swimlanes()
        assert isinstance(result, IRPCollection)
        assert len(result) == 2

    def test_set_is_analysis_only_delegates(self) -> None:
        fake = make_fake_element("Flowchart")
        flowchart = IRPFlowchart(fake)
        flowchart.set_is_analysis_only(1)
        fake.setIsAnalysisOnly.assert_called_once_with(1)

    def test_set_its_owner_delegates(self) -> None:
        fake = make_fake_element("Flowchart")
        owner = make_fake_element("Operation", properties={"name": "myOperation"})
        flowchart = IRPFlowchart(fake)
        flowchart.set_its_owner(cast("IRPOperation", IRPModelElement.wrap(owner)))
        fake.setItsOwner.assert_called_once_with(owner)

    def test_is_registered_for_meta_class_flowchart(self) -> None:
        fake = make_fake_element("Flowchart", properties={"name": "MyActivity"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPFlowchart)


class TestRPObjectNode:
    """Tests for IRPObjectNode (7 methods)."""

    def test_is_state(self) -> None:
        fake = make_fake_element("ObjectNode", properties={"name": "MyObjectNode"})
        node = IRPObjectNode(fake)
        assert isinstance(node, IRPState)
        assert node.name == "MyObjectNode"

    def test_add_in_state_delegates(self) -> None:
        fake = make_fake_element("ObjectNode")
        state = make_fake_element("State", properties={"name": "InStateValue"})
        node = IRPObjectNode(fake)
        node.add_in_state(cast(IRPModelElement, IRPModelElement.wrap(state)))
        fake.addInState.assert_called_once_with(state)

    def test_get_in_state_returns_string(self) -> None:
        fake = make_fake_element("ObjectNode", getInState="SomeState")
        node = IRPObjectNode(fake)
        assert node.get_in_state() == "SomeState"

    def test_get_in_state_list_returns_collection(self) -> None:
        fake = make_fake_element("ObjectNode")
        state1 = make_fake_element("State", properties={"name": "State1"})
        state2 = make_fake_element("State", properties={"name": "State2"})
        fake.getInStateList.return_value = make_fake_collection([state1, state2])
        node = IRPObjectNode(fake)
        result = node.get_in_state_list()
        assert isinstance(result, IRPCollection)
        assert len(result) == 2

    def test_get_represents_wraps_result(self) -> None:
        fake = make_fake_element("ObjectNode")
        represents = make_fake_element("Class", properties={"name": "MyClass"})
        fake.getRepresents.return_value = represents
        node = IRPObjectNode(fake)
        result = node.get_represents()
        assert cast(IRPModelElement, result).name == "MyClass"

    def test_remove_in_state_delegates(self) -> None:
        fake = make_fake_element("ObjectNode")
        state = make_fake_element("State", properties={"name": "InStateValue"})
        node = IRPObjectNode(fake)
        node.remove_in_state(cast(IRPModelElement, IRPModelElement.wrap(state)))
        fake.removeInState.assert_called_once_with(state)

    def test_set_in_state_delegates(self) -> None:
        fake = make_fake_element("ObjectNode")
        node = IRPObjectNode(fake)
        node.set_in_state("SomeState")
        fake.setInState.assert_called_once_with("SomeState")

    def test_set_represents_delegates(self) -> None:
        fake = make_fake_element("ObjectNode")
        represents = make_fake_element("Class", properties={"name": "MyClass"})
        node = IRPObjectNode(fake)
        node.set_represents(cast(IRPModelElement, IRPModelElement.wrap(represents)))
        fake.setRepresents.assert_called_once_with(represents)

    def test_is_registered_for_meta_class_object_node(self) -> None:
        fake = make_fake_element("ObjectNode", properties={"name": "MyObjectNode"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPObjectNode)


class TestRPSwimlane:
    """Tests for IRPSwimlane (5 methods - note: addSwimlane + getSwimlanes = 5 total)."""

    def test_is_model_element(self) -> None:
        fake = make_fake_element("Swimlane", properties={"name": "MySwimlane"})
        swimlane = IRPSwimlane(fake)
        assert isinstance(swimlane, IRPModelElement)
        assert swimlane.name == "MySwimlane"

    def test_add_swimlane_wraps_result(self) -> None:
        fake = make_fake_element("Swimlane")
        nested = make_fake_element("Swimlane", properties={"name": "NestedLane"})
        fake.addSwimlane.return_value = nested
        swimlane = IRPSwimlane(fake)
        result = swimlane.add_swimlane("NestedLane")
        assert result.name == "NestedLane"
        fake.addSwimlane.assert_called_once_with("NestedLane")

    def test_get_contents_returns_collection(self) -> None:
        fake = make_fake_element("Swimlane")
        item1 = make_fake_element("State", properties={"name": "Content1"})
        item2 = make_fake_element("State", properties={"name": "Content2"})
        fake.getContents.return_value = make_fake_collection([item1, item2])
        swimlane = IRPSwimlane(fake)
        result = swimlane.get_contents()
        assert isinstance(result, IRPCollection)
        assert len(result) == 2

    def test_get_represents_wraps_result(self) -> None:
        fake = make_fake_element("Swimlane")
        represents = make_fake_element("Class", properties={"name": "MyClass"})
        fake.getRepresents.return_value = represents
        swimlane = IRPSwimlane(fake)
        result = swimlane.get_represents()
        assert cast(IRPModelElement, result).name == "MyClass"

    def test_get_swimlanes_returns_collection(self) -> None:
        fake = make_fake_element("Swimlane")
        lane1 = make_fake_element("Swimlane", properties={"name": "NestedLane1"})
        lane2 = make_fake_element("Swimlane", properties={"name": "NestedLane2"})
        fake.getSwimlanes.return_value = make_fake_collection([lane1, lane2])
        swimlane = IRPSwimlane(fake)
        result = swimlane.get_swimlanes()
        assert isinstance(result, IRPCollection)
        assert len(result) == 2

    def test_set_represents_delegates(self) -> None:
        fake = make_fake_element("Swimlane")
        represents = make_fake_element("Class", properties={"name": "MyClass"})
        swimlane = IRPSwimlane(fake)
        swimlane.set_represents(cast(IRPModelElement, IRPModelElement.wrap(represents)))
        fake.setRepresents.assert_called_once_with(represents)

    def test_is_registered_for_meta_class_swimlane(self) -> None:
        fake = make_fake_element("Swimlane", properties={"name": "MySwimlane"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPSwimlane)
