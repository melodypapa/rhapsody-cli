"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPVariable."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit, IRPVariable
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_variable_is_a_unit() -> None:
    fake = make_fake_element("Variable", properties={"name": "count"})
    variable = IRPVariable(fake)

    assert isinstance(variable, IRPUnit)
    assert variable.name == "count"


def test_variable_add_element_default_value_wraps_result() -> None:
    fake = make_fake_element("Variable")
    new_value = make_fake_element("Class", properties={"name": "Extra"})
    element = make_fake_element("Class", properties={"name": "Extra"})
    fake.addElementDefaultValue.return_value = new_value
    variable = IRPVariable(fake)

    result = variable.add_element_default_value(cast(IRPModelElement, IRPModelElement.wrap(element)))

    fake.addElementDefaultValue.assert_called_once_with(element)
    assert result.name == "Extra"


def test_variable_add_string_default_value_wraps_result() -> None:
    fake = make_fake_element("Variable")
    literal = make_fake_element("LiteralSpecification", properties={"name": "42"})
    fake.addStringDefaultValue.return_value = literal
    variable = IRPVariable(fake)

    result = variable.add_string_default_value("42")

    fake.addStringDefaultValue.assert_called_once_with("42")
    assert result.name == "42"


def test_variable_get_declaration_delegates_to_com() -> None:
    fake = make_fake_element("Variable", getDeclaration="int*")
    variable = IRPVariable(fake)

    assert variable.get_declaration() == "int*"


def test_variable_get_default_value_delegates_to_com() -> None:
    fake = make_fake_element("Variable", getDefaultValue="0")
    variable = IRPVariable(fake)

    assert variable.get_default_value() == "0"


def test_variable_get_type_wraps_result() -> None:
    fake = make_fake_element("Variable")
    type_com = make_fake_element("Class", properties={"name": "int"})
    fake.getType.return_value = type_com
    variable = IRPVariable(fake)

    result = variable.get_type()
    assert result.name == "int"


def test_variable_get_value_specifications_returns_collection() -> None:
    inner = make_fake_element("Class", properties={"name": "Spec"})
    fake = make_fake_element("Variable")
    fake.getValueSpecifications.return_value = make_fake_collection([inner])
    variable = IRPVariable(fake)

    result = variable.get_value_specifications()

    assert isinstance(result, IRPCollection)
    assert len(result) == 1


def test_variable_set_declaration_delegates_to_com() -> None:
    fake = make_fake_element("Variable")
    variable = IRPVariable(fake)

    variable.set_declaration("int*")

    fake.setDeclaration.assert_called_once_with("int*")


def test_variable_set_default_value_delegates_to_com() -> None:
    fake = make_fake_element("Variable")
    variable = IRPVariable(fake)

    variable.set_default_value("42")

    fake.setDefaultValue.assert_called_once_with("42")


def test_variable_set_type_delegates_to_com() -> None:
    fake = make_fake_element("Variable")
    type_fake = make_fake_element("Class", properties={"name": "int"})
    variable = IRPVariable(fake)

    variable.set_type(IRPClassifier(type_fake))

    fake.setType.assert_called_once_with(type_fake)


def test_variable_set_type_declaration_delegates_to_com() -> None:
    fake = make_fake_element("Variable")
    variable = IRPVariable(fake)

    variable.set_type_declaration("int*")

    fake.setTypeDeclaration.assert_called_once_with("int*")


# =============================================================================
# IRPAttribute tests
# =============================================================================


def test_attribute_get_is_constant_returns_int() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute", properties={"isConstant": 1})
    attr = IRPAttribute(fake)
    assert attr.is_constant == 1


def test_attribute_get_is_constant_returns_zero() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute", properties={"isConstant": 0})
    attr = IRPAttribute(fake)
    assert attr.is_constant == 0


def test_attribute_get_is_ordered_returns_int() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute", properties={"isOrdered": 1})
    attr = IRPAttribute(fake)
    assert attr.is_ordered == 1


def test_attribute_get_is_ordered_returns_zero() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute", properties={"isOrdered": 0})
    attr = IRPAttribute(fake)
    assert attr.is_ordered == 0


def test_attribute_get_is_reference_returns_int() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute", properties={"isReference": 1})
    attr = IRPAttribute(fake)
    assert attr.is_reference == 1


def test_attribute_get_is_reference_returns_zero() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute", properties={"isReference": 0})
    attr = IRPAttribute(fake)
    assert attr.is_reference == 0


def test_attribute_set_is_constant_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_constant = True

    assert fake.isConstant == 1


def test_attribute_set_is_constant_false_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_constant = False

    assert fake.isConstant == 0


def test_attribute_set_is_ordered_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_ordered = True

    assert fake.isOrdered == 1


def test_attribute_set_is_ordered_false_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_ordered = False

    assert fake.isOrdered == 0


def test_attribute_set_is_reference_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_reference = True

    assert fake.isReference == 1


def test_attribute_set_is_reference_false_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute

    fake = make_fake_element("Attribute")
    attr = IRPAttribute(fake)

    attr.is_reference = False

    assert fake.isReference == 0


# =============================================================================
# IRPTag tests
# =============================================================================


def test_tag_get_base_wraps_result() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

    base_com = make_fake_element("Class", properties={"name": "BaseClass"})
    fake = make_fake_element("Tag")
    fake.getBase.return_value = base_com
    tag = IRPTag(fake)

    result = tag.get_base()
    assert result.name == "BaseClass"


def test_tag_get_from_profile_returns_profile() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_profile import IRPProfile

    fake_profile = make_fake_element("Profile", properties={"name": "MyProfile"})
    fake = make_fake_element("Tag", getFromProfile=fake_profile)
    tag = IRPTag(fake)

    result = tag.get_from_profile()
    assert isinstance(result, IRPProfile)
    assert result.name == "MyProfile"


def test_tag_get_multiplicity_returns_str() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

    fake = make_fake_element("Tag", getMultiplicity="0..*")
    tag = IRPTag(fake)

    assert tag.get_multiplicity() == "0..*"


def test_tag_get_tag_meta_class_returns_str() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

    fake = make_fake_element("Tag", getTagMetaClass="Stereotype")
    tag = IRPTag(fake)

    assert tag.get_tag_meta_class() == "Stereotype"


def test_tag_get_value_returns_str() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

    fake = make_fake_element("Tag", getValue="some_value")
    tag = IRPTag(fake)

    assert tag.get_value() == "some_value"


def test_tag_set_multiplicity_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

    fake = make_fake_element("Tag")
    tag = IRPTag(fake)

    tag.set_multiplicity("1..*")

    fake.setMultiplicity.assert_called_once_with("1..*")


def test_tag_set_tag_meta_class_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

    fake = make_fake_element("Tag")
    tag = IRPTag(fake)

    tag.set_tag_meta_class("NewStereotype")

    fake.setTagMetaClass.assert_called_once_with("NewStereotype")


def test_tag_set_value_delegates_to_com() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPTag

    fake = make_fake_element("Tag")
    tag = IRPTag(fake)

    tag.set_value("new_value")

    fake.setValue.assert_called_once_with("new_value")
