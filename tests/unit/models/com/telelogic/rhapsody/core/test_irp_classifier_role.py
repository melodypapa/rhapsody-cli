"""Tests for the IRPClassifierRole wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier_role import IRPClassifierRole
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPSequenceDiagram
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_is_registered_for_meta_class_classifier_role() -> None:
    fake = make_fake_element("ClassifierRole", properties={"name": "L1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPClassifierRole)
    assert wrapped.name == "L1"


def test_formal_classifier_wraps_result() -> None:
    classifier = make_fake_element("Class", properties={"name": "Foo"})
    fake = make_fake_element("ClassifierRole", properties={"formalClassifier": classifier})
    result = IRPClassifierRole(fake).formal_classifier
    assert result is not None
    assert result.name == "Foo"


def test_formal_classifier_setter() -> None:
    fake = make_fake_element("ClassifierRole")
    classifier = make_fake_element("Class", properties={"name": "Foo"})
    IRPClassifierRole(fake).formal_classifier = cast(IRPClassifier, IRPModelElement.wrap(classifier))
    assert fake.formalClassifier is classifier


def test_formal_instance_wraps_result() -> None:
    instance = make_fake_element("Instance", properties={"name": "Inst1"})
    fake = make_fake_element("ClassifierRole", properties={"formalInstance": instance})
    result = IRPClassifierRole(fake).formal_instance
    assert result is not None
    assert result.name == "Inst1"


def test_formal_instance_setter() -> None:
    fake = make_fake_element("ClassifierRole")
    instance = make_fake_element("Instance", properties={"name": "Inst1"})
    IRPClassifierRole(fake).formal_instance = cast(IRPInstance, IRPModelElement.wrap(instance))
    assert fake.formalInstance is instance


def test_referenced_sequence_diagram_wraps_result() -> None:
    diagram = make_fake_element("SequenceDiagram", properties={"name": "SD1"})
    fake = make_fake_element("ClassifierRole", properties={"referencedSequenceDiagram": diagram})
    result = IRPClassifierRole(fake).referenced_sequence_diagram
    assert result is not None
    assert result.name == "SD1"


def test_referenced_sequence_diagram_setter() -> None:
    fake = make_fake_element("ClassifierRole")
    diagram = make_fake_element("SequenceDiagram", properties={"name": "SD1"})
    IRPClassifierRole(fake).referenced_sequence_diagram = cast(IRPSequenceDiagram, IRPModelElement.wrap(diagram))
    assert fake.referencedSequenceDiagram is diagram


def test_get_referencing_classifier_roles_recursively_returns_collection() -> None:
    sub = make_fake_element("ClassifierRole", properties={"name": "Sub"})
    fake = make_fake_element("ClassifierRole")
    fake.getReferencingClassifierRolesRecursively.return_value = make_fake_collection([sub])
    result = IRPClassifierRole(fake).get_referencing_classifier_roles_recursively()
    assert isinstance(result, IRPCollection)
    assert len(result) == 1


def test_role_type_returns_string() -> None:
    fake = make_fake_element("ClassifierRole", properties={"roleType": "CLASS"})
    assert IRPClassifierRole(fake).role_type == "CLASS"
