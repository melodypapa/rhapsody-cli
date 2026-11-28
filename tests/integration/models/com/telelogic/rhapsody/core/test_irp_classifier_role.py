"""Integration tests for IRPClassifierRole with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier_role import IRPClassifierRole
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collaboration import IRPCollaboration
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPCollaborationDiagram
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPClassifierRoleIntegration:
    """Integration tests for IRPClassifierRole with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _role(pkg: IRPPackage) -> tuple[IRPPackage, IRPClassifierRole]:
        diagram = pkg.add_collaboration_diagram(f"Collaboration_{uuid.uuid4().hex[:8]}")
        assert isinstance(diagram, IRPCollaborationDiagram)
        collaboration = diagram.get_logical_collaboration()
        assert isinstance(collaboration, IRPCollaboration)
        classifier = pkg.add_class(f"RoleClass_{uuid.uuid4().hex[:8]}")
        role = collaboration.add_classifier_role(f"Lifeline_{uuid.uuid4().hex[:8]}", classifier)
        assert isinstance(role, IRPClassifierRole)
        return pkg, role

    def test_formal_classifier(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ClassifierPkg"))
        try:
            _, role = self._role(pkg)
            classifier = pkg.add_class(self._unique("RealizedClass"))
            role.formal_classifier = classifier
            result = role.formal_classifier
            assert result is not None
            assert result == classifier
        finally:
            pkg.delete_from_project()

    def test_formal_instance(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("InstancePkg"))
        try:
            _, role = self._role(pkg)
            owner = pkg.add_class(self._unique("InstanceOwner"))
            instance = IRPInstance(owner.add_new_aggr("Instance", self._unique("RealizedInstance"))._com)
            role.formal_instance = instance
            result = role.formal_instance
            assert result is not None
            assert result == instance
        finally:
            pkg.delete_from_project()

    def test_referenced_sequence_diagram_unset_returns_none(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("DiagramPkg"))
        try:
            _, role = self._role(pkg)

            # Positive setter/readback remains a live blocker; see issue #202.
            assert role.referenced_sequence_diagram is None
        finally:
            pkg.delete_from_project()

    def test_role_type(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("RoleTypePkg"))
        try:
            _, role = self._role(pkg)
            role.formal_classifier = pkg.add_class(self._unique("TypedClass"))
            assert role.role_type == "CLASS"
        finally:
            pkg.delete_from_project()

    def test_get_referencing_classifier_roles_recursively(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("RecursivePkg"))
        try:
            _, role = self._role(pkg)
            roles = role.get_referencing_classifier_roles_recursively()
            assert isinstance(roles, IRPCollection)
        finally:
            pkg.delete_from_project()
