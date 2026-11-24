"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPRequirement."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_requirements import IRPAnnotation, IRPRequirement
from tests.unit.models.fakes import make_fake_element


def test_requirement_is_an_annotation() -> None:
    fake = make_fake_element("Requirement", properties={"name": "REQ-1"})
    requirement = IRPRequirement(fake)

    assert isinstance(requirement, IRPAnnotation)
    assert requirement.name == "REQ-1"


def test_requirement_get_requirement_id_delegates_to_com() -> None:
    fake = make_fake_element("Requirement", getRequirementID="REQ-001")
    requirement = IRPRequirement(fake)

    assert requirement.get_requirement_id() == "REQ-001"


def test_requirement_set_requirement_id_delegates_to_com() -> None:
    fake = make_fake_element("Requirement")
    requirement = IRPRequirement(fake)

    requirement.set_requirement_id("REQ-002")

    fake.setRequirementID.assert_called_once_with("REQ-002")


def test_requirement_is_registered_for_meta_class_requirement() -> None:
    fake = make_fake_element("Requirement", properties={"name": "REQ-1"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPRequirement)
