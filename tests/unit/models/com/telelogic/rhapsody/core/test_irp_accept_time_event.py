"""Tests for the IRPAcceptTimeEvent wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_accept_time_event import IRPAcceptTimeEvent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from tests.unit.models.fakes import make_fake_element


def test_is_registered_for_meta_class_accept_time_event() -> None:
    fake = make_fake_element("AcceptTimeEvent", properties={"name": "ATE1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPAcceptTimeEvent)
    assert isinstance(wrapped, IRPState)
    assert wrapped.name == "ATE1"


def test_duration_time_returns_string() -> None:
    fake = make_fake_element("AcceptTimeEvent", properties={"durationTime": "5s"})
    assert IRPAcceptTimeEvent(fake).duration_time == "5s"


def test_duration_time_setter() -> None:
    fake = make_fake_element("AcceptTimeEvent")
    IRPAcceptTimeEvent(fake).duration_time = "10s"
    assert fake.durationTime == "10s"
