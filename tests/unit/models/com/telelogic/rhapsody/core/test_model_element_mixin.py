"""Tests for ComHelper, the COM-helper mixin behind IRPModelElement."""

from rhapsody_cli.models import core
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.core import ComHelper


def test_irp_model_element_uses_com_helper() -> None:
    assert issubclass(IRPModelElement, ComHelper)


def test_legacy_abstract_base_is_removed() -> None:
    assert not hasattr(core, "AbstractRPModelElement")


def test_helper_methods_are_reachable_from_an_instance() -> None:
    element = IRPModelElement(object())
    assert element.call_com(lambda: "ok") == "ok"
    assert callable(element.wrap)
    assert callable(element.get_com_property)
    assert callable(element.set_com_property)
    assert callable(element.register_wrapper)
