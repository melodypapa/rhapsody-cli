"""Fake-COM unit tests for the IRPCollaboration wrapper."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPCollaboration, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier_role import IRPClassifierRole
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPSequenceDiagram
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPMessage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_collaboration_is_registered() -> None:
    fake = make_fake_element("Collaboration", properties={"name": "C1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPCollaboration)


def test_activation_condition() -> None:
    fake = make_fake_element("Collaboration", properties={"activationCondition": "value"})
    assert IRPCollaboration(fake).activation_condition == "value"


def test_activation_mode() -> None:
    fake = make_fake_element("Collaboration", properties={"activationMode": "Invariant"})
    assert IRPCollaboration(fake).activation_mode == "Invariant"


def test_associations() -> None:
    fake = make_fake_element("Collaboration", properties={"associations": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPCollaboration(fake).associations) == 1


def test_classifier() -> None:
    role = make_fake_element("ClassifierRole", properties={"name": "R1"})
    classifier_com = make_fake_collection([role])
    fake = make_fake_element("Collaboration", properties={"classifier": classifier_com})

    classifier = IRPCollaboration(fake).classifier

    assert isinstance(classifier, IRPCollection)
    assert classifier._com is classifier_com


def test_execution_occurrences() -> None:
    fake = make_fake_element("Collaboration", properties={"executionOccurrences": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPCollaboration(fake).execution_occurrences) == 1


def test_interaction_occurrences() -> None:
    fake = make_fake_element("Collaboration", properties={"interactionOccurrences": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPCollaboration(fake).interaction_occurrences) == 1


def test_interaction_operators() -> None:
    fake = make_fake_element("Collaboration", properties={"interactionOperators": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPCollaboration(fake).interaction_operators) == 1


def test_message_points() -> None:
    fake = make_fake_element("Collaboration", properties={"messagePoints": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPCollaboration(fake).message_points) == 1


def test_messages() -> None:
    fake = make_fake_element("Collaboration", properties={"messages": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPCollaboration(fake).messages) == 1


def test_mode() -> None:
    fake = make_fake_element("Collaboration", properties={"mode": "EXISTENTIAL"})
    assert IRPCollaboration(fake).mode == "EXISTENTIAL"


def test_add_action_block() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addActionBlock.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_action_block(name)
    assert result.name == "R1"


def test_add_cancelled_timeout() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addCancelledTimeout.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_cancelled_timeout(name)
    assert result.name == "R1"


def test_add_classifier_role() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    classifier = IRPClassifier(make_fake_element("Class", properties={"name": "C1"}))
    role_com = make_fake_element("ClassifierRole", properties={"name": "R1"})
    fake.addClassifierRole.return_value = role_com

    result = collab.add_classifier_role("R1", classifier)

    fake.addClassifierRole.assert_called_once_with("R1", classifier._com)
    assert isinstance(result, IRPClassifierRole)
    assert result._com is role_com


def test_add_classifier_role_by_name() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addClassifierRoleByName.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_classifier_role_by_name(name)
    assert result.name == "R1"


def test_add_classifier_role_for_instance() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    instance = IRPUnit(make_fake_element("Unit"))
    fake.addClassifierRoleForInstance.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_classifier_role_for_instance(instance)
    assert result.name == "R1"


def test_add_condition_mark() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addConditionMark.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_condition_mark(name)
    assert result.name == "R1"


def test_add_ctor() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addCtor.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_ctor(name)
    assert result.name == "R1"


def test_add_data_flow() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addDataFlow.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_data_flow(name)
    assert result.name == "R1"


def test_add_destruction_event() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addDestructionEvent.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_destruction_event(name)
    assert result.name == "R1"


def test_add_dtor() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addDtor.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_dtor(name)
    assert result.name == "R1"


def test_add_duration_constraint() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addDurationConstraint.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_duration_constraint(name)
    assert result.name == "R1"


def test_add_duration_observation() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addDurationObservation.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_duration_observation(name)
    assert result.name == "R1"


def test_add_found_message() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addFoundMessage.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_found_message(name)
    assert result.name == "R1"


def test_add_interaction_occurrence() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addInteractionOccurrence.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_interaction_occurrence(name)
    assert result.name == "R1"


def test_add_interaction_operator() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addInteractionOperator.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_interaction_operator(name)
    assert result.name == "R1"


def test_add_lost_message() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addLostMessage.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_lost_message(name)
    assert result.name == "R1"


def test_add_message() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    interface_item = IRPInterfaceItem(make_fake_element("Operation", properties={"name": "Call"}))
    sender = IRPClassifierRole(make_fake_element("ClassifierRole", properties={"name": "Sender"}))
    receiver = IRPClassifierRole(make_fake_element("ClassifierRole", properties={"name": "Receiver"}))
    message_com = make_fake_element("Message", properties={"name": "Message1"})
    fake.addMessage.return_value = message_com

    result = collab.add_message(interface_item, "", sender, receiver)

    fake.addMessage.assert_called_once_with(interface_item._com, "", sender._com, receiver._com)
    assert isinstance(result, IRPMessage)
    assert result._com is message_com


def test_add_reply_message() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addReplyMessage.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_reply_message(name)
    assert result.name == "R1"


def test_add_state_invariant() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addStateInvariant.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_state_invariant(name)
    assert result.name == "R1"


def test_add_system_border() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addSystemBorder.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_system_border(name)
    assert result.name == "R1"


def test_add_time_constraint() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addTimeConstraint.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_time_constraint(name)
    assert result.name == "R1"


def test_add_time_interval() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addTimeInterval.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_time_interval(name)
    assert result.name == "R1"


def test_add_time_observation() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addTimeObservation.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_time_observation(name)
    assert result.name == "R1"


def test_add_timeout() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    name = "N1"
    fake.addTimeout.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_timeout(name)
    assert result.name == "R1"


def test_generate_sequence_wraps_documented_result() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    package_com = make_fake_element("Package")
    package = IRPPackage(package_com)
    sequence_com = make_fake_element("SequenceDiagram", properties={"name": "GeneratedSequence"})
    fake.generateSequence.return_value = sequence_com

    sequence = collab.generate_sequence("GeneratedSequence", package)

    fake.generateSequence.assert_called_once_with("GeneratedSequence", package_com)
    assert isinstance(sequence, IRPSequenceDiagram)
    assert sequence._com is sequence_com


def test_get_activator_none() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    fake.getActivator.return_value = None
    assert collab.get_activator() is None


def test_get_activator_value() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    fake.getActivator.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.get_activator()
    assert result is not None
    assert result.name == "R1"


def test_get_concurrent_group() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    fake.getConcurrentGroup.return_value = 1
    assert collab.get_concurrent_group() == 1


def test_get_predecessor_none() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    fake.getPredecessor.return_value = None
    assert collab.get_predecessor() is None


def test_get_predecessor_value() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    fake.getPredecessor.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.get_predecessor()
    assert result is not None
    assert result.name == "R1"


def test_get_successor_none() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    fake.getSuccessor.return_value = None
    assert collab.get_successor() is None


def test_get_successor_value() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    fake.getSuccessor.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.get_successor()
    assert result is not None
    assert result.name == "R1"
