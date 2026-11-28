"""Integration tests for IRPNode with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_node import IRPNode
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPNodeIntegration:
    """Integration tests for IRPNode with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _node(pkg: IRPPackage) -> tuple[IRPPackage, IRPNode]:
        element = pkg.add_node(f"Node_{uuid.uuid4().hex[:8]}")
        node = IRPNode(element._com)
        assert isinstance(node, IRPNode)
        return pkg, node

    def test_cpu_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("CpuPkg"))
        try:
            _, node = self._node(pkg)
            node.cpu_type = "ARM"
            assert node.cpu_type == "ARM"
        finally:
            pkg.delete_from_project()

    def test_component_instances(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("InstancesPkg"))
        try:
            _, node = self._node(pkg)
            instance = node.add_component_instance(self._unique("Instance"))
            assert instance in list(node.component_instances)
        finally:
            pkg.delete_from_project()

    def test_find_component_instance(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("FindPkg"))
        try:
            _, node = self._node(pkg)
            created = node.add_component_instance(self._unique("Instance"))
            found = node.find_component_instance(created.name)
            assert found is not None
            assert found == created
        finally:
            pkg.delete_from_project()
