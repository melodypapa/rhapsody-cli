"""Integration tests for IRPSendAction with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_send_action import IRPSendAction


@pytest.mark.integration
class TestIRPSendActionIntegration:
    """Integration tests for IRPSendAction with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _send_action(pkg: IRPPackage) -> tuple[IRPPackage, IRPSendAction]:
        owner = pkg.add_class(f"{pkg.name}_Owner")
        statechart = owner.add_statechart()
        root = statechart.root_state
        assert root is not None
        state = root.add_state(f"State_{uuid.uuid4().hex[:8]}")
        send_action = state.get_send_action()
        assert isinstance(send_action, IRPSendAction)
        return pkg, send_action

    def test_arg_vals(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ArgValsPkg"))
        try:
            _, send_action = self._send_action(pkg)
            send_action.add_argument_value("42", 1)
            values = list(send_action.arg_vals)
            assert "42" in values
        finally:
            pkg.delete_from_project()

    def test_event(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("EventPkg"))
        try:
            _, send_action = self._send_action(pkg)
            event = IRPEvent(pkg.add_event(self._unique("Event"))._com)
            send_action.event = event
            result = send_action.event
            assert result is not None
            assert result == event
        finally:
            pkg.delete_from_project()

    def test_invoked_operation(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("InvokedPkg"))
        try:
            _, send_action = self._send_action(pkg)
            operation = IRPEvent(pkg.add_event(self._unique("OpEvent"))._com)
            send_action.invoked_operation = operation
            result = send_action.invoked_operation
            assert result is not None
            assert result == operation
        finally:
            pkg.delete_from_project()

    def test_target(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TargetPkg"))
        try:
            _, send_action = self._send_action(pkg)
            target = pkg.add_class(self._unique("TargetClass"))
            send_action.target = target
            result = send_action.target
            assert result is not None
            assert result == target
        finally:
            pkg.delete_from_project()

    def test_add_argument_value(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AddArgPkg"))
        try:
            _, send_action = self._send_action(pkg)
            send_action.add_argument_value("value1", 1)
            assert "value1" in list(send_action.arg_vals)
        finally:
            pkg.delete_from_project()
