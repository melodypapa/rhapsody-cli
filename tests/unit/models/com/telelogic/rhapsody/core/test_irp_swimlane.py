"""Tests for the IRPSwimlane wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_swimlane import IRPSwimlane
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_is_registered_for_meta_class_swimlane() -> None:
    fake = make_fake_element("Swimlane", properties={"name": "MySwimlane"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPSwimlane)
    assert wrapped.name == "MySwimlane"


def test_add_swimlane_wraps_result() -> None:
    fake = make_fake_element("Swimlane")
    nested = make_fake_element("Swimlane", properties={"name": "NestedLane"})
    fake.addSwimlane.return_value = nested
    result = IRPSwimlane(fake).add_swimlane("NestedLane")
    assert isinstance(result, IRPSwimlane)
    assert result.name == "NestedLane"
    fake.addSwimlane.assert_called_once_with("NestedLane")


def test_contents_returns_collection() -> None:
    item1 = make_fake_element("State", properties={"name": "Content1"})
    item2 = make_fake_element("State", properties={"name": "Content2"})
    fake = make_fake_element("Swimlane", properties={"contents": make_fake_collection([item1, item2])})
    result = IRPSwimlane(fake).contents
    assert isinstance(result, IRPCollection)
    assert len(result) == 2


def test_represents_wraps_result() -> None:
    represents = make_fake_element("Class", properties={"name": "MyClass"})
    fake = make_fake_element("Swimlane", properties={"represents": represents})
    result = IRPSwimlane(fake).represents
    assert result is not None
    assert result.name == "MyClass"


def test_represents_setter() -> None:
    fake = make_fake_element("Swimlane")
    represents = make_fake_element("Class", properties={"name": "MyClass"})
    IRPSwimlane(fake).represents = cast(IRPModelElement, IRPModelElement.wrap(represents))
    assert fake.represents is represents


def test_swimlanes_returns_collection() -> None:
    lane1 = make_fake_element("Swimlane", properties={"name": "NestedLane1"})
    lane2 = make_fake_element("Swimlane", properties={"name": "NestedLane2"})
    fake = make_fake_element("Swimlane", properties={"swimlanes": make_fake_collection([lane1, lane2])})
    result = IRPSwimlane(fake).swimlanes
    assert isinstance(result, IRPCollection)
    assert len(result) == 2
