"""Tests for rhapsody_cli.models.elements.interactions.* classes."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.interactions import (
    RPDestructionEvent,
    RPEvent,
    RPEventReception,
    RPExecutionOccurrence,
    RPGuard,
    RPInteractionOccurrence,
    RPInteractionOperand,
    RPInteractionOperator,
    RPMessage,
    RPTransition,
    RPTrigger,
)
from tests.unit.models.fakes import make_fake_collection, make_fake_element

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort
    from rhapsody_cli.models.elements.classifiers.model_statechart import RPStatechart
    from rhapsody_cli.models.elements.common.model_other_model import RPSysMLPort
    from rhapsody_cli.models.elements.diagrams.model_diagram_types import RPSequenceDiagram
    from rhapsody_cli.models.elements.statemachine.model_statemachine import RPStateVertex


class TestRPEvent:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("Event", properties={"name": "Evt1"})
        evt = RPEvent(fake)
        assert isinstance(evt, IRPModelElement)
        assert evt.get_name() == "Evt1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("Event", properties={"name": "Evt1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPEvent)

    def test_get_base_event_wraps_result(self) -> None:
        fake = make_fake_element("Event")
        base = make_fake_element("Event", properties={"name": "Base"})
        fake.getBaseEvent.return_value = base
        evt = RPEvent(fake)
        result = evt.get_base_event()
        assert result.get_name() == "Base"

    def test_get_super_event_wraps_result(self) -> None:
        fake = make_fake_element("Event")
        sup = make_fake_element("Event", properties={"name": "Super"})
        fake.getSuperEvent.return_value = sup
        evt = RPEvent(fake)
        result = evt.get_super_event()
        assert result.get_name() == "Super"

    def test_set_base_event_delegates(self) -> None:
        fake = make_fake_element("Event")
        base = make_fake_element("Event", properties={"name": "Base"})
        fake.setBaseEvent.return_value = None
        evt = RPEvent(fake)
        evt.set_base_event(RPEvent(base))
        fake.setBaseEvent.assert_called_once_with(base)

    def test_set_super_event_delegates(self) -> None:
        fake = make_fake_element("Event")
        sup = make_fake_element("Event", properties={"name": "Super"})
        fake.setSuperEvent.return_value = None
        evt = RPEvent(fake)
        evt.set_super_event(RPEvent(sup))
        fake.setSuperEvent.assert_called_once_with(sup)


class TestRPEventReception:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("EventReception", properties={"name": "ER1"})
        er = RPEventReception(fake)
        assert isinstance(er, IRPModelElement)
        assert er.get_name() == "ER1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("EventReception", properties={"name": "ER1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPEventReception)

    def test_get_event_wraps_result(self) -> None:
        fake = make_fake_element("EventReception")
        evt = make_fake_element("Event", properties={"name": "Evt1"})
        fake.getEvent.return_value = evt
        er = RPEventReception(fake)
        result = er.get_event()
        assert result.get_name() == "Evt1"

    def test_set_event_delegates(self) -> None:
        fake = make_fake_element("EventReception")
        evt = make_fake_element("Event", properties={"name": "Evt1"})
        fake.setEvent.return_value = None
        er = RPEventReception(fake)
        er.set_event(RPEvent(evt))
        fake.setEvent.assert_called_once_with(evt)


class TestRPExecutionOccurrence:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("ExecutionOccurrence", properties={"name": "EO1"})
        eo = RPExecutionOccurrence(fake)
        assert isinstance(eo, IRPModelElement)
        assert eo.get_name() == "EO1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("ExecutionOccurrence", properties={"name": "EO1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPExecutionOccurrence)

    def test_get_message_wraps_result(self) -> None:
        fake = make_fake_element("ExecutionOccurrence")
        msg = make_fake_element("Message", properties={"name": "Msg1"})
        fake.getMessage.return_value = msg
        eo = RPExecutionOccurrence(fake)
        result = eo.get_message()
        assert result.get_name() == "Msg1"


class TestRPGuard:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("Guard", properties={"name": "G1"})
        g = RPGuard(fake)
        assert isinstance(g, IRPModelElement)
        assert g.get_name() == "G1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("Guard", properties={"name": "G1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPGuard)

    def test_get_body_returns_string(self) -> None:
        fake = make_fake_element("Guard", getBody="x > 0")
        g = RPGuard(fake)
        assert g.get_body() == "x > 0"

    def test_set_body_delegates(self) -> None:
        fake = make_fake_element("Guard")
        fake.setBody.return_value = None
        g = RPGuard(fake)
        g.set_body("x > 0")
        fake.setBody.assert_called_once_with("x > 0")


class TestRPInteractionOccurrence:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("InteractionOccurrence", properties={"name": "IO1"})
        io = RPInteractionOccurrence(fake)
        assert isinstance(io, IRPModelElement)
        assert io.get_name() == "IO1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("InteractionOccurrence", properties={"name": "IO1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPInteractionOccurrence)

    def test_get_message_points_returns_collection(self) -> None:
        inner = make_fake_element("Class", properties={"name": "MP"})
        fake = make_fake_element("InteractionOccurrence")
        fake.getMessagePoints.return_value = make_fake_collection([inner])
        io = RPInteractionOccurrence(fake)
        result = io.get_message_points()
        assert isinstance(result, IRPCollection)

    def test_get_reference_sequence_diagram_wraps_result(self) -> None:
        fake = make_fake_element("InteractionOccurrence")
        seq = make_fake_element("SequenceDiagram", properties={"name": "SD1"})
        fake.getReferenceSequenceDiagram.return_value = seq
        io = RPInteractionOccurrence(fake)
        result = io.get_reference_sequence_diagram()
        assert result.get_name() == "SD1"

    def test_set_reference_sequence_diagram_delegates(self) -> None:
        fake = make_fake_element("InteractionOccurrence")
        seq = make_fake_element("SequenceDiagram", properties={"name": "SD1"})
        fake.setReferenceSequenceDiagram.return_value = None
        io = RPInteractionOccurrence(fake)
        io.set_reference_sequence_diagram(cast("RPSequenceDiagram", IRPModelElement(seq)))
        fake.setReferenceSequenceDiagram.assert_called_once_with(seq)


class TestRPInteractionOperand:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("InteractionOperand", properties={"name": "IOp1"})
        iop = RPInteractionOperand(fake)
        assert isinstance(iop, IRPModelElement)
        assert iop.get_name() == "IOp1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("InteractionOperand", properties={"name": "IOp1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPInteractionOperand)

    def test_get_contained_messages_returns_collection(self) -> None:
        inner = make_fake_element("Message", properties={"name": "M1"})
        fake = make_fake_element("InteractionOperand")
        fake.getContainedMessages.return_value = make_fake_collection([inner])
        iop = RPInteractionOperand(fake)
        result = iop.get_contained_messages()
        assert isinstance(result, IRPCollection)

    def test_get_interaction_constraint_returns_string(self) -> None:
        fake = make_fake_element("InteractionOperand", getInteractionConstraint="x > 0")
        iop = RPInteractionOperand(fake)
        assert iop.get_interaction_constraint() == "x > 0"

    def test_set_interaction_constraint_delegates(self) -> None:
        fake = make_fake_element("InteractionOperand")
        fake.setInteractionConstraint.return_value = None
        iop = RPInteractionOperand(fake)
        iop.set_interaction_constraint("x > 0")
        fake.setInteractionConstraint.assert_called_once_with("x > 0")


class TestRPInteractionOperator:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("InteractionOperator", properties={"name": "Alt"})
        iop = RPInteractionOperator(fake)
        assert isinstance(iop, IRPModelElement)
        assert iop.get_name() == "Alt"

    def test_is_registered(self) -> None:
        fake = make_fake_element("InteractionOperator", properties={"name": "Alt"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPInteractionOperator)

    def test_get_interaction_operands_returns_collection(self) -> None:
        inner = make_fake_element("InteractionOperand", properties={"name": "IOp1"})
        fake = make_fake_element("InteractionOperator")
        fake.getInteractionOperands.return_value = make_fake_collection([inner])
        iop = RPInteractionOperator(fake)
        result = iop.get_interaction_operands()
        assert isinstance(result, IRPCollection)

    def test_get_interaction_type_returns_string(self) -> None:
        fake = make_fake_element("InteractionOperator", getInteractionType="alt")
        iop = RPInteractionOperator(fake)
        assert iop.get_interaction_type() == "alt"

    def test_set_interaction_type_delegates(self) -> None:
        fake = make_fake_element("InteractionOperator")
        fake.setInteractionType.return_value = None
        iop = RPInteractionOperator(fake)
        iop.set_interaction_type("alt")
        fake.setInteractionType.assert_called_once_with("alt")


class TestRPMessage:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("Message", properties={"name": "Msg1"})
        msg = RPMessage(fake)
        assert isinstance(msg, IRPModelElement)
        assert msg.get_name() == "Msg1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("Message", properties={"name": "Msg1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPMessage)

    def test_add_source_execution_occurrence_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        eo = make_fake_element("ExecutionOccurrence", properties={"name": "EO1"})
        fake.addSourceExecutionOccurrence.return_value = eo
        msg = RPMessage(fake)
        result = msg.add_source_execution_occurrence()
        assert result.get_name() == "EO1"
        fake.addSourceExecutionOccurrence.assert_called_once_with()

    def test_add_target_execution_occurrence_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        eo = make_fake_element("ExecutionOccurrence", properties={"name": "EO2"})
        fake.addTargetExecutionOccurrence.return_value = eo
        msg = RPMessage(fake)
        result = msg.add_target_execution_occurrence()
        assert result.get_name() == "EO2"
        fake.addTargetExecutionOccurrence.assert_called_once_with()

    def test_get_actual_parameter_list_returns_collection(self) -> None:
        inner = make_fake_element("Class", properties={"name": "P"})
        fake = make_fake_element("Message")
        fake.getActualParameterList.return_value = make_fake_collection([inner])
        msg = RPMessage(fake)
        result = msg.get_actual_parameter_list()
        assert isinstance(result, IRPCollection)

    def test_get_communication_connection_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        conn = make_fake_element("AssociationRole", properties={"name": "conn1"})
        fake.getCommunicationConnection.return_value = conn
        msg = RPMessage(fake)
        result = msg.get_communication_connection()
        assert result.get_name() == "conn1"

    def test_get_condition_returns_string(self) -> None:
        fake = make_fake_element("Message", getCondition="cond")
        msg = RPMessage(fake)
        assert msg.get_condition() == "cond"

    def test_get_duration_constraint_returns_string(self) -> None:
        fake = make_fake_element("Message", getDurationConstraint="5s")
        msg = RPMessage(fake)
        assert msg.get_duration_constraint() == "5s"

    def test_get_duration_observation_returns_string(self) -> None:
        fake = make_fake_element("Message", getDurationObservation="{t}")
        msg = RPMessage(fake)
        assert msg.get_duration_observation() == "{t}"

    def test_get_flow_port_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        fp = make_fake_element("SysMLPort", properties={"name": "fp1"})
        fake.getFlowPort.return_value = fp
        msg = RPMessage(fake)
        result = msg.get_flow_port()
        assert result.get_name() == "fp1"

    def test_get_formal_interface_item_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        op = make_fake_element("InterfaceItem", properties={"name": "op1"})
        fake.getFormalInterfaceItem.return_value = op
        msg = RPMessage(fake)
        result = msg.get_formal_interface_item()
        assert result.get_name() == "op1"

    def test_get_formal_type_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        ft = make_fake_element("Class", properties={"name": "FT"})
        fake.getFormalType.return_value = ft
        msg = RPMessage(fake)
        result = msg.get_formal_type()
        assert cast(IRPModelElement, result).get_name() == "FT"

    def test_get_invariant_returns_string(self) -> None:
        fake = make_fake_element("Message", getInvariant="inv")
        msg = RPMessage(fake)
        assert msg.get_invariant() == "inv"

    def test_get_message_type_returns_string(self) -> None:
        fake = make_fake_element("Message", getMessageType="asynch")
        msg = RPMessage(fake)
        assert msg.get_message_type() == "asynch"

    def test_get_port_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        p = make_fake_element("Port", properties={"name": "p1"})
        fake.getPort.return_value = p
        msg = RPMessage(fake)
        result = msg.get_port()
        assert result.get_name() == "p1"

    def test_get_return_value_returns_string(self) -> None:
        fake = make_fake_element("Message", getReturnValue="result")
        msg = RPMessage(fake)
        assert msg.get_return_value() == "result"

    def test_get_sequence_number_returns_string(self) -> None:
        fake = make_fake_element("Message", getSequenceNumber="1")
        msg = RPMessage(fake)
        assert msg.get_sequence_number() == "1"

    def test_get_signature_returns_string(self) -> None:
        fake = make_fake_element("Message", getSignature="sig")
        msg = RPMessage(fake)
        assert msg.get_signature() == "sig"

    def test_get_source_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        src = make_fake_element("ClassifierRole", properties={"name": "src"})
        fake.getSource.return_value = src
        msg = RPMessage(fake)
        result = msg.get_source()
        assert result.get_name() == "src"

    def test_get_source_execution_occurrence_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        eo = make_fake_element("ExecutionOccurrence", properties={"name": "EO1"})
        fake.getSourceExecutionOccurrence.return_value = eo
        msg = RPMessage(fake)
        result = msg.get_source_execution_occurrence()
        assert result.get_name() == "EO1"

    def test_get_target_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        tgt = make_fake_element("ClassifierRole", properties={"name": "tgt"})
        fake.getTarget.return_value = tgt
        msg = RPMessage(fake)
        result = msg.get_target()
        assert result.get_name() == "tgt"

    def test_get_target_execution_occurrence_wraps_result(self) -> None:
        fake = make_fake_element("Message")
        eo = make_fake_element("ExecutionOccurrence", properties={"name": "EO2"})
        fake.getTargetExecutionOccurrence.return_value = eo
        msg = RPMessage(fake)
        result = msg.get_target_execution_occurrence()
        assert result.get_name() == "EO2"

    def test_get_time_constraint_returns_string(self) -> None:
        fake = make_fake_element("Message", getTimeConstraint="{t}")
        msg = RPMessage(fake)
        assert msg.get_time_constraint() == "{t}"

    def test_get_time_observation_returns_string(self) -> None:
        fake = make_fake_element("Message", getTimeObservation="{now}")
        msg = RPMessage(fake)
        assert msg.get_time_observation() == "{now}"

    def test_get_timer_value_returns_string(self) -> None:
        fake = make_fake_element("Message", getTimerValue="100")
        msg = RPMessage(fake)
        assert msg.get_timer_value() == "100"

    def test_reroute_delegates(self) -> None:
        fake = make_fake_element("Message")
        fake.reroute.return_value = None
        msg = RPMessage(fake)
        msg.reroute()
        fake.reroute.assert_called_once_with()

    def test_set_actual_parameter_list_delegates(self) -> None:
        inner = make_fake_element("Class", properties={"name": "P"})
        fake = make_fake_element("Message")
        col = IRPCollection(make_fake_collection([inner]))
        fake.setActualParameterList.return_value = None
        msg = RPMessage(fake)
        msg.set_actual_parameter_list(col)
        fake.setActualParameterList.assert_called_once_with(col._com)

    def test_set_duration_constraint_delegates(self) -> None:
        fake = make_fake_element("Message")
        fake.setDurationConstraint.return_value = None
        msg = RPMessage(fake)
        msg.set_duration_constraint("5s")
        fake.setDurationConstraint.assert_called_once_with("5s")

    def test_set_duration_observation_delegates(self) -> None:
        fake = make_fake_element("Message")
        fake.setDurationObservation.return_value = None
        msg = RPMessage(fake)
        msg.set_duration_observation("{t}")
        fake.setDurationObservation.assert_called_once_with("{t}")

    def test_set_flow_port_delegates(self) -> None:
        fake = make_fake_element("Message")
        fp = make_fake_element("SysMLPort", properties={"name": "fp1"})
        fake.setFlowPort.return_value = None
        msg = RPMessage(fake)
        msg.set_flow_port(cast("RPSysMLPort", IRPModelElement(fp)))
        fake.setFlowPort.assert_called_once_with(fp)

    def test_set_formal_interface_item_delegates(self) -> None:
        fake = make_fake_element("Message")
        op = make_fake_element("InterfaceItem", properties={"name": "op1"})
        fake.setFormalInterfaceItem.return_value = None
        msg = RPMessage(fake)
        msg.set_formal_interface_item(IRPInterfaceItem(op))
        fake.setFormalInterfaceItem.assert_called_once_with(op)

    def test_set_formal_type_delegates(self) -> None:
        fake = make_fake_element("Message")
        ft = make_fake_element("Class", properties={"name": "FT"})
        fake.setFormalType.return_value = None
        msg = RPMessage(fake)
        msg.set_formal_type(IRPModelElement(ft))
        fake.setFormalType.assert_called_once_with(ft)

    def test_set_invariant_delegates(self) -> None:
        fake = make_fake_element("Message")
        fake.setInvariant.return_value = None
        msg = RPMessage(fake)
        msg.set_invariant("inv")
        fake.setInvariant.assert_called_once_with("inv")

    def test_set_port_delegates(self) -> None:
        fake = make_fake_element("Message")
        p = make_fake_element("Port", properties={"name": "p1"})
        fake.setPort.return_value = None
        msg = RPMessage(fake)
        msg.set_port(cast("IRPPort", IRPModelElement(p)))
        fake.setPort.assert_called_once_with(p)

    def test_set_return_value_delegates(self) -> None:
        fake = make_fake_element("Message")
        fake.setReturnValue.return_value = None
        msg = RPMessage(fake)
        msg.set_return_value("result")
        fake.setReturnValue.assert_called_once_with("result")

    def test_set_time_constraint_delegates(self) -> None:
        fake = make_fake_element("Message")
        fake.setTimeConstraint.return_value = None
        msg = RPMessage(fake)
        msg.set_time_constraint("{t}")
        fake.setTimeConstraint.assert_called_once_with("{t}")

    def test_set_time_observation_delegates(self) -> None:
        fake = make_fake_element("Message")
        fake.setTimeObservation.return_value = None
        msg = RPMessage(fake)
        msg.set_time_observation("{now}")
        fake.setTimeObservation.assert_called_once_with("{now}")

    def test_set_timer_value_delegates(self) -> None:
        fake = make_fake_element("Message")
        fake.setTimerValue.return_value = None
        msg = RPMessage(fake)
        msg.set_timer_value("100")
        fake.setTimerValue.assert_called_once_with("100")


class TestRPTransition:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("Transition", properties={"name": "T1"})
        t = RPTransition(fake)
        assert isinstance(t, IRPModelElement)
        assert t.get_name() == "T1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("Transition", properties={"name": "T1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPTransition)

    def test_get_inherits_from_wraps_result(self) -> None:
        fake = make_fake_element("Transition")
        base = make_fake_element("Transition", properties={"name": "Base"})
        fake.getInheritsFrom.return_value = base
        t = RPTransition(fake)
        result = t.get_inherits_from()
        assert result.get_name() == "Base"

    def test_get_is_overridden_returns_int(self) -> None:
        fake = make_fake_element("Transition", getIsOverridden=True)
        t = RPTransition(fake)
        assert t.get_is_overridden() == 1

    def test_get_its_action_wraps_result(self) -> None:
        fake = make_fake_element("Transition")
        action = make_fake_element("Action", properties={"name": "doIt"})
        fake.getItsAction.return_value = action
        t = RPTransition(fake)
        result = t.get_its_action()
        assert result.get_name() == "doIt"

    def test_get_its_guard_wraps_result(self) -> None:
        fake = make_fake_element("Transition")
        guard = make_fake_element("Guard", properties={"name": "G1"})
        fake.getItsGuard.return_value = guard
        t = RPTransition(fake)
        result = t.get_its_guard()
        assert result.get_name() == "G1"

    def test_get_its_label_returns_string(self) -> None:
        fake = make_fake_element("Transition", getItsLabel="e[g]/a")
        t = RPTransition(fake)
        assert t.get_its_label() == "e[g]/a"

    def test_get_its_source_wraps_result(self) -> None:
        fake = make_fake_element("Transition")
        src = make_fake_element("StateVertex", properties={"name": "S1"})
        fake.getItsSource.return_value = src
        t = RPTransition(fake)
        result = t.get_its_source()
        assert result.get_name() == "S1"

    def test_get_its_statechart_wraps_result(self) -> None:
        fake = make_fake_element("Transition")
        sc = make_fake_element("Statechart", properties={"name": "SC1"})
        fake.getItsStatechart.return_value = sc
        t = RPTransition(fake)
        result = t.get_its_statechart()
        assert result.get_name() == "SC1"

    def test_get_its_target_wraps_result(self) -> None:
        fake = make_fake_element("Transition")
        tgt = make_fake_element("StateVertex", properties={"name": "S2"})
        fake.getItsTarget.return_value = tgt
        t = RPTransition(fake)
        result = t.get_its_target()
        assert result.get_name() == "S2"

    def test_get_its_trigger_wraps_result(self) -> None:
        fake = make_fake_element("Transition")
        trig = make_fake_element("Trigger", properties={"name": "Trg1"})
        fake.getItsTrigger.return_value = trig
        t = RPTransition(fake)
        result = t.get_its_trigger()
        assert result.get_name() == "Trg1"

    def test_get_of_state_wraps_result(self) -> None:
        fake = make_fake_element("Transition")
        st = make_fake_element("State", properties={"name": "S1"})
        fake.getOfState.return_value = st
        t = RPTransition(fake)
        result = t.get_of_state()
        assert result.get_name() == "S1"

    def test_is_default_transition_returns_int(self) -> None:
        fake = make_fake_element("Transition", isDefaultTransition=True)
        t = RPTransition(fake)
        assert t.is_default_transition() == 1
        fake.isDefaultTransition.assert_called_once_with()

    def test_is_static_reaction_returns_int(self) -> None:
        fake = make_fake_element("Transition", isStaticReaction=True)
        t = RPTransition(fake)
        assert t.is_static_reaction() == 1
        fake.isStaticReaction.assert_called_once_with()

    def test_its_compound_source_returns_collection(self) -> None:
        inner = make_fake_element("StateVertex", properties={"name": "S1"})
        fake = make_fake_element("Transition")
        fake.itsCompoundSource.return_value = make_fake_collection([inner])
        t = RPTransition(fake)
        result = t.its_compound_source()
        assert isinstance(result, IRPCollection)
        fake.itsCompoundSource.assert_called_once_with()

    def test_override_inheritance_delegates(self) -> None:
        fake = make_fake_element("Transition")
        fake.overrideInheritance.return_value = None
        t = RPTransition(fake)
        t.override_inheritance()
        fake.overrideInheritance.assert_called_once_with()

    def test_reset_label_inheritance_wraps_result(self) -> None:
        fake = make_fake_element("Transition", properties={"name": "T1"})
        fake.resetLabelInheritance.return_value = fake
        t = RPTransition(fake)
        result = t.reset_label_inheritance()
        assert result.get_name() == "T1"
        fake.resetLabelInheritance.assert_called_once_with()

    def test_set_its_action_wraps_result(self) -> None:
        fake = make_fake_element("Transition", properties={"name": "T1"})
        action = make_fake_element("Action", properties={"name": "doIt"})
        fake.setItsAction.return_value = action
        t = RPTransition(fake)
        result = t.set_its_action("doIt()")
        assert result.get_name() == "doIt"
        fake.setItsAction.assert_called_once_with("doIt()")

    def test_set_its_guard_wraps_result(self) -> None:
        fake = make_fake_element("Transition", properties={"name": "T1"})
        guard = make_fake_element("Guard", properties={"name": "G1"})
        fake.setItsGuard.return_value = guard
        t = RPTransition(fake)
        result = t.set_its_guard("x > 0")
        assert result.get_name() == "G1"
        fake.setItsGuard.assert_called_once_with("x > 0")

    def test_set_its_label_delegates(self) -> None:
        fake = make_fake_element("Transition")
        fake.setItsLabel.return_value = None
        t = RPTransition(fake)
        t.set_its_label("evt", "g", "act")
        fake.setItsLabel.assert_called_once_with("evt", "g", "act")

    def test_set_its_source_delegates(self) -> None:
        fake = make_fake_element("Transition")
        src = make_fake_element("StateVertex", properties={"name": "S1"})
        fake.setItsSource.return_value = None
        t = RPTransition(fake)
        t.set_its_source(cast("RPStateVertex", IRPModelElement(src)))
        fake.setItsSource.assert_called_once_with(src)

    def test_set_its_statechart_delegates(self) -> None:
        fake = make_fake_element("Transition")
        sc = make_fake_element("Statechart", properties={"name": "SC1"})
        fake.setItsStatechart.return_value = None
        t = RPTransition(fake)
        t.set_its_statechart(cast("RPStatechart", IRPModelElement(sc)))
        fake.setItsStatechart.assert_called_once_with(sc)

    def test_set_its_target_delegates(self) -> None:
        fake = make_fake_element("Transition")
        tgt = make_fake_element("StateVertex", properties={"name": "S2"})
        fake.setItsTarget.return_value = None
        t = RPTransition(fake)
        t.set_its_target(cast("RPStateVertex", IRPModelElement(tgt)))
        fake.setItsTarget.assert_called_once_with(tgt)

    def test_set_its_trigger_wraps_result(self) -> None:
        fake = make_fake_element("Transition", properties={"name": "T1"})
        trig = make_fake_element("Trigger", properties={"name": "Trg1"})
        fake.setItsTrigger.return_value = trig
        t = RPTransition(fake)
        result = t.set_its_trigger("evt")
        assert result.get_name() == "Trg1"
        fake.setItsTrigger.assert_called_once_with("evt")

    def test_unoverride_inheritance_delegates(self) -> None:
        fake = make_fake_element("Transition")
        fake.unoverrideInheritance.return_value = None
        t = RPTransition(fake)
        t.unoverride_inheritance()
        fake.unoverrideInheritance.assert_called_once_with()


class TestRPTrigger:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("Trigger", properties={"name": "Trg1"})
        trg = RPTrigger(fake)
        assert isinstance(trg, IRPModelElement)
        assert trg.get_name() == "Trg1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("Trigger", properties={"name": "Trg1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPTrigger)

    def test_get_body_returns_string(self) -> None:
        fake = make_fake_element("Trigger", getBody="evt")
        trg = RPTrigger(fake)
        assert trg.get_body() == "evt"

    def test_get_its_operation_wraps_result(self) -> None:
        fake = make_fake_element("Trigger")
        op = make_fake_element("InterfaceItem", properties={"name": "op1"})
        fake.getItsOperation.return_value = op
        trg = RPTrigger(fake)
        result = trg.get_its_operation()
        assert result.get_name() == "op1"

    def test_is_operation_returns_int(self) -> None:
        fake = make_fake_element("Trigger", isOperation=True)
        trg = RPTrigger(fake)
        assert trg.is_operation() == 1
        fake.isOperation.assert_called_once_with()

    def test_is_timeout_returns_int(self) -> None:
        fake = make_fake_element("Trigger", isTimeout=True)
        trg = RPTrigger(fake)
        assert trg.is_timeout() == 1
        fake.isTimeout.assert_called_once_with()

    def test_set_body_delegates(self) -> None:
        fake = make_fake_element("Trigger")
        fake.setBody.return_value = None
        trg = RPTrigger(fake)
        trg.set_body("evt")
        fake.setBody.assert_called_once_with("evt")


class TestRPDestructionEvent:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("DestructionEvent", properties={"name": "DE1"})
        de = RPDestructionEvent(fake)
        assert isinstance(de, IRPModelElement)
        assert de.get_name() == "DE1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("DestructionEvent", properties={"name": "DE1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPDestructionEvent)
