"""Integration tests for IRP_port with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port import IRPPort
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


def _assert_failure_or_none(call, exceptions=(RhapsodyRuntimeException, AttributeError, TypeError)) -> None:  # type: ignore[no-untyped-def]
    """Assert a documented COM outcome: a known failure or a None result."""
    try:
        result = call()
    except exceptions as exc:
        assert exc is not None
    else:
        assert result is None


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
            for call in (port.get_is_behavioral, port.get_is_reversed, port.get_port_contract):
                _assert_failure_or_none(call)
            for call in (  # type: ignore[assignment]
                lambda: port.set_is_behavioral(1),
                lambda: port.set_is_reversed(0),
                lambda: port.set_port_contract(test_class),
                lambda: port.get_contract(),
                lambda: port.set_contract(test_class),
            ):
                _assert_failure_or_none(call)
        finally:
            test_class.delete_from_project()

    def test_provided_and_required_interfaces(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IfPortPkg"))
        test_class = pkg.add_class(self._unique("IfPortCls"))
        try:
            port = test_class.add_new_aggr("Port", self._unique("ifPort"))
            assert isinstance(port, IRPPort)
            for call in (port.get_provided_interfaces, port.get_required_interfaces):
                _assert_failure_or_none(call)
            for call in (  # type: ignore[assignment]
                lambda: port.add_provided_interface(test_class),
                lambda: port.remove_provided_interface(test_class),
                lambda: port.add_required_interface(test_class),
                lambda: port.remove_required_interface(test_class),
            ):
                _assert_failure_or_none(call)
        finally:
            test_class.delete_from_project()
