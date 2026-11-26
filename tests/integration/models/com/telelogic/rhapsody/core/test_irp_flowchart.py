"""Integration tests for IRPFlowchart with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions import IRPAcceptEventAction, IRPAcceptTimeEvent, IRPCallOperation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPActivityDiagram
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPPin
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_object_node import IRPObjectNode
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_swimlane import IRPSwimlane


@pytest.mark.integration
class TestIRPFlowchartIntegration:
    """Integration tests for IRPFlowchart with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _activity(pkg: IRPPackage) -> IRPFlowchart:
        flowchart = pkg.add_activity_diagram()
        assert isinstance(flowchart, IRPFlowchart)
        return flowchart

    def _root(self, flowchart: IRPFlowchart) -> IRPState:
        root = flowchart.root_state
        assert isinstance(root, IRPState)
        return root

    def test_is_analysis_only(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AnalysisOnlyPkg"))
        try:
            flowchart = self._activity(pkg)
            flowchart.is_analysis_only = 1
            assert flowchart.is_analysis_only == 1
        finally:
            pkg.delete_from_project()

    def test_its_owner(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("OwnerPkg"))
        try:
            flowchart = self._activity(pkg)
            owner = pkg.add_class(self._unique("OwnerClass")).add_operation(self._unique("OwnerOp"))
            flowchart.its_owner = owner
            result = flowchart.its_owner
            assert result is not None
            assert result._com is owner._com
        finally:
            pkg.delete_from_project()

    def test_swimlanes(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("SwimlanesPkg"))
        try:
            flowchart = self._activity(pkg)
            lane = flowchart.add_swimlane(self._unique("Lane"))
            assert lane in list(flowchart.swimlanes)
        finally:
            pkg.delete_from_project()

    def test_add_accept_event_action(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AcceptEventPkg"))
        try:
            flowchart = self._activity(pkg)
            created = flowchart.add_accept_event_action(self._unique("AcceptEvent"), self._root(flowchart))
            assert isinstance(created, IRPAcceptEventAction)
        finally:
            pkg.delete_from_project()

    def test_add_accept_time_event(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AcceptTimePkg"))
        try:
            flowchart = self._activity(pkg)
            created = flowchart.add_accept_time_event(self._unique("AcceptTime"), self._root(flowchart))
            assert isinstance(created, IRPAcceptTimeEvent)
        finally:
            pkg.delete_from_project()

    def test_add_activity_parameter(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ActivityParamPkg"))
        try:
            flowchart = self._activity(pkg)
            created = flowchart.add_activity_parameter(self._unique("Param"))
            assert isinstance(created, IRPPin)
        finally:
            pkg.delete_from_project()

    def test_add_call_behavior(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("CallBehaviorPkg"))
        try:
            flowchart = self._activity(pkg)
            referenced = self._activity(pkg)
            created = flowchart.add_call_behavior(referenced)
            assert isinstance(created, IRPState)
        finally:
            pkg.delete_from_project()

    def test_add_call_operation(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("CallOperationPkg"))
        try:
            flowchart = self._activity(pkg)
            created = flowchart.add_call_operation(self._unique("CallOp"), self._root(flowchart))
            assert isinstance(created, IRPCallOperation)
        finally:
            pkg.delete_from_project()

    def test_add_object_node(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ObjectNodePkg"))
        try:
            flowchart = self._activity(pkg)
            created = flowchart.add_object_node(self._unique("ObjectNode"), self._root(flowchart))
            assert isinstance(created, IRPObjectNode)
        finally:
            pkg.delete_from_project()

    def test_add_reference_activity(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ReferenceActivityPkg"))
        try:
            flowchart = self._activity(pkg)
            referenced = self._activity(pkg)
            created = flowchart.add_reference_activity(referenced)
            assert isinstance(created, IRPState)
        finally:
            pkg.delete_from_project()

    def test_add_swimlane(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AddSwimlanePkg"))
        try:
            flowchart = self._activity(pkg)
            created = flowchart.add_swimlane(self._unique("Lane"))
            assert isinstance(created, IRPSwimlane)
        finally:
            pkg.delete_from_project()

    def test_get_flowchart_diagram(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("DiagramPkg"))
        try:
            flowchart = self._activity(pkg)
            diagram = flowchart.get_flowchart_diagram()
            assert isinstance(diagram, IRPActivityDiagram)
        finally:
            pkg.delete_from_project()
