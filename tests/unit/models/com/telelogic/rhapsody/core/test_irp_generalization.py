"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPGeneralization."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPGeneralization
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_generalization_is_a_model_element() -> None:
    fake = make_fake_element("Generalization")
    gen = IRPGeneralization(fake)

    assert isinstance(gen, IRPModelElement)


def test_generalization_is_registered_for_meta_class_generalization() -> None:
    fake = make_fake_element("Generalization")

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPGeneralization)
