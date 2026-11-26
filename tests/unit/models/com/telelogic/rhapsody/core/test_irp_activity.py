"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_activity flowchart classes."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_activity import (
    IRPObjectNode,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from tests.unit.models.fakes import make_fake_collection, make_fake_element


class TestRPObjectNode:
    """Tests for IRPObjectNode (7 methods)."""

    def test_is_state(self) -> None:
        fake = make_fake_element("ObjectNode", properties={"name": "MyObjectNode"})
        node = IRPObjectNode(fake)
        assert isinstance(node, IRPState)
        assert node.name == "MyObjectNode"

    def test_add_in_state_delegates(self) -> None:
        fake = make_fake_element("ObjectNode")
        state = make_fake_element("State", properties={"name": "InStateValue"})
        node = IRPObjectNode(fake)
        node.add_in_state(cast(IRPModelElement, IRPModelElement.wrap(state)))
        fake.addInState.assert_called_once_with(state)

    def test_get_in_state_returns_string(self) -> None:
        fake = make_fake_element("ObjectNode", getInState="SomeState")
        node = IRPObjectNode(fake)
        assert node.get_in_state() == "SomeState"

    def test_get_in_state_list_returns_collection(self) -> None:
        fake = make_fake_element("ObjectNode")
        state1 = make_fake_element("State", properties={"name": "State1"})
        state2 = make_fake_element("State", properties={"name": "State2"})
        fake.getInStateList.return_value = make_fake_collection([state1, state2])
        node = IRPObjectNode(fake)
        result = node.get_in_state_list()
        assert isinstance(result, IRPCollection)
        assert len(result) == 2

    def test_get_represents_wraps_result(self) -> None:
        fake = make_fake_element("ObjectNode")
        represents = make_fake_element("Class", properties={"name": "MyClass"})
        fake.getRepresents.return_value = represents
        node = IRPObjectNode(fake)
        result = node.get_represents()
        assert cast(IRPModelElement, result).name == "MyClass"

    def test_remove_in_state_delegates(self) -> None:
        fake = make_fake_element("ObjectNode")
        state = make_fake_element("State", properties={"name": "InStateValue"})
        node = IRPObjectNode(fake)
        node.remove_in_state(cast(IRPModelElement, IRPModelElement.wrap(state)))
        fake.removeInState.assert_called_once_with(state)

    def test_set_in_state_delegates(self) -> None:
        fake = make_fake_element("ObjectNode")
        node = IRPObjectNode(fake)
        node.set_in_state("SomeState")
        fake.setInState.assert_called_once_with("SomeState")

    def test_set_represents_delegates(self) -> None:
        fake = make_fake_element("ObjectNode")
        represents = make_fake_element("Class", properties={"name": "MyClass"})
        node = IRPObjectNode(fake)
        node.set_represents(cast(IRPModelElement, IRPModelElement.wrap(represents)))
        fake.setRepresents.assert_called_once_with(represents)

    def test_is_registered_for_meta_class_object_node(self) -> None:
        fake = make_fake_element("ObjectNode", properties={"name": "MyObjectNode"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPObjectNode)
