"""Tests for rhapsody_cli.models.elements.relations.RPDependency."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.relations import RPDependency
from tests.unit.models.fakes import make_fake_element


def test_dependency_is_a_model_element() -> None:
    fake = make_fake_element("Dependency")
    dep = RPDependency(fake)

    assert isinstance(dep, IRPModelElement)


def test_dependency_is_registered_for_meta_class_dependency() -> None:
    fake = make_fake_element("Dependency")

    wrapped = AbstractRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPDependency)
