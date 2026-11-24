"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPModule."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPInstance, IRPModule
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_module_is_an_instance() -> None:
    fake = make_fake_element("Module", properties={"name": "Module1"})
    module = IRPModule(fake)

    assert isinstance(module, IRPInstance)
    assert module.name == "Module1"


def test_module_is_registered_for_meta_class_module() -> None:
    fake = make_fake_element("Module", properties={"name": "Module1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPModule)
