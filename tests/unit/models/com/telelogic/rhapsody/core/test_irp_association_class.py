"""Tests for rhapsody_cli.models.elements.classifiers.IRPAssociationClass."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_association_class_is_a_class() -> None:
    fake = make_fake_element("AssociationClass", properties={"name": "MyAssoc"})
    ac = IRPAssociationClass(fake)

    assert isinstance(ac, IRPClass)
    assert ac.get_name() == "MyAssoc"


def test_association_class_is_registered_for_meta_class_association_class() -> None:
    fake = make_fake_element("AssociationClass", properties={"name": "MyAssoc"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPAssociationClass)


def test_get_end1_reads_property() -> None:
    fake = make_fake_element("AssociationClass", properties={"end1": make_fake_element("Relation", properties={"name": "e1"})})
    assert IRPAssociationClass(fake).get_end1().get_name() == "e1"


def test_get_end2_reads_property() -> None:
    fake = make_fake_element("AssociationClass", properties={"end2": make_fake_element("Relation", properties={"name": "e2"})})
    assert IRPAssociationClass(fake).get_end2().get_name() == "e2"


def test_get_is_class_reads_property() -> None:
    fake = make_fake_element("AssociationClass", properties={"isClass": 1})
    assert IRPAssociationClass(fake).get_is_class() == 1


def test_set_is_class_writes_property() -> None:
    fake = make_fake_element("AssociationClass")
    IRPAssociationClass(fake).set_is_class(1)
    assert fake.isClass == 1
