"""Wraps ``com.telelogic.rhapsody.core.IRPActor``."""

from __future__ import annotations

from typing import TYPE_CHECKING

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPEvent, IRPEventReception


class IRPActor(IRPClassifier):
    """Represents an actor in a Rhapsody model."""

    # The behavior-override getter/setter pair maps to the writable COM property
    # isBehaviorOverriden. Inherited classifier/unit/model-element members remain
    # owned by their respective wrappers.

    def add_event_reception_with_event(self, name: str, event: IRPEvent) -> IRPEventReception:
        """Adds an event reception associated with the specified event.

        The registered IRPActor typelib does not expose this JavaDoc method, so
        the wrapper raises before attempting COM dispatch.

        Args:
            name: Name for the new event reception.
            event: Event to associate with the reception.

        Returns:
            The event reception that would be created when the Java API is available.

        Raises:
            NotImplementedError: ``addEventReceptionWithEvent`` is absent from
                the registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPActor::addEventReceptionWithEvent(
            java.lang.String name, IRPEvent event)
        """
        raise NotImplementedError("addEventReceptionWithEvent is not exposed by the registered pywin32 interface.")

    @property
    def is_behavior_overriden(self) -> bool:
        """Checks whether the actor does not inherit its base class's statechart behavior.

        Returns:
            ``True`` if the actor overrides the inherited behavior, otherwise ``False``.

        Reference:
            com.telelogic.rhapsody.core.IRPActor::getIsBehaviorOverriden()
        """
        return bool(self.get_com_property(self._com, "isBehaviorOverriden"))

    @is_behavior_overriden.setter
    def is_behavior_overriden(self, is_overridden: bool) -> None:
        """Sets whether the actor should inherit the base class's statechart behavior.

        Args:
            is_overridden: ``True`` to stop inheriting the base behavior;
                ``False`` to inherit it.

        Reference:
            com.telelogic.rhapsody.core.IRPActor::setIsBehaviorOverriden(int isBehaviorOverriden)
        """
        self.set_com_property(self._com, "isBehaviorOverriden", 1 if is_overridden else 0)

    def update_contained_diagrams_on_server(self, enforce_update: int) -> int:
        """Updates views on the Rhapsody Model Manager server for contained diagrams.

        Args:
            enforce_update: ``0`` updates only changed views; ``1`` forces an update.

        Returns:
            Number of views updated; JavaDoc specifies ``0`` when none need
            updating and ``-1`` when the update attempt fails.

        Raises:
            NotImplementedError: ``updateContainedDiagramsOnServer`` is absent
                from the registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPActor::updateContainedDiagramsOnServer(int enforceUpdate)
        """
        raise NotImplementedError("updateContainedDiagramsOnServer is not exposed by the registered pywin32 interface.")


IRPModelElement.register_wrapper("Actor", IRPActor)
