"""Integration tests for IRPType with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType


@pytest.mark.integration
class TestIRPTypeIntegration:
    """Generated live coverage for IRPType owned methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_enumeration_literal(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.add_enumeration_literal("x") is not None
        finally:
            pass

    def test_delete_enumeration_literal(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.delete_enumeration_literal(None) is not None  # type: ignore[arg-type,func-returns-value]
        finally:
            pass

    def test_get_declaration(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_declaration() is not None
        finally:
            pass

    def test_get_enumeration_literals(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_enumeration_literals() is not None
        finally:
            pass

    def test_get_is_predefined(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_is_predefined() is not None
        finally:
            pass

    def test_get_is_typedef(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_is_typedef() is not None
        finally:
            pass

    def test_get_is_typedef_constant(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_is_typedef_constant() is not None
        finally:
            pass

    def test_get_is_typedef_ordered(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_is_typedef_ordered() is not None
        finally:
            pass

    def test_get_is_typedef_reference(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_is_typedef_reference() is not None
        finally:
            pass

    def test_get_kind(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_kind() is not None
        finally:
            pass

    def test_get_typedef_base_type(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_typedef_base_type() is not None
        finally:
            pass

    def test_get_typedef_multiplicity(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.get_typedef_multiplicity() is not None
        finally:
            pass

    def test_is_array(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_array() is not None
        finally:
            pass

    def test_is_enum(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_enum() is not None
        finally:
            pass

    def test_is_equal_to(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_equal_to() is not None
        finally:
            pass

    def test_is_implicit(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_implicit() is not None
        finally:
            pass

    def test_is_kind_enumeration(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_kind_enumeration() is not None
        finally:
            pass

    def test_is_kind_language(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_kind_language() is not None
        finally:
            pass

    def test_is_kind_struct(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_kind_struct() is not None
        finally:
            pass

    def test_is_kind_typedef(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_kind_typedef() is not None
        finally:
            pass

    def test_is_kind_union(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_kind_union() is not None
        finally:
            pass

    def test_is_pointer(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_pointer() is not None
        finally:
            pass

    def test_is_pointer_to_pointer(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_pointer_to_pointer() is not None
        finally:
            pass

    def test_is_reference(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_reference() is not None
        finally:
            pass

    def test_is_reference_to_pointer(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_reference_to_pointer() is not None
        finally:
            pass

    def test_is_struct(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_struct() is not None
        finally:
            pass

    def test_is_template(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_template() is not None
        finally:
            pass

    def test_is_union(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.is_union() is not None
        finally:
            pass

    def test_set_declaration(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.set_declaration("x") is not None  # type: ignore[func-returns-value]
        finally:
            pass

    def test_set_is_typedef_constant(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.set_is_typedef_constant(0) is not None  # type: ignore[func-returns-value]
        finally:
            pass

    def test_set_is_typedef_ordered(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.set_is_typedef_ordered(0) is not None  # type: ignore[func-returns-value]
        finally:
            pass

    def test_set_is_typedef_reference(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.set_is_typedef_reference(0) is not None  # type: ignore[func-returns-value]
        finally:
            pass

    def test_set_kind(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.set_kind("x") is not None  # type: ignore[func-returns-value]
        finally:
            pass

    def test_set_typedef_base_type(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.set_typedef_base_type(None) is not None  # type: ignore[arg-type,func-returns-value]
        finally:
            pass

    def test_set_typedef_multiplicity(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            assert type_element.set_typedef_multiplicity("x") is not None  # type: ignore[func-returns-value]
        finally:
            pass
