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
    component_type = IRPComponentInstance(fake).component_type
    assert component_type is not None
    assert component_type.name == "Comp1"


def test_component_type_setter() -> None:
    fake = make_fake_element("ComponentInstance")
    component = make_fake_element("Component", properties={"name": "Comp1"})
    IRPComponentInstance(fake).component_type = IRPComponent(component)
    assert fake.componentType is component


def test_node() -> None:
    node = make_fake_element("Node", properties={"name": "Node1"})
    fake = make_fake_element("ComponentInstance", properties={"node": node})
    wrapped_node = IRPComponentInstance(fake).node
    assert wrapped_node is not None
    assert wrapped_node.name == "Node1"
