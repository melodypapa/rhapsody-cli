"""Wrappers for ``com.telelogic.rhapsody.core.IRPArgument``.

Canonical module for :class:`IRPArgument`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_argument.md``.
"""

from __future__ import annotations

from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.variables.model_variables import RPVariable


class IRPArgument(RPVariable):
    """Wraps ``IRPArgument``: an argument/parameter of an operation."""

    # IRPArgument method parity checklist:
    # [x] get_argument_direction  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_argument_direction  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_variable / irp_unit / irp_model_element methods (covered by rp_variable / rp_unit / rp_model_element checklists)
    # No deprecated IRPArgument methods.

    def get_argument_direction(self) -> str:
        """Returns the direction of the argument (e.g. ``"in"``, ``"out"``, ``"inout"``).

        Returns:
            The argument direction as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPArgument::getArgumentDirection()
        """
        return str(AbstractRPModelElement.get_com_property(self._com, "argumentDirection"))

    def set_argument_direction(self, argument_direction: str) -> None:
        """Sets the direction of the argument.

        Args:
            argument_direction: The direction to set (e.g. ``"in"``, ``"out"``, ``"inout"``).

        Reference:
            com.telelogic.rhapsody.core.IRPArgument::setArgumentDirection(java.lang.String argumentDirection)
        """
        AbstractRPModelElement.set_com_property(self._com, "argumentDirection", argument_direction)


AbstractRPModelElement.register_wrapper("Argument", IRPArgument)
