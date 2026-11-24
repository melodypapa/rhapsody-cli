"""Wrappers for ``com.telelogic.rhapsody.core.IRPAttribute``.

Canonical module for :class:`IRPAttribute`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_attribute.md``.
"""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_variables import IRPVariable


class IRPAttribute(IRPVariable):
    """Wraps ``IRPAttribute``: represents an attribute in a classifier."""

    # IRPAttribute method parity checklist:
    # [x] is_constant  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_ordered  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_reference  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_static  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] multiplicity  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] visibility  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_variable / irp_unit / irp_model_element methods (covered by rp_variable / rp_unit / rp_model_element checklists)
    # No deprecated IRPAttribute methods.

    @property
    def is_constant(self) -> int:
        """Checks whether the attribute is defined as constant.

        Returns:
            ``1`` if the attribute is constant, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getIsConstant()
        """
        return int(self.get_com_property(self._com, "isConstant"))

    @is_constant.setter
    def is_constant(self, is_constant: bool) -> None:
        """Specifies whether the attribute should be defined as constant.

        Args:
            is_constant: ``True`` to mark the attribute constant, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setIsConstant(int isConstant)
        """
        self.set_com_property(self._com, "isConstant", 1 if is_constant else 0)

    @property
    def is_ordered(self) -> int:
        """Checks whether the attribute is ordered.

        Returns:
            ``1`` if the attribute is ordered, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getIsOrdered()
        """
        return int(self.get_com_property(self._com, "isOrdered"))

    @is_ordered.setter
    def is_ordered(self, is_ordered: bool) -> None:
        """Specifies whether the attribute should be ordered.

        Args:
            is_ordered: ``True`` to mark the attribute ordered, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setIsOrdered(int isOrdered)
        """
        self.set_com_property(self._com, "isOrdered", 1 if is_ordered else 0)

    @property
    def is_reference(self) -> int:
        """Checks whether the attribute is a reference.

        Returns:
            ``1`` if the attribute is a reference, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getIsReference()
        """
        return int(self.get_com_property(self._com, "isReference"))

    @is_reference.setter
    def is_reference(self, is_reference: bool) -> None:
        """Specifies whether the attribute should be a reference.

        Args:
            is_reference: ``True`` to mark the attribute as a reference, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setIsReference(int isReference)
        """
        self.set_com_property(self._com, "isReference", 1 if is_reference else 0)

    @property
    def is_static(self) -> bool:
        """Checks whether the attribute was defined as static.

        Returns:
            ``True`` if the attribute is static, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getIsStatic()
        """
        return bool(self.get_com_property(self._com, "isStatic"))

    @is_static.setter
    def is_static(self, is_static: bool) -> None:
        """Specifies whether an attribute should be defined as static.

        Args:
            is_static: ``True`` to mark the attribute static, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setIsStatic(int isStatic)
        """
        self.set_com_property(self._com, "isStatic", 1 if is_static else 0)

    @property
    def multiplicity(self) -> str:
        """Gets the multiplicity specified for the attribute.

        Returns:
            The multiplicity string (e.g. ``"1"``, ``"0..*"``).

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getMultiplicity()
        """
        return str(self.get_com_property(self._com, "multiplicity"))

    @multiplicity.setter
    def multiplicity(self, multiplicity: str) -> None:
        """Specifies the multiplicity for the attribute.

        Args:
            multiplicity: The multiplicity string to set (e.g. ``"1"``, ``"0..*"``).

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setMultiplicity(java.lang.String multiplicity)
        """
        self.set_com_property(self._com, "multiplicity", multiplicity)

    @property
    def visibility(self) -> str:
        """Gets the visibility specified for the attribute.

        Returns:
            The visibility string (e.g. ``"public"``, ``"private"``).

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::getVisibility()
        """
        return str(self.get_com_property(self._com, "visibility"))

    @visibility.setter
    def visibility(self, visibility: str) -> None:
        """Specifies the visibility of the attribute.

        Args:
            visibility: The visibility string to set (e.g. ``"public"``, ``"private"``).

        Reference:
            com.telelogic.rhapsody.core.IRPAttribute::setVisibility(java.lang.String visibility)
        """
        self.set_com_property(self._com, "visibility", visibility)


IRPModelElement.register_wrapper("Attribute", IRPAttribute)
