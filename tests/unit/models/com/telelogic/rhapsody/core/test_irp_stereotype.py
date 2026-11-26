"""Fake-COM tests for the JavaDoc-owned IRPStereotype API."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPStereotype
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_stereotype_is_a_classifier() -> None:
    fake = make_fake_element("Stereotype", properties={"name": "MyStereo"})
    stereotype = IRPStereotype(fake)

    assert isinstance(stereotype, IRPClassifier)
    assert stereotype.name == "MyStereo"


def test_stereotype_is_registered_for_meta_class_stereotype() -> None:
    fake = make_fake_element("Stereotype", properties={"name": "MyStereo"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPStereotype)


def test_add_meta_class_calls_catalogued_method() -> None:
    fake = make_fake_element("Stereotype")
    stereotype = IRPStereotype(fake)

    stereotype.add_meta_class("Class")

    fake.addMetaClass.assert_called_once_with("Class")


def test_icon_property_reads_catalogued_com_property() -> None:
    fake = make_fake_element("Stereotype", properties={"icon": "C:/Rhapsody/icons/stereotype.ico"})

    assert IRPStereotype(fake).icon == "C:/Rhapsody/icons/stereotype.ico"


def test_is_new_term_property_reads_and_writes_catalogued_com_property() -> None:
    fake = make_fake_element("Stereotype", properties={"isNewTerm": 0})
    stereotype = IRPStereotype(fake)

    assert stereotype.is_new_term == 0

    stereotype.is_new_term = 1

    assert fake.isNewTerm == 1
    assert stereotype.is_new_term == 1


def test_of_meta_class_property_reads_catalogued_com_property() -> None:
    fake = make_fake_element("Stereotype", properties={"ofMetaClass": "Package,Class"})

    assert IRPStereotype(fake).of_meta_class == "Package,Class"


def test_remove_meta_class_calls_catalogued_method() -> None:
    fake = make_fake_element("Stereotype")
    stereotype = IRPStereotype(fake)

    stereotype.remove_meta_class("Class")

    fake.removeMetaClass.assert_called_once_with("Class")
