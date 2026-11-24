"""Interactions model-element wrappers (auto-generated stubs)."""

from typing import TYPE_CHECKING, Optional, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collaboration import IRPCollaboration
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions import IRPAction
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_role import (
        IRPAssociationRole,
    )
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPSequenceDiagram
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model import (
        IRPClassifierRole,
        IRPSysMLPort,
    )
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart import IRPStatechart
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState, IRPStateVertex


class IRPEvent(IRPInterfaceItem):
    """Wraps ``IRPEvent``: represents events in Rhapsody models."""

    # IRPEvent method parity checklist:
    # [ ] get_base_event                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_super_event                [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_base_event                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_super_event                [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_classifier methods (covered by rp_classifier checklist)
    # [inherited] irp_interface_item methods (covered by rp_interface_item checklist)
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_unit methods (covered by rp_unit checklist)
    # No deprecated IRPEvent methods.

    def get_base_event(self) -> "IRPEvent":
        return cast("IRPEvent", self.wrap(self._get_method_or_property(self._com, "getBaseEvent", "baseEvent")))

    def get_super_event(self) -> "IRPEvent":
        return cast("IRPEvent", self.wrap(self._get_method_or_property(self._com, "getSuperEvent", "superEvent")))

    def set_base_event(self, base_event: "IRPEvent") -> None:
        self._set_method_or_property(self._com, "setBaseEvent", "baseEvent", base_event._com)

    def set_super_event(self, super_event: "IRPEvent") -> None:
        self._set_method_or_property(self._com, "setSuperEvent", "superEvent", super_event._com)


class IRPEventReception(IRPInterfaceItem):
    """Wraps ``IRPEventReception``."""

    # IRPEventReception method parity checklist:
    # [ ] get_event                     [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_event                     [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_classifier methods (covered by rp_classifier checklist)
    # [inherited] irp_interface_item methods (covered by rp_interface_item checklist)
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_unit methods (covered by rp_unit checklist)
    # No deprecated IRPEventReception methods.

    def get_event(self) -> "IRPEvent":
        return cast("IRPEvent", self.wrap(self._get_method_or_property(self._com, "getEvent", "event")))

    def set_event(self, p_val: "IRPEvent") -> None:
        self._set_method_or_property(self._com, "setEvent", "event", p_val._com)


class IRPExecutionOccurrence(IRPModelElement):
    """Wraps ``IRPExecutionOccurrence``."""

    # IRPExecutionOccurrence method parity checklist:
    # [ ] get_message                   [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPExecutionOccurrence methods.

    def get_message(self) -> "IRPMessage":
        return cast("IRPMessage", self.wrap(self._get_method_or_property(self._com, "getMessage", "message")))


class IRPGuard(IRPModelElement):
    """Wraps ``IRPGuard``."""

    # IRPGuard method parity checklist:
    # [ ] get_body                      [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_body                      [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPGuard methods.

    def get_body(self) -> str:
        return str(self._get_method_or_property(self._com, "getBody", "body"))

    def set_body(self, body: str) -> None:
        self._set_method_or_property(self._com, "setBody", "body", body)


class IRPInteractionOccurrence(IRPModelElement):
    """Wraps ``IRPInteractionOccurrence``."""

    # IRPInteractionOccurrence method parity checklist:
    # [ ] get_message_points             [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_reference_sequence_diagram  [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_reference_sequence_diagram  [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPInteractionOccurrence methods.

    def get_message_points(self) -> "IRPCollection":
        return IRPCollection(self._get_method_or_property(self._com, "getMessagePoints", "messagePoints"))

    def get_reference_sequence_diagram(self) -> "IRPSequenceDiagram":
        return cast("IRPSequenceDiagram", self.wrap(self._get_method_or_property(self._com, "getReferenceSequenceDiagram", "referenceSequenceDiagram")))

    def set_reference_sequence_diagram(self, reference_sequence_diagram: "IRPSequenceDiagram") -> None:
        self._set_method_or_property(self._com, "setReferenceSequenceDiagram", "referenceSequenceDiagram", reference_sequence_diagram._com)


class IRPInteractionOperand(IRPCollaboration):
    """Wraps ``IRPInteractionOperand``: represents interaction operands in Rhapsody models."""

    # IRPInteractionOperand method parity checklist:
    # [ ] get_contained_messages         [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_interaction_constraint     [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_interaction_constraint     [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_collaboration methods (covered by rp_collaboration checklist)
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPInteractionOperand methods.

    def get_contained_messages(self) -> "IRPCollection":
        return IRPCollection(self._get_method_or_property(self._com, "getContainedMessages", "containedMessages"))

    def get_interaction_constraint(self) -> str:
        return str(self._get_method_or_property(self._com, "getInteractionConstraint", "interactionConstraint"))

    def set_interaction_constraint(self, interaction_constraint: str) -> None:
        self._set_method_or_property(self._com, "setInteractionConstraint", "interactionConstraint", interaction_constraint)


class IRPInteractionOperator(IRPModelElement):
    """Wraps ``IRPInteractionOperator``."""

    # IRPInteractionOperator method parity checklist:
    # [ ] get_interaction_operands       [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_interaction_type           [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_interaction_type           [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPInteractionOperator methods.

    def get_interaction_operands(self) -> "IRPCollection":
        return IRPCollection(self._get_method_or_property(self._com, "getInteractionOperands", "interactionOperands"))

    def get_interaction_type(self) -> str:
        return str(self._get_method_or_property(self._com, "getInteractionType", "interactionType"))

    def set_interaction_type(self, interaction_type: str) -> None:
        self._set_method_or_property(self._com, "setInteractionType", "interactionType", interaction_type)


class IRPMessage(IRPModelElement):
    """Wraps ``IRPMessage``."""

    # IRPMessage method parity checklist:
    # [ ] add_source_execution_occurrence [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] add_target_execution_occurrence [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_actual_parameter_list       [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_communication_connection   [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_condition                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_duration_constraint        [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_duration_observation       [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_flow_port                  [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_formal_interface_item       [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_formal_type                [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_invariant                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_message_type               [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_port                      [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_return_value               [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_sequence_number            [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_signature                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_source                    [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_source_execution_occurrence [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_target                    [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_target_execution_occurrence [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_time_constraint            [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_time_observation           [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_timer_value                [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] reroute                      [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_actual_parameter_list       [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_duration_constraint        [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_duration_observation       [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_flow_port                  [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_formal_interface_item       [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_formal_type                [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_invariant                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_port                      [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_return_value               [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_time_constraint            [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_time_observation           [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_timer_value                [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPMessage methods.

    def add_source_execution_occurrence(self) -> "IRPExecutionOccurrence":
        return cast("IRPExecutionOccurrence", self.wrap(self.call_com(lambda: self._com.addSourceExecutionOccurrence())))

    def add_target_execution_occurrence(self) -> "IRPExecutionOccurrence":
        return cast("IRPExecutionOccurrence", self.wrap(self.call_com(lambda: self._com.addTargetExecutionOccurrence())))

    def get_actual_parameter_list(self) -> "IRPCollection":
        return IRPCollection(self._get_method_or_property(self._com, "getActualParameterList", "actualParameterList"))

    def get_communication_connection(self) -> "IRPAssociationRole":
        return cast("IRPAssociationRole", self.wrap(self._get_method_or_property(self._com, "getCommunicationConnection", "communicationConnection")))

    def get_condition(self) -> str:
        return str(self._get_method_or_property(self._com, "getCondition", "condition"))

    def get_duration_constraint(self) -> str:
        return str(self._get_method_or_property(self._com, "getDurationConstraint", "durationConstraint"))

    def get_duration_observation(self) -> str:
        return str(self._get_method_or_property(self._com, "getDurationObservation", "durationObservation"))

    def get_flow_port(self) -> "IRPSysMLPort":
        return cast("IRPSysMLPort", self.wrap(self._get_method_or_property(self._com, "getFlowPort", "flowPort")))

    def get_formal_interface_item(self) -> "IRPInterfaceItem":
        return cast("IRPInterfaceItem", self.wrap(self._get_method_or_property(self._com, "getFormalInterfaceItem", "formalInterfaceItem")))

    def get_formal_type(self) -> "Optional[IRPModelElement]":
        return self.wrap(self._get_method_or_property(self._com, "getFormalType", "formalType"))

    def get_invariant(self) -> str:
        return str(self._get_method_or_property(self._com, "getInvariant", "invariant"))

    def get_message_type(self) -> str:
        return str(self._get_method_or_property(self._com, "getMessageType", "messageType"))

    def get_port(self) -> "IRPPort":
        return cast("IRPPort", self.wrap(self._get_method_or_property(self._com, "getPort", "port")))

    def get_return_value(self) -> str:
        return str(self._get_method_or_property(self._com, "getReturnValue", "returnValue"))

    def get_sequence_number(self) -> str:
        return str(self._get_method_or_property(self._com, "getSequenceNumber", "sequenceNumber"))

    def get_signature(self) -> str:
        return str(self._get_method_or_property(self._com, "getSignature", "signature"))

    def get_source(self) -> "IRPClassifierRole":
        return cast("IRPClassifierRole", self.wrap(self._get_method_or_property(self._com, "getSource", "source")))

    def get_source_execution_occurrence(self) -> "IRPExecutionOccurrence":
        return cast("IRPExecutionOccurrence", self.wrap(self._get_method_or_property(self._com, "getSourceExecutionOccurrence", "sourceExecutionOccurrence")))

    def get_target(self) -> "IRPClassifierRole":
        return cast("IRPClassifierRole", self.wrap(self._get_method_or_property(self._com, "getTarget", "target")))

    def get_target_execution_occurrence(self) -> "IRPExecutionOccurrence":
        return cast("IRPExecutionOccurrence", self.wrap(self._get_method_or_property(self._com, "getTargetExecutionOccurrence", "targetExecutionOccurrence")))

    def get_time_constraint(self) -> str:
        return str(self._get_method_or_property(self._com, "getTimeConstraint", "timeConstraint"))

    def get_time_observation(self) -> str:
        return str(self._get_method_or_property(self._com, "getTimeObservation", "timeObservation"))

    def get_timer_value(self) -> str:
        return str(self._get_method_or_property(self._com, "getTimerValue", "timerValue"))

    def reroute(self) -> None:
        self.call_com(lambda: self._com.reroute())

    def set_actual_parameter_list(self, p_val: "IRPCollection") -> None:
        self.call_com(lambda: self._com.setActualParameterList(p_val._com))

    def set_duration_constraint(self, duration_constraint: str) -> None:
        self._set_method_or_property(self._com, "setDurationConstraint", "durationConstraint", duration_constraint)

    def set_duration_observation(self, duration_observation: str) -> None:
        self._set_method_or_property(self._com, "setDurationObservation", "durationObservation", duration_observation)

    def set_flow_port(self, flow_port: "IRPSysMLPort") -> None:
        self._set_method_or_property(self._com, "setFlowPort", "flowPort", flow_port._com)

    def set_formal_interface_item(self, new_val: "IRPInterfaceItem") -> None:
        self._set_method_or_property(self._com, "setFormalInterfaceItem", "formalInterfaceItem", new_val._com)

    def set_formal_type(self, formal_type: "IRPModelElement") -> None:
        self._set_method_or_property(self._com, "setFormalType", "formalType", formal_type._com)

    def set_invariant(self, invariant: str) -> None:
        self._set_method_or_property(self._com, "setInvariant", "invariant", invariant)

    def set_port(self, port: "IRPPort") -> None:
        self._set_method_or_property(self._com, "setPort", "port", port._com)

    def set_return_value(self, return_value: str) -> None:
        self._set_method_or_property(self._com, "setReturnValue", "returnValue", return_value)

    def set_time_constraint(self, time_constraint: str) -> None:
        self._set_method_or_property(self._com, "setTimeConstraint", "timeConstraint", time_constraint)

    def set_time_observation(self, time_observation: str) -> None:
        self._set_method_or_property(self._com, "setTimeObservation", "timeObservation", time_observation)

    def set_timer_value(self, timer_value: str) -> None:
        self._set_method_or_property(self._com, "setTimerValue", "timerValue", timer_value)


class IRPTransition(IRPModelElement):
    """Wraps ``IRPTransition``: represents transitions in a statechart."""

    # IRPTransition method parity checklist:
    # [ ] get_inherits_from              [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_is_overridden              [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_its_action                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_its_guard                  [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_its_label                  [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_its_source                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_its_statechart             [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_its_target                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_its_trigger                [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_of_state                   [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] is_default_transition          [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] is_static_reaction             [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] its_compound_source            [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] override_inheritance          [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] reset_label_inheritance        [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_its_action                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_its_guard                  [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_its_label                  [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_its_source                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_its_statechart             [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_its_target                 [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_its_trigger                [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] unoverride_inheritance        [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPTransition methods.

    def get_inherits_from(self) -> "IRPTransition":
        return cast("IRPTransition", self.wrap(self._get_method_or_property(self._com, "getInheritsFrom", "inheritsFrom")))

    def get_is_overridden(self) -> int:
        return int(self._get_method_or_property(self._com, "getIsOverridden", "isOverridden"))

    def get_its_action(self) -> "IRPAction":
        return cast("IRPAction", self.wrap(self._get_method_or_property(self._com, "getItsAction", "itsAction")))

    def get_its_guard(self) -> "IRPGuard":
        return cast("IRPGuard", self.wrap(self._get_method_or_property(self._com, "getItsGuard", "itsGuard")))

    def get_its_label(self) -> str:
        return str(self._get_method_or_property(self._com, "getItsLabel", "itsLabel"))

    def get_its_source(self) -> "IRPStateVertex":
        return cast("IRPStateVertex", self.wrap(self._get_method_or_property(self._com, "getItsSource", "itsSource")))

    def get_its_statechart(self) -> "IRPStatechart":
        return cast("IRPStatechart", self.wrap(self._get_method_or_property(self._com, "getItsStatechart", "itsStatechart")))

    def get_its_target(self) -> "IRPStateVertex":
        return cast("IRPStateVertex", self.wrap(self._get_method_or_property(self._com, "getItsTarget", "itsTarget")))

    def get_its_trigger(self) -> "IRPTrigger":
        return cast("IRPTrigger", self.wrap(self._get_method_or_property(self._com, "getItsTrigger", "itsTrigger")))

    def get_of_state(self) -> "IRPState":
        return cast("IRPState", self.wrap(self._get_method_or_property(self._com, "getOfState", "ofState")))

    def is_default_transition(self) -> int:
        return int(self.call_com(lambda: self._com.isDefaultTransition()))

    def is_static_reaction(self) -> int:
        return int(self.call_com(lambda: self._com.isStaticReaction()))

    def its_compound_source(self) -> "IRPCollection":
        return IRPCollection(self.call_com(lambda: self._com.itsCompoundSource()))

    def override_inheritance(self) -> None:
        self.call_com(lambda: self._com.overrideInheritance())

    def reset_label_inheritance(self) -> "IRPTransition":
        return cast("IRPTransition", self.wrap(self.call_com(lambda: self._com.resetLabelInheritance())))

    def set_its_action(self, action: str) -> "IRPAction":
        return cast("IRPAction", self.wrap(self.call_com(lambda: self._com.setItsAction(action))))

    def set_its_guard(self, guard: str) -> "IRPGuard":
        return cast("IRPGuard", self.wrap(self.call_com(lambda: self._com.setItsGuard(guard))))

    def set_its_label(self, trigger: str, guard: str, action: str) -> None:
        self.call_com(lambda: self._com.setItsLabel(trigger, guard, action))

    def set_its_source(self, its_source: "IRPStateVertex") -> None:
        self._set_method_or_property(self._com, "setItsSource", "itsSource", its_source._com)

    def set_its_statechart(self, its_statechart: "IRPStatechart") -> None:
        self._set_method_or_property(self._com, "setItsStatechart", "itsStatechart", its_statechart._com)

    def set_its_target(self, its_target: "IRPStateVertex") -> None:
        self._set_method_or_property(self._com, "setItsTarget", "itsTarget", its_target._com)

    def set_its_trigger(self, trigger: str) -> "IRPTrigger":
        return cast("IRPTrigger", self.wrap(self.call_com(lambda: self._com.setItsTrigger(trigger))))

    def unoverride_inheritance(self) -> None:
        self.call_com(lambda: self._com.unoverrideInheritance())


class IRPTrigger(IRPModelElement):
    """Wraps ``IRPTrigger``: represents the trigger of a transition in a statechart."""

    # IRPTrigger method parity checklist:
    # [ ] get_body                      [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] get_its_operation              [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] is_operation                  [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] is_timeout                    [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [ ] set_body                      [x] impl  [ ] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPTrigger methods.

    def get_body(self) -> str:
        return str(self._get_method_or_property(self._com, "getBody", "body"))

    def get_its_operation(self) -> "IRPInterfaceItem":
        return cast("IRPInterfaceItem", self.wrap(self._get_method_or_property(self._com, "getItsOperation", "itsOperation")))

    def is_operation(self) -> int:
        return int(self.call_com(lambda: self._com.isOperation()))

    def is_timeout(self) -> int:
        return int(self.call_com(lambda: self._com.isTimeout()))

    def set_body(self, body: str) -> None:
        self._set_method_or_property(self._com, "setBody", "body", body)


class IRPDestructionEvent(IRPMessage):
    """Wraps ``IRPDestructionEvent``: represents destruction events in sequence diagrams."""

    # IRPDestructionEvent method parity checklist:
    # [inherited] irp_message methods (covered by rp_message checklist)
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPDestructionEvent methods.

    pass


IRPModelElement.register_wrapper("Message", IRPMessage)
IRPModelElement.register_wrapper("Event", IRPEvent)
IRPModelElement.register_wrapper("Transition", IRPTransition)
IRPModelElement.register_wrapper("Trigger", IRPTrigger)
IRPModelElement.register_wrapper("Guard", IRPGuard)
IRPModelElement.register_wrapper("DestructionEvent", IRPDestructionEvent)
IRPModelElement.register_wrapper("ExecutionOccurrence", IRPExecutionOccurrence)
IRPModelElement.register_wrapper("EventReception", IRPEventReception)
IRPModelElement.register_wrapper("InteractionOccurrence", IRPInteractionOccurrence)
IRPModelElement.register_wrapper("InteractionOperand", IRPInteractionOperand)
IRPModelElement.register_wrapper("InteractionOperator", IRPInteractionOperator)
