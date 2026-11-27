"""Integration tests for IRPCallOperation with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_call_operation import IRPCallOperation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState


@pytest.mark.integration
class TestIRPCallOperationIntegration:
    """Integration tests for IRPCallOperation with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _call_operation(pkg: IRPPackage) -> tuple[IRPPackage, IRPCallOperation]:
        activity = pkg.add_activity_diagram()
        assert isinstance(activity, IRPFlowchart)
        root = activity.root_state
        assert isinstance(root, IRPState)
        call = activity.add_call_operation(f"CallOp_{uuid.uuid4().hex[:8]}", root)
        assert isinstance(call, IRPCallOperation)
        return pkg, call

    def test_operation(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("OperationPkg"))
        try:
            _, call = self._call_operation(pkg)
            operation = pkg.add_class(self._unique("OpOwner")).add_operation(self._unique("MyOperation"))
            call.operation = operation
            result = call.operation
            assert result is not None
            assert result == operation
        finally:
            pkg.delete_from_project()

    def test_target(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TargetPkg"))
        try:
            _, call = self._call_operation(pkg)
            class_a = pkg.add_class(self._unique("TargetA"))
            class_b = pkg.add_class(self._unique("TargetB"))
            relation = class_a.add_relation_to(class_b, "source", "Association", "1", "target", "Association", "1", "")
            call.target = relation
            result = call.target
            assert result is not None
            assert result == relation
        finally:
            pkg.delete_from_project()
