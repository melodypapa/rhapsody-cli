"""Integration tests for IRPPort with live Rhapsody COM API."""

import uuid

import pytest
from win32com.client import CastTo

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
        """JavaDoc getContract/setContract exist as deprecated aliases; pywin32 exposes only portContract, so the stubs raise NotImplementedError (port_contract is covered above)."""
        pkg = self._create_package(test_project, self._unique("PortPkg"))
        test_class = pkg.add_class(self._unique("PortCls"))
        try:
            # add_new_aggr returns an IRPModelElement COM interface; QueryInterface
            # to IRPPort so its owned properties are reachable (no mock bindings).
            port = IRPPort(CastTo(test_class.add_new_aggr("Port", self._unique("port"))._com, "IRPPort"))
            assert isinstance(port, IRPPort)
            assert port.is_behavioral in (0, 1)
            assert port.is_reversed in (0, 1)
            contract = port.port_contract
            assert contract is None or isinstance(contract, IRPClass)
            port.is_behavioral = 1
            assert port.is_behavioral == 1
            port.is_reversed = 0
            assert port.is_reversed == 0
            # JavaDoc: portContract expects an interface/protocol, not a Class.
            contract_interface = pkg.add_new_aggr("Interface", self._unique("contractIface"))
            port.port_contract = contract_interface
            assert port.port_contract is not None
            assert port.port_contract.name == contract_interface.name
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
            port = IRPPort(CastTo(test_class.add_new_aggr("Port", self._unique("ifPort"))._com, "IRPPort"))
            assert isinstance(port, IRPPort)
            # The collection getters return real IRPCollection objects. The
            # add/remove interface mutators are rejected by this Rhapsody build
            # for any element type and are recorded as blockers in irp_port.md.
            assert isinstance(port.provided_interfaces, IRPCollection)
            assert isinstance(port.required_interfaces, IRPCollection)
        finally:
            test_class.delete_from_project()
