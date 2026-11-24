"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPTag."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag, IRPVariable
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_tag_is_a_variable() -> None:
    fake = make_fake_element("Tag", properties={"name": "MyTag"})
    tag = IRPTag(fake)

    assert isinstance(tag, IRPVariable)
    assert tag.name == "MyTag"


def test_tag_is_registered_for_meta_class_tag() -> None:
    fake = make_fake_element("Tag", properties={"name": "MyTag"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPTag)
