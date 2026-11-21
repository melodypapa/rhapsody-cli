"""Tests for the fake COM object builders in ``tests/unit/models/fakes.py``."""

from typing import Any, Dict

from tests.unit.models.fakes import make_fake_element


def test_make_fake_element_method_returns_stay_method_shaped() -> None:
    fake = make_fake_element("Class", getIsFinal=1)

    assert fake.getIsFinal() == 1


def test_make_fake_element_properties_are_plain_attribute_reads() -> None:
    fake = make_fake_element("Class", properties={"isAbstract": 1})

    assert fake.isAbstract == 1


def test_make_fake_element_properties_and_methods_combine() -> None:
    fake = make_fake_element("Class", properties={"isActive": 0}, getIsFinal=1)

    assert fake.isActive == 0
    assert fake.getIsFinal() == 1


def test_make_fake_element_property_writes_are_observable() -> None:
    properties: Dict[str, Any] = {"isActive": 1}
    fake = make_fake_element("Class", properties=properties)

    fake.isActive = 0

    assert fake.isActive == 0
