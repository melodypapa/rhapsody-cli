"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPAcceptTimeEvent``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState


class IRPAcceptTimeEvent(IRPState):
    """Wraps ``IRPAcceptTimeEvent``: an Accept Time Event element.

    The JavaDoc ``getDurationTime`` / ``setDurationTime`` pair is exposed by
    pywin32 as a single read/write ``durationTime`` property.
    """

    # IRPAcceptTimeEvent method parity checklist:
    # [x] duration_time                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)
    # [inherited] irp_state methods (covered by irp_state checklist)
    # [inherited] irp_state_vertex methods (covered by irp_state_vertex checklist)

    @property
    def duration_time(self) -> str:
        """Returns the duration specified for this element.

        Returns:
            The duration string.

        Reference:
            com.telelogic.rhapsody.core.IRPAcceptTimeEvent::getDurationTime()
        """
        return str(self.get_com_property(self._com, "durationTime"))

    @duration_time.setter
    def duration_time(self, duration_time: str) -> None:
        """Specifies the duration used for this element.

        Args:
            duration_time: The duration string.

        Reference:
            com.telelogic.rhapsody.core.IRPAcceptTimeEvent::setDurationTime(java.lang.String durationTime)
        """
        self.set_com_property(self._com, "durationTime", duration_time)


IRPModelElement.register_wrapper("AcceptTimeEvent", IRPAcceptTimeEvent)
