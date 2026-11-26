"""Tests for the IRPObjectNode wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_object_node import IRPObjectNode
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_is_registered_for_meta_class_object_node() -> None:
    fake = make_fake_element("ObjectNode", properties={"name": "MyObjectNode"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPObjectNode)
    assert isinstance(wrapped, IRPState)
    assert wrapped.name == "MyObjectNode"


def test_in_state_returns_string() -> None:
    fake = make_fake_element("ObjectNode", properties={"inState": "Active"})
    assert IRPObjectNode(fake).in_state == "Active"


def test_in_state_setter() -> None:
    fake = make_fake_element("ObjectNode")
    IRPObjectNode(fake).in_state = "Inactive"
    assert fake.inState == "Inactive"


def test_in_state_list_returns_collection() -> None:
    state1 = make_fake_element("State", properties={"name": "S1"})
    state2 = make_fake_element("State", properties={"name": "S2"})
    fake = make_fake_element("ObjectNode", properties={"inStateList": make_fake_collection([state1, state2])})
    result = IRPObjectNode(fake).in_state_list
    assert isinstance(result, IRPCollection)
    assert len(result) == 2


def test_represents_wraps_result() -> None:
    represents = make_fake_element("Class", properties={"name": "MyClass"})
    fake = make_fake_element("ObjectNode", properties={"represents": represents})
    result = IRPObjectNode(fake).represents
    assert result is not None
    assert result.name == "MyClass"


def test_represents_setter() -> None:
    fake = make_fake_element("ObjectNode")
    represents = make_fake_element("Class", properties={"name": "MyClass"})
    IRPObjectNode(fake).represents = cast(IRPModelElement, IRPModelElement.wrap(represents))
    assert fake.represents is represents


def test_add_in_state_delegates() -> None:
    fake = make_fake_element("ObjectNode")
    state = make_fake_element("State", properties={"name": "AddedState"})
    IRPObjectNode(fake).add_in_state(cast(IRPModelElement, IRPModelElement.wrap(state)))
    fake.addInState.assert_called_once_with(state)


def test_remove_in_state_delegates() -> None:
    fake = make_fake_element("ObjectNode")
    state = make_fake_element("State", properties={"name": "RemovedState"})
    IRPObjectNode(fake).remove_in_state(cast(IRPModelElement, IRPModelElement.wrap(state)))
    fake.removeInState.assert_called_once_with(state)
