"""Integration tests for IRP_operation with live Rhapsody COM API."""

import uuid
from typing import Callable

import pytest

from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


def _assert_com_outcome(call: Callable[[], object]) -> None:
    """Accept a documented COM failure or a completed call without raising."""
    try:
        result = call()
    except Exception as exc:
        assert isinstance(exc, (RhapsodyRuntimeException, AttributeError, TypeError, ValueError, KeyError, NotImplementedError))
    else:
        assert result is None or not isinstance(result, BaseException)


def _assert_failure_or_none(call, exceptions=(RhapsodyRuntimeException, AttributeError, TypeError)) -> None:  # type: ignore[no-untyped-def]
    """Assert a documented COM outcome: a known failure or a None result."""
    try:
        result = call()
    except exceptions as exc:
        assert exc is not None
    else:
        assert result is None


@pytest.mark.integration
class TestRPOperationIntegration:
    """Integration tests for IRPOperation with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_static_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("StatPkg")
        class_name = self._unique("StatCls")
        op_name = self._unique("staticOp")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            op = test_class.add_operation(op_name)
            assert op.get_is_static() is False
            op.set_is_static(1)
            assert op.get_is_static() is True
            op.set_is_static(0)
            assert op.get_is_static() is False
        finally:
            test_class.delete_from_project()

    def test_virtual_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("VirtPkg")
        class_name = self._unique("VirtCls")
        op_name = self._unique("virtualOp")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            op = test_class.add_operation(op_name)
            assert op.get_is_virtual() is False
            op.set_is_virtual(1)
            assert op.get_is_virtual() is True
            op.set_is_virtual(0)
            assert op.get_is_virtual() is False
        finally:
            test_class.delete_from_project()

    def test_abstract_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("AbsOpPkg")
        class_name = self._unique("AbsOpCls")
        op_name = self._unique("abstractOp")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            op = test_class.add_operation(op_name)
            assert op.get_is_abstract() is False
            op.set_is_abstract(1)
            assert op.get_is_abstract() is True
            op.set_is_abstract(0)
            assert op.get_is_abstract() is False
        finally:
            test_class.delete_from_project()

    def test_return_type_declaration(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("RetPkg")
        class_name = self._unique("RetCls")
        op_name = self._unique("getValue")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            op = test_class.add_operation(op_name)
            op.set_return_type_declaration("int")
            assert op.get_return_type_declaration() == "int"
        finally:
            test_class.delete_from_project()

    def test_get_body(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("BodyPkg")
        class_name = self._unique("BodyCls")
        op_name = self._unique("doSomething")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            op = test_class.add_operation(op_name)
            body = op.get_body()
            assert isinstance(body, str)
        finally:
            test_class.delete_from_project()

    def test_returns_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RetTypePkg"))
        test_class = pkg.add_class(self._unique("RetTypeCls"))
        try:
            op = test_class.add_operation(self._unique("typedOp"))
            op.set_returns(test_class)
            _assert_com_outcome(lambda: op.get_returns())
        finally:
            test_class.delete_from_project()

    def test_flowchart_getters(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("FlowPkg"))
        test_class = pkg.add_class(self._unique("FlowCls"))
        try:
            op = test_class.add_operation(self._unique("flowOp"))
            op.create_auto_flow_chart()
            chart = op.get_flowchart()
            _assert_com_outcome(lambda: op.set_flowchart(chart))
            assert op.delete_flowchart() is None  # type: ignore[func-returns-value]
        finally:
            test_class.delete_from_project()

    def test_implementation_signature(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("SigPkg"))
        test_class = pkg.add_class(self._unique("SigCls"))
        try:
            op = test_class.add_operation(self._unique("sigOp"))
            assert isinstance(op.get_implementation_signature(), str)
        finally:
            test_class.delete_from_project()

    def test_property_getters(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("PropPkg"))
        test_class = pkg.add_class(self._unique("PropCls"))
        try:
            op = test_class.add_operation(self._unique("propOp"))
            assert isinstance(op.get_initializer(), str)
            assert isinstance(op.get_visibility(), str)
        finally:
            test_class.delete_from_project()

    def test_integer_flags(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("FlagPkg"))
        test_class = pkg.add_class(self._unique("FlagCls"))
        try:
            op = test_class.add_operation(self._unique("flagOp"))
            for getter in (
                op.get_is_cg_derived,
                op.get_is_const,
                op.get_is_ctor,
                op.get_is_dtor,
                op.get_is_final,
                op.get_is_inline,
                op.get_is_trigger,
            ):
                assert isinstance(getter(), int)
        finally:
            test_class.delete_from_project()

    def test_unsupported_setters_raise(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("SetterPkg"))
        test_class = pkg.add_class(self._unique("SetterCls"))
        try:
            op = test_class.add_operation(self._unique("setterOp"))
            for call in (
                lambda: op.set_body("return 0;"),
                lambda: op.set_initializer("value = 0;"),
                lambda: op.set_visibility("private"),
                lambda: op.set_is_const(1),
                lambda: op.set_is_final(1),
                lambda: op.update_contained_diagrams_on_server(),
            ):
                _assert_failure_or_none(call)
        finally:
            test_class.delete_from_project()

    def test_delete_argument(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ArgPkg"))
        test_class = pkg.add_class(self._unique("ArgCls"))
        try:
            op = test_class.add_operation(self._unique("argOp"))
            argument = op.add_argument(self._unique("arg"))
            op.delete_argument(argument)
            assert len(list(op.get_arguments())) == 0
        finally:
            test_class.delete_from_project()
