"""Integration tests for IRPFlow with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_flow import IRPFlow
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_other_model import IRPSysMLPort
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPFlowIntegration:
    """Integration tests for IRPFlow with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _flow(pkg: IRPPackage) -> IRPFlow:
        flow = pkg.add_flows(f"Flow_{uuid.uuid4().hex[:8]}")
        assert isinstance(flow, IRPFlow)
        return flow

    def test_conveyed(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ConveyedPkg"))
        try:
            flow = self._flow(pkg)
            element = pkg.add_class(self._unique("ConveyedClass"))
            flow.add_conveyed(element)
            assert element in list(flow.conveyed)
        finally:
            pkg.delete_from_project()

    def test_direction(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("DirectionPkg"))
        try:
            flow = self._flow(pkg)
            flow.direction = "toEnd2"
            assert flow.direction == "toEnd2"
        finally:
            pkg.delete_from_project()

    def test_end1(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("End1Pkg"))
        try:
            flow = self._flow(pkg)
            end = pkg.add_class(self._unique("End1Class"))
            flow.end1 = end
            result = flow.end1
            assert result is not None
            assert result == end
        finally:
            pkg.delete_from_project()

    def test_end1_port(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("End1PortPkg"))
        try:
            flow = self._flow(pkg)
            owner = pkg.add_class(self._unique("End1PortCls"))
            instance = pkg.add_implicit_object(self._unique("End1Instance"))
            port = IRPPort(owner.add_new_aggr("Port", self._unique("End1Port"))._com)
            flow.set_end1_via_port(instance, port)
            assert flow.end1_port.name == port.name
        finally:
            pkg.delete_from_project()

    def test_end1_sys_ml_port(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("End1SysMLPkg"))
        try:
            flow = self._flow(pkg)
            owner = pkg.add_class(self._unique("End1SysMLCls"))
            instance = pkg.add_implicit_object(self._unique("End1SysMLInstance"))
            port = IRPSysMLPort(owner.add_new_aggr("SysMLPort", self._unique("End1SysMLPort"))._com)
            flow.set_end1_via_sys_ml_port(instance, port)
            assert flow.end1_sys_ml_port.name == port.name
        finally:
            pkg.delete_from_project()

    def test_end2(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("End2Pkg"))
        try:
            flow = self._flow(pkg)
            end = pkg.add_class(self._unique("End2Class"))
            flow.end2 = end
            result = flow.end2
            assert result is not None
            assert result == end
        finally:
            pkg.delete_from_project()

    def test_end2_port(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("End2PortPkg"))
        try:
            flow = self._flow(pkg)
            owner = pkg.add_class(self._unique("End2PortCls"))
            instance = pkg.add_implicit_object(self._unique("End2Instance"))
            port = IRPPort(owner.add_new_aggr("Port", self._unique("End2Port"))._com)
            flow.set_end2_via_port(instance, port)
            assert flow.end2_port.name == port.name
        finally:
            pkg.delete_from_project()

    def test_end2_sys_ml_port(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("End2SysMLPkg"))
        try:
            flow = self._flow(pkg)
            owner = pkg.add_class(self._unique("End2SysMLCls"))
            instance = pkg.add_implicit_object(self._unique("End2SysMLInstance"))
            port = IRPSysMLPort(owner.add_new_aggr("SysMLPort", self._unique("End2SysMLPort"))._com)
            flow.set_end2_via_sys_ml_port(instance, port)
            assert flow.end2_sys_ml_port.name == port.name
        finally:
            pkg.delete_from_project()

    def test_add_conveyed(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AddConveyedPkg"))
        try:
            flow = self._flow(pkg)
            element = pkg.add_class(self._unique("AddConveyedClass"))
            flow.add_conveyed(element)
            assert element in list(flow.conveyed)
        finally:
            pkg.delete_from_project()

    def test_remove_conveyed(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("RemoveConveyedPkg"))
        try:
            flow = self._flow(pkg)
            element = pkg.add_class(self._unique("RemoveConveyedClass"))
            flow.add_conveyed(element)
            flow.remove_conveyed(element)
            assert element not in list(flow.conveyed)
        finally:
            pkg.delete_from_project()

    def test_set_end1_via_port(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("SetEnd1PortPkg"))
        try:
            flow = self._flow(pkg)
            owner = pkg.add_class(self._unique("SetEnd1PortCls"))
            instance = pkg.add_implicit_object(self._unique("SetEnd1Instance"))
            port = IRPPort(owner.add_new_aggr("Port", self._unique("SetEnd1Port"))._com)
            flow.set_end1_via_port(instance, port)
            assert flow.end1_port.name == port.name
        finally:
            pkg.delete_from_project()

    def test_set_end1_via_sys_ml_port(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("SetEnd1SysMLPkg"))
        try:
            flow = self._flow(pkg)
            owner = pkg.add_class(self._unique("SetEnd1SysMLCls"))
            instance = pkg.add_implicit_object(self._unique("SetEnd1SysMLInstance"))
            port = IRPSysMLPort(owner.add_new_aggr("SysMLPort", self._unique("SetEnd1SysMLPort"))._com)
            flow.set_end1_via_sys_ml_port(instance, port)
            assert flow.end1_sys_ml_port.name == port.name
        finally:
            pkg.delete_from_project()

    def test_set_end2_via_port(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("SetEnd2PortPkg"))
        try:
            flow = self._flow(pkg)
            owner = pkg.add_class(self._unique("SetEnd2PortCls"))
            instance = pkg.add_implicit_object(self._unique("SetEnd2Instance"))
            port = IRPPort(owner.add_new_aggr("Port", self._unique("SetEnd2Port"))._com)
            flow.set_end2_via_port(instance, port)
            assert flow.end2_port.name == port.name
        finally:
            pkg.delete_from_project()

    def test_set_end2_via_sys_ml_port(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("SetEnd2SysMLPkg"))
        try:
            flow = self._flow(pkg)
            owner = pkg.add_class(self._unique("SetEnd2SysMLCls"))
            instance = pkg.add_implicit_object(self._unique("SetEnd2SysMLInstance"))
            port = IRPSysMLPort(owner.add_new_aggr("SysMLPort", self._unique("SetEnd2SysMLPort"))._com)
            flow.set_end2_via_sys_ml_port(instance, port)
            assert flow.end2_sys_ml_port.name == port.name
        finally:
            pkg.delete_from_project()
