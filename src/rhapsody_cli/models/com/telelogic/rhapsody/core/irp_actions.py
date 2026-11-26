"""Actions model-element wrappers (auto-generated stubs)."""

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPMessage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_values import IRPValueSpecification

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


class IRPAcceptTimeEvent(IRPState):
    """Wraps ``IRPAcceptTimeEvent``: represents Accept Time Event elements in activity diagrams and statecharts."""

    # IRPAcceptTimeEvent method parity checklist:
    # [x] get_duration_time              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_duration_time              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_state methods (covered by rp_state checklist)
    # [inherited] irp_state_vertex methods (covered by rp_state_vertex checklist)
    # No deprecated IRPAcceptTimeEvent methods.

    def get_duration_time(self) -> str:
        """Returns the duration that was specified for this element.

        Returns:
            The duration that was specified for this element.

        Reference:
            com.telelogic.rhapsody.core.IRPAcceptTimeEvent::getDurationTime()
        """
        return str(self._get_method_or_property(self._com, "getDurationTime", "durationTime"))

    def set_duration_time(self, duration_time: str) -> None:
        """Specifies the duration that should be used for this element.

        Args:
            duration_time: The duration that should be used for this element.

        Reference:
            com.telelogic.rhapsody.core.IRPAcceptTimeEvent::setDurationTime(java.lang.String durationTime)
        """
        self._set_method_or_property(self._com, "setDurationTime", "durationTime", duration_time)


class IRPActionBlock(IRPMessage):
    """Wraps ``IRPActionBlock``: represents action blocks in sequence diagrams."""

    # IRPActionBlock method parity checklist:
    # [inherited] irp_message methods (covered by rp_message checklist)
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPActionBlock methods.

    pass


class IRPContextSpecification(IRPValueSpecification):
    """Wraps ``IRPContextSpecification``: represents the exact context of an object in a hierarchy.

    Uses a collection of strings for the full path to the element and a collection
    of indices to disambiguate when multiplicity is greater than one.
    """

    # IRPContextSpecification method parity checklist:
    # [x] get_multiplicities            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_value                     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_multiplicities            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_value                     [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_value_specification methods (covered by rp_value_specification checklist)
    # No deprecated IRPContextSpecification methods.

    def get_multiplicities(self) -> "IRPCollection":
        """Returns the collection of relevant indices for each of the model elements in the "value" collection.

        Returns:
            A ``IRPCollection`` of indices (integers provided as strings) for the
            model elements in the "value" collection.

        Reference:
            com.telelogic.rhapsody.core.IRPContextSpecification::getMultiplicities()
        """
        return IRPCollection(self._get_method_or_property(self._com, "getMultiplicities", "multiplicities"))

    def get_value(self) -> "IRPCollection":
        """Returns the collection of strings that represents the model elements constituting the full path to the element.

        Returns:
            A ``IRPCollection`` of strings representing the full path to the element.

        Reference:
            com.telelogic.rhapsody.core.IRPContextSpecification::getValue()
        """
        return IRPCollection(self._get_method_or_property(self._com, "getValue", "value"))

    def set_multiplicities(self, multiplicities: "IRPCollection") -> None:
        """Specifies the collection of indices to use for the model elements in the "value" collection.

        Args:
            multiplicities: A ``IRPCollection`` of indices (integers provided as
                strings) for the model elements in the "value" collection.

        Reference:
            com.telelogic.rhapsody.core.IRPContextSpecification::setMultiplicities(com.telelogic.rhapsody.core.IRPCollection multiplicities)
        """
        self.call_com(lambda: self._com.setMultiplicities(multiplicities._com))

    def set_value(self, value: "IRPCollection") -> None:
        """Specifies the collection of strings that represents the model elements constituting the full path to the element.

        Args:
            value: A ``IRPCollection`` of strings representing the full path to the
                element.

        Reference:
            com.telelogic.rhapsody.core.IRPContextSpecification::setValue(com.telelogic.rhapsody.core.IRPCollection value)
        """
        self.call_com(lambda: self._com.setValue(value._com))


# Register wrappers for Rhapsody meta classes
IRPModelElement.register_wrapper("AcceptEventAction", IRPAcceptEventAction)
IRPModelElement.register_wrapper("AcceptTimeEvent", IRPAcceptTimeEvent)
IRPModelElement.register_wrapper("ActionBlock", IRPActionBlock)
IRPModelElement.register_wrapper("ContextSpecification", IRPContextSpecification)
