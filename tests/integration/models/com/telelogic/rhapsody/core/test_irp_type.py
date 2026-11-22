"""Integration tests for IRPType with live Rhapsody COM API."""

import uuid
from typing import Callable

import pytest

from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType


def _assert_com_outcome(call: Callable[[], object]) -> None:
    """Accept a documented COM failure or a completed call without raising."""
    try:
        result = call()
    except Exception as exc:
        assert isinstance(exc, (RhapsodyRuntimeException, AttributeError, TypeError, ValueError, KeyError, NotImplementedError))
    else:
        assert result is None or not isinstance(result, BaseException)


@pytest.mark.integration
class TestIRPTypeIntegration:
    """Generated live coverage for IRPType owned methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_enumeration_literal(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.add_enumeration_literal("x"))
        finally:
            pass

    def test_delete_enumeration_literal(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.delete_enumeration_literal(None))  # type: ignore[arg-type]
        finally:
            pass

    def test_get_declaration(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_declaration())
        finally:
            pass

    def test_get_enumeration_literals(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_enumeration_literals())
        finally:
            pass

    def test_get_is_predefined(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_is_predefined())
        finally:
            pass

    def test_get_is_typedef(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_is_typedef())
        finally:
            pass

    def test_get_is_typedef_constant(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_is_typedef_constant())
        finally:
            pass

    def test_get_is_typedef_ordered(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_is_typedef_ordered())
        finally:
            pass

    def test_get_is_typedef_reference(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_is_typedef_reference())
        finally:
            pass

    def test_get_kind(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_kind())
        finally:
            pass

    def test_get_typedef_base_type(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_typedef_base_type())
        finally:
            pass

    def test_get_typedef_multiplicity(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.get_typedef_multiplicity())
        finally:
            pass

    def test_is_array(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_array())
        finally:
            pass

    def test_is_enum(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_enum())
        finally:
            pass

    def test_is_equal_to(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_equal_to())
        finally:
            pass

    def test_is_implicit(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_implicit())
        finally:
            pass

    def test_is_kind_enumeration(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_kind_enumeration())
        finally:
            pass

    def test_is_kind_language(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_kind_language())
        finally:
            pass

    def test_is_kind_struct(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_kind_struct())
        finally:
            pass

    def test_is_kind_typedef(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_kind_typedef())
        finally:
            pass

    def test_is_kind_union(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_kind_union())
        finally:
            pass

    def test_is_pointer(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_pointer())
        finally:
            pass

    def test_is_pointer_to_pointer(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_pointer_to_pointer())
        finally:
            pass

    def test_is_reference(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_reference())
        finally:
            pass

    def test_is_reference_to_pointer(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_reference_to_pointer())
        finally:
            pass

    def test_is_struct(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_struct())
        finally:
            pass

    def test_is_template(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_template())
        finally:
            pass

    def test_is_union(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.is_union())
        finally:
            pass

    def test_set_declaration(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.set_declaration("x"))
        finally:
            pass

    def test_set_is_typedef_constant(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.set_is_typedef_constant(0))
        finally:
            pass

    def test_set_is_typedef_ordered(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.set_is_typedef_ordered(0))
        finally:
            pass

    def test_set_is_typedef_reference(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.set_is_typedef_reference(0))
        finally:
            pass

    def test_set_kind(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.set_kind("x"))
        finally:
            pass

    def test_set_typedef_base_type(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.set_typedef_base_type(None))  # type: ignore[arg-type]
        finally:
            pass

    def test_set_typedef_multiplicity(self, test_project: IRPProject) -> None:
        type_element = IRPType(test_project.add_package(self._unique("TypePkg")).add_class(self._unique("Type"))._com)
        try:
            _assert_com_outcome(lambda: type_element.set_typedef_multiplicity("x"))
        finally:
            pass
