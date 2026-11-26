"""Integration tests for IRPSwimlane with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPConnector
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_swimlane import IRPSwimlane


@pytest.mark.integration
class TestIRPSwimlaneIntegration:
    """Integration tests for IRPSwimlane with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _lane(pkg: IRPPackage) -> tuple[IRPPackage, IRPFlowchart, IRPSwimlane]:
        activity = pkg.add_activity_diagram()
        assert isinstance(activity, IRPFlowchart)
        lane = activity.add_swimlane(f"Lane_{uuid.uuid4().hex[:8]}")
        assert isinstance(lane, IRPSwimlane)
        return pkg, activity, lane

    def test_contents(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ContentsPkg"))
        try:
            _, activity, lane = self._lane(pkg)
            root = activity.root_state
            assert root is not None
            state = root.add_state(self._unique("ConnectorOwner"))
            connector = state.add_connector("Condition")
            assert isinstance(connector, IRPConnector)
            # JavaDoc IRPConnector.setItsSwimlane places the connector in the lane.
            connector.set_its_swimlane(lane)
            assert connector in list(lane.contents)
        finally:
            pkg.delete_from_project()

    def test_represents(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("RepresentsPkg"))
        try:
            _, _, lane = self._lane(pkg)
            represented = pkg.add_class(self._unique("RepresentsClass"))
            lane.represents = represented
            result = lane.represents
            assert result is not None
            assert result._com is represented._com
        finally:
            pkg.delete_from_project()

    def test_swimlanes(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("NestedLanesPkg"))
        try:
            _, _, lane = self._lane(pkg)
            nested = lane.add_swimlane(self._unique("NestedLane"))
            assert nested in list(lane.swimlanes)
        finally:
            pkg.delete_from_project()

    def test_add_swimlane(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AddLanePkg"))
        try:
            _, _, lane = self._lane(pkg)
            nested = lane.add_swimlane(self._unique("NestedLane"))
            assert isinstance(nested, IRPSwimlane)
        finally:
            pkg.delete_from_project()
