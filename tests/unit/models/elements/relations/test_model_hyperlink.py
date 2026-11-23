"""Tests for rhapsody_cli.models.elements.relations.RPHyperLink."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.relations import RPDependency, RPHyperLink
from tests.unit.models.fakes import make_fake_element


def test_hyperlink_is_a_dependency() -> None:
    fake = make_fake_element("HyperLink")
    link = RPHyperLink(fake)

    assert isinstance(link, RPDependency)


def test_hyperlink_is_registered_for_meta_class_hyperlink() -> None:
    fake = make_fake_element("HyperLink")

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPHyperLink)
