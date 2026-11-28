"""Tests for the IRPConstraint wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

import sys
from types import ModuleType
from unittest.mock import Mock

import pytest

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


def test_constraints_by_me_casts_generic_pywin_dispatch_to_constraint_interface(monkeypatch: pytest.MonkeyPatch) -> None:
    class RawDispatch:
        pass

    class ConstraintDispatch:
        def __init__(self) -> None:
            self.constraintsByMe = make_fake_collection([])

    raw = RawDispatch()
    typed = ConstraintDispatch()
    cast_to = Mock(return_value=typed)
    client_module = ModuleType("win32com.client")
    client_module.__dict__.update({"CastTo": cast_to, "DispatchBaseClass": RawDispatch})
    parent_module = ModuleType("win32com")
    parent_module.__dict__["client"] = client_module
    monkeypatch.setitem(sys.modules, "win32com", parent_module)
    monkeypatch.setitem(sys.modules, "win32com.client", client_module)

    result = IRPConstraint(raw).constraints_by_me

    cast_to.assert_called_once_with(raw, "IRPConstraint")
    assert isinstance(result, IRPCollection)
    assert result._com is typed.constraintsByMe
