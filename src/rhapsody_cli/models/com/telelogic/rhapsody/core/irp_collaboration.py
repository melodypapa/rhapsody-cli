"""Wraps ``com.telelogic.rhapsody.core.IRPCollaboration``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClassifierRole, IRPConditionMark
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPSequenceDiagram
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPInteractionOccurrence, IRPInteractionOperator, IRPMessage
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage


class IRPCollaboration(IRPUnit):
    """Wraps ``IRPCollaboration``: a collaboration that extends ``IRPUnit``."""

    # IRPCollaboration method parity checklist:
    # [ ] add_action_block  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_cancelled_timeout  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] add_classifier_role  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] add_classifier_role_by_name  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_classifier_role_for_instance  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_condition_mark  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_ctor  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_data_flow  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_destruction_event  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_dtor  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_duration_constraint  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_duration_observation  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_found_message  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_interaction_occurrence  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_interaction_operator  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_lost_message  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] add_message  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] add_reply_message  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_state_invariant  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_system_border  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_time_constraint  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_time_interval  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_time_observation  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_timeout  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] generate_sequence  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_activation_condition  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_activation_mode  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_activator  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_associations  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_classifier  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [wrong-interface] get_classifier_roles  - REMOVED; exists on IRPAssociationRole, not IRPCollaboration (use IRPAssociationRole instead)
    # [ ] get_concurrent_group  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_execution_occurrences  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_interaction_occurrences  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_interaction_operators  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_message_points  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_messages  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_mode  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_predecessor  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_successor  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [inherited] irp_unit / irp_model_element methods (covered by rp_unit / rp_model_element checklists)
    # No deprecated IRPCollaboration methods.

    def add_action_block(self, name: str) -> IRPUnit:
        """Adds an action block to the collaboration.

        Args:
            name: The name of the action block.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addActionBlock(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addActionBlock(name))))

    def add_cancelled_timeout(self, name: str) -> IRPUnit:
        """Adds a cancelled timeout to the collaboration.

        Args:
            name: The name of the cancelled timeout.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addCancelledTimeout(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addCancelledTimeout(name))))

    def add_classifier_role(self, name: str, classifier: IRPClassifier) -> IRPClassifierRole:
        """Adds an instance line based on the specified classifier.

        Args:
            name: The name to use for the new instance line.
            classifier: The class on which the instance line is based.

        Returns:
            The new classifier role.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addClassifierRole(java.lang.String newVal, com.telelogic.rhapsody.core.IRPClassifier cls)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier_role import IRPClassifierRole

        return IRPClassifierRole(self.call_com(lambda: self._com.addClassifierRole(name, classifier._com)))

    def add_classifier_role_by_name(self, name: str) -> IRPClassifierRole:
        """Adds a classifier role by name to the collaboration.

        Args:
            name: The name of the classifier role.

        Returns:
            The wrapped ``IRPClassifierRole`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addClassifierRoleByName(java.lang.String name)
        """
        return cast("IRPClassifierRole", self.wrap(self.call_com(lambda: self._com.addClassifierRoleByName(name))))

    def add_classifier_role_for_instance(self, instance: IRPUnit) -> IRPClassifierRole:
        """Adds a classifier role for an instance to the collaboration.

        Args:
            instance: The instance to create a classifier role for.

        Returns:
            The wrapped ``IRPClassifierRole`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addClassifierRoleForInstance(IRPInstance instance)
        """
        return cast("IRPClassifierRole", self.wrap(self.call_com(lambda: self._com.addClassifierRoleForInstance(instance._com))))

    def add_condition_mark(self, name: str) -> IRPConditionMark:
        """Adds a condition mark to the collaboration.

        Args:
            name: The name of the condition mark.

        Returns:
            The wrapped ``IRPConditionMark`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addConditionMark(java.lang.String name)
        """
        return cast("IRPConditionMark", self.wrap(self.call_com(lambda: self._com.addConditionMark(name))))

    def add_ctor(self, name: str) -> IRPUnit:
        """Adds a constructor to the collaboration.

        Args:
            name: The name of the constructor.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addCtor(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addCtor(name))))

    def add_data_flow(self, name: str) -> IRPUnit:
        """Adds a data flow to the collaboration.

        Args:
            name: The name of the data flow.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addDataFlow(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addDataFlow(name))))

    def add_destruction_event(self, name: str) -> IRPUnit:
        """Adds a destruction event to the collaboration.

        Args:
            name: The name of the destruction event.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addDestructionEvent(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addDestructionEvent(name))))

    def add_dtor(self, name: str) -> IRPUnit:
        """Adds a destructor to the collaboration.

        Args:
            name: The name of the destructor.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addDtor(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addDtor(name))))

    def add_duration_constraint(self, name: str) -> IRPUnit:
        """Adds a duration constraint to the collaboration.

        Args:
            name: The name of the duration constraint.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addDurationConstraint(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addDurationConstraint(name))))

    def add_duration_observation(self, name: str) -> IRPUnit:
        """Adds a duration observation to the collaboration.

        Args:
            name: The name of the duration observation.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addDurationObservation(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addDurationObservation(name))))

    def add_found_message(self, name: str) -> IRPMessage:
        """Adds a found message to the collaboration.

        Args:
            name: The name of the found message.

        Returns:
            The wrapped ``IRPMessage`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addFoundMessage(java.lang.String name)
        """
        return cast("IRPMessage", self.wrap(self.call_com(lambda: self._com.addFoundMessage(name))))

    def add_interaction_occurrence(self, name: str) -> IRPInteractionOccurrence:
        """Adds an interaction occurrence to the collaboration.

        Args:
            name: The name of the interaction occurrence.

        Returns:
            The wrapped ``IRPInteractionOccurrence`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addInteractionOccurrence(java.lang.String name)
        """
        return cast("IRPInteractionOccurrence", self.wrap(self.call_com(lambda: self._com.addInteractionOccurrence(name))))

    def add_interaction_operator(self, name: str) -> IRPInteractionOperator:
        """Adds an interaction operator to the collaboration.

        Args:
            name: The name of the interaction operator.

        Returns:
            The wrapped ``IRPInteractionOperator`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addInteractionOperator(java.lang.String name)
        """
        return cast("IRPInteractionOperator", self.wrap(self.call_com(lambda: self._com.addInteractionOperator(name))))

    def add_lost_message(self, name: str) -> IRPMessage:
        """Adds a lost message to the collaboration.

        Args:
            name: The name of the lost message.

        Returns:
            The wrapped ``IRPMessage`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addLostMessage(java.lang.String name)
        """
        return cast("IRPMessage", self.wrap(self.call_com(lambda: self._com.addLostMessage(name))))

    def add_message(self, inter_item: IRPInterfaceItem, actual_param_list: str, sender: IRPClassifierRole, receiver: IRPClassifierRole) -> IRPMessage:
        """Adds a message between the specified sequence-diagram roles.

        Args:
            inter_item: The operation call represented by the message.
            actual_param_list: Arguments to pass to the operation, or an empty
                string when the operation has no arguments.
            sender: The instance line sending the message.
            receiver: The instance line receiving the message.

        Returns:
            The message added to the diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addMessage(
                com.telelogic.rhapsody.core.IRPInterfaceItem interItem, java.lang.String actualParamList,
                com.telelogic.rhapsody.core.IRPClassifierRole sender,
                com.telelogic.rhapsody.core.IRPClassifierRole receiver)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPMessage

        return IRPMessage(self.call_com(lambda: self._com.addMessage(inter_item._com, actual_param_list, sender._com, receiver._com)))

    def add_reply_message(self, name: str) -> IRPMessage:
        """Adds a reply message to the collaboration.

        Args:
            name: The name of the reply message.

        Returns:
            The wrapped ``IRPMessage`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addReplyMessage(java.lang.String name)
        """
        return cast("IRPMessage", self.wrap(self.call_com(lambda: self._com.addReplyMessage(name))))

    def add_state_invariant(self, name: str) -> IRPUnit:
        """Adds a state invariant to the collaboration.

        Args:
            name: The name of the state invariant.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addStateInvariant(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addStateInvariant(name))))

    def add_system_border(self, name: str) -> IRPUnit:
        """Adds a system border to the collaboration.

        Args:
            name: The name of the system border.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addSystemBorder(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addSystemBorder(name))))

    def add_time_constraint(self, name: str) -> IRPUnit:
        """Adds a time constraint to the collaboration.

        Args:
            name: The name of the time constraint.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addTimeConstraint(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addTimeConstraint(name))))

    def add_time_interval(self, name: str) -> IRPUnit:
        """Adds a time interval to the collaboration.

        Args:
            name: The name of the time interval.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addTimeInterval(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addTimeInterval(name))))

    def add_time_observation(self, name: str) -> IRPUnit:
        """Adds a time observation to the collaboration.

        Args:
            name: The name of the time observation.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addTimeObservation(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addTimeObservation(name))))

    def add_timeout(self, name: str) -> IRPUnit:
        """Adds a timeout to the collaboration.

        Args:
            name: The name of the timeout.

        Returns:
            The wrapped ``IRPUnit`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::addTimeout(java.lang.String name)
        """
        return cast("IRPUnit", self.wrap(self.call_com(lambda: self._com.addTimeout(name))))

    def generate_sequence(self, name: str, owner: IRPPackage) -> IRPSequenceDiagram:
        """Generates a sequence diagram from the collaboration content.

        Args:
            name: The name to give to the generated diagram.
            owner: The package to which the generated diagram belongs.

        Returns:
            The generated sequence diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::generateSequence(java.lang.String newVal, com.telelogic.rhapsody.core.IRPPackage owner)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPSequenceDiagram

        return IRPSequenceDiagram(self.call_com(lambda: self._com.generateSequence(name, owner._com)))

    @property
    def activation_condition(self) -> str:
        """COM-backed ``activationCondition`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::get_activation_condition()
        """
        return str(self.get_com_property(self._com, "activationCondition"))

    @property
    def activation_mode(self) -> str:
        """Returns the collaboration's activation mode.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::getActivationMode()
        """
        return str(self.get_com_property(self._com, "activationMode"))

    def get_activator(self) -> IRPUnit | None:
        """Returns the activator of the collaboration.

        Returns:
            The wrapped ``IRPUnit`` activator if set, ``None`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::getActivator()
        """
        result = self.call_com(lambda: self._com.getActivator())
        if result is None:
            return None
        return cast("IRPUnit", self.wrap(result))

    @property
    def associations(self) -> IRPCollection:
        """COM-backed ``associations`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::get_associations()
        """
        return IRPCollection(self.get_com_property(self._com, "associations"))

    @property
    def classifier(self) -> IRPCollection:
        """Returns the instance lines in the sequence diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::getClassifier()
        """
        return IRPCollection(self.get_com_property(self._com, "classifier"))

    def get_concurrent_group(self) -> int:
        """Returns the concurrent group of the collaboration.

        Returns:
            The concurrent group as an integer.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::getConcurrentGroup()
        """
        return int(self.call_com(lambda: self._com.getConcurrentGroup()))

    @property
    def execution_occurrences(self) -> IRPCollection:
        """COM-backed ``executionOccurrences`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::get_execution_occurrences()
        """
        return IRPCollection(self.get_com_property(self._com, "executionOccurrences"))

    @property
    def interaction_occurrences(self) -> IRPCollection:
        """COM-backed ``interactionOccurrences`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::get_interaction_occurrences()
        """
        return IRPCollection(self.get_com_property(self._com, "interactionOccurrences"))

    @property
    def interaction_operators(self) -> IRPCollection:
        """COM-backed ``interactionOperators`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::get_interaction_operators()
        """
        return IRPCollection(self.get_com_property(self._com, "interactionOperators"))

    @property
    def message_points(self) -> IRPCollection:
        """COM-backed ``messagePoints`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::get_message_points()
        """
        return IRPCollection(self.get_com_property(self._com, "messagePoints"))

    @property
    def messages(self) -> IRPCollection:
        """COM-backed ``messages`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::get_messages()
        """
        return IRPCollection(self.get_com_property(self._com, "messages"))

    @property
    def mode(self) -> str:
        """Returns the collaboration's mode.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::getMode()
        """
        return str(self.get_com_property(self._com, "mode"))

    def get_predecessor(self) -> IRPUnit | None:
        """Returns the predecessor of the collaboration.

        Returns:
            The wrapped ``IRPUnit`` predecessor if set, ``None`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::getPredecessor()
        """
        result = self.call_com(lambda: self._com.getPredecessor())
        if result is None:
            return None
        return cast("IRPUnit", self.wrap(result))

    def get_successor(self) -> IRPUnit | None:
        """Returns the successor of the collaboration.

        Returns:
            The wrapped ``IRPUnit`` successor if set, ``None`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPCollaboration::getSuccessor()
        """
        result = self.call_com(lambda: self._com.getSuccessor())
        if result is None:
            return None
        return cast("IRPUnit", self.wrap(result))


IRPModelElement.register_wrapper("Collaboration", IRPCollaboration)
