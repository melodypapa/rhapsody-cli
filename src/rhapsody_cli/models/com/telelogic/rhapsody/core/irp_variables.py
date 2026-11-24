"""Variable-family wrappers: mirrors IRPVariable from
com.telelogic.rhapsody.core (IRPAttribute/IRPArgument live in the canonical package).
"""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_profile import IRPProfile
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_values import (
        IRPInstanceValue,
        IRPLiteralSpecification,
    )


class IRPVariable(IRPUnit):
    """Wraps ``IRPVariable``: the base interface for typed elements (such as
    attributes and parameters) that carry a type and default value.
    """

    # IRPVariable method parity checklist:
    # [x] add_element_default_value  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_string_default_value  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_declaration  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_default_value  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_type  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_value_specifications  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_declaration  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_default_value  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_type  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_type_declaration  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [inherited] irp_unit / irp_model_element methods (covered by rp_unit / rp_model_element checklists)
    # No deprecated IRPVariable methods.

    def add_element_default_value(self, new_default_val: IRPModelElement) -> "IRPInstanceValue":
        """For tags with multiplicity greater than 1, adds a model element as an additional value.

        Args:
            new_default_val: The model element to add as an additional default value.

        Returns:
            The wrapped ``IRPInstanceValue`` created for the new default value.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::addElementDefaultValue(com.telelogic.rhapsody.core.IRPModelElement newDefaultVal)
        """
        return cast("IRPInstanceValue", self.wrap(self.call_com(lambda: self._com.addElementDefaultValue(new_default_val._com))))

    def add_string_default_value(self, new_default_val: str) -> "IRPLiteralSpecification":
        """For tags with multiplicity greater than 1, adds a string as an additional value.

        Args:
            new_default_val: The string to add as an additional default value.

        Returns:
            The wrapped ``IRPLiteralSpecification`` created for the new default value.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::addStringDefaultValue(java.lang.String newDefaultVal)
        """
        return cast("IRPLiteralSpecification", self.wrap(self.call_com(lambda: self._com.addStringDefaultValue(new_default_val))))

    def get_declaration(self) -> str:
        """Returns the type declaration if an on-the-fly type was used for the element.

        Returns:
            The on-the-fly type declaration, or an existing type's info if one was used.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::getDeclaration()
        """
        return str(self._get_method_or_property(self._com, "getDeclaration", "declaration"))

    def get_default_value(self) -> str:
        """Returns the default value that was set for the variable.

        Returns:
            The default value as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::getDefaultValue()
        """
        return str(self._get_method_or_property(self._com, "getDefaultValue", "defaultValue"))

    def get_type(self) -> "IRPClassifier":
        """Returns the type of the variable.

        Returns:
            The wrapped ``IRPClassifier`` that is the type of the variable.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::getType()
        """
        return cast("IRPClassifier", self.wrap(self._get_method_or_property(self._com, "getType", "type")))

    def get_value_specifications(self) -> IRPCollection:
        """Returns the initial values declared for elements with multiplicity greater than one.

        Returns:
            An ``IRPCollection`` of the declared initial value specifications.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::getValueSpecifications()
        """
        return IRPCollection(self._get_method_or_property(self._com, "getValueSpecifications", "valueSpecifications"))

    def set_declaration(self, declaration: str) -> None:
        """Specifies an on-the-fly declaration for the type of the element.

        Args:
            declaration: The on-the-fly type declaration to use instead of an existing type.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::setDeclaration(java.lang.String declaration)
        """
        self._set_method_or_property(self._com, "setDeclaration", "declaration", declaration)

    def set_default_value(self, default_value: str) -> None:
        """Sets a new default value for the variable.

        Args:
            default_value: The new default value.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::setDefaultValue(java.lang.String defaultValue)
        """
        self._set_method_or_property(self._com, "setDefaultValue", "defaultValue", default_value)

    def set_type(self, type_: IRPClassifier) -> None:
        """Sets the type of the variable.

        Args:
            type_: The classifier to use as the variable's type.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::setType(com.telelogic.rhapsody.core.IRPClassifier type)
        """
        self._set_method_or_property(self._com, "setType", "type", type_._com)

    def set_type_declaration(self, new_val: str) -> None:
        """Specifies an on-the-fly type declaration, reusing a matching existing type if found.

        Args:
            new_val: The on-the-fly type declaration.

        Reference:
            com.telelogic.rhapsody.core.IRPVariable::setTypeDeclaration(java.lang.String newVal)
        """
        # TODO: Under Rhapsody2.Application.1 the 'typeDeclaration' property is not settable (or the
        # 'setTypeDeclaration' method is absent), so this silently no-ops. Persist the type declaration
        # via the metatype property system in a future Rhapsody build.
        self._set_method_or_property(self._com, "setTypeDeclaration", "typeDeclaration", new_val)


IRPModelElement.register_wrapper("Variable", IRPVariable)


class IRPTag(IRPVariable):
    """Wraps ``IRPTag``: a tag that extends ``IRPVariable``."""

    # IRPTag method parity checklist:
    # [x] get_base  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_from_profile  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_multiplicity  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_tag_meta_class  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_value  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_multiplicity  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_tag_context_value  [x] impl  [x] docstring  [x] unit test  [ ] integration test   (inherited from rp_model_element)
    # [x] set_tag_meta_class  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_value  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_variable / irp_unit / irp_model_element methods (covered by rp_variable / rp_unit / rp_model_element checklists)
    # No deprecated IRPTag methods.

    def get_base(self) -> "IRPTag":
        """Returns the base tag on which the local copy of the tag is based.

        Returns:
            The wrapped ``IRPTag`` that is the base of the tag.

        Reference:
            com.telelogic.rhapsody.core.IRPTag::getBase()
        """
        return cast("IRPTag", self.wrap(self._get_method_or_property(self._com, "getBase", "base")))

    def get_from_profile(self) -> "IRPProfile":
        """Returns the profile from which the tag originates.

        Returns:
            The wrapped ``IRPProfile`` from which the tag originates.

        Reference:
            com.telelogic.rhapsody.core.IRPTag::getFromProfile()
        """
        return cast("IRPProfile", self.wrap(self._get_method_or_property(self._com, "getFromProfile", "fromProfile")))

    def get_multiplicity(self) -> str:
        """Gets the multiplicity specified for the tag.

        Returns:
            The multiplicity string (e.g. ``"1"``, ``"0..*"``).

        Reference:
            com.telelogic.rhapsody.core.IRPTag::getMultiplicity()
        """
        return str(self._get_method_or_property(self._com, "getMultiplicity", "multiplicity"))

    def get_tag_meta_class(self) -> str:
        """Returns the meta class of the tag.

        Returns:
            The meta class name as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPTag::getTagMetaClass()
        """
        return str(self._get_method_or_property(self._com, "getTagMetaClass", "tagMetaClass"))

    def get_value(self) -> str:
        """Returns the value of the tag.

        Returns:
            The tag value as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPTag::getValue()
        """
        return str(self._get_method_or_property(self._com, "getValue", "value"))

    def set_multiplicity(self, multiplicity: str) -> None:
        """Specifies the multiplicity for the tag.

        Args:
            multiplicity: The multiplicity string to set (e.g. ``"1"``, ``"0..*"``).

        Reference:
            com.telelogic.rhapsody.core.IRPTag::setMultiplicity(java.lang.String multiplicity)
        """
        self._set_method_or_property(self._com, "setMultiplicity", "multiplicity", multiplicity)

    def set_tag_meta_class(self, tag_meta_class: str) -> None:
        """Sets the meta class of the tag.

        Args:
            tag_meta_class: The meta class name to set.

        Reference:
            com.telelogic.rhapsody.core.IRPTag::setTagMetaClass(java.lang.String tagMetaClass)
        """
        self._set_method_or_property(self._com, "setTagMetaClass", "tagMetaClass", tag_meta_class)

    def set_value(self, value: str) -> None:
        """Sets the value of the tag.

        Args:
            value: The value to set for the tag.

        Reference:
            com.telelogic.rhapsody.core.IRPTag::setValue(java.lang.String value)
        """
        self._set_method_or_property(self._com, "setValue", "value", value)


IRPModelElement.register_wrapper("Tag", IRPTag)
