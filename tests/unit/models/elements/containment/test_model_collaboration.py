"""Tests for rhapsody_cli.models.elements.containment.RPCollaboration."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.containment import RPCollaboration
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_collaboration_is_a_unit() -> None:
    fake = make_fake_element("Collaboration", properties={"name": "Collab1"})
    collab = RPCollaboration(fake)

    assert isinstance(collab, IRPUnit)
    assert collab.name == "Collab1"


def test_collaboration_is_registered_for_meta_class_collaboration() -> None:
    fake = make_fake_element("Collaboration", properties={"name": "Collab1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPCollaboration)


# Tests for methods from Task 12


def test_collaboration_add_classifier_role_delegates_and_wraps() -> None:
    fake = make_fake_element("Collaboration")
    cr = make_fake_element("ClassifierRole", properties={"name": "cr1"})
    fake.addClassifierRole.return_value = cr
    collab = RPCollaboration(fake)

    result = collab.add_classifier_role("cr1")

    fake.addClassifierRole.assert_called_once_with("cr1")
    assert result.name == "cr1"


def test_collaboration_add_message_delegates_and_wraps() -> None:
    fake = make_fake_element("Collaboration")
    msg = make_fake_element("Message", properties={"name": "msg1"})
    fake.addMessage.return_value = msg
    collab = RPCollaboration(fake)

    result = collab.add_message("msg1")

    fake.addMessage.assert_called_once_with("msg1")
    assert result.name == "msg1"


def test_collaboration_get_messages_returns_collection() -> None:
    fake = make_fake_element("Collaboration")
    msg = make_fake_element("Message", properties={"name": "msg1"})
    fake.getMessages.return_value = make_fake_collection([msg])
    collab = RPCollaboration(fake)

    result = collab.get_messages()
    assert isinstance(result, IRPCollection)


def test_collaboration_generate_sequence_delegates() -> None:
    fake = make_fake_element("Collaboration")
    collab = RPCollaboration(fake)

    collab.generate_sequence()

    fake.generateSequence.assert_called_once_with()


def test_collaboration_get_activation_condition_returns_str() -> None:
    fake = make_fake_element("Collaboration")
    fake.getActivationCondition.return_value = "some_condition"
    collab = RPCollaboration(fake)

    result = collab.get_activation_condition()
    assert result == "some_condition"
