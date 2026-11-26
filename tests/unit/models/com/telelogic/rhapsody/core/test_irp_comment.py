"""Tests for the IRPComment wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_comment import IRPComment
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_is_registered_for_meta_class_comment() -> None:
    fake = make_fake_element("Comment", properties={"name": "Comment1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPComment)
    assert wrapped.name == "Comment1"


def test_inherits_model_element_behavior() -> None:
    fake = make_fake_element("Comment", properties={"name": "Comment2"})
    comment = IRPComment(fake)
    assert isinstance(comment, IRPModelElement)
    assert comment.name == "Comment2"
