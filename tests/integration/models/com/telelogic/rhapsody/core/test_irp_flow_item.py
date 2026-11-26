"""Integration tests for IRPFlowItem with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flow_item import IRPFlowItem
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPFlowItemIntegration:
    """Integration tests for IRPFlowItem with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _flow_item(pkg: IRPPackage) -> IRPFlowItem:
        item = pkg.add_flow_items(f"FlowItem_{uuid.uuid4().hex[:8]}")
        assert isinstance(item, IRPFlowItem)
        return item

    def test_add_represented(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AddRepresentedPkg"))
        try:
            flow_item = self._flow_item(pkg)
            represented = pkg.add_class(self._unique("AddRepresentedClass"))
            flow_item.add_represented(represented)
            assert represented in list(flow_item.represented)
        finally:
            pkg.delete_from_project()

    def test_remove_represented(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("RemoveRepresentedPkg"))
        try:
            flow_item = self._flow_item(pkg)
            represented = pkg.add_class(self._unique("RemoveRepresentedClass"))
            flow_item.add_represented(represented)
            flow_item.remove_represented(represented)
            assert represented not in list(flow_item.represented)
        finally:
            pkg.delete_from_project()
