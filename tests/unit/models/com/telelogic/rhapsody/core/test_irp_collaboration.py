"""Fake-COM unit tests for the IRPCollaboration wrapper."""


from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPCollaboration, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_collaboration_is_registered() -> None:
    fake = make_fake_element("Collaboration", properties={"name": "C1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPCollaboration)


def test_activation_condition() -> None:
    fake = make_fake_element("Collaboration", properties={"activationCondition": "value"})
    assert IRPCollaboration(fake).activation_condition == "value"


def test_activation_mode() -> None:
    fake = make_fake_element("Collaboration", properties={"activationMode": 1})
    assert IRPCollaboration(fake).activation_mode == 1


def test_associations() -> None:
    fake = make_fake_element("Collaboration", properties={"associations": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPCollaboration(fake).associations) == 1


def test_classifier() -> None:
    fake = make_fake_element("Collaboration", properties={"classifier": make_fake_element("Unit", properties={"name": "R1"})})
    assert IRPCollaboration(fake).classifier.name == "R1"


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
    fake = make_fake_element("Collaboration", properties={"mode": 1})
    assert IRPCollaboration(fake).mode == 1


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
    name = "N1"
    fake.addClassifierRole.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_classifier_role(name)
    assert result.name == "R1"


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
    name = "N1"
    fake.addMessage.return_value = make_fake_element("Unit", properties={"name": "R1"})
    result = collab.add_message(name)
    assert result.name == "R1"


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


def test_generate_sequence() -> None:
    fake = make_fake_element("Collaboration")
    collab = IRPCollaboration(fake)
    fake.generateSequence.return_value = None
    collab.generate_sequence()
    fake.generateSequence.assert_called_once_with()


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
    assert result.name == "R1"
