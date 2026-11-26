"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core wrappers."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_misc import (
    IRPComment,
    IRPConstraint,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_comment_is_a_model_element() -> None:
    fake = make_fake_element("Comment", properties={"name": "Comment1"})
    comment = IRPComment(fake)

    assert isinstance(comment, IRPModelElement)
    assert comment.name == "Comment1"


def test_comment_is_registered() -> None:
    fake = make_fake_element("Comment", properties={"name": "Comment1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPComment)


def test_constraint_is_a_model_element() -> None:
    fake = make_fake_element("Constraint", properties={"name": "Constraint1"})
    constraint = IRPConstraint(fake)

    assert isinstance(constraint, IRPModelElement)
    assert constraint.name == "Constraint1"


def test_constraint_is_registered() -> None:
    fake = make_fake_element("Constraint", properties={"name": "Constraint1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPConstraint)


def test_constraint_get_constraints_by_me_returns_collection() -> None:
    fake = make_fake_element("Constraint")
    inner = make_fake_element("Class", properties={"name": "ConstrainedClass"})
    fake.getConstraintsByMe.return_value = make_fake_collection([inner])
    constraint = IRPConstraint(fake)
    result = constraint.get_constraints_by_me()
    assert isinstance(result, IRPCollection)
