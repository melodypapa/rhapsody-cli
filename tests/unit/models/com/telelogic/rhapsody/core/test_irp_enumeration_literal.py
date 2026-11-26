"""Tests for the IRPEnumerationLiteral wrapper in the canonical ``com.telelogic.rhapsody.core`` package."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_enumeration_literal import IRPEnumerationLiteral
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_is_registered_for_meta_class_enumeration_literal() -> None:
    fake = make_fake_element("EnumerationLiteral", properties={"name": "L1", "value": "1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPEnumerationLiteral)
    assert wrapped.name == "L1"


def test_value_returns_string() -> None:
    fake = make_fake_element("EnumerationLiteral", properties={"value": "42"})
    assert IRPEnumerationLiteral(fake).value == "42"


def test_value_setter() -> None:
    fake = make_fake_element("EnumerationLiteral")
    IRPEnumerationLiteral(fake).value = "43"
    assert fake.value == "43"
