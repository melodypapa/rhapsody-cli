"""Integration tests for IRPOperation with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPOperationIntegration:
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
            assert op.create_auto_flow_chart() is None  # type: ignore[func-returns-value]
            # This build does not expose a chart through the flowchart property
            # after createAutoFlowChart(); assert the real COM-returned value.
            assert op.flowchart is None
            assert op.delete_flowchart() is None
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
            assert op.initializer in ("", "0") or op.initializer.startswith("class ")
            assert op.visibility in {"public", "private", "protected"}
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
                assert getattr(op, attribute) in (0, 1)
        finally:
            test_class.delete_from_project()

    def test_property_setters_round_trip(self, test_project: IRPProject) -> None:
        """Set each writable property through the real COM binding and read it
        back; JavaDoc IRPOperation.updateContainedDiagramsOnServer exists but
        pywin32 does not expose it, so the documented stub raises."""
        pkg = self._create_package(test_project, self._unique("SetterPkg"))
        test_class = pkg.add_class(self._unique("SetterCls"))
        try:
            op = test_class.add_operation(self._unique("setterOp"))
            op.body = "return 0;"
            assert op.body == "return 0;"
            op.visibility = "private"
            assert op.visibility == "private"
            op.is_const = 1
            assert op.is_const == 1
            op.is_final = 1
            assert op.is_final == 1
            with pytest.raises(NotImplementedError):
                op.update_contained_diagrams_on_server(1)
        finally:
            test_class.delete_from_project()

    def test_delete_argument(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ArgPkg"))
        test_class = pkg.add_class(self._unique("ArgCls"))
        try:
            op = test_class.add_operation(self._unique("argOp"))
            argument = op.add_argument(self._unique("Argument"))
            op.delete_argument(argument)
            assert len(list(op.arguments)) == 0
        finally:
            test_class.delete_from_project()
