"""Other Model model-element wrappers (auto-generated stubs)."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPSequenceDiagram


class IRPClassifierRole(IRPModelElement):
    """Wraps ``IRPClassifierRole``: represents lifelines in sequence diagrams and "objects" (lifelines) in communication diagrams."""

    # IRPClassifierRole method parity checklist:
    # [x] get_formal_classifier          [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_formal_instance            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_referenced_sequence_diagram [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_referencing_classifier_roles_recursively [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_role_type                  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_formal_classifier          [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_formal_instance            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_referenced_sequence_diagram [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPClassifierRole methods.

    def get_formal_classifier(self) -> "IRPClassifier":
        """Returns the classifier (for example, class or actor) that the lifeline realizes.

        Returns:
            The classifier that the lifeline realizes.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getFormalClassifier()
        """
        return cast("IRPClassifier", self.wrap(self.call_com(lambda: self._com.getFormalClassifier())))

    def get_formal_instance(self) -> "IRPInstance":
        """Returns the object that is realized by the lifeline, for cases where a lifeline represents an object and not just a classifier.

        Returns:
            The object that is realized by the lifeline, or null if the lifeline does not realize an object.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getFormalInstance()
        """
        return cast("IRPInstance", self.wrap(self.call_com(lambda: self._com.getFormalInstance())))

    def get_referenced_sequence_diagram(self) -> "IRPSequenceDiagram":
        """Returns the sequence diagram referenced by the lifeline.

        Returns:
            The sequence diagram referenced by the lifeline, or null if there is no referenced diagram.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getReferencedSequenceDiagram()
        """
        return cast("IRPSequenceDiagram", self.wrap(self.call_com(lambda: self._com.getReferencedSequenceDiagram())))

    def get_referencing_classifier_roles_recursively(self) -> "IRPCollection":
        """Returns a collection of all the lifelines in referenced sequence diagrams, recursively including all lifelines in the decomposition hierarchy.

        Returns:
            A collection of all the lifelines in referenced sequence diagrams.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getReferencingClassifierRolesRecursively()
        """
        return IRPCollection(self.call_com(lambda: self._com.getReferencingClassifierRolesRecursively()))

    def get_role_type(self) -> str:
        """Returns a string representing the type of the classifier role.

        For example, ``CLASS`` for elements of type IRPClass and ``ACTOR`` for
        elements of type IRPActor. For objects, the string returned is ``CLASS``.

        Returns:
            A string representing the type of the classifier role.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getRoleType()
        """
        return str(self._get_method_or_property(self._com, "getRoleType", "roleType"))

    def set_formal_classifier(self, formal_classifier: "IRPClassifier") -> None:
        """Sets the specified element as the classifier realized by the lifeline.

        Args:
            formal_classifier: The model element that should be used as the
                classifier realized by the lifeline.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::setFormalClassifier(com.telelogic.rhapsody.core.IRPClassifier formalClassifier)
        """
        self.call_com(lambda: self._com.setFormalClassifier(formal_classifier._com))

    def set_formal_instance(self, formal_instance: "IRPInstance") -> None:
        """Sets the specified element as the object realized by the lifeline.

        Args:
            formal_instance: The model element that should be used as the object
                realized by the lifeline.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::setFormalInstance(com.telelogic.rhapsody.core.IRPInstance formalInstance)
        """
        self.call_com(lambda: self._com.setFormalInstance(formal_instance._com))

    def set_referenced_sequence_diagram(self, referenced_sequence_diagram: "IRPSequenceDiagram") -> None:
        """Sets the specified diagram to be the sequence diagram referenced by the lifeline.

        Args:
            referenced_sequence_diagram: The diagram that should be used as the
                sequence diagram referenced by the lifeline.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::setReferencedSequenceDiagram(com.telelogic.rhapsody.core.IRPSequenceDiagram referencedSequenceDiagram)
        """
        self.call_com(lambda: self._com.setReferencedSequenceDiagram(referenced_sequence_diagram._com))


IRPModelElement.register_wrapper("ClassifierRole", IRPClassifierRole)
