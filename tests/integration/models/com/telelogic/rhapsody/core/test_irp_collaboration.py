"""Integration tests for IRPCollaboration with live Rhapsody COM API."""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collaboration import IRPCollaboration
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPCollaborationDiagram
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPCollaborationIntegration:
    """Integration tests for IRPCollaboration with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _collaboration(pkg: IRPPackage) -> tuple[IRPPackage, IRPCollaboration]:
        diagram = pkg.add_collaboration_diagram(f"Collaboration_{uuid.uuid4().hex[:8]}")
        assert isinstance(diagram, IRPCollaborationDiagram)
        collaboration = diagram.get_logical_collaboration()
        assert isinstance(collaboration, IRPCollaboration)
        return pkg, collaboration

    def test_activation_condition(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Activation_ConditionPkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            # No documented API populates this read-only property on a fresh collaboration.
            assert collaboration.activation_condition in (0, 1, "", None)
        finally:
            pkg.delete_from_project()

    def test_activation_mode(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Activation_ModePkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            assert collaboration.activation_mode == "Invariant"
        finally:
            pkg.delete_from_project()

    def test_associations(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AssociationsPkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            # No documented API populates this read-only property on a fresh collaboration.
            assert len(list(collaboration.associations)) == 0
        finally:
            pkg.delete_from_project()

    def test_classifier(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ClassifierPkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            classifier = pkg.add_class(self._unique("Classifier"))
            role = collaboration.add_classifier_role(self._unique("InstanceLine"), classifier)

            assert role in list(collaboration.classifier)
        finally:
            pkg.delete_from_project()

    def test_execution_occurrences(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Execution_OccurrencesPkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            # No documented API populates this read-only property on a fresh collaboration.
            assert len(list(collaboration.execution_occurrences)) == 0
        finally:
            pkg.delete_from_project()

    def test_interaction_occurrences(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Interaction_OccurrencesPkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            # No documented API populates this read-only property on a fresh collaboration.
            assert len(list(collaboration.interaction_occurrences)) == 0
        finally:
            pkg.delete_from_project()

    def test_interaction_operators(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Interaction_OperatorsPkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            # No documented API populates this read-only property on a fresh collaboration.
            assert len(list(collaboration.interaction_operators)) == 0
        finally:
            pkg.delete_from_project()

    def test_message_points(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("Message_PointsPkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            # No documented API populates this read-only property on a fresh collaboration.
            assert len(list(collaboration.message_points)) == 0
        finally:
            pkg.delete_from_project()

    def test_messages(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("MessagesPkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            sender_class = pkg.add_class(self._unique("SenderClass"))
            receiver_class = pkg.add_class(self._unique("ReceiverClass"))
            sender = collaboration.add_classifier_role(self._unique("Sender"), sender_class)
            receiver = collaboration.add_classifier_role(self._unique("Receiver"), receiver_class)
            operation = sender_class.add_operation(self._unique("MessageOperation"))

            message = collaboration.add_message(operation, "", sender, receiver)

            assert message in list(collaboration.messages)
        finally:
            pkg.delete_from_project()

    def test_mode(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("ModePkg"))
        try:
            _, collaboration = self._collaboration(pkg)
            assert collaboration.mode == "EXISTENTIAL"
        finally:
            pkg.delete_from_project()
