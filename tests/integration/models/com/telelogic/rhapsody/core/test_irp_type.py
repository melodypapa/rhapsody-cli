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

    def test_is_predicates_and_flags_read_as_ints_on_plain_type(self, test_project: IRPProject) -> None:
        """Every is_*/typedef flag resolves through the live COM binding and
        returns an int-typed value; semantic pins live in the enumeration test."""
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
            for flag in (
                type_element.is_predefined,
                type_element.is_typedef,
                type_element.is_typedef_constant,
                type_element.is_typedef_ordered,
                type_element.is_typedef_reference,
            ):
                assert flag in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_is_enum_flags_follow_kind(self, test_project: IRPProject) -> None:
        """An Enumeration-kind type must report the enum predicates as set —
        the two is_* predicates whose live semantics are unambiguous."""
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            type_element.kind = "Enumeration"
            assert type_element.is_enum() == 1
            assert type_element.is_kind_enumeration() == 1
        finally:
            pkg.delete_from_project()

    def test_get_typedef_base_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            assert ti.typedef_base_type is None
        finally:
            pkg.delete_from_project()

    def test_get_typedef_multiplicity(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            # Live 2026-11-25: typedefMultiplicity is readable but every write
            # faults with COM HRESULT -2147221498, so the setter is a recorded
            # blocker (index.md) and the getter asserts the observed default.
            value = type_element.typedef_multiplicity
            assert value in {"1", "0..1"}
        finally:
            pkg.delete_from_project()
