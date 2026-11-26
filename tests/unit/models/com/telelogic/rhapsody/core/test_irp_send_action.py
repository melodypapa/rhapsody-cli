"""Tests for the IRPSendAction wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_action import IRPAction
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_send_action import IRPSendAction
from tests.unit.models.fakes import make_fake_collection, make_fake_element

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem


def test_is_registered_for_meta_class_send_action() -> None:
    fake = make_fake_element("SendAction", properties={"name": "SA1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPSendAction)
    assert isinstance(wrapped, IRPAction)
    assert wrapped.name == "SA1"


def test_add_argument_value_delegates() -> None:
    fake = make_fake_element("SendAction")
    IRPSendAction(fake).add_argument_value("value1", 1)
    fake.addArgumentValue.assert_called_once_with("value1", 1)


def test_arg_vals_returns_collection() -> None:
    fake = make_fake_element("SendAction", properties={"argVals": make_fake_collection(["arg1", "arg2"])})
    result = IRPSendAction(fake).arg_vals
    assert isinstance(result, IRPCollection)
    assert len(result) == 2


def test_event_wraps_result() -> None:
    event = make_fake_element("Event", properties={"name": "MyEvent"})
    fake = make_fake_element("SendAction", properties={"event": event})
    result = IRPSendAction(fake).event
    assert result is not None
    assert result.name == "MyEvent"


def test_event_setter() -> None:
    fake = make_fake_element("SendAction")
    event = make_fake_element("Event", properties={"name": "MyEvent"})
    IRPSendAction(fake).event = cast("IRPEvent", IRPModelElement.wrap(event))
    assert fake.event is event


def test_invoked_operation_wraps_result() -> None:
    op = make_fake_element("Operation", properties={"name": "myOp"})
    fake = make_fake_element("SendAction", properties={"invokedOperation": op})
    result = IRPSendAction(fake).invoked_operation
    assert result is not None
    assert result.name == "myOp"


def test_invoked_operation_setter() -> None:
    fake = make_fake_element("SendAction")
    op = make_fake_element("Operation", properties={"name": "myOp"})
    IRPSendAction(fake).invoked_operation = cast("IRPInterfaceItem", IRPModelElement.wrap(op))
    assert fake.invokedOperation is op


def test_target_wraps_result() -> None:
    target = make_fake_element("Class", properties={"name": "MyClass"})
    fake = make_fake_element("SendAction", properties={"target": target})
    result = IRPSendAction(fake).target
    assert result is not None
    assert result.name == "MyClass"


def test_target_setter() -> None:
    fake = make_fake_element("SendAction")
    target = make_fake_element("Class", properties={"name": "MyClass"})
    IRPSendAction(fake).target = cast(IRPModelElement, IRPModelElement.wrap(target))
    assert fake.target is target
