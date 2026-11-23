"""Other Model model-element wrappers (auto-generated stubs)."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.elements.relations.model_instance import RPInstance

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
    from rhapsody_cli.models.elements.diagrams.model_diagram_types import RPSequenceDiagram
    from rhapsody_cli.models.elements.graphics.model_graphics import RPLink
    from rhapsody_cli.models.elements.relations.model_relation import RPRelation


class RPClassifierRole(IRPModelElement):
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

    def get_formal_instance(self) -> "RPInstance":
        """Returns the object that is realized by the lifeline, for cases where a lifeline represents an object and not just a classifier.

        Returns:
            The object that is realized by the lifeline, or null if the lifeline does not realize an object.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getFormalInstance()
        """
        return cast("RPInstance", self.wrap(self.call_com(lambda: self._com.getFormalInstance())))

    def get_referenced_sequence_diagram(self) -> "RPSequenceDiagram":
        """Returns the sequence diagram referenced by the lifeline.

        Returns:
            The sequence diagram referenced by the lifeline, or null if there is no referenced diagram.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPClassifierRole::getReferencedSequenceDiagram()
        """
        return cast("RPSequenceDiagram", self.wrap(self.call_com(lambda: self._com.getReferencedSequenceDiagram())))

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

    def set_formal_instance(self, formal_instance: "RPInstance") -> None:
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

    def set_referenced_sequence_diagram(self, referenced_sequence_diagram: "RPSequenceDiagram") -> None:
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


class RPSysMLPort(RPInstance):
    """Wraps ``IRPSysMLPort``: represents flowport elements in Rhapsody models."""

    # IRPSysMLPort method parity checklist:
    # [x] add_link                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_is_reversed                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_port_direction             [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_type                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_is_reversed                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_port_direction             [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_type                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_instance methods (covered by rp_instance checklist)
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_relation methods (covered by rp_relation checklist)
    # [inherited] irp_unit methods (covered by rp_unit checklist)
    # No deprecated IRPSysMLPort methods.

    def add_link(self, from_part: "RPInstance", to_part: "RPInstance", assoc: "RPRelation", to_port: "RPSysMLPort", new_owner: "IRPPackage") -> "RPLink":
        """Creates a link between flowports on two parts.

        Args:
            from_part: The "from" part for the link.
            to_part: The "to" part for the link.
            assoc: Use ``None`` for this argument (it is not relevant for links
                between flowports).
            to_port: The "to" port for the link.
            new_owner: The package that should be the owner of the link created.

        Returns:
            The link that was created.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::addLink(
                com.telelogic.rhapsody.core.IRPInstance fromPart,
                com.telelogic.rhapsody.core.IRPInstance toPart,
                com.telelogic.rhapsody.core.IRPRelation assoc,
                com.telelogic.rhapsody.core.IRPSysMLPort toPort,
                com.telelogic.rhapsody.core.IRPPackage newOwner)
        """
        return cast("RPLink", self.wrap(self.call_com(lambda: self._com.addLink(from_part._com, to_part._com, assoc._com, to_port._com, new_owner._com))))

    def get_is_reversed(self) -> int:
        """Checks whether the flowport was specified as conjugated.

        Returns:
            1 if the flowport was specified as conjugated, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::getIsReversed()
        """
        return int(self.call_com(lambda: self._com.getIsReversed()))

    def get_port_direction(self) -> str:
        """Returns the direction that was specified for the flowport.

        Returns:
            The direction that was specified for the flowport — one of ``"In"``,
            ``"Out"``, or ``"InOut"``.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::getPortDirection()
        """
        return str(self._get_method_or_property(self._com, "getPortDirection", "portDirection"))

    def get_type(self) -> "IRPClassifier":
        """Returns the type that was specified for the flowport.

        Returns:
            The type that was specified for the flowport.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::getType()
        """
        return cast("IRPClassifier", self.wrap(self.call_com(lambda: self._com.getType())))

    def set_is_reversed(self, is_reversed: int) -> None:
        """Specifies whether the flowport should be conjugated.

        Args:
            is_reversed: Use 1 to specify that the flowport should be conjugated,
                0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::setIsReversed(int isReversed)
        """
        self._set_method_or_property(self._com, "setIsReversed", "isReversed", is_reversed)

    def set_port_direction(self, port_direction: str) -> None:
        """Sets the direction of the flowport.

        Args:
            port_direction: The direction to use for the flowport. The valid values
                are ``"In"``, ``"Out"``, and ``"InOut"``.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::setPortDirection(java.lang.String portDirection)
        """
        self._set_method_or_property(self._com, "setPortDirection", "portDirection", port_direction)

    def set_type(self, type_: "IRPClassifier") -> None:
        """Sets the type for the flowport.

        Args:
            type_: The type to use for the flowport.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPSysMLPort::setType(com.telelogic.rhapsody.core.IRPClassifier type)
        """
        self.call_com(lambda: self._com.setType(type_._com))


IRPModelElement.register_wrapper("ClassifierRole", RPClassifierRole)
IRPModelElement.register_wrapper("SysMLPort", RPSysMLPort)
