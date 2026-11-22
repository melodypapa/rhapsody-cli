"""Integration tests for IRPArgument with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.exceptions import RhapsodyRuntimeException
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

    def test_argument_direction_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ArgDirPkg"))
        test_class = pkg.add_class(self._unique("ArgDirCls"))
        try:
            op = test_class.add_operation(self._unique("dirOp"))
            argument = op.add_argument(self._unique("arg"))
            assert isinstance(argument, IRPArgument)
            original = argument.get_argument_direction()
            assert isinstance(original, str)
            with pytest.raises(RhapsodyRuntimeException):
                argument.set_argument_direction("out")
        finally:
            test_class.delete_from_project()
