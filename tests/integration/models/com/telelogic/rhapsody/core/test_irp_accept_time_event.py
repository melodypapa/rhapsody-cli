"""Integration tests for IRPAcceptTimeEvent with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_accept_time_event import IRPAcceptTimeEvent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState


@pytest.mark.integration
class TestIRPAcceptTimeEventIntegration:
    """Integration tests for IRPAcceptTimeEvent with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _accept_time_event(pkg: IRPPackage) -> tuple[IRPPackage, IRPAcceptTimeEvent]:
        activity = pkg.add_activity_diagram()
        assert isinstance(activity, IRPFlowchart)
        root = activity.root_state
        assert isinstance(root, IRPState)
        element = activity.add_accept_time_event(f"AcceptTime_{uuid.uuid4().hex[:8]}", root)
        assert isinstance(element, IRPAcceptTimeEvent)
        return pkg, element

    def test_duration_time(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("DurationPkg"))
        try:
            _, element = self._accept_time_event(pkg)
            duration = "5s"
            element.duration_time = duration
            assert element.duration_time == duration
        finally:
            pkg.delete_from_project()
