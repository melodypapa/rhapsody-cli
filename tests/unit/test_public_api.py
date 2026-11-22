"""Tests for the public rhapsody_cli package API surface."""

import rhapsody_cli
from rhapsody_cli.models.core import AbstractRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_rhapsody_application_is_exported() -> None:
    assert rhapsody_cli.RhapsodyApplication is not None


def test_exceptions_are_exported() -> None:
    assert rhapsody_cli.RhapsodyConnectionError is not None
    assert rhapsody_cli.RhapsodyRuntimeException is not None


def test_importing_package_registers_all_core_element_wrappers() -> None:
    for meta_class, expected_name, expected_module in [
        ("Project", "IRPProject", "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project"),
        ("Package", "IRPPackage", "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package"),
        ("Class", "IRPClass", "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class"),
        ("Attribute", "IRPAttribute", "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute"),
        ("Operation", "IRPOperation", "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation"),
        ("Actor", "RPActor", "rhapsody_cli.models.elements.classifiers.model_actor"),
        ("UseCase", "IRPUseCase", "rhapsody_cli.models.com.telelogic.rhapsody.core.irp_use_case"),
        ("Instance", "RPInstance", "rhapsody_cli.models.elements.relations.model_instance"),
        ("Statechart", "RPStatechart", "rhapsody_cli.models.elements.classifiers.model_statechart"),
        ("Requirement", "RPRequirement", "rhapsody_cli.models.elements.requirements.model_requirements"),
        ("ActivityDiagram", "RPDiagram", "rhapsody_cli.models.elements.diagrams.model_diagrams"),
    ]:
        fake = make_fake_element(meta_class, properties={"name": "X"})
        wrapped = AbstractRPModelElement.wrap(fake)
        assert type(wrapped).__name__ == expected_name, meta_class
        assert type(wrapped).__module__ == expected_module, meta_class
