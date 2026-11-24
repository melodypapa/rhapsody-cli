"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPHyperLink."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDependency, IRPHyperLink
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_hyperlink_is_a_dependency() -> None:
    fake = make_fake_element("HyperLink")
    link = IRPHyperLink(fake)

    assert isinstance(link, IRPDependency)


def test_hyperlink_is_registered_for_meta_class_hyperlink() -> None:
    fake = make_fake_element("HyperLink")

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPHyperLink)
