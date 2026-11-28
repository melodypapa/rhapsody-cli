"""Integration tests for IRPRequirement with live Rhapsody COM API.

Scope: the IRPRequirement-owned ``requirement_id`` property, backed by the
pywin32 ``requirementID`` property. ``add_new_aggr`` is an IRPModelElement
method used only to build the fixture.
"""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPRequirement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPRequirementIntegration:
    """Integration tests for IRPRequirement with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, IRPPackage)
        return pkg

    def test_requirement_id_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ReqPkg"))
        try:
            req = IRPRequirement(pkg.add_new_aggr("Requirement", self._unique("MyRequirement"))._com)
            assert isinstance(req, IRPRequirement)
            assert isinstance(req.requirement_id, str)

            req.requirement_id = "REQ-001"
            assert req.requirement_id == "REQ-001"
            req.requirement_id = "REQ-002"
            assert req.requirement_id == "REQ-002"
        finally:
            pkg.delete_from_project()
