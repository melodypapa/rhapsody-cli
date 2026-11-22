"""Wrappers for ``com.telelogic.rhapsody.core.IRPAttribute``.

Canonical module for :class:`IRPAttribute`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_attribute.md``.
"""

from __future__ import annotations

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.variables import RPVariable


class IRPAttribute(RPVariable):
    """Wraps ``IRPAttribute``: represents an attribute in a classifier."""

    # IRPAttribute method parity checklist:
    # [x] get_is_constant  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_is_ordered  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_is_reference  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_is_static  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_multiplicity  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_visibility  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_is_constant  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_is_ordered  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_is_reference  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_is_static  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_multiplicity  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_visibility  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_variable / irp_unit / irp_model_element methods (covered by rp_variable / rp_unit / rp_model_element checklists)
    # No deprecated IRPAttribute methods.

    def get_is_constant(self) -> int:
        """Checks whether the attribute is defined as constant.

        Returns:
            ``1`` if the attribute is constant, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getIsConstant()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "isConstant"))

    def get_is_ordered(self) -> int:
        """Checks whether the attribute is ordered.

        Returns:
            ``1`` if the attribute is ordered, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getIsOrdered()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "isOrdered"))

    def get_is_reference(self) -> int:
        """Checks whether the attribute is a reference.

        Returns:
            ``1`` if the attribute is a reference, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getIsReference()
        """
        return int(AbstractRPModelElement.get_com_property(self._com, "isReference"))

    def set_is_constant(self, is_constant: bool) -> None:
        """Specifies whether the attribute should be defined as constant.

        Args:
            is_constant: ``True`` to mark the attribute constant, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setIsConstant(int isConstant)
        """
        AbstractRPModelElement.set_com_property(self._com, "isConstant", 1 if is_constant else 0)

    def set_is_ordered(self, is_ordered: bool) -> None:
        """Specifies whether the attribute should be ordered.

        Args:
            is_ordered: ``True`` to mark the attribute ordered, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setIsOrdered(int isOrdered)
        """
        AbstractRPModelElement.set_com_property(self._com, "isOrdered", 1 if is_ordered else 0)

    def set_is_reference(self, is_reference: bool) -> None:
        """Specifies whether the attribute should be a reference.

        Args:
            is_reference: ``True`` to mark the attribute as a reference, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setIsReference(int isReference)
        """
        AbstractRPModelElement.set_com_property(self._com, "isReference", 1 if is_reference else 0)

    def get_multiplicity(self) -> str:
        """Gets the multiplicity specified for the attribute.

        Returns:
            The multiplicity string (e.g. ``"1"``, ``"0..*"``).

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getMultiplicity()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "multiplicity"))

    def set_multiplicity(self, multiplicity: str) -> None:
        """Specifies the multiplicity for the attribute.

        Args:
            multiplicity: The multiplicity string to set (e.g. ``"1"``, ``"0..*"``).

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setMultiplicity(java.lang.String multiplicity)
        """
        AbstractRPModelElement.set_com_property(self._com, "multiplicity", multiplicity)

    def get_is_static(self) -> bool:
        """Checks whether the attribute was defined as static.

        Returns:
            ``True`` if the attribute is static, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getIsStatic()
        """
        return bool(AbstractRPModelElement.get_com_property(self._com, "isStatic"))

    def set_is_static(self, is_static: bool) -> None:
        """Specifies whether an attribute should be defined as static.

        Args:
            is_static: ``True`` to mark the attribute static, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setIsStatic(int isStatic)
        """
        AbstractRPModelElement.set_com_property(self._com, "isStatic", 1 if is_static else 0)

    def get_visibility(self) -> str:
        """Gets the visibility specified for the attribute.

        Returns:
            The visibility string (e.g. ``"public"``, ``"private"``).

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getVisibility()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "visibility"))

    def set_visibility(self, visibility: str) -> None:
        """Specifies the visibility of the attribute.

        Args:
            visibility: The visibility string to set (e.g. ``"public"``, ``"private"``).

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setVisibility(java.lang.String visibility)
        """
        AbstractRPModelElement.set_com_property(self._com, "visibility", visibility)


AbstractRPModelElement.register_wrapper("Attribute", IRPAttribute)
