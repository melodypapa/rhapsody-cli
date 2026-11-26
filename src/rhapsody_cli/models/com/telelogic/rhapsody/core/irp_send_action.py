"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPSendAction``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_action import IRPAction
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem


class IRPSendAction(IRPAction):
    """Wraps ``IRPSendAction``: a Send Action element in an activity or statechart.

    JavaDoc accessors exposed by pywin32 as properties are surfaced as
    ``@property`` members; ``add_argument_value`` remains a method.
    """

    # IRPSendAction method parity checklist:
    # [x] arg_vals                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] event                         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] invoked_operation             [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] target                        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_argument_value            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_action methods (covered by irp_action checklist)
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)

    @property
    def arg_vals(self) -> IRPCollection:
        """Returns the argument values set for the associated event.

        Returns:
            A collection of string argument values.

        Reference:
            com.telelogic.rhapsody.core.IRPSendAction::getArgVals()
        """
        return IRPCollection(self.get_com_property(self._com, "argVals"))

    @property
    def event(self) -> IRPEvent | None:
        """Returns the event sent by this Send Action element.

        Returns:
            The event, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPSendAction::getEvent()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent

        return cast(IRPEvent, self.wrap(self.get_com_property(self._com, "event")))

    @event.setter
    def event(self, event: IRPEvent) -> None:
        """Specifies the event sent by this Send Action element.

        Args:
            event: The event to send.

        Reference:
            com.telelogic.rhapsody.core.IRPSendAction::setEvent(com.telelogic.rhapsody.core.IRPEvent event)
        """
        self.set_com_property(self._com, "event", event._com)

    @property
    def invoked_operation(self) -> IRPInterfaceItem | None:
        """Returns the interface item invoked by this Send Action element.

        Returns:
            The invoked interface item, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPSendAction::getInvokedOperation()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem

        return cast(IRPInterfaceItem, self.wrap(self.get_com_property(self._com, "invokedOperation")))

    @invoked_operation.setter
    def invoked_operation(self, invoked_operation: IRPInterfaceItem) -> None:
        """Sets the interface item invoked by this Send Action element.

        Args:
            invoked_operation: The interface item to invoke.

        Reference:
            com.telelogic.rhapsody.core.IRPSendAction::setInvokedOperation(com.telelogic.rhapsody.core.IRPInterfaceItem invokedOperation)
        """
        self.set_com_property(self._com, "invokedOperation", invoked_operation._com)

    @property
    def target(self) -> IRPModelElement | None:
        """Returns the event target of this Send Action element.

        Returns:
            The target element, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPSendAction::getTarget()
        """
        return self.wrap(self.get_com_property(self._com, "target"))

    @target.setter
    def target(self, target: IRPModelElement) -> None:
        """Sets the model element that is the target of this Send Action element.

        Args:
            target: The target model element.

        Reference:
            com.telelogic.rhapsody.core.IRPSendAction::setTarget(com.telelogic.rhapsody.core.IRPModelElement target)
        """
        self.set_com_property(self._com, "target", target._com)

    def add_argument_value(self, value: str, position: int) -> None:
        """Provides an argument value for an argument of the associated event.

        Args:
            value: The argument value, expressed as a string.
            position: The argument position in the list (starts at 1).

        Reference:
            com.telelogic.rhapsody.core.IRPSendAction::addArgumentValue(java.lang.String value, int position)
        """
        self.call_com(lambda: self._com.addArgumentValue(value, position))


IRPModelElement.register_wrapper("SendAction", IRPSendAction)
