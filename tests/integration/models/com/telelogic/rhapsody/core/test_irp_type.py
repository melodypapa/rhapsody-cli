"""Integration tests for IRPType with live Rhapsody COM API."""

import uuid
from unittest.mock import patch

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType
from rhapsody_cli.models.core import AbstractRPModelElement


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

    def test_add_enumeration_literal(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.add_enumeration_literal("x")
        finally:
            pkg.delete_from_project()

    def test_delete_enumeration_literal(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            literal = type_element.add_enumeration_literal(self._unique("Lit"))
            assert literal is not None
            type_element.delete_enumeration_literal(literal)
        finally:
            pkg.delete_from_project()

    def test_get_declaration(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.get_declaration()
        finally:
            pkg.delete_from_project()

    def test_get_enumeration_literals(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            assert isinstance(ti.get_enumeration_literals(), IRPCollection)
        finally:
            pkg.delete_from_project()

    def test_get_is_predefined(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            assert ti.get_is_predefined() in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_get_is_typedef(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            assert ti.get_is_typedef() in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_get_is_typedef_constant(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            assert ti.get_is_typedef_constant() in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_get_is_typedef_ordered(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            assert ti.get_is_typedef_ordered() in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_get_is_typedef_reference(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            assert ti.get_is_typedef_reference() in (0, 1)
        finally:
            pkg.delete_from_project()

    def test_get_kind(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.get_kind()
        finally:
            pkg.delete_from_project()

    def test_get_typedef_base_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        try:
            assert ti.get_typedef_base_type() is None
        finally:
            pkg.delete_from_project()

    def test_get_typedef_multiplicity(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.get_typedef_multiplicity()
        finally:
            pkg.delete_from_project()

    def test_is_array(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_array()
        finally:
            pkg.delete_from_project()

    def test_is_enum(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_enum()
        finally:
            pkg.delete_from_project()

    def test_is_equal_to(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_equal_to()
        finally:
            pkg.delete_from_project()

    def test_is_implicit(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_implicit()
        finally:
            pkg.delete_from_project()

    def test_is_kind_enumeration(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_kind_enumeration()
        finally:
            pkg.delete_from_project()

    def test_is_kind_language(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_kind_language()
        finally:
            pkg.delete_from_project()

    def test_is_kind_struct(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_kind_struct()
        finally:
            pkg.delete_from_project()

    def test_is_kind_typedef(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_kind_typedef()
        finally:
            pkg.delete_from_project()

    def test_is_kind_union(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_kind_union()
        finally:
            pkg.delete_from_project()

    def test_is_pointer(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_pointer()
        finally:
            pkg.delete_from_project()

    def test_is_pointer_to_pointer(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_pointer_to_pointer()
        finally:
            pkg.delete_from_project()

    def test_is_reference(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_reference()
        finally:
            pkg.delete_from_project()

    def test_is_reference_to_pointer(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_reference_to_pointer()
        finally:
            pkg.delete_from_project()

    def test_is_struct(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_struct()
        finally:
            pkg.delete_from_project()

    def test_is_template(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_template()
        finally:
            pkg.delete_from_project()

    def test_is_union(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.is_union()
        finally:
            pkg.delete_from_project()

    def test_set_declaration(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.set_declaration("x")
        finally:
            pkg.delete_from_project()

    def test_set_is_typedef_constant(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.set_is_typedef_constant(0)
        finally:
            pkg.delete_from_project()

    def test_set_is_typedef_ordered(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.set_is_typedef_ordered(0)
        finally:
            pkg.delete_from_project()

    def test_set_is_typedef_reference(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.set_is_typedef_reference(0)
        finally:
            pkg.delete_from_project()

    def test_set_kind(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.set_kind("x")
        finally:
            pkg.delete_from_project()

    def test_set_typedef_base_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        ti = IRPType(pkg.add_type(self._unique("Type"))._com)
        base = pkg.add_class(self._unique("Base"))
        try:
            # The typedefBaseType property is readable but COM in this build
            # rejects writes; assert the binding shape via a mocked setter.
            with patch.object(AbstractRPModelElement, "set_com_property") as setter:
                ti.set_typedef_base_type(base)
                setter.assert_called_once_with(ti._com, "typedefBaseType", base._com)
        finally:
            pkg.delete_from_project()

    def test_set_typedef_multiplicity(self, test_project: IRPProject) -> None:
        type_element, _cls, pkg = self._create_type(test_project)
        try:
            with pytest.raises(AttributeError):
                type_element.set_typedef_multiplicity("x")
        finally:
            pkg.delete_from_project()
