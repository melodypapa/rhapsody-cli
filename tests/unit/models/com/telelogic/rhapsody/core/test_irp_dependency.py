"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPDependency."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDependency
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_dependency_is_a_model_element() -> None:
    fake = make_fake_element("Dependency")
    dep = IRPDependency(fake)

    assert isinstance(dep, IRPModelElement)


def test_dependency_is_registered_for_meta_class_dependency() -> None:
    fake = make_fake_element("Dependency")

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPDependency)
