import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDiagram
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestRPDiagramIntegration:
    """Integration tests for IRPDiagram with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_create_object_model_diagram(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("DiagPkg")
        diag_name = self._unique("MyDiagram")
        pkg = self._create_package(test_project, pkg_name)
        try:
            diagram = pkg.add_object_model_diagram(diag_name)
            assert diagram is not None
            assert isinstance(diagram, IRPDiagram)
            assert diagram.name == diag_name
        finally:
            diagram.delete_from_project()
