"""Integration tests for IRPPort with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
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
            assert port.get_is_behavioral() in (0, 1)
            assert port.get_is_reversed() in (0, 1)
            contract = port.get_port_contract()
            assert contract is None or isinstance(contract, IRPClass)
            assert port.set_is_behavioral(1) is None  # type: ignore[func-returns-value]
            assert port.set_is_reversed(0) is None  # type: ignore[func-returns-value]
            assert port.set_port_contract(test_class) is None  # type: ignore[func-returns-value]
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
            assert isinstance(port.get_provided_interfaces(), IRPCollection)
            assert isinstance(port.get_required_interfaces(), IRPCollection)
            assert port.add_provided_interface(test_class) is None  # type: ignore[func-returns-value]
            assert port.remove_provided_interface(test_class) is None  # type: ignore[func-returns-value]
            assert port.add_required_interface(test_class) is None  # type: ignore[func-returns-value]
            assert port.remove_required_interface(test_class) is None  # type: ignore[func-returns-value]
        finally:
            test_class.delete_from_project()
