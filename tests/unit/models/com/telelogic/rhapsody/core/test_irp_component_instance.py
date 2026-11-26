"""Fake-COM unit tests for the IRPComponentInstance wrapper."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPComponent, IRPComponentInstance, IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_component_instance_is_registered() -> None:
    fake = make_fake_element("ComponentInstance", properties={"name": "CompInst1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPComponentInstance)
    assert isinstance(wrapped, IRPInstance)


def test_component_type() -> None:
    component = make_fake_element("Component", properties={"name": "Comp1"})
    fake = make_fake_element("ComponentInstance", properties={"componentType": component})
    assert IRPComponentInstance(fake).component_type.name == "Comp1"


def test_component_type_setter() -> None:
    fake = make_fake_element("ComponentInstance")
    component = make_fake_element("Component", properties={"name": "Comp1"})
    IRPComponentInstance(fake).component_type = IRPComponent(component)
    assert fake.componentType is component


def test_node() -> None:
    node = make_fake_element("Node", properties={"name": "Node1"})
    fake = make_fake_element("ComponentInstance", properties={"node": node})
    assert IRPComponentInstance(fake).node.name == "Node1"
