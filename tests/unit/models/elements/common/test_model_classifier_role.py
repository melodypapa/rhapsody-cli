"""Tests for rhapsody_cli.models.elements.common.model_other_model.RPClassifierRole."""

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.common import RPClassifierRole
from rhapsody_cli.models.elements.relations import RPInstance
from tests.unit.models.fakes import make_fake_collection, make_fake_element


class TestRPClassifierRole:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("ClassifierRole", properties={"name": "Lifeline1"})
        role = RPClassifierRole(fake)
        assert isinstance(role, IRPModelElement)
        assert role.name == "Lifeline1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("ClassifierRole", properties={"name": "L1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPClassifierRole)

    def test_get_formal_classifier_wraps_result(self) -> None:
        # Pattern B — no-arg getter returning wrapped element
        fake = make_fake_element("ClassifierRole")
        clf = make_fake_element("Class", properties={"name": "Foo"})
        fake.getFormalClassifier.return_value = clf
        role = RPClassifierRole(fake)
        wrapped = role.get_formal_classifier()
        assert wrapped.name == "Foo"

    def test_get_formal_instance_wraps_result(self) -> None:
        # Pattern B
        fake = make_fake_element("ClassifierRole")
        inst = make_fake_element("Instance", properties={"name": "Inst1"})
        fake.getFormalInstance.return_value = inst
        role = RPClassifierRole(fake)
        wrapped = role.get_formal_instance()
        assert wrapped.name == "Inst1"

    def test_get_referenced_sequence_diagram_wraps_result(self) -> None:
        # Pattern B
        fake = make_fake_element("ClassifierRole")
        sd = make_fake_element("SequenceDiagram", properties={"name": "SD1"})
        fake.getReferencedSequenceDiagram.return_value = sd
        role = RPClassifierRole(fake)
        wrapped = role.get_referenced_sequence_diagram()
        assert wrapped.name == "SD1"

    def test_get_referencing_classifier_roles_recursively_returns_collection(self) -> None:
        # Pattern C — no-arg getter returning IRPCollection
        fake = make_fake_element("ClassifierRole")
        sub = make_fake_element("ClassifierRole", properties={"name": "Sub"})
        fake.getReferencingClassifierRolesRecursively.return_value = make_fake_collection([sub])
        role = RPClassifierRole(fake)
        result = role.get_referencing_classifier_roles_recursively()
        assert isinstance(result, IRPCollection)

    def test_get_role_type_returns_string(self) -> None:
        # Pattern A — no-arg getter returning primitive
        fake = make_fake_element("ClassifierRole", getRoleType="CLASS")
        role = RPClassifierRole(fake)
        assert role.get_role_type() == "CLASS"

    def test_set_formal_classifier_delegates(self) -> None:
        # Pattern F — multi-arg void method (single IRPClassifier arg)
        fake = make_fake_element("ClassifierRole")
        clf = make_fake_element("Class", properties={"name": "Foo"})
        fake.setFormalClassifier.return_value = None
        role = RPClassifierRole(fake)
        role.set_formal_classifier(IRPClassifier(clf))
        fake.setFormalClassifier.assert_called_once_with(clf)

    def test_set_formal_instance_delegates(self) -> None:
        # Pattern F
        fake = make_fake_element("ClassifierRole")
        inst = make_fake_element("Instance", properties={"name": "Inst1"})
        fake.setFormalInstance.return_value = None
        role = RPClassifierRole(fake)
        role.set_formal_instance(RPInstance(inst))
        fake.setFormalInstance.assert_called_once_with(inst)

    def test_set_referenced_sequence_diagram_delegates(self) -> None:
        # Pattern F
        from rhapsody_cli.models.elements.diagrams import RPSequenceDiagram

        fake = make_fake_element("ClassifierRole")
        sd = make_fake_element("SequenceDiagram", properties={"name": "SD1"})
        fake.setReferencedSequenceDiagram.return_value = None
        role = RPClassifierRole(fake)
        role.set_referenced_sequence_diagram(RPSequenceDiagram(sd))
        fake.setReferencedSequenceDiagram.assert_called_once_with(sd)
