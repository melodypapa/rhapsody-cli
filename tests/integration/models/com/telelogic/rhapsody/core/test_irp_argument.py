"""Integration tests for IRPArgument with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument import IRPArgument
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPArgumentIntegration:
    """Integration tests for IRPArgument with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_argument_direction_is_readable(self, test_project: IRPProject) -> None:
        """The argumentDirection property is readable on a real argument; the
        setter faults in this Rhapsody build and is recorded as a blocker."""
        pkg = self._create_package(test_project, self._unique("ArgDirPkg"))
        test_class = pkg.add_class(self._unique("ArgDirCls"))
        try:
            op = test_class.add_operation(self._unique("dirOp"))
            argument = op.add_argument(self._unique("arg"))
            assert isinstance(argument, IRPArgument)
            assert argument.argument_direction in {"In", "Out", "InOut"}
        finally:
            test_class.delete_from_project()
