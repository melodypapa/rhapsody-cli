"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model.IRPType."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType
from tests.unit.models.fakes import make_fake_collection, make_fake_element


class TestRPType:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("Type", properties={"name": "T1"})
        t = IRPType(fake)
        assert isinstance(t, IRPModelElement)
        assert t.name == "T1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("Type", properties={"name": "T1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPType)

    def test_add_enumeration_literal_delegates_and_wraps(self) -> None:
        # Pattern E

        fake = make_fake_element("Type")
        lit = make_fake_element("EnumerationLiteral", properties={"name": "RED"})
        fake.addEnumerationLiteral.return_value = lit
        t = IRPType(fake)
        wrapped = t.add_enumeration_literal("RED")
        assert wrapped.name == "RED"
        fake.addEnumerationLiteral.assert_called_once_with("RED")

    def test_delete_enumeration_literal_delegates(self) -> None:
        # Pattern F
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPEnumerationLiteral

        fake = make_fake_element("Type")
        lit = make_fake_element("EnumerationLiteral", properties={"name": "RED"})
        fake.deleteEnumerationLiteral.return_value = None
        t = IRPType(fake)
        t.delete_enumeration_literal(IRPEnumerationLiteral(lit))
        fake.deleteEnumerationLiteral.assert_called_once_with(lit)

    def test_get_declaration_returns_string(self) -> None:
        # Pattern A
        fake = make_fake_element("Type", properties={"declaration": "int x"})
        t = IRPType(fake)
        assert t.declaration == "int x"

    def test_get_enumeration_literals_returns_collection(self) -> None:
        # Pattern C
        lit = make_fake_element("EnumerationLiteral", properties={"name": "RED"})
        fake = make_fake_element("Type", properties={"enumerationLiterals": make_fake_collection([lit])})
        fake.getEnumerationLiterals.return_value = make_fake_collection([])  # old member: wrong
        t = IRPType(fake)
        result = t.enumeration_literals
        assert isinstance(result, IRPCollection)
        assert len(result) == 1  # property-backed collection has RED

    def test_get_is_predefined_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", properties={"isPredefined": 1})
        fake.getIsPredefined.return_value = 0  # old Java member would return the wrong value
        t = IRPType(fake)
        assert t.is_predefined == 1

    def test_get_is_typedef_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", properties={"isTypedef": 1})
        fake.getIsTypedef.return_value = 0  # old Java member would return the wrong value
        t = IRPType(fake)
        assert t.is_typedef == 1

    def test_get_is_typedef_constant_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", properties={"isTypedefConstant": 1})
        fake.getIsTypedefConstant.return_value = 0  # old Java member would return the wrong value
        t = IRPType(fake)
        assert t.is_typedef_constant == 1

    def test_get_is_typedef_ordered_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", properties={"isTypedefOrdered": 1})
        fake.getIsTypedefOrdered.return_value = 0  # old Java member would return the wrong value
        t = IRPType(fake)
        assert t.is_typedef_ordered == 1

    def test_get_is_typedef_reference_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", properties={"isTypedefReference": 1})
        fake.getIsTypedefReference.return_value = 0  # old Java member would return the wrong value
        t = IRPType(fake)
        assert t.is_typedef_reference == 1

    def test_get_kind_returns_string(self) -> None:
        # Pattern A
        fake = make_fake_element("Type", properties={"kind": "Enumeration"})
        t = IRPType(fake)
        assert t.kind == "Enumeration"

    def test_get_typedef_base_type_wraps_result(self) -> None:
        # Pattern B
        fake = make_fake_element("Type")
        base = make_fake_element("Class", properties={"name": "Base"})
        fake.typedefBaseType = base
        t = IRPType(fake)
        wrapped = t.typedef_base_type
        assert wrapped.name == "Base"

    def test_get_typedef_multiplicity_returns_string(self) -> None:
        # Pattern A
        fake = make_fake_element("Type", properties={"typedefMultiplicity": "0..1"})
        t = IRPType(fake)
        assert t.typedef_multiplicity == "0..1"

    def test_is_array_returns_int(self) -> None:
        # Pattern G — representative for all 16 is_* checks
        fake = make_fake_element("Type", isArray=True)
        t = IRPType(fake)
        assert t.is_array() == 1

    def test_is_enum_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isEnum=True)
        t = IRPType(fake)
        assert t.is_enum() == 1

    def test_is_equal_to_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isEqualTo=True)
        t = IRPType(fake)
        assert t.is_equal_to() == 1

    def test_is_implicit_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isImplicit=True)
        t = IRPType(fake)
        assert t.is_implicit() == 1

    def test_is_kind_enumeration_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isKindEnumeration=True)
        t = IRPType(fake)
        assert t.is_kind_enumeration() == 1

    def test_is_kind_language_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isKindLanguage=True)
        t = IRPType(fake)
        assert t.is_kind_language() == 1

    def test_is_kind_struct_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isKindStruct=True)
        t = IRPType(fake)
        assert t.is_kind_struct() == 1

    def test_is_kind_typedef_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isKindTypedef=True)
        t = IRPType(fake)
        assert t.is_kind_typedef() == 1

    def test_is_kind_union_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isKindUnion=True)
        t = IRPType(fake)
        assert t.is_kind_union() == 1

    def test_is_pointer_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isPointer=True)
        t = IRPType(fake)
        assert t.is_pointer() == 1

    def test_is_pointer_to_pointer_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isPointerToPointer=True)
        t = IRPType(fake)
        assert t.is_pointer_to_pointer() == 1

    def test_is_reference_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isReference=True)
        t = IRPType(fake)
        assert t.is_reference() == 1

    def test_is_reference_to_pointer_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isReferenceToPointer=True)
        t = IRPType(fake)
        assert t.is_reference_to_pointer() == 1

    def test_is_struct_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isStruct=True)
        t = IRPType(fake)
        assert t.is_struct() == 1

    def test_is_template_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isTemplate=True)
        t = IRPType(fake)
        assert t.is_template() == 1

    def test_is_union_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Type", isUnion=True)
        t = IRPType(fake)
        assert t.is_union() == 1

    def test_set_kind_delegates(self) -> None:
        # Pattern D — representative for set_* str-arg setters
        fake = make_fake_element("Type")
        t = IRPType(fake)
        t.kind = "Enumeration"
        assert fake.kind == "Enumeration"

    def test_set_declaration_delegates(self) -> None:
        # Pattern D — str arg
        fake = make_fake_element("Type")
        t = IRPType(fake)
        t.declaration = "int x"
        assert fake.declaration == "int x"

    def test_set_is_typedef_constant_delegates(self) -> None:
        # Pattern D — int-arg setter
        fake = make_fake_element("Type")
        t = IRPType(fake)
        t.is_typedef_constant = 1
        assert fake.isTypedefConstant == 1

    def test_set_is_typedef_ordered_delegates(self) -> None:
        # Pattern D — int-arg setter
        fake = make_fake_element("Type")
        t = IRPType(fake)
        t.is_typedef_ordered = 1
        assert fake.isTypedefOrdered == 1

    def test_set_is_typedef_reference_delegates(self) -> None:
        # Pattern D — int-arg setter
        fake = make_fake_element("Type")
        t = IRPType(fake)
        t.is_typedef_reference = 1
        assert fake.isTypedefReference == 1

    def test_set_typedef_base_type_delegates(self) -> None:
        # Pattern F — IRPClassifier arg
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier

        fake = make_fake_element("Type")
        base = make_fake_element("Class", properties={"name": "Base"})
        t = IRPType(fake)
        t.typedef_base_type = IRPClassifier(base)
        assert fake.typedefBaseType is base

    def test_set_typedef_multiplicity_delegates(self) -> None:
        # Pattern D — str-arg setter
        fake = make_fake_element("Type")
        t = IRPType(fake)
        t.typedef_multiplicity = "0..1"
        assert fake.typedefMultiplicity == "0..1"
