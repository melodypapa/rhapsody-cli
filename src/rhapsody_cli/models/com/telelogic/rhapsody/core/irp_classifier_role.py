"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPClassifierRole``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPSequenceDiagram
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance


class IRPClassifierRole(IRPModelElement):
    """Wraps ``IRPClassifierRole``: a lifeline in a sequence or communication diagram.

    JavaDoc accessor pairs exposed by pywin32 as properties are surfaced as
    ``@property`` members; ``get_referencing_classifier_roles_recursively``
    remains a method.
    """

    # IRPClassifierRole method parity checklist:
    # [x] formal_classifier               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] formal_instance                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] referenced_sequence_diagram     [x] impl  [x] docstring  [x] unit test  [ ] integration test (empty-state only; populated readback blocked in #202)
    # [x] role_type                       [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_referencing_classifier_roles_recursively [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)

    @property
    def formal_classifier(self) -> IRPClassifier | None:
        """Returns the classifier realized by the lifeline.

        Returns:
            The realized classifier, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getFormalClassifier()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier

        return cast(IRPClassifier, self.wrap(self.get_com_property(self._com, "formalClassifier")))

    @formal_classifier.setter
    def formal_classifier(self, formal_classifier: IRPClassifier) -> None:
        """Sets the classifier realized by the lifeline.

        Args:
            formal_classifier: The classifier to use.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::setFormalClassifier(com.telelogic.rhapsody.core.IRPClassifier formalClassifier)
        """
        self.set_com_property(self._com, "formalClassifier", formal_classifier._com)

    @property
    def formal_instance(self) -> IRPInstance | None:
        """Returns the object realized by the lifeline.

        Returns:
            The realized object, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getFormalInstance()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance

        return cast(IRPInstance, self.wrap(self.get_com_property(self._com, "formalInstance")))

    @formal_instance.setter
    def formal_instance(self, formal_instance: IRPInstance) -> None:
        """Sets the object realized by the lifeline.

        Args:
            formal_instance: The object to use.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::setFormalInstance(com.telelogic.rhapsody.core.IRPInstance formalInstance)
        """
        self.set_com_property(self._com, "formalInstance", formal_instance._com)

    @property
    def referenced_sequence_diagram(self) -> IRPSequenceDiagram | None:
        """Returns the sequence diagram referenced by the lifeline.

        Returns:
            The referenced diagram, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getReferencedSequenceDiagram()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPSequenceDiagram

        return cast(IRPSequenceDiagram, self.wrap(self.get_com_property(self._com, "referencedSequenceDiagram")))

    @referenced_sequence_diagram.setter
    def referenced_sequence_diagram(self, referenced_sequence_diagram: IRPSequenceDiagram) -> None:
        """Sets the sequence diagram referenced by the lifeline.

        Args:
            referenced_sequence_diagram: The diagram to use.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::setReferencedSequenceDiagram(com.telelogic.rhapsody.core.IRPSequenceDiagram referencedSequenceDiagram)
        """
        self.set_com_property(self._com, "referencedSequenceDiagram", referenced_sequence_diagram._com)

    @property
    def role_type(self) -> str:
        """Returns the classifier-role type, e.g. ``CLASS`` or ``ACTOR``.

        Returns:
            The role type string.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getRoleType()
        """
        return str(self.get_com_property(self._com, "roleType"))

    def get_referencing_classifier_roles_recursively(self) -> IRPCollection:
        """Returns all lifelines in referenced sequence diagrams, recursively.

        Returns:
            A collection of referencing classifier roles.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getReferencingClassifierRolesRecursively()
        """
        return IRPCollection(self.call_com(lambda: self._com.getReferencingClassifierRolesRecursively()))


IRPModelElement.register_wrapper("ClassifierRole", IRPClassifierRole)
