"""Actions model-element wrappers (auto-generated stubs)."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPMessage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent


class IRPAcceptEventAction(IRPState):
    """Wraps ``IRPAcceptEventAction``: represents Accept Event Action elements in a statechart or activity diagram."""

    # IRPAcceptEventAction method parity checklist:
    # [x] get_event                     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_event                     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_state methods (covered by rp_state checklist)
    # [inherited] irp_state_vertex methods (covered by rp_state_vertex checklist)
    # No deprecated IRPAcceptEventAction methods.

    def get_event(self) -> "IRPEvent":
        """Returns the event that the action waits for.

        Returns:
            The event that the action waits for.

        Reference:
            com.telelogic.rhapsody.core.IRPAcceptEventAction::getEvent()
        """
        return cast("IRPEvent", self.wrap(self._get_method_or_property(self._com, "getEvent", "event")))

    def set_event(self, event: "IRPEvent") -> None:
        """Specifies the event that the action should wait for.

        Args:
            event: The event that the action should wait for.

        Reference:
            com.telelogic.rhapsody.core.IRPAcceptEventAction::setEvent(com.telelogic.rhapsody.core.IRPEvent event)
        """
        self._set_method_or_property(self._com, "setEvent", "event", event._com)


class IRPActionBlock(IRPMessage):
    """Wraps ``IRPActionBlock``: represents action blocks in sequence diagrams."""

    # IRPActionBlock method parity checklist:
    # [inherited] irp_message methods (covered by rp_message checklist)
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPActionBlock methods.

    pass


# Register wrappers for Rhapsody meta classes
IRPModelElement.register_wrapper("AcceptEventAction", IRPAcceptEventAction)
IRPModelElement.register_wrapper("ActionBlock", IRPActionBlock)
