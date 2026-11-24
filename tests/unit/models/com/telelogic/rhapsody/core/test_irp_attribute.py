"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPAttribute."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_variables import IRPVariable
from tests.unit.models.fakes import make_fake_element


def test_attribute_is_a_variable() -> None:
    fake = make_fake_element("Attribute", properties={"name": "count"})
    attribute = IRPAttribute(fake)

    assert isinstance(attribute, IRPVariable)
    assert attribute.name == "count"


def test_attribute_get_multiplicity_delegates_to_com() -> None:
    fake = make_fake_element("Attribute", properties={"multiplicity": "1"})
    attribute = IRPAttribute(fake)

    assert attribute.multiplicity == "1"


def test_attribute_set_multiplicity_delegates_to_com() -> None:
    fake = make_fake_element("Attribute")
    attribute = IRPAttribute(fake)

    attribute.multiplicity = "0..*"

    assert fake.multiplicity == "0..*"


def test_attribute_get_is_static_delegates_to_com() -> None:
    fake = make_fake_element("Attribute", properties={"isStatic": 0})
    attribute = IRPAttribute(fake)

    assert attribute.is_static is False


def test_attribute_set_is_static_delegates_to_com() -> None:
    fake = make_fake_element("Attribute")
    attribute = IRPAttribute(fake)

    attribute.is_static = True

    assert fake.isStatic == 1


def test_attribute_get_visibility_delegates_to_com() -> None:
    fake = make_fake_element("Attribute", properties={"visibility": "private"})
    attribute = IRPAttribute(fake)

    assert attribute.visibility == "private"


def test_attribute_set_visibility_delegates_to_com() -> None:
    fake = make_fake_element("Attribute")
    attribute = IRPAttribute(fake)

    attribute.visibility = "public"

    assert fake.visibility == "public"


def test_attribute_is_registered_for_meta_class_attribute() -> None:
    fake = make_fake_element("Attribute", properties={"name": "count"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPAttribute)


def test_attribute_get_is_constant_returns_int() -> None:
    fake = make_fake_element("Attribute", properties={"isConstant": 1})
    attr = IRPAttribute(fake)
    assert attr.is_constant == 1


def test_attribute_get_is_constant_returns_zero() -> None:
    fake = make_fake_element("Attribute", properties={"isConstant": 0})
    attr = IRPAttribute(fake)
    assert attr.is_constant == 0


def test_attribute_get_is_ordered_returns_int() -> None:
    fake = make_fake_element("Attribute", properties={"isOrdered": 1})
    attr = IRPAttribute(fake)
    assert attr.is_ordered == 1


def test_attribute_get_is_ordered_returns_zero() -> None:
    fake = make_fake_element("Attribute", properties={"isOrdered": 0})
    attr = IRPAttribute(fake)
    assert attr.is_ordered == 0


def test_attribute_get_is_reference_returns_int() -> None:
    fake = make_fake_element("Attribute", properties={"isReference": 1})
    attr = IRPAttribute(fake)
    assert attr.is_reference == 1


def test_attribute_get_is_reference_returns_zero() -> None:
    fake = make_fake_element("Attribute", properties={"isReference": 0})
    attr = IRPAttribute(fake)
    assert attr.is_reference == 0


def test_attribute_set_is_constant_delegates_to_com() -> None:
    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_constant = True

    assert fake.isConstant == 1


def test_attribute_set_is_constant_false_delegates_to_com() -> None:
    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_constant = False

    assert fake.isConstant == 0


def test_attribute_set_is_ordered_delegates_to_com() -> None:
    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_ordered = True

    assert fake.isOrdered == 1


def test_attribute_set_is_ordered_false_delegates_to_com() -> None:
    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_ordered = False

    assert fake.isOrdered == 0


def test_attribute_set_is_reference_delegates_to_com() -> None:
    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_reference = True

    assert fake.isReference == 1


def test_attribute_set_is_reference_false_delegates_to_com() -> None:
    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_reference = False

    assert fake.isReference == 0
