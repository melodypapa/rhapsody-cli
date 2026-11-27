"""Integration tests for IRPComponentInstance with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component_instance import IRPComponentInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_node import IRPNode
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPComponentInstanceIntegration:
    """Integration tests for IRPComponentInstance with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _instance(pkg: IRPPackage) -> tuple[IRPPackage, IRPNode, IRPComponentInstance]:
        node = IRPNode(pkg.add_node(f"Node_{uuid.uuid4().hex[:8]}")._com)
        instance = node.add_component_instance(f"Instance_{uuid.uuid4().hex[:8]}")
        assert isinstance(instance, IRPComponentInstance)
        return pkg, node, instance

    def test_component_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        try:
            _, _, instance = self._instance(pkg)
            component = IRPComponent(pkg.add_new_aggr("Component", self._unique("Component"))._com)
            instance.component_type = component
            result = instance.component_type
            assert result is not None
            assert result._com is component._com
        finally:
            pkg.delete_from_project()

    def test_node(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("NodePkg"))
        try:
            _, node, instance = self._instance(pkg)
            result = instance.node
            assert result is not None
            assert result._com is node._com
        finally:
            pkg.delete_from_project()
