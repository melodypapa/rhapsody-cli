"""Wrappers for ``com.telelogic.rhapsody.core.IRPType``.

Canonical module for :class:`IRPType`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_type.md``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.core import AbstractRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.elements.common.model_misc import RPEnumerationLiteral


class IRPType(IRPClassifier):
    """Wraps ``IRPType``."""

    # IRPType method parity checklist:
    # [x] add_enumeration_literal        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] delete_enumeration_literal     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_declaration               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_enumeration_literals       [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_is_predefined              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_is_typedef                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_is_typedef_constant         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_is_typedef_ordered          [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_is_typedef_reference        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_kind                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_typedef_base_type           [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_typedef_multiplicity       [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_array                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_enum                       [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_equal_to                    [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_implicit                   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_kind_enumeration            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_kind_language               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_kind_struct                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_kind_typedef                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_kind_union                  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_pointer                    [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_pointer_to_pointer           [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_reference                  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_reference_to_pointer         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_struct                     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_template                   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_union                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_declaration               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_is_typedef_constant         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_is_typedef_ordered          [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_is_typedef_reference        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_kind                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_typedef_base_type           [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_typedef_multiplicity       [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_classifier methods (covered by rp_classifier checklist)
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_unit methods (covered by rp_unit checklist)
    # No deprecated IRPType methods.

    def add_enumeration_literal(self, name: str) -> RPEnumerationLiteral:
        """Adds an enumeration literal with the specified name to this type.

        Args:
            name: The name for the new enumeration literal.

        Returns:
            The enumeration literal that was created.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::addEnumerationLiteral(java.lang.String name)
        """
        from rhapsody_cli.models.elements.common.model_misc import RPEnumerationLiteral

        return cast(RPEnumerationLiteral, AbstractRPModelElement.wrap(self.call_com(lambda: self._com.addEnumerationLiteral(name))))

    def delete_enumeration_literal(self, literal: RPEnumerationLiteral) -> None:
        """Deletes the specified enumeration literal from this type.

        Args:
            literal: The enumeration literal to delete.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::deleteEnumerationLiteral(com.telelogic.rhapsody.core.IRPEnumerationLiteral literal)
        """
        self.call_com(lambda: self._com.deleteEnumerationLiteral(literal._com))

    def get_declaration(self) -> str:
        """Returns the declaration of the type.

        Returns:
            The declaration of the type.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getDeclaration()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "declaration"))

    def get_enumeration_literals(self) -> IRPCollection:
        """Returns the enumeration literals of the type.

        Returns:
            A collection of the type's enumeration literals.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getEnumerationLiterals()
        """
        return IRPCollection(AbstractRPModelElement.get_com_property(self._com, "enumerationLiterals"))

    def get_is_predefined(self) -> int:
        """Returns whether the type is predefined.

        Returns:
            1 if the type is predefined, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getIsPredefined()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "isPredefined"))

    def get_is_typedef(self) -> int:
        """Returns whether the type is a typedef.

        Returns:
            1 if the type is a typedef, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getIsTypedef()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "isTypedef"))

    def get_is_typedef_constant(self) -> int:
        """Returns whether the typedef is a constant.

        Returns:
            1 if the typedef is a constant, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getIsTypedefConstant()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "isTypedefConstant"))

    def get_is_typedef_ordered(self) -> int:
        """Returns whether the typedef is ordered.

        Returns:
            1 if the typedef is ordered, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getIsTypedefOrdered()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "isTypedefOrdered"))

    def get_is_typedef_reference(self) -> int:
        """Returns whether the typedef is a reference.

        Returns:
            1 if the typedef is a reference, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getIsTypedefReference()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "isTypedefReference"))

    def get_kind(self) -> str:
        """Returns the kind of the type.

        Returns:
            The kind of the type.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getKind()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "kind"))

    def get_typedef_base_type(self) -> IRPClassifier:
        """Returns the base type of the typedef.

        Returns:
            The base type of the typedef.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getTypedefBaseType()
        """
        return cast(IRPClassifier, AbstractRPModelElement.wrap(AbstractRPModelElement.get_com_property(self._com, "typedefBaseType")))

    def get_typedef_multiplicity(self) -> str:
        """Returns the multiplicity of the typedef.

        Returns:
            The multiplicity of the typedef.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::getTypedefMultiplicity()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "typedefMultiplicity"))

    def is_array(self) -> int:
        """Checks whether the type is an array.

        Returns:
            1 if the type is an array, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isArray()
        """
        return int(self.call_com(lambda: self._com.isArray()))

    def is_enum(self) -> int:
        """For types whose kind was set to Language, parses the declaration to see if the type is actually an enum.

        Returns:
            1 if the type is an enum, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isEnum()
        """
        return int(self.call_com(lambda: self._com.isEnum()))

    def is_equal_to(self) -> int:
        """Checks whether the type is an equal-to type.

        Returns:
            1 if the type is an equal-to type, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isEqualTo()
        """
        return int(self.call_com(lambda: self._com.isEqualTo()))

    def is_implicit(self) -> int:
        """Checks whether the type is implicit.

        Returns:
            1 if the type is implicit, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isImplicit()
        """
        return int(self.call_com(lambda: self._com.isImplicit()))

    def is_kind_enumeration(self) -> int:
        """Checks whether the kind of the type is Enumeration.

        Returns:
            1 if the kind of the type is Enumeration, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isKindEnumeration()
        """
        return int(self.call_com(lambda: self._com.isKindEnumeration()))

    def is_kind_language(self) -> int:
        """Checks whether the kind of the type was set to Language.

        Returns:
            1 if the kind of the type is Language, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isKindLanguage()
        """
        return int(self.call_com(lambda: self._com.isKindLanguage()))

    def is_kind_struct(self) -> int:
        """Checks whether the kind of the type is Structure.

        Returns:
            1 if the kind of the type is Structure, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isKindStruct()
        """
        return int(self.call_com(lambda: self._com.isKindStruct()))

    def is_kind_typedef(self) -> int:
        """Checks whether the kind of the type is Typedef.

        Returns:
            1 if the kind of the type is Typedef, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isKindTypedef()
        """
        return int(self.call_com(lambda: self._com.isKindTypedef()))

    def is_kind_union(self) -> int:
        """Checks whether the kind of the type is Union.

        Returns:
            1 if the kind of the type is Union, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isKindUnion()
        """
        return int(self.call_com(lambda: self._com.isKindUnion()))

    def is_pointer(self) -> int:
        """Checks whether the type is a pointer.

        Returns:
            1 if the type is a pointer, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isPointer()
        """
        return int(self.call_com(lambda: self._com.isPointer()))

    def is_pointer_to_pointer(self) -> int:
        """Checks whether the type is a pointer to a pointer.

        Returns:
            1 if the type is a pointer to a pointer, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isPointerToPointer()
        """
        return int(self.call_com(lambda: self._com.isPointerToPointer()))

    def is_reference(self) -> int:
        """Checks whether the type is a reference.

        Returns:
            1 if the type is a reference, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isReference()
        """
        return int(self.call_com(lambda: self._com.isReference()))

    def is_reference_to_pointer(self) -> int:
        """Checks whether the type is a reference to a pointer.

        Returns:
            1 if the type is a reference to a pointer, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isReferenceToPointer()
        """
        return int(self.call_com(lambda: self._com.isReferenceToPointer()))

    def is_struct(self) -> int:
        """For types whose kind was set to Language, parses the declaration to see if the type is actually a struct.

        Returns:
            1 if the type is a struct, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isStruct()
        """
        return int(self.call_com(lambda: self._com.isStruct()))

    def is_template(self) -> int:
        """Checks whether the type is a template.

        Returns:
            1 if the type is a template, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isTemplate()
        """
        return int(self.call_com(lambda: self._com.isTemplate()))

    def is_union(self) -> int:
        """For types whose kind was set to Language, parses the declaration to see if the type is actually a union.

        Returns:
            1 if the type is a union, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::isUnion()
        """
        return int(self.call_com(lambda: self._com.isUnion()))

    def set_declaration(self, declaration: str) -> None:
        """Sets the declaration of the type.

        Args:
            declaration: The declaration to set for the type.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::setDeclaration(java.lang.String declaration)
        """
        AbstractRPModelElement.set_com_property(self._com, "declaration", declaration)

    def set_is_typedef_constant(self, is_typedef_constant: int) -> None:
        """Sets whether the typedef is a constant.

        Args:
            is_typedef_constant: Use 1 to specify that the typedef is a constant,
                0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::setIsTypedefConstant(int isTypedefConstant)
        """
        AbstractRPModelElement.set_com_property(self._com, "isTypedefConstant", is_typedef_constant)

    def set_is_typedef_ordered(self, is_typedef_ordered: int) -> None:
        """Sets whether the typedef is ordered.

        Args:
            is_typedef_ordered: Use 1 to specify that the typedef is ordered,
                0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::setIsTypedefOrdered(int isTypedefOrdered)
        """
        AbstractRPModelElement.set_com_property(self._com, "isTypedefOrdered", is_typedef_ordered)

    def set_is_typedef_reference(self, is_typedef_reference: int) -> None:
        """Sets whether the typedef is a reference.

        Args:
            is_typedef_reference: Use 1 to specify that the typedef is a reference,
                0 otherwise.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::setIsTypedefReference(int isTypedefReference)
        """
        AbstractRPModelElement.set_com_property(self._com, "isTypedefReference", is_typedef_reference)

    def set_kind(self, kind: str) -> None:
        """Sets the kind of the type.

        Args:
            kind: The kind to set for the type.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::setKind(java.lang.String kind)
        """
        AbstractRPModelElement.set_com_property(self._com, "kind", kind)

    def set_typedef_base_type(self, typedef_base_type: IRPClassifier) -> None:
        """Sets the base type of the typedef.

        Args:
            typedef_base_type: The base type to set for the typedef.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::setTypedefBaseType(com.telelogic.rhapsody.core.IRPClassifier typedefBaseType)
        """
        AbstractRPModelElement.set_com_property(self._com, "typedefBaseType", typedef_base_type._com)

    def set_typedef_multiplicity(self, typedef_multiplicity: str) -> None:
        """Sets the multiplicity of the typedef.

        Args:
            typedef_multiplicity: The multiplicity to set for the typedef.

        Raises:
            RhapsodyRuntimeException: If an error occurs during the operation.

        Reference:
            com.telelogic.rhapsody.core.IRPType::setTypedefMultiplicity(java.lang.String typedefMultiplicity)
        """
        AbstractRPModelElement.set_com_property(self._com, "typedefMultiplicity", typedef_multiplicity)


AbstractRPModelElement.register_wrapper("Type", IRPType)
