"""Fake-COM unit tests for the IRPAcceptEventAction wrapper."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_accept_event_action import IRPAcceptEventAction
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from tests.unit.models.fakes import make_fake_element


def test_accept_event_action_inherits_state_and_registers_by_meta_class() -> None:
    fake = make_fake_element("AcceptEventAction", properties={"name": "AEA1"})

    action = IRPAcceptEventAction(fake)
    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(action, IRPState)
    assert action.name == "AEA1"
    assert isinstance(wrapped, IRPAcceptEventAction)


def test_event_property_reads_the_catalog_property_and_wraps_event() -> None:
    event_com = make_fake_element("Event", properties={"name": "AcceptedEvent"})
    action_com = make_fake_element("AcceptEventAction", properties={"event": event_com})

    event = IRPAcceptEventAction(action_com).event

    assert isinstance(event, IRPEvent)
    assert event._com is event_com
    action_com.getEvent.assert_not_called()


def test_event_property_setter_writes_the_catalog_property() -> None:
    action_com = make_fake_element("AcceptEventAction")
    event_com = make_fake_element("Event", properties={"name": "AcceptedEvent"})

    IRPAcceptEventAction(action_com).event = IRPEvent(event_com)

    assert action_com.event is event_com
    action_com.setEvent.assert_not_called()
