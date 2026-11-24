"""Integration tests for IRP_operation with live Rhapsody COM API."""

import uuid
from unittest.mock import patch

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


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
            assert op.is_static is False
            op.is_static = True
            assert op.is_static is True
            op.is_static = False
            assert op.is_static is False
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
            assert op.is_virtual is False
            op.is_virtual = True
            assert op.is_virtual is True
            op.is_virtual = False
            assert op.is_virtual is False
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
            assert op.is_abstract is False
            op.is_abstract = True
            assert op.is_abstract is True
            op.is_abstract = False
            assert op.is_abstract is False
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

    def test_body(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("BodyPkg")
        class_name = self._unique("BodyCls")
        op_name = self._unique("doSomething")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            op = test_class.add_operation(op_name)
            original_body = op.body
            body = "return 42;"
            op.body = body
            assert op.body == body
            op.body = original_body
            assert op.body == original_body
        finally:
            test_class.delete_from_project()

    def test_returns_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RetTypePkg"))
        test_class = pkg.add_class(self._unique("RetTypeCls"))
        try:
            op = test_class.add_operation(self._unique("typedOp"))
            op.returns = test_class
            assert op.returns.name == test_class.name
        finally:
            test_class.delete_from_project()

    def test_flowchart_getters(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("FlowPkg"))
        test_class = pkg.add_class(self._unique("FlowCls"))
        try:
            op = test_class.add_operation(self._unique("flowOp"))
            op.create_auto_flow_chart()
            chart = op.flowchart
            assert chart is not None
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
            assert isinstance(op.initializer, str)
            assert isinstance(op.visibility, str)
        finally:
            test_class.delete_from_project()

    def test_integer_flags(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("FlagPkg"))
        test_class = pkg.add_class(self._unique("FlagCls"))
        try:
            op = test_class.add_operation(self._unique("flagOp"))
            for attribute in (
                "is_cg_derived",
                "is_const",
                "is_ctor",
                "is_dtor",
                "is_final",
                "is_inline",
                "is_trigger",
            ):
                assert isinstance(getattr(op, attribute), int)
        finally:
            test_class.delete_from_project()

    def test_property_setters_binding_shape(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("SetterPkg"))
        test_class = pkg.add_class(self._unique("SetterCls"))
        try:
            op = test_class.add_operation(self._unique("setterOp"))
            # Property-shaped setters bind to documented COM properties.
            with patch.object(IRPModelElement, "set_com_property") as setter:
                op.body = "return 0;"
                setter.assert_called_once_with(op._com, "body", "return 0;")
            with patch.object(IRPModelElement, "set_com_property") as setter:
                op.initializer = "value = 0;"
                setter.assert_called_once_with(op._com, "initializer", "value = 0;")
            with patch.object(IRPModelElement, "set_com_property") as setter:
                op.visibility = "private"
                setter.assert_called_once_with(op._com, "visibility", "private")
            with patch.object(IRPModelElement, "set_com_property") as setter:
                op.is_const = 1
                setter.assert_called_once_with(op._com, "isConst", 1)
            with patch.object(IRPModelElement, "set_com_property") as setter:
                op.is_final = 1
                setter.assert_called_once_with(op._com, "isFinal", 1)
            with pytest.raises(NotImplementedError):
                op.update_contained_diagrams_on_server(1)
        finally:
            test_class.delete_from_project()

    def test_delete_argument(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ArgPkg"))
        test_class = pkg.add_class(self._unique("ArgCls"))
        try:
            op = test_class.add_operation(self._unique("argOp"))
            argument = op.add_argument(self._unique("arg"))
            op.delete_argument(argument)
            assert len(list(op.arguments)) == 0
        finally:
            test_class.delete_from_project()
