"""Tests for rhapsody_cli.models.elements.variables.RPTag."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.variables import RPTag, RPVariable
from tests.unit.models.fakes import make_fake_element


def test_tag_is_a_variable() -> None:
    fake = make_fake_element("Tag", properties={"name": "MyTag"})
    tag = RPTag(fake)

    assert isinstance(tag, RPVariable)
    assert tag.name == "MyTag"


def test_tag_is_registered_for_meta_class_tag() -> None:
    fake = make_fake_element("Tag", properties={"name": "MyTag"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPTag)
