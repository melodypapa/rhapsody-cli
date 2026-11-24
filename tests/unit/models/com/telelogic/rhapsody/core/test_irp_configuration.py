"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPConfiguration."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPComponent, IRPConfiguration, IRPInstance, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_configuration_is_a_unit() -> None:
    fake = make_fake_element("Configuration", properties={"name": "Config1"})
    config = IRPConfiguration(fake)

    assert isinstance(config, IRPUnit)
    assert config.name == "Config1"


def test_configuration_is_registered_for_meta_class_configuration() -> None:
    fake = make_fake_element("Configuration", properties={"name": "Config1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPConfiguration)


# Tests for methods from Task 12


def test_configuration_add_initial_instance_delegates() -> None:
    fake = make_fake_element("Configuration")
    config = IRPConfiguration(fake)
    instance_fake = make_fake_element("Instance", properties={"name": "Inst1"})
    instance = IRPInstance(instance_fake)

    config.add_initial_instance(instance)

    fake.addInitialInstance.assert_called_once_with(instance_fake)


def test_configuration_get_initial_instances_returns_collection() -> None:
    fake = make_fake_element("Configuration")
    instance = make_fake_element("Instance", properties={"name": "Inst1"})
    fake.getInitialInstances.return_value = make_fake_collection([instance])
    config = IRPConfiguration(fake)

    result = config.get_initial_instances()
    assert isinstance(result, IRPCollection)


def test_configuration_delete_initial_instance_delegates() -> None:
    fake = make_fake_element("Configuration")
    config = IRPConfiguration(fake)
    instance_fake = make_fake_element("Instance", properties={"name": "Inst1"})
    instance = IRPInstance(instance_fake)

    config.delete_initial_instance(instance)

    fake.deleteInitialInstance.assert_called_once_with(instance_fake)


def test_configuration_get_directory_returns_str() -> None:
    fake = make_fake_element("Configuration")
    fake.getDirectory.return_value = "/some/dir"
    config = IRPConfiguration(fake)

    result = config.get_directory()
    assert result == "/some/dir"


def test_configuration_set_directory_delegates() -> None:
    fake = make_fake_element("Configuration")
    config = IRPConfiguration(fake)

    config.set_directory("/new/dir")

    fake.setDirectory.assert_called_once_with("/new/dir")


def test_configuration_get_its_component_wraps_result() -> None:
    fake = make_fake_element("Configuration")
    comp = make_fake_element("Component", properties={"name": "Comp1"})
    fake.getItsComponent.return_value = comp
    config = IRPConfiguration(fake)

    result = config.get_its_component()
    assert result.name == "Comp1"


def test_configuration_set_its_component_delegates() -> None:
    fake = make_fake_element("Configuration")
    config = IRPConfiguration(fake)
    comp_fake = make_fake_element("Component", properties={"name": "Comp1"})
    comp = IRPComponent(comp_fake)

    config.set_its_component(comp)

    fake.setItsComponent.assert_called_once_with(comp_fake)


def test_configuration_needs_code_generation_returns_int() -> None:
    fake = make_fake_element("Configuration")
    fake.needsCodeGeneration.return_value = 1
    config = IRPConfiguration(fake)

    result = config.needs_code_generation()

    fake.needsCodeGeneration.assert_called_once_with()
    assert result == 1
