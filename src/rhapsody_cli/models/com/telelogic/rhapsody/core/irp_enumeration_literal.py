"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPEnumerationLiteral``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement


class IRPEnumerationLiteral(IRPModelElement):
    """Wraps ``IRPEnumerationLiteral``: a literal value in an enumeration.

    The JavaDoc ``getValue`` / ``setValue`` pair is exposed by pywin32 as a
    read/write ``value`` property.
    """

    # IRPEnumerationLiteral method parity checklist:
    # [x] value                         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)

    @property
    def value(self) -> str:
        """Returns the value of the enumeration literal.

        Returns:
            The literal value as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPEnumerationLiteral::getValue()
        """
        return str(self.get_com_property(self._com, "value"))

    @value.setter
    def value(self, value: str) -> None:
        """Sets the value of the enumeration literal.

        Args:
            value: The value to set.

        Reference:
            com.telelogic.rhapsody.core.IRPEnumerationLiteral::setValue(java.lang.String value)
        """
        self.set_com_property(self._com, "value", value)


IRPModelElement.register_wrapper("EnumerationLiteral", IRPEnumerationLiteral)
