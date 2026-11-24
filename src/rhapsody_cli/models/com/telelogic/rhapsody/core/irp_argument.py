"""Wrappers for ``com.telelogic.rhapsody.core.IRPArgument``.

Canonical module for :class:`IRPArgument`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_argument.md``.
"""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_variables import IRPVariable


class IRPArgument(IRPVariable):
    """Wraps ``IRPArgument``: an argument/parameter of an operation."""

    # IRPArgument method parity checklist:
    # [x] argument_direction  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_variable / irp_unit / irp_model_element methods (covered by rp_variable / rp_unit / rp_model_element checklists)
    # No deprecated IRPArgument methods.

    @property
    def argument_direction(self) -> str:
        """Returns the direction of the argument (e.g. ``"in"``, ``"out"``, ``"inout"``).

        Returns:
            The argument direction as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPArgument::getArgumentDirection()
        """
        return str(self.get_com_property(self._com, "argumentDirection"))

    @argument_direction.setter
    def argument_direction(self, argument_direction: str) -> None:
        """Sets the direction of the argument.

        Args:
            argument_direction: The direction to set (e.g. ``"in"``, ``"out"``, ``"inout"``).

        Reference:
            com.telelogic.rhapsody.core.IRPArgument::setArgumentDirection(java.lang.String argumentDirection)
        """
        self.set_com_property(self._com, "argumentDirection", argument_direction)


IRPModelElement.register_wrapper("Argument", IRPArgument)
