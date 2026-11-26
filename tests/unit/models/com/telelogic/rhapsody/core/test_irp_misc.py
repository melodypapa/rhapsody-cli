"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core wrappers."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_misc import (
    IRPComment,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_comment_is_a_model_element() -> None:
    fake = make_fake_element("Comment", properties={"name": "Comment1"})
    comment = IRPComment(fake)

    assert isinstance(comment, IRPModelElement)
    assert comment.name == "Comment1"


def test_comment_is_registered() -> None:
    fake = make_fake_element("Comment", properties={"name": "Comment1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPComment)
