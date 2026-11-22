"""Integration tests for IRP_port with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPPortIntegration:
    """Integration tests for IRPPort with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_port_state_and_contract(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("PortPkg"))
        test_class = pkg.add_class(self._unique("PortCls"))
        try:
            port = test_class.add_new_aggr("Port", self._unique("port"))
            assert isinstance(port, IRPPort)
            with pytest.raises(AttributeError):
                port.get_is_behavioral()
            with pytest.raises(AttributeError):
                port.get_is_reversed()
            with pytest.raises(AttributeError):
                port.get_port_contract()
            with pytest.raises(AttributeError):
                port.set_is_behavioral(1)
            with pytest.raises(AttributeError):
                port.set_is_reversed(0)
            with pytest.raises(AttributeError):
                port.set_port_contract(test_class)
            with pytest.raises(NotImplementedError):
                port.get_contract()
            with pytest.raises(NotImplementedError):
                port.set_contract(test_class)
        finally:
            test_class.delete_from_project()

    def test_provided_and_required_interfaces(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IfPortPkg"))
        test_class = pkg.add_class(self._unique("IfPortCls"))
        try:
            port = test_class.add_new_aggr("Port", self._unique("ifPort"))
            assert isinstance(port, IRPPort)
            with pytest.raises(AttributeError):
                port.get_provided_interfaces()
            with pytest.raises(AttributeError):
                port.get_required_interfaces()
            with pytest.raises(AttributeError):
                port.add_provided_interface(test_class)
            with pytest.raises(AttributeError):
                port.remove_provided_interface(test_class)
            with pytest.raises(AttributeError):
                port.add_required_interface(test_class)
            with pytest.raises(AttributeError):
                port.remove_required_interface(test_class)
        finally:
            test_class.delete_from_project()
