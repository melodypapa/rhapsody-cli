"""Tests for rhapsody_cli.models.elements.containment.RPComponentInstance."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.containment import RPComponent, RPComponentInstance
from rhapsody_cli.models.elements.relations import RPInstance
from tests.unit.models.fakes import make_fake_element


def test_component_instance_is_an_instance() -> None:
    fake = make_fake_element("ComponentInstance", properties={"name": "CompInst1"})
    comp_inst = RPComponentInstance(fake)

    assert isinstance(comp_inst, RPInstance)
    assert comp_inst.get_name() == "CompInst1"


def test_component_instance_is_registered_for_meta_class_component_instance() -> None:
    fake = make_fake_element("ComponentInstance", properties={"name": "CompInst1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPComponentInstance)


# Tests for methods from Task 12


def test_component_instance_get_component_type_wraps_result() -> None:
    fake = make_fake_element("ComponentInstance")
    comp = make_fake_element("Component", properties={"name": "Comp1"})
    fake.getComponentType.return_value = comp
    inst = RPComponentInstance(fake)

    result = inst.get_component_type()
    assert result.get_name() == "Comp1"


def test_component_instance_get_node_wraps_result() -> None:
    fake = make_fake_element("ComponentInstance")
    node = make_fake_element("Node", properties={"name": "Node1"})
    fake.getNode.return_value = node
    inst = RPComponentInstance(fake)

    result = inst.get_node()
    assert result.get_name() == "Node1"


def test_component_instance_set_component_type_delegates() -> None:
    fake = make_fake_element("ComponentInstance")
    inst = RPComponentInstance(fake)
    comp_fake = make_fake_element("Component", properties={"name": "Comp1"})
    comp = RPComponent(comp_fake)

    inst.set_component_type(comp)

    fake.setComponentType.assert_called_once_with(comp_fake)
