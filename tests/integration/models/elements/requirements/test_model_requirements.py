"""Integration tests for RPRequirement with live Rhapsody COM API.

Scope: the RPRequirement-owned methods (IRPRequirement::getRequirementID,
setRequirementID). A creation smoke-test is kept to confirm the element is
wrapped correctly; ``add_new_aggr`` is an IRPModelElement method used only
to build the fixture.
"""

import uuid

import pytest

from rhapsody_cli.models.elements.containment import RPPackage, RPProject
from rhapsody_cli.models.elements.requirements import RPRequirement


@pytest.mark.integration
class TestRPRequirementIntegration:
    """Integration tests for RPRequirement with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_create_requirement_in_package(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ReqPkg")
        req_name = self._unique("MyRequirement")
        pkg = self._create_package(test_project, pkg_name)
        try:
            req = pkg.add_new_aggr("Requirement", req_name)
            assert req is not None
            assert isinstance(req, RPRequirement)
            assert req.get_name() == req_name
            assert req.get_meta_class() == "Requirement"
        finally:
            req.delete_from_project()

    def test_requirement_id_roundtrip(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ReqPkg")
        req_name = self._unique("MyRequirement")
        pkg = self._create_package(test_project, pkg_name)
        req = pkg.add_new_aggr("Requirement", req_name)
        assert isinstance(req, RPRequirement)
        try:
            assert isinstance(req.get_requirement_id(), str)
            req.set_requirement_id("REQ-001")
            assert req.get_requirement_id() == "REQ-001"
            req.set_requirement_id("REQ-002")
            assert req.get_requirement_id() == "REQ-002"
        finally:
            req.delete_from_project()
