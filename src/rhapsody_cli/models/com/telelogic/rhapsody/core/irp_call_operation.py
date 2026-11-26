"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPCallOperation``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation


class IRPCallOperation(IRPState):
    """Wraps ``IRPCallOperation``: a call operation in an activity diagram.

    The JavaDoc ``getOperation`` / ``getTarget`` accessors and their setters
    are exposed by pywin32 as two read/write properties.
    """

    # IRPCallOperation method parity checklist:
    # [x] operation                     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] target                        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)
    # [inherited] irp_state methods (covered by irp_state checklist)
    # [inherited] irp_state_vertex methods (covered by irp_state_vertex checklist)

    @property
    def operation(self) -> IRPInterfaceItem | None:
        """Returns the operation specified for this call operation element.

        Returns:
            The specified operation, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPCallOperation::getOperation()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem

        return cast(IRPInterfaceItem, self.wrap(self.get_com_property(self._com, "operation")))

    @operation.setter
    def operation(self, operation: IRPInterfaceItem) -> None:
        """Specifies the operation used by this call operation element.

        Args:
            operation: The operation to use.

        Reference:
            com.telelogic.rhapsody.core.IRPCallOperation::setOperation(com.telelogic.rhapsody.core.IRPInterfaceItem operation)
        """
        self.set_com_property(self._com, "operation", operation._com)

    @property
    def target(self) -> IRPRelation | None:
        """Returns the target specified for this call operation element.

        Returns:
            The specified target, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPCallOperation::getTarget()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation

        return cast(IRPRelation, self.wrap(self.get_com_property(self._com, "target")))

    @target.setter
    def target(self, target: IRPRelation) -> None:
        """Specifies the target used by this call operation element.

        Args:
            target: The target to use.

        Reference:
            com.telelogic.rhapsody.core.IRPCallOperation::setTarget(com.telelogic.rhapsody.core.IRPRelation target)
        """
        self.set_com_property(self._com, "target", target._com)


IRPModelElement.register_wrapper("CallOperation", IRPCallOperation)
