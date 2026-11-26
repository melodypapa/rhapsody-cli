"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions import (
    IRPAcceptEventAction,
    IRPAcceptTimeEvent,
    IRPActionBlock,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent


class TestRPAcceptEventAction:
    def test_is_state(self) -> None:
        fake = make_fake_element("AcceptEventAction", properties={"name": "AEA1"})
        aea = IRPAcceptEventAction(fake)
        assert isinstance(aea, IRPModelElement)
        assert aea.name == "AEA1"

    def test_get_event_wraps_result(self) -> None:
        fake = make_fake_element("AcceptEventAction")
        event = make_fake_element("Event", properties={"name": "MyEvent"})
        fake.getEvent.return_value = event
        aea = IRPAcceptEventAction(fake)
        result = aea.get_event()
        assert result.name == "MyEvent"

    def test_set_event_delegates(self) -> None:
        fake = make_fake_element("AcceptEventAction")
        event = make_fake_element("Event", properties={"name": "MyEvent"})
        aea = IRPAcceptEventAction(fake)
        aea.set_event(cast("IRPEvent", IRPModelElement.wrap(event)))
        fake.setEvent.assert_called_once_with(event)

    def test_is_registered(self) -> None:
        fake = make_fake_element("AcceptEventAction", properties={"name": "AEA1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPAcceptEventAction)


class TestRPAcceptTimeEvent:
    def test_is_state(self) -> None:
        fake = make_fake_element("AcceptTimeEvent", properties={"name": "ATE1"})
        ate = IRPAcceptTimeEvent(fake)
        assert isinstance(ate, IRPModelElement)
        assert ate.name == "ATE1"

    def test_get_duration_time_returns_string(self) -> None:
        fake = make_fake_element("AcceptTimeEvent", getDurationTime="5s")
        ate = IRPAcceptTimeEvent(fake)
        assert ate.get_duration_time() == "5s"

    def test_set_duration_time_delegates(self) -> None:
        fake = make_fake_element("AcceptTimeEvent")
        ate = IRPAcceptTimeEvent(fake)
        ate.set_duration_time("10s")
        fake.setDurationTime.assert_called_once_with("10s")

    def test_is_registered(self) -> None:
        fake = make_fake_element("AcceptTimeEvent", properties={"name": "ATE1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPAcceptTimeEvent)


class TestRPActionBlock:
    def test_is_message(self) -> None:
        fake = make_fake_element("ActionBlock", properties={"name": "AB1"})
        ab = IRPActionBlock(fake)
        assert isinstance(ab, IRPModelElement)
        assert ab.name == "AB1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("ActionBlock", properties={"name": "AB1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPActionBlock)
