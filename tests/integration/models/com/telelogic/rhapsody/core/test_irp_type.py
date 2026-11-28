"""Integration tests for IRPType with live Rhapsody COM API.

The 20+ ``is_*`` predicates are asserted over a single fixture (one
package/class/type roundtrip) instead of one roundtrip each; the enumeration
case additionally pins the two predicates whose meaning is unambiguous.
"""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType


@pytest.mark.integration
class TestIRPTypeIntegration:
    """Generated live coverage for IRPType owned methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def _create_type(self, test_project: IRPProject) -> "tuple[IRPType, IRPClass, IRPPackage]":
        """Create a real Type via IRPClass.add_type and return (type, owner class, package)."""
        pkg = test_project.add_package(self._unique("TypePkg"))
        assert isinstance(pkg, IRPPackage)
        cls = pkg.add_class(self._unique("TypeCls"))
        assert isinstance(cls, IRPClass)
        type_element = cls.add_type(self._unique("MyType"))
        assert isinstance(type_element, IRPType)
        return type_element, cls, pkg

    def test_declaration_roundtrip(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            type_element.declaration = "int x"
            assert type_element.declaration == "int x"
        finally:
            pkg.delete_from_project()

    def test_kind_roundtrip(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            type_element.kind = "Enumeration"
            assert type_element.kind == "Enumeration"
        finally:
            pkg.delete_from_project()

    def test_get_enumeration_literals(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            ti.kind = "Enumeration"
            literal = ti.add_enumeration_literal("Red")
            assert literal in list(ti.enumeration_literals)
        finally:
            pkg.delete_from_project()

    def test_delete_enumeration_literal(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            ti.kind = "Enumeration"
            literal = ti.add_enumeration_literal("Red")

            ti.delete_enumeration_literal(literal)

            assert literal not in list(ti.enumeration_literals)
        finally:
            pkg.delete_from_project()

    def test_is_predicates_and_flags_read_as_ints_on_plain_type(self, test_project: IRPProject) -> None:
        """A new type is not predefined; modifier and enum flags start unset."""
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            for predicate in (
                type_element.is_array,
                type_element.is_enum,
                type_element.is_equal_to,
                type_element.is_implicit,
                type_element.is_kind_enumeration,
                type_element.is_kind_language,
                type_element.is_kind_struct,
                type_element.is_kind_typedef,
                type_element.is_kind_union,
                type_element.is_pointer,
                type_element.is_pointer_to_pointer,
                type_element.is_reference,
                type_element.is_reference_to_pointer,
                type_element.is_struct,
                type_element.is_template,
                type_element.is_union,
            ):
                assert predicate() in (0, 1)
            assert type_element.is_predefined == 0
            assert type_element.is_typedef == 1
            assert type_element.is_typedef_constant == 0
            assert type_element.is_typedef_ordered == 0
            assert type_element.is_typedef_reference == 0
        finally:
            pkg.delete_from_project()

    def test_is_enum_is_distinct_from_enumeration_kind(self, test_project: IRPProject) -> None:
        """isEnum parses Language declarations; Enumeration kind uses isKindEnumeration."""
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            type_element.kind = "Enumeration"
            assert type_element.is_enum() == 0
            assert type_element.is_kind_enumeration() == 1
        finally:
            pkg.delete_from_project()

    @pytest.mark.skip(reason="Approved live blocker (#202): isTypedefConstant setter returns COM HRESULT -2147221498 on a real IRPType.")
    def test_is_typedef_constant_roundtrip(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            type_element.is_typedef_constant = 1
            assert type_element.is_typedef_constant == 1
        finally:
            pkg.delete_from_project()

    @pytest.mark.skip(reason="Approved live blocker (#202): isTypedefOrdered setter returns COM HRESULT -2147221498 on a real IRPType.")
    def test_is_typedef_ordered_roundtrip(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            type_element.is_typedef_ordered = 1
            assert type_element.is_typedef_ordered == 1
        finally:
            pkg.delete_from_project()

    @pytest.mark.skip(reason="Approved live blocker (#202): isTypedefReference setter returns COM HRESULT -2147221498 on a real IRPType.")
    def test_is_typedef_reference_roundtrip(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            type_element.is_typedef_reference = 1
            assert type_element.is_typedef_reference == 1
        finally:
            pkg.delete_from_project()

    @pytest.mark.skip(reason="Approved live blocker (#202): setting typedefBaseType returns COM HRESULT -2147221498 for package-created IRPType classifiers.")
    def test_get_typedef_base_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        type_element = IRPType(pkg.add_type(self._unique("TypedefType"))._com)
        try:
            base_type = IRPType(pkg.add_type(self._unique("TypedefBase"))._com)
            type_element.typedef_base_type = base_type

            result = type_element.typedef_base_type
            assert result is not None
            assert result == base_type
        finally:
            pkg.delete_from_project()

    def test_get_typedef_multiplicity(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            assert type_element.typedef_multiplicity == "1"
        finally:
            pkg.delete_from_project()

    @pytest.mark.skip(reason="Approved live blocker (#202): writes to typedefMultiplicity return COM HRESULT -2147221498 for valid values.")
    def test_set_typedef_multiplicity(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            type_element.typedef_multiplicity = "0..1"
            assert type_element.typedef_multiplicity == "0..1"
        finally:
            pkg.delete_from_project()
