"""Integration tests for IRPSendAction with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
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
    def _send_action(pkg: IRPPackage) -> tuple[IRPPackage, IRPClass, IRPSendAction]:
        owner = pkg.add_class(f"{pkg.name}_Owner")
        statechart = owner.add_statechart()
        root = statechart.root_state
        assert root is not None
        state = root.add_state(f"State_{uuid.uuid4().hex[:8]}")
        state.set_state_type("EventState")
        send_action = state.get_send_action()
        assert isinstance(send_action, IRPSendAction)
        return pkg, owner, send_action

    def test_event(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("EventPkg"))
        try:
            _, _, send_action = self._send_action(pkg)
            event = IRPEvent(pkg.add_event(self._unique("Event"))._com)
            send_action.event = event
            result = send_action.event
            assert result is not None
            assert result == event
        finally:
            pkg.delete_from_project()

    @pytest.mark.skip(reason="Approved live blocker (#202): after EventState, event, object target, and class-owned operation are set, invokedOperation readback remains None.")
    def test_invoked_operation(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("InvokedPkg"))
        try:
            _, owner, send_action = self._send_action(pkg)
            target_element = pkg.add_global_object(self._unique("InvokedTarget"), owner.name, pkg.name)
            send_action.target = IRPInstance(target_element._com)
            event = IRPEvent(pkg.add_event(self._unique("InvokedEvent"))._com)
            send_action.event = event
            operation = owner.add_operation(self._unique("InvokedOperation"))
            send_action.invoked_operation = operation
            result = send_action.invoked_operation
            assert result is not None
            assert result == operation
        finally:
            pkg.delete_from_project()

    def test_target(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TargetPkg"))
        try:
            _, _, send_action = self._send_action(pkg)
            target_class = pkg.add_class(self._unique("TargetClass"))
            target_element = pkg.add_global_object(self._unique("TargetObject"), target_class.name, pkg.name)
            target = IRPInstance(target_element._com)
            send_action.target = target
            result = send_action.target
            assert result is not None
            assert result == target
        finally:
            pkg.delete_from_project()

    def test_add_argument_value(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AddArgPkg"))
        try:
            _, _, send_action = self._send_action(pkg)
            event = IRPEvent(pkg.add_event(self._unique("ArgEvent"))._com)
            event.add_argument(self._unique("Arg"))
            send_action.event = event

            send_action.add_argument_value("1", 1)

            assert "1" in list(send_action.arg_vals)
        finally:
            pkg.delete_from_project()
