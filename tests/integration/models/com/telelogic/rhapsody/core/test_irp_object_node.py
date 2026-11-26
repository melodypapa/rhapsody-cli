"""Integration tests for IRPObjectNode with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flowchart import IRPFlowchart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_object_node import IRPObjectNode
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState


@pytest.mark.integration
class TestIRPObjectNodeIntegration:
    """Integration tests for IRPObjectNode with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _node(pkg: IRPPackage) -> tuple[IRPPackage, IRPObjectNode, IRPState]:
        activity = pkg.add_activity_diagram()
        assert isinstance(activity, IRPFlowchart)
        root = activity.root_state
        assert isinstance(root, IRPState)
        node = activity.add_object_node(f"ObjectNode_{uuid.uuid4().hex[:8]}", root)
        assert isinstance(node, IRPObjectNode)
        return pkg, node, root

    def test_in_state(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("InStatePkg"))
        try:
            _, node, _ = self._node(pkg)
            value = "Active"
            node.in_state = value
            assert node.in_state == value
        finally:
            pkg.delete_from_project()

    def test_in_state_list(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("InStateListPkg"))
        try:
            _, node, root = self._node(pkg)
            state = root.add_state(self._unique("InState"))
            node.add_in_state(state)
            assert state in list(node.in_state_list)
        finally:
            pkg.delete_from_project()

    def test_represents(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("RepresentsPkg"))
        try:
            _, node, _ = self._node(pkg)
            represented = pkg.add_class(self._unique("RepresentedClass"))
            node.represents = represented
            result = node.represents
            assert result is not None
            assert result._com is represented._com
        finally:
            pkg.delete_from_project()

    def test_add_in_state(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AddInStatePkg"))
        try:
            _, node, root = self._node(pkg)
            state = root.add_state(self._unique("AddedState"))
            node.add_in_state(state)
            assert state in list(node.in_state_list)
        finally:
            pkg.delete_from_project()

    def test_remove_in_state(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("RemoveInStatePkg"))
        try:
            _, node, root = self._node(pkg)
            state = root.add_state(self._unique("RemovedState"))
            node.add_in_state(state)
            node.remove_in_state(state)
            assert state not in list(node.in_state_list)
        finally:
            pkg.delete_from_project()
