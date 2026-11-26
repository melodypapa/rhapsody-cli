"""Tests for the IRPConstraint wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_constraint import IRPConstraint
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_is_registered_for_meta_class_constraint() -> None:
    fake = make_fake_element("Constraint", properties={"name": "C1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPConstraint)
    assert wrapped.name == "C1"


def test_constraints_by_me_returns_collection() -> None:
    target = make_fake_element("Class", properties={"name": "Constrained"})
    fake = make_fake_element("Constraint", properties={"constraintsByMe": make_fake_collection([target])})
    result = IRPConstraint(fake).constraints_by_me
    assert isinstance(result, IRPCollection)
    assert len(result) == 1
