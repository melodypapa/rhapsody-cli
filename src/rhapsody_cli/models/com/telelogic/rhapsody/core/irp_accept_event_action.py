"""Wrapper for ``com.telelogic.rhapsody.core.IRPAcceptEventAction``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent


class IRPAcceptEventAction(IRPState):
    """Represents an Accept Event Action in a statechart or activity diagram."""

    @property
    def event(self) -> IRPEvent:
        """Returns the event that the action waits for.

        Returns:
            The event that the action waits for.

        Reference:
            com.telelogic.rhapsody.core.IRPAcceptEventAction::getEvent()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent

        return cast(IRPEvent, self.wrap(self.get_com_property(self._com, "event")))

    @event.setter
    def event(self, event: IRPEvent) -> None:
        """Specifies the event that the action should wait for.

        Args:
            event: The event that the action should wait for.

        Reference:
            com.telelogic.rhapsody.core.IRPAcceptEventAction::setEvent(com.telelogic.rhapsody.core.IRPEvent event)
        """
        self.set_com_property(self._com, "event", event._com)


IRPModelElement.register_wrapper("AcceptEventAction", IRPAcceptEventAction)
