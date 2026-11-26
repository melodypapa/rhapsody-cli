"""Integration tests for IRPSysMLPort with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_sysml_port import IRPSysMLPort


@pytest.mark.integration
class TestIRPSysMLPortIntegration:
    """Integration tests for IRPSysMLPort with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _port(pkg: IRPPackage) -> tuple[IRPPackage, IRPSysMLPort]:
        owner = pkg.add_class(f"PortOwner_{uuid.uuid4().hex[:8]}")
        element = owner.add_new_aggr("SysMLPort", f"Port_{uuid.uuid4().hex[:8]}")
        port = IRPSysMLPort(element._com)
        assert isinstance(port, IRPSysMLPort)
        return pkg, port

    def test_is_reversed(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ReversedPkg"))
        try:
            _, port = self._port(pkg)
            port.is_reversed = 1
            assert port.is_reversed == 1
        finally:
            pkg.delete_from_project()

    def test_port_direction(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("DirectionPkg"))
        try:
            _, port = self._port(pkg)
            port.port_direction = "InOut"
            assert port.port_direction == "InOut"
        finally:
            pkg.delete_from_project()

    def test_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("TypePkg"))
        try:
            _, port = self._port(pkg)
            type_ = pkg.add_class(self._unique("PortType"))
            port.type = type_
            result = port.type
            assert result is not None
            assert result._com is type_._com
        finally:
            pkg.delete_from_project()

    def test_add_link(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("LinkPkg"))
        try:
            from_owner = pkg.add_class(self._unique("FromOwner"))
            to_owner = pkg.add_class(self._unique("ToOwner"))
            from_port = IRPSysMLPort(from_owner.add_new_aggr("SysMLPort", self._unique("FromPort"))._com)
            to_port = IRPSysMLPort(to_owner.add_new_aggr("SysMLPort", self._unique("ToPort"))._com)
            from_part = IRPInstance(from_owner.add_new_aggr("Instance", self._unique("FromPart"))._com)
            to_part = IRPInstance(to_owner.add_new_aggr("Instance", self._unique("ToPart"))._com)
            relation = from_owner.add_relation_to(to_owner, "from", "Association", "1", "to", "Association", "1", "")
            link = from_port.add_link(from_part, to_part, relation, to_port, pkg)
            assert link._com is not None
        finally:
            pkg.delete_from_project()
