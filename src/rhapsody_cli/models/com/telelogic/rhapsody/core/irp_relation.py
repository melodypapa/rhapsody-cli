"""Wraps ``com.telelogic.rhapsody.core.IRPRelation``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass


class IRPRelation(IRPUnit):
    """Wraps ``IRPRelation``: the base interface for relationships between
    classifiers (such as associations, and the instance links derived from
    them).
    """

    # IRPRelation parity checklist (typelib authority 2026-11-26):
    # [x] add_qualifier                 method                       [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_association_class         method                       [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] inverse                       property (read)              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_inverse                   method (roleName, linkType)  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_navigable                  property (read/write)        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_symmetric                  property (read)              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] multiplicity                  property (read/write)        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] object_as_object_type         property (read)              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] of_class                      property (read/write)        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] other_class                   property (read/write)        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] qualifier                     property (read/write)        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_qualifiers                method                       [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_qualifier_type / set_qualifier_type  methods           [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] relation_label                property (read/write)        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] relation_link_name            property (read/write)        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] relation_role_name            property (read/write)        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] relation_type                 property (read/write)        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] visibility                    property (read)              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_typeless_object / make_unidirect / add_qualifier / remove_qualifier  methods  [x] impl  [x] unit test  [ ] integration test
    # No deprecated methods in IRPRelation.

    def add_qualifier(self, p_val: IRPModelElement) -> None:
        """Adds a qualifier to the association.

        Args:
            p_val: The model element to add as a qualifier.

        Raises:
            RhapsodyRuntimeException: if the qualifier cannot be added.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::addQualifier(com.telelogic.rhapsody.core.IRPModelElement pVal)
        """
        self.call_com(lambda: self._com.addQualifier(p_val._com))

    def get_association_class(self) -> IRPAssociationClass | None:
        """Returns the association class linked to this relation, if any.

        Returns:
            The wrapped ``IRPAssociationClass``, or ``None`` if none exists.

        Raises:
            RhapsodyRuntimeException: if the association class cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getAssociationClass()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass

        raw = self.call_com(lambda: self._com.getAssociationClass())
        return cast(IRPAssociationClass, self.wrap(raw)) if raw is not None else None

    @property
    def inverse(self) -> IRPRelation | None:
        """The inverse relation for this (bidirectional) relation, or ``None``.

        The result is constructed as ``IRPRelation`` directly because association
        ends carry the ``AssociationEnd`` meta class, which has no registered wrapper.

        Raises:
            RhapsodyRuntimeException: if the inverse relation cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getInverse()
        """
        raw = self.get_com_property(self._com, "inverse")
        return IRPRelation(raw) if raw is not None else None

    @property
    def is_navigable(self) -> bool:
        """Whether the relation is navigable.

        Raises:
            RhapsodyRuntimeException: if the property cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getIsNavigable()
        """
        return bool(self.get_com_property(self._com, "isNavigable"))

    @is_navigable.setter
    def is_navigable(self, is_navigable: bool) -> None:
        """Sets whether the relation is navigable.

        Args:
            is_navigable: ``True`` to make the relation navigable, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setIsNavigable(int isNavigable)
        """
        self.set_com_property(self._com, "isNavigable", 1 if is_navigable else 0)

    @property
    def is_symmetric(self) -> bool:
        """Whether the relation is symmetric.

        Raises:
            RhapsodyRuntimeException: if the property cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getIsSymmetric()
        """
        return bool(self.get_com_property(self._com, "isSymmetric"))

    @property
    def multiplicity(self) -> str:
        """The multiplicity of the relation (for example ``"1"`` or ``"0..*"``).

        Raises:
            RhapsodyRuntimeException: if the multiplicity cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getMultiplicity()
        """
        return str(self.get_com_property(self._com, "multiplicity"))

    @multiplicity.setter
    def multiplicity(self, multiplicity: str) -> None:
        """Sets the multiplicity of the relation.

        Args:
            multiplicity: The multiplicity string.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setMultiplicity(java.lang.String multiplicity)
        """
        self.set_com_property(self._com, "multiplicity", multiplicity)

    @property
    def object_as_object_type(self) -> IRPClass:
        """The object's class, treated as the object's type.

        Raises:
            RhapsodyRuntimeException: if the object type cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getObjectAsObjectType()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass

        return cast(IRPClass, self.wrap(self.get_com_property(self._com, "ObjectAsObjectType")))

    @property
    def of_class(self) -> IRPClassifier:
        """The classifier that owns this relation.

        Raises:
            RhapsodyRuntimeException: if the owner classifier cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getOfClass()
        """
        return cast(IRPClassifier, self.wrap(self.get_com_property(self._com, "ofClass")))

    @of_class.setter
    def of_class(self, of_class: IRPClassifier) -> None:
        """Sets the classifier that owns this relation.

        Args:
            of_class: The owner classifier.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setOfClass(com.telelogic.rhapsody.core.IRPClassifier ofClass)
        """
        self.set_com_property(self._com, "ofClass", of_class._com)

    @property
    def other_class(self) -> IRPClassifier:
        """The class at the other end of this relation.

        Raises:
            RhapsodyRuntimeException: if the other classifier cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getOtherClass()
        """
        return cast(IRPClassifier, self.wrap(self.get_com_property(self._com, "otherClass")))

    @other_class.setter
    def other_class(self, other_class: IRPClassifier) -> None:
        """Sets the class at the other end of this relation.

        Args:
            other_class: The other-end classifier.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setOtherClass(com.telelogic.rhapsody.core.IRPClassifier otherClass)
        """
        self.set_com_property(self._com, "otherClass", other_class._com)

    @property
    def qualifier(self) -> str:
        """The qualifier text for the association.

        Raises:
            RhapsodyRuntimeException: if the qualifier cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getQualifier()
        """
        return str(self.get_com_property(self._com, "qualifier"))

    @qualifier.setter
    def qualifier(self, qualifier: str) -> None:
        """Sets the qualifier text for the association.

        Args:
            qualifier: The qualifier string.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setQualifier(java.lang.String qualifier)
        """
        self.set_com_property(self._com, "qualifier", qualifier)

    def get_qualifiers(self) -> IRPCollection:
        """Gets the collection of qualifier model elements for the association.

        Returns:
            An ``IRPCollection`` of qualifier model elements.

        Raises:
            RhapsodyRuntimeException: if the qualifiers cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getQualifiers()
        """
        return IRPCollection(self.call_com(lambda: self._com.getQualifiers()))

    def get_qualifier_type(self) -> IRPClassifier:
        """For associations that use qualifiers, returns the type of the qualifier.

        Returns:
            The wrapped ``IRPClassifier`` used as the qualifier's type.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getQualifierType()
        """
        return cast(IRPClassifier, self.wrap(self.call_com(lambda: self._com.getQualifierType())))

    @property
    def relation_label(self) -> str:
        """The label of the relation.

        Raises:
            RhapsodyRuntimeException: if the relation label cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getRelationLabel()
        """
        return str(self.get_com_property(self._com, "relationLabel"))

    @relation_label.setter
    def relation_label(self, relation_label: str) -> None:
        """Sets the label of the relation.

        Args:
            relation_label: The relation label string.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setRelationLabel(java.lang.String relationLabel)
        """
        self.set_com_property(self._com, "relationLabel", relation_label)

    @property
    def relation_link_name(self) -> str:
        """The link name of the relation.

        Raises:
            RhapsodyRuntimeException: if the relation link name cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getRelationLinkName()
        """
        return str(self.get_com_property(self._com, "relationLinkName"))

    @relation_link_name.setter
    def relation_link_name(self, relation_link_name: str) -> None:
        """Sets the link name of the relation.

        Args:
            relation_link_name: The relation link name.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setRelationLinkName(java.lang.String relationLinkName)
        """
        self.set_com_property(self._com, "relationLinkName", relation_link_name)

    @property
    def relation_role_name(self) -> str:
        """The role name of the relation.

        Raises:
            RhapsodyRuntimeException: if the relation role name cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getRelationRoleName()
        """
        return str(self.get_com_property(self._com, "relationRoleName"))

    @relation_role_name.setter
    def relation_role_name(self, relation_role_name: str) -> None:
        """Sets the role name of the relation.

        Args:
            relation_role_name: The relation role name.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setRelationRoleName(java.lang.String relationRoleName)
        """
        self.set_com_property(self._com, "relationRoleName", relation_role_name)

    @property
    def relation_type(self) -> str:
        """The type of the relation (for example ``"Association"``).

        Raises:
            RhapsodyRuntimeException: if the relation type cannot be retrieved or set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getRelationType()
        """
        return str(self.get_com_property(self._com, "relationType"))

    @relation_type.setter
    def relation_type(self, relation_type: str) -> None:
        """Sets the type of the relation.

        Args:
            relation_type: The relation type string.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setRelationType(java.lang.String relationType)
        """
        self.set_com_property(self._com, "relationType", relation_type)

    @property
    def visibility(self) -> str:
        """The visibility of the relation (for example ``"public"`` or ``"private"``).

        Raises:
            RhapsodyRuntimeException: if the visibility cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::getVisibility()
        """
        return str(self.get_com_property(self._com, "visibility"))

    def is_typeless_object(self) -> bool:
        """Checks whether the object at the other end of the relation has no type.

        Returns:
            ``True`` if the related object is typeless, ``False`` otherwise.

        Raises:
            RhapsodyRuntimeException: if the typeless state cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::isTypelessObject()
        """
        return bool(self.call_com(lambda: self._com.isTypelessObject()))

    def make_unidirect(self) -> None:
        """Makes the relation unidirectional.

        Raises:
            RhapsodyRuntimeException: if the relation cannot be made unidirectional.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::makeUnidirect()
        """
        self.call_com(lambda: self._com.makeUnidirect())

    def remove_qualifier(self, p_val: IRPModelElement) -> None:
        """Removes a qualifier from the association.

        Args:
            p_val: The model element to remove from the qualifiers.

        Raises:
            RhapsodyRuntimeException: if the qualifier cannot be removed.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::removeQualifier(com.telelogic.rhapsody.core.IRPModelElement pVal)
        """
        self.call_com(lambda: self._com.removeQualifier(p_val._com))

    def set_inverse(self, role_name: str, link_type: str) -> None:
        """Sets the inverse role name and link type for the relation.

        Args:
            role_name: The role name to use for the inverse relation.
            link_type: The link type to use for the inverse relation.

        Raises:
            RhapsodyRuntimeException: if the inverse cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setInverse(java.lang.String roleName, java.lang.String linkType)
        """
        self.call_com(lambda: self._com.setInverse(role_name, link_type))

    def set_qualifier_type(self, p_val: IRPClassifier) -> None:
        """Sets the type of the qualifier for associations that use qualifiers.

        Args:
            p_val: The classifier to use as the qualifier type.

        Raises:
            RhapsodyRuntimeException: if the qualifier type cannot be set.

        Reference:
            com.telelogic.rhapsody.core.IRPRelation::setQualifierType(com.telelogic.rhapsody.core.IRPClassifier pVal)
        """
        self.call_com(lambda: self._com.setQualifierType(p_val._com))
