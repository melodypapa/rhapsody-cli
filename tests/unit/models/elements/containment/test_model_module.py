"""Tests for rhapsody_cli.models.elements.containment.RPModule."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.containment import RPModule
from rhapsody_cli.models.elements.relations import RPInstance
from tests.unit.models.fakes import make_fake_element


def test_module_is_an_instance() -> None:
    fake = make_fake_element("Module", properties={"name": "Module1"})
    module = RPModule(fake)

    assert isinstance(module, RPInstance)
    assert module.get_name() == "Module1"


def test_module_is_registered_for_meta_class_module() -> None:
    fake = make_fake_element("Module", properties={"name": "Module1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPModule)
