"""Tests for the IRPFlowchart wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart import IRPStatechart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from tests.unit.models.fakes import make_fake_collection, make_fake_element

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation


def test_is_registered_for_meta_class_flowchart() -> None:
    fake = make_fake_element("Flowchart", properties={"name": "MyActivity"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPFlowchart)
    assert isinstance(wrapped, IRPStatechart)
    assert wrapped.name == "MyActivity"


def test_add_accept_event_action_wraps_result() -> None:
    fake = make_fake_element("Flowchart")
    parent = make_fake_element("State", properties={"name": "RootState"})
    aea = make_fake_element("AcceptEventAction", properties={"name": "AEA1"})
    fake.addAcceptEventAction.return_value = aea
    result = IRPFlowchart(fake).add_accept_event_action("AEA1", IRPState(parent))
    assert result.name == "AEA1"
    fake.addAcceptEventAction.assert_called_once_with("AEA1", parent)


def test_add_accept_time_event_wraps_result() -> None:
    fake = make_fake_element("Flowchart")
    parent = make_fake_element("State", properties={"name": "RootState"})
    ate = make_fake_element("AcceptTimeEvent", properties={"name": "ATE1"})
    fake.addAcceptTimeEvent.return_value = ate
    result = IRPFlowchart(fake).add_accept_time_event("ATE1", IRPState(parent))
    assert result.name == "ATE1"
    fake.addAcceptTimeEvent.assert_called_once_with("ATE1", parent)


def test_add_activity_parameter_wraps_result() -> None:
    fake = make_fake_element("Flowchart")
    pin = make_fake_element("Pin", properties={"name": "Param1"})
    fake.addActivityParameter.return_value = pin
    result = IRPFlowchart(fake).add_activity_parameter("Param1")
    assert result.name == "Param1"
    fake.addActivityParameter.assert_called_once_with("Param1")


def test_add_call_behavior_wraps_result() -> None:
    fake = make_fake_element("Flowchart")
    referenced = make_fake_element("Flowchart", properties={"name": "ReferencedActivity"})
    state = make_fake_element("State", properties={"name": "CallBehaviorState"})
    fake.addCallBehavior.return_value = state
    result = IRPFlowchart(fake).add_call_behavior(cast(IRPModelElement, IRPModelElement.wrap(referenced)))
    assert result.name == "CallBehaviorState"
    fake.addCallBehavior.assert_called_once_with(referenced)


def test_add_call_operation_wraps_result() -> None:
    fake = make_fake_element("Flowchart")
    parent = make_fake_element("State", properties={"name": "RootState"})
    co = make_fake_element("CallOperation", properties={"name": "CO1"})
    fake.addCallOperation.return_value = co
    result = IRPFlowchart(fake).add_call_operation("CO1", IRPState(parent))
    assert result.name == "CO1"
    fake.addCallOperation.assert_called_once_with("CO1", parent)


def test_add_object_node_wraps_result() -> None:
    fake = make_fake_element("Flowchart")
    parent = make_fake_element("State", properties={"name": "RootState"})
    node = make_fake_element("ObjectNode", properties={"name": "ObjectNode1"})
    fake.addObjectNode.return_value = node
    result = IRPFlowchart(fake).add_object_node("ObjectNode1", IRPState(parent))
    assert result.name == "ObjectNode1"
    fake.addObjectNode.assert_called_once_with("ObjectNode1", parent)


def test_add_reference_activity_wraps_result() -> None:
    fake = make_fake_element("Flowchart")
    referenced = make_fake_element("Flowchart", properties={"name": "ReferencedActivity"})
    state = make_fake_element("State", properties={"name": "RefActivityState"})
    fake.addReferenceActivity.return_value = state
    result = IRPFlowchart(fake).add_reference_activity(cast(IRPModelElement, IRPModelElement.wrap(referenced)))
    assert result.name == "RefActivityState"
    fake.addReferenceActivity.assert_called_once_with(referenced)


def test_add_swimlane_wraps_result() -> None:
    fake = make_fake_element("Flowchart")
    swimlane = make_fake_element("Swimlane", properties={"name": "Lane1"})
    fake.addSwimlane.return_value = swimlane
    result = IRPFlowchart(fake).add_swimlane("Lane1")
    assert result.name == "Lane1"
    fake.addSwimlane.assert_called_once_with("Lane1")


def test_get_flowchart_diagram_wraps_result() -> None:
    fake = make_fake_element("Flowchart")
    diagram = make_fake_element("ActivityDiagram", properties={"name": "ActivityDiagram1"})
    fake.getFlowchartDiagram.return_value = diagram
    result = IRPFlowchart(fake).get_flowchart_diagram()
    assert result.name == "ActivityDiagram1"


def test_is_analysis_only_returns_int() -> None:
    fake = make_fake_element("Flowchart", properties={"isAnalysisOnly": 1})
    assert IRPFlowchart(fake).is_analysis_only == 1


def test_is_analysis_only_setter() -> None:
    fake = make_fake_element("Flowchart")
    IRPFlowchart(fake).is_analysis_only = 1
    assert fake.isAnalysisOnly == 1


def test_its_owner_wraps_result() -> None:
    owner = make_fake_element("Operation", properties={"name": "myOperation"})
    fake = make_fake_element("Flowchart", properties={"itsOwner": owner})
    result = IRPFlowchart(fake).its_owner
    assert result is not None
    assert result.name == "myOperation"


def test_its_owner_setter() -> None:
    fake = make_fake_element("Flowchart")
    owner = make_fake_element("Operation", properties={"name": "myOperation"})
    IRPFlowchart(fake).its_owner = cast("IRPOperation", IRPModelElement.wrap(owner))
    assert fake.itsOwner is owner


def test_swimlanes_returns_collection() -> None:
    lane1 = make_fake_element("Swimlane", properties={"name": "Lane1"})
    lane2 = make_fake_element("Swimlane", properties={"name": "Lane2"})
    fake = make_fake_element("Flowchart", properties={"swimlanes": make_fake_collection([lane1, lane2])})
    result = IRPFlowchart(fake).swimlanes
    assert isinstance(result, IRPCollection)
    assert len(result) == 2
