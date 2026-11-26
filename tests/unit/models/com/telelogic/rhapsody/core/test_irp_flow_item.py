"""Tests for the IRPFlowItem wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flow_item import IRPFlowItem
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_is_registered_for_meta_class_flow_item() -> None:
    fake = make_fake_element("FlowItem", properties={"name": "MyFlowItem"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPFlowItem)
    assert isinstance(wrapped, IRPClassifier)
    assert wrapped.name == "MyFlowItem"


def test_add_represented_delegates() -> None:
    fake = make_fake_element("FlowItem")
    element = make_fake_element("Class", properties={"name": "RepresentedClass"})
    IRPFlowItem(fake).add_represented(cast(IRPModelElement, IRPModelElement.wrap(element)))
    fake.addRepresented.assert_called_once_with(element)


def test_represented_returns_collection() -> None:
    item1 = make_fake_element("Class", properties={"name": "Rep1"})
    item2 = make_fake_element("Class", properties={"name": "Rep2"})
    fake = make_fake_element("FlowItem", properties={"represented": make_fake_collection([item1, item2])})
    result = IRPFlowItem(fake).represented
    assert isinstance(result, IRPCollection)
    assert len(result) == 2


def test_remove_represented_delegates() -> None:
    fake = make_fake_element("FlowItem")
    element = make_fake_element("Class", properties={"name": "RepresentedClass"})
    IRPFlowItem(fake).remove_represented(cast(IRPModelElement, IRPModelElement.wrap(element)))
    fake.removeRepresented.assert_called_once_with(element)
