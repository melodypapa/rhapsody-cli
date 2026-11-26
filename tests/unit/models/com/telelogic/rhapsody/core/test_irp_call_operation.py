"""Tests for the IRPCallOperation wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_call_operation import IRPCallOperation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from tests.unit.models.fakes import make_fake_element

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation


def test_is_registered_for_meta_class_call_operation() -> None:
    fake = make_fake_element("CallOperation", properties={"name": "CO1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPCallOperation)
    assert isinstance(wrapped, IRPState)
    assert wrapped.name == "CO1"


def test_operation_wraps_result() -> None:
    op = make_fake_element("Operation", properties={"name": "myOp"})
    fake = make_fake_element("CallOperation", properties={"operation": op})
    result = IRPCallOperation(fake).operation
    assert result is not None
    assert result.name == "myOp"


def test_operation_setter() -> None:
    fake = make_fake_element("CallOperation")
    op = make_fake_element("Operation", properties={"name": "myOp"})
    IRPCallOperation(fake).operation = cast("IRPInterfaceItem", IRPModelElement.wrap(op))
    assert fake.operation is op


def test_target_wraps_result() -> None:
    target = make_fake_element("Relation", properties={"name": "myTarget"})
    fake = make_fake_element("CallOperation", properties={"target": target})
    result = IRPCallOperation(fake).target
    assert result is not None
    assert result.name == "myTarget"


def test_target_setter() -> None:
    fake = make_fake_element("CallOperation")
    target = make_fake_element("Relation", properties={"name": "myTarget"})
    IRPCallOperation(fake).target = cast("IRPRelation", IRPModelElement.wrap(target))
    assert fake.target is target
