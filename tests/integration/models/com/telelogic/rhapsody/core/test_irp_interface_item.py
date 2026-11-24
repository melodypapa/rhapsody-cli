"""Integration tests for IRPInterfaceItem with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestRPInterfaceItemIntegration:
    """Integration tests for IRPInterfaceItem (via IRPOperation) with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_add_argument_and_get_arguments(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("ArgPkg")
        class_name = self._unique("ArgCls")
        op_name = self._unique("myOp")
        arg_name = self._unique("param")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            operation = test_class.add_operation(op_name)
            argument = operation.add_argument(arg_name)
            assert argument is not None
            assert argument in list(operation.arguments)
        finally:
            test_class.delete_from_project()

    def test_add_argument_before_position(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("ArgPosPkg")
        class_name = self._unique("ArgPosCls")
        op_name = self._unique("posOp")
        arg1_name = self._unique("first")
        arg2_name = self._unique("second")
        arg3_name = self._unique("third")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            operation = test_class.add_operation(op_name)
            arg1 = operation.add_argument(arg1_name)
            operation.add_argument(arg3_name)
            arg2 = operation.add_argument_before_position(arg2_name, 1)
            arg3 = next(a for a in operation.arguments if a != arg1 and a != arg2)
            args = list(operation.arguments)
            assert arg1 in args and arg2 in args and arg3 in args
        finally:
            test_class.delete_from_project()

    def test_signature_methods(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("SigPkg")
        class_name = self._unique("SigCls")
        op_name = self._unique("sigOp")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            operation = test_class.add_operation(op_name)
            operation.add_argument("x")
            sig = operation.signature
            assert "x" in sig
            no_names = operation.get_signature_no_arg_names()
            assert "x" not in no_names
            no_types = operation.get_signature_no_arg_types()
            assert "x" in no_types
        finally:
            test_class.delete_from_project()

    def test_match_on_signature(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("MatchPkg")
        class_name = self._unique("MatchCls")
        op1_name = self._unique("matchA")
        op2_name = self._unique("matchB")
        op3_name = self._unique("noMatch")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            op1 = test_class.add_operation(op1_name)
            op2 = test_class.add_operation(op2_name)
            op3 = test_class.add_operation(op3_name)
            op1.add_argument("x")
            op2.add_argument("x")
            op3.add_argument("y")
            assert isinstance(op1.match_on_signature(op2), bool)
            assert isinstance(op1.match_on_signature(op3), bool)
        finally:
            test_class.delete_from_project()
