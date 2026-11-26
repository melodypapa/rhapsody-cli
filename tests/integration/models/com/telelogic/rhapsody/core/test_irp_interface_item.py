"""Integration tests for IRPInterfaceItem with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPInterfaceItemIntegration:
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
            pkg.delete_from_project()

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
            first_argument = operation.add_argument(arg1_name)
            third_argument = operation.add_argument(arg3_name)
            inserted_argument = operation.add_argument_before_position(arg2_name, 1)
            args = list(operation.arguments)
            assert args == [inserted_argument, first_argument, third_argument]
        finally:
            pkg.delete_from_project()

    def test_signature_methods(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("SigPkg")
        class_name = self._unique("SigCls")
        op_name = self._unique("sigOp")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            operation = test_class.add_operation(op_name)
            argument_name = self._unique("sigArg")
            operation.add_argument(argument_name)
            sig = operation.signature
            assert sig == f"{op_name}(int {argument_name})"
            no_names = operation.get_signature_no_arg_names()
            assert no_names == f"{op_name}(int)"
            no_types = operation.get_signature_no_arg_types()
            assert no_types == f"{op_name}({argument_name})"
        finally:
            pkg.delete_from_project()

    def test_match_on_signature(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("MatchPkg")
        class_name = self._unique("MatchCls")
        matching_class_name = self._unique("MatchingCls")
        nonmatching_class_name = self._unique("NonmatchingCls")
        op_name = self._unique("matchOp")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        matching_class = pkg.add_class(matching_class_name)
        nonmatching_class = pkg.add_class(nonmatching_class_name)
        try:
            op1 = test_class.add_operation(op_name)
            op2 = matching_class.add_operation(op_name)
            op3 = nonmatching_class.add_operation(op_name)
            # JavaDoc compares operation signatures. Separate classes permit
            # authentic equal signatures without creating a duplicate in one class.
            match_arg = self._unique("MatchArg")
            other_arg = self._unique("OtherArg")
            op1.add_argument(match_arg)
            op2.add_argument(match_arg)
            nonmatching_argument = op3.add_argument(other_arg)
            nonmatching_argument.set_declaration("char")
            assert op1.match_on_signature(op2) is True
            assert op1.match_on_signature(op3) is False
        finally:
            pkg.delete_from_project()
