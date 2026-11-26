import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPModule
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPModuleIntegration:
    """Integration tests for IRPModule's registration with a live module.

    IRPModule declares no members of its own in JavaDoc (it extends IRPInstance), so the
    only owned behavior is that a live module returned by IRPPackage.addModule is wrapped as IRPModule.
    """

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    def test_add_module_returns_an_irp_module(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ModPkg"))
        module_name = self._unique("Module")
        try:
            module = pkg.add_module(module_name)
            assert isinstance(module, IRPModule)
            assert module.name == module_name
        finally:
            pkg.delete_from_project()
