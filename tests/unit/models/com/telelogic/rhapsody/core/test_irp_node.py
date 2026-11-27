"""Fake-COM unit tests for the IRPNode wrapper."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPComponentInstance, IRPNode, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_node_is_registered() -> None:
    fake = make_fake_element("Node", properties={"name": "Node1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPNode)
    assert isinstance(wrapped, IRPUnit)


def test_cpu_type() -> None:
    fake = make_fake_element("Node", properties={"CPUtype": "ARM"})
    assert IRPNode(fake).cpu_type == "ARM"


def test_cpu_type_setter() -> None:
    fake = make_fake_element("Node")
    IRPNode(fake).cpu_type = "ARM"
    assert fake.CPUtype == "ARM"


def test_component_instances() -> None:
    fake = make_fake_element("Node", properties={"componentInstances": make_fake_collection([make_fake_element("ComponentInstance")])})
    result = IRPNode(fake).component_instances
    assert isinstance(result, IRPCollection)
    assert len(result) == 1


def test_add_component_instance() -> None:
    fake = make_fake_element("Node")
    instance = make_fake_element("ComponentInstance", properties={"name": "Inst1"})
    fake.addComponentInstance.return_value = instance
    assert IRPNode(fake).add_component_instance("Inst1").name == "Inst1"
    fake.addComponentInstance.assert_called_once_with("Inst1")


def test_delete_component_instance() -> None:
    fake = make_fake_element("Node")
    instance = make_fake_element("ComponentInstance", properties={"name": "Inst1"})
    IRPNode(fake).delete_component_instance(IRPComponentInstance(instance))
    fake.deleteComponentInstance.assert_called_once_with(instance)


def test_find_component_instance_found() -> None:
    fake = make_fake_element("Node")
    instance = make_fake_element("ComponentInstance", properties={"name": "Inst1"})
    fake.findComponentInstance.return_value = instance
    found = IRPNode(fake).find_component_instance("Inst1")
    assert found is not None
    assert found.name == "Inst1"


def test_find_component_instance_missing() -> None:
    fake = make_fake_element("Node")
    fake.findComponentInstance.return_value = None
    assert IRPNode(fake).find_component_instance("missing") is None
