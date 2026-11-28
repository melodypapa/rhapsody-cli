"""Integration tests for IRPAcceptEventAction with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_accept_event_action import IRPAcceptEventAction
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState


@pytest.mark.integration
class TestIRPAcceptEventActionIntegration:
    """Live COM tests for IRPAcceptEventAction's own API."""

    @staticmethod
    def _unique(prefix: str) -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_event(self, test_project: IRPProject) -> None:
        package = test_project.add_package(self._unique("AcceptEventActionPkg"))
        try:
            flowchart = package.add_activity_diagram()
            assert isinstance(flowchart, IRPFlowchart)
            root_state = flowchart.root_state
            assert isinstance(root_state, IRPState)
            action = flowchart.add_accept_event_action(self._unique("AcceptEventAction"), root_state)
            assert isinstance(action, IRPAcceptEventAction)
            event = package.add_event(self._unique("AcceptedEvent"))
            assert isinstance(event, IRPEvent)

            action.event = event

            assert action.event == event
        finally:
            package.delete_from_project()
