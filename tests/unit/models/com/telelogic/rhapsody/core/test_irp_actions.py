"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions import (
    IRPAcceptEventAction,
    IRPAcceptTimeEvent,
    IRPActionBlock,
    IRPCallOperation,
    IRPContextSpecification,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation


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


class TestRPCallOperation:
    def test_is_state(self) -> None:
        fake = make_fake_element("CallOperation", properties={"name": "CO1"})
        co = IRPCallOperation(fake)
        assert isinstance(co, IRPModelElement)
        assert co.name == "CO1"

    def test_get_operation_wraps_result(self) -> None:
        fake = make_fake_element("CallOperation")
        op = make_fake_element("Operation", properties={"name": "myOp"})
        fake.getOperation.return_value = op
        co = IRPCallOperation(fake)
        result = co.get_operation()
        assert result.name == "myOp"

    def test_get_target_wraps_result(self) -> None:
        fake = make_fake_element("CallOperation")
        target = make_fake_element("Relation", properties={"name": "myTarget"})
        fake.getTarget.return_value = target
        co = IRPCallOperation(fake)
        result = co.get_target()
        assert result.name == "myTarget"

    def test_set_operation_delegates(self) -> None:
        fake = make_fake_element("CallOperation")
        op = make_fake_element("Operation", properties={"name": "myOp"})
        co = IRPCallOperation(fake)
        co.set_operation(cast("IRPInterfaceItem", IRPModelElement.wrap(op)))
        fake.setOperation.assert_called_once_with(op)

    def test_set_target_delegates(self) -> None:
        fake = make_fake_element("CallOperation")
        target = make_fake_element("Relation", properties={"name": "myTarget"})
        co = IRPCallOperation(fake)
        co.set_target(cast("IRPRelation", IRPModelElement.wrap(target)))
        fake.setTarget.assert_called_once_with(target)

    def test_is_registered(self) -> None:
        fake = make_fake_element("CallOperation", properties={"name": "CO1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPCallOperation)


class TestRPContextSpecification:
    def test_is_value_specification(self) -> None:
        fake = make_fake_element("ContextSpecification", properties={"name": "CS1"})
        cs = IRPContextSpecification(fake)
        assert isinstance(cs, IRPModelElement)
        assert cs.name == "CS1"

    def test_get_multiplicities_returns_collection(self) -> None:
        fake = make_fake_element("ContextSpecification")
        fake.getMultiplicities.return_value = make_fake_collection(["1", "2"])
        cs = IRPContextSpecification(fake)
        result = cs.get_multiplicities()
        assert isinstance(result, IRPCollection)
        assert len(result) == 2

    def test_get_value_returns_collection(self) -> None:
        fake = make_fake_element("ContextSpecification")
        fake.getValue.return_value = make_fake_collection(["pkg", "cls"])
        cs = IRPContextSpecification(fake)
        result = cs.get_value()
        assert isinstance(result, IRPCollection)
        assert len(result) == 2

    def test_set_multiplicities_delegates(self) -> None:
        fake = make_fake_element("ContextSpecification")
        coll = make_fake_collection(["1", "2"])
        cs = IRPContextSpecification(fake)
        cs.set_multiplicities(IRPCollection(coll))
        fake.setMultiplicities.assert_called_once_with(coll)

    def test_set_value_delegates(self) -> None:
        fake = make_fake_element("ContextSpecification")
        coll = make_fake_collection(["pkg", "cls"])
        cs = IRPContextSpecification(fake)
        cs.set_value(IRPCollection(coll))
        fake.setValue.assert_called_once_with(coll)

    def test_is_registered(self) -> None:
        fake = make_fake_element("ContextSpecification", properties={"name": "CS1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPContextSpecification)
