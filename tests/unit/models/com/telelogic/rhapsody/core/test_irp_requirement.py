"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPRequirement."""

import sys
from types import ModuleType
from unittest.mock import Mock, patch

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_requirement import IRPRequirement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_requirements import IRPAnnotation
from tests.unit.models.fakes import make_fake_element


def test_requirement_is_an_annotation() -> None:
    fake = make_fake_element("Requirement", properties={"name": "REQ-1"})
    requirement = IRPRequirement(fake)

    assert isinstance(requirement, IRPAnnotation)
    assert requirement.name == "REQ-1"


def test_requirement_constructor_casts_generic_pywin_dispatch_to_exact_interface() -> None:
    class RawDispatch:
        pass

    class TypedRequirementDispatch:
        pass

    raw = RawDispatch()
    typed = TypedRequirementDispatch()
    cast_to = Mock(return_value=typed)
    client_module = ModuleType("win32com.client")
    client_module.__dict__.update({"CastTo": cast_to, "DispatchBaseClass": RawDispatch})
    parent_module = ModuleType("win32com")
    parent_module.__dict__["client"] = client_module

    with patch.dict(sys.modules, {"win32com": parent_module, "win32com.client": client_module}):
        requirement = IRPRequirement(raw)

    cast_to.assert_called_once_with(raw, "IRPRequirement")
    assert requirement._com is typed


def test_requirement_constructor_keeps_fake_dispatch_when_pywin_is_unavailable() -> None:
    fake = make_fake_element("Requirement")

    with patch.dict(sys.modules, {"win32com.client": None}):
        requirement = IRPRequirement(fake)

    assert requirement._com is fake


def test_requirement_id_reads_pywin32_property() -> None:
    fake = make_fake_element("Requirement", properties={"requirementID": "REQ-001"})
    requirement = IRPRequirement(fake)

    assert requirement.requirement_id == "REQ-001"
    fake.getRequirementID.assert_not_called()


def test_requirement_id_writes_pywin32_property() -> None:
    fake = make_fake_element("Requirement")
    requirement = IRPRequirement(fake)

    requirement.requirement_id = "REQ-002"

    assert fake.requirementID == "REQ-002"
    fake.setRequirementID.assert_not_called()


def test_requirement_id_has_no_method_aliases() -> None:
    assert "get_requirement_id" not in IRPRequirement.__dict__
    assert "set_requirement_id" not in IRPRequirement.__dict__


def test_requirement_is_registered_for_meta_class_requirement() -> None:
    fake = make_fake_element("Requirement", properties={"name": "REQ-1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPRequirement)
