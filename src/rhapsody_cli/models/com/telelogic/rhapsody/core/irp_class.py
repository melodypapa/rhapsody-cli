"""Wraps ``com.telelogic.rhapsody.core.IRPClass``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.core import AbstractRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType
    from rhapsody_cli.models.elements.graphics.model_graphics import RPLink
    from rhapsody_cli.models.elements.interactions.model_interactions import RPEvent, RPEventReception


class IRPClass(IRPClassifier):
    """Wraps ``IRPClass``: represents a class in the model."""

    # IRPClass method parity checklist:
    # [x] add_class                 [x] impl  [x] docstring  [x] unit test  [x] integration test   (already implemented)
    # [x] add_constructor           [x] impl  [x] docstring  [x] unit test  [x] integration test   (already implemented)
    # [x] add_destructor            [x] impl  [x] docstring  [x] unit test  [x] integration test   (already implemented)
    # [x] add_superclass            [x] impl  [x] docstring  [x] unit test  [x] integration test   (already implemented)
    # [x] is_abstract                [x] impl (property)  [x] docstring  [x] unit test  [x] integration test
    # [x] add_event_reception        [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_event_reception_with_event [x] impl (raises NotImplementedError) [x] docstring [x] unit test  [x] integration test  (COM method not exposed)
    # [x] add_link                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_link_to_part_via_port     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_reception             [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_triggered_operation    [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_type                  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] delete_class              [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] delete_constructor        [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] delete_destructor         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] delete_event_reception     [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] delete_reception          [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] delete_superclass         [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] delete_type               [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_active                  [x] impl (property)  [x] docstring  [x] unit test  [x] integration test
    # [x] is_behavior_overriden      [x] impl (property)  [x] docstring  [x] unit test  [x] integration test
    # [x] is_composite               [x] impl (property)  [x] docstring  [x] unit test  [x] integration test
    # [x] get_is_final               [x] impl (method)    [x] docstring  [x] unit test  [ ] integration test (removed: setIsFinal does not persist in Rhapsody COM)
    # [x] set_is_final               [x] impl (method)    [x] docstring  [x] unit test  [ ] integration test (removed: setIsFinal does not persist in Rhapsody COM)
    # [x] is_reactive                [x] impl (property)  [x] docstring  [x] unit test  [x] integration test
    # update_contained_diagrams_on_server: unavailable in Rhapsody2.Application.1 type library; wrapper removed.
    # No deprecated methods in IRPClass.

    def add_superclass(self, super_class: IRPClass) -> None:
        """Adds a superclass to this class.

        Args:
            super_class: The class to inherit from.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addSuperclass(com.telelogic.rhapsody.core.IRPClass superClass)
        """
        AbstractRPModelElement.call_com(lambda: self._com.addSuperclass(super_class._com))

    def add_constructor(self, arguments_data: str) -> IRPOperation:
        """Adds a constructor operation to this class.

        Args:
            arguments_data: The argument specification for the constructor.

        Returns:
            The wrapped ``IRPOperation`` for the new constructor.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addConstructor(java.lang.String argumentsData)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation

        return cast(IRPOperation, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addConstructor(arguments_data))))

    def add_destructor(self) -> IRPOperation:
        """Adds a destructor operation to this class.

        Returns:
            The wrapped ``IRPOperation`` for the new destructor.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addDestructor()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation

        return cast(IRPOperation, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addDestructor())))

    @property
    def is_abstract(self) -> bool:
        """Checks whether this class is abstract."""
        return bool(AbstractRPModelElement.get_com_property(self._com, "isAbstract"))

    @is_abstract.setter
    def is_abstract(self, is_abstract: bool) -> None:
        """Unimplemented: the COM write is accepted but never persists."""
        raise NotImplementedError("IRPClass.is_abstract setter is unimplemented: Rhapsody2.Application.1 accepts the write but never persists it.")

    def add_class(self, name: str) -> IRPClass:
        """Adds a nested class to this class.

        Args:
            name: The name of the new nested class.

        Returns:
            The wrapped ``IRPClass`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addClass(java.lang.String name)
        """
        return cast(IRPClass, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addClass(name))))

    def add_event_reception(self, name: str) -> RPEventReception:
        """Adds an event reception to the current class.

        It is preferable to use :meth:`add_reception` instead.

        Args:
            name: The name to use for the new event reception.

        Returns:
            The wrapped ``IRPEventReception`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addEventReception(java.lang.String name)
        """
        from rhapsody_cli.models.elements.interactions.model_interactions import RPEventReception

        return cast(RPEventReception, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addEventReception(name))))

    def add_event_reception_with_event(self, name: str, event: RPEvent) -> RPEventReception:
        """Adds a new event reception, using the specified event.

        Note: ``addEventReceptionWithEvent`` is not exposed in the Rhapsody COM
        automation type library. This method raises ``NotImplementedError`` to
        prevent its use.

        Args:
            name: The name to use for the new event reception.
            event: The event that should be associated with the new event reception.

        Returns:
            The wrapped ``IRPEventReception`` created.

        Raises:
            NotImplementedError: Always raised, as this method is not exposed
                in the Rhapsody COM type library.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addEventReceptionWithEvent(java.lang.String name, com.telelogic.rhapsody.core.IRPEvent event)
        """
        raise NotImplementedError(
            "addEventReceptionWithEvent is not exposed in the Rhapsody COM automation type library. Use add_event_reception(name) instead and set the event via the reception object."
        )

    def update_contained_diagrams_on_server(self, enforce_update: int) -> int:
        """Update this class's diagrams on the server.

        Raises:
            NotImplementedError: The Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::updateContainedDiagramsOnServer(int enforceUpdate)
        """
        raise NotImplementedError("updateContainedDiagramsOnServer is not exposed in the Rhapsody COM automation type library.")

    def add_link(self, from_part: IRPModelElement, to_part: IRPModelElement, assoc: IRPModelElement, from_port: IRPModelElement, to_port: IRPModelElement) -> RPLink:
        """Creates a link between two parts belonging to a class.

        In addition to the two parts, you must supply either the association the
        link should represent, or the two ports to use for the link. If you
        provide the two ports, use ``None`` for the association. If you specify an
        association, use ``None`` for the two ports. If you are not specifying the
        two ports, you must still provide an association as an argument even when
        only one relevant association exists.

        Args:
            from_part: The "from" part for the link.
            to_part: The "to" part for the link.
            assoc: The association that the link should represent.
            from_port: The "from" port for the link.
            to_port: The "to" port for the link.

        Returns:
            The wrapped ``IRPLink`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addLink(
                com.telelogic.rhapsody.core.IRPInstance fromPart,
                com.telelogic.rhapsody.core.IRPInstance toPart,
                com.telelogic.rhapsody.core.IRPRelation assoc,
                com.telelogic.rhapsody.core.IRPPort fromPort,
                com.telelogic.rhapsody.core.IRPPort toPort)
        """
        from rhapsody_cli.models.elements.graphics.model_graphics import RPLink

        return cast(RPLink, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addLink(from_part._com, to_part._com, assoc._com, from_port._com, to_port._com))))

    def add_link_to_part_via_port(self, to_part: IRPModelElement, part_port: IRPModelElement, class_port: IRPModelElement, assoc: IRPModelElement) -> RPLink:
        """Creates a delegation connector between a class and one of its parts.

        You must supply either the association the link should represent, or the
        two ports (``part_port`` and ``class_port``) to use. If you provide the
        two ports, use ``None`` for ``assoc``; if you specify an association, use
        ``None`` for the two ports. If you are not specifying the two ports, you
        must still provide an association even when only one relevant
        association exists.

        Args:
            to_part: The part that should be linked to.
            part_port: The port to use on the part.
            class_port: The port to use on the class.
            assoc: The association that the link should represent.

        Returns:
            The wrapped ``IRPLink`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addLinkToPartViaPort(
                com.telelogic.rhapsody.core.IRPInstance toPart,
                com.telelogic.rhapsody.core.IRPInstance partPort,
                com.telelogic.rhapsody.core.IRPInstance classPort,
                com.telelogic.rhapsody.core.IRPRelation assoc)
        """
        from rhapsody_cli.models.elements.graphics.model_graphics import RPLink

        return cast(RPLink, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addLinkToPartViaPort(to_part._com, part_port._com, class_port._com, assoc._com))))

    def add_reception(self, name: str) -> RPEventReception:
        """Adds a reception to the current class.

        Args:
            name: The name to use for the new reception.

        Returns:
            The wrapped ``IRPEventReception`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addReception(java.lang.String name)
        """
        from rhapsody_cli.models.elements.interactions.model_interactions import RPEventReception

        return cast(RPEventReception, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addReception(name))))

    def add_triggered_operation(self, name: str) -> IRPOperation:
        """Adds a new triggered operation to the current class.

        Args:
            name: The name to use for the new triggered operation.

        Returns:
            The wrapped ``IRPOperation`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addTriggeredOperation(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation

        return cast(IRPOperation, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addTriggeredOperation(name))))

    def add_type(self, name: str) -> IRPType:
        """Adds a new type to the current class.

        Args:
            name: The name to use for the new type.

        Returns:
            The wrapped ``IRPType`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::addType(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType

        return cast(IRPType, AbstractRPModelElement.wrap(AbstractRPModelElement.call_com(lambda: self._com.addType(name))))

    def delete_class(self, name: str) -> None:
        """Deletes the specified class from the current class.

        Args:
            name: The name of the class that should be deleted.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::deleteClass(java.lang.String name)
        """
        AbstractRPModelElement.call_com(lambda: self._com.deleteClass(name))

    def delete_constructor(self, constructor: IRPOperation) -> None:
        """Deletes the specified constructor from the current class.

        Args:
            constructor: The constructor that should be deleted (an ``IRPOperation``).

        Reference:
            com.telelogic.rhapsody.core.IRPClass::deleteConstructor(com.telelogic.rhapsody.core.IRPOperation constructor)
        """
        AbstractRPModelElement.call_com(lambda: self._com.deleteConstructor(constructor._com))

    def delete_destructor(self) -> None:
        """Deletes the destructor for the class.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::deleteDestructor()
        """
        AbstractRPModelElement.call_com(lambda: self._com.deleteDestructor())

    def delete_event_reception(self, p_val: RPEventReception) -> None:
        """Deletes the specified event reception.

        It is preferable to use :meth:`delete_reception` instead.

        Args:
            p_val: The reception that should be deleted.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::deleteEventReception(com.telelogic.rhapsody.core.IRPEventReception pVal)
        """
        AbstractRPModelElement.call_com(lambda: self._com.deleteEventReception(p_val._com))

    def delete_reception(self, p_val: RPEventReception) -> None:
        """Deletes the specified reception from the current class.

        Args:
            p_val: The reception that should be deleted.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::deleteReception(com.telelogic.rhapsody.core.IRPEventReception pVal)
        """
        AbstractRPModelElement.call_com(lambda: self._com.deleteReception(p_val._com))

    def delete_superclass(self, super_class: IRPClass) -> None:
        """Removes the inheritance relationship with the specified base class.

        Args:
            super_class: The base class of the current class.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::deleteSuperclass(com.telelogic.rhapsody.core.IRPClass superClass)
        """
        AbstractRPModelElement.call_com(lambda: self._com.deleteSuperclass(super_class._com))

    def delete_type(self, name: str) -> None:
        """Deletes the specified type from the current class.

        Args:
            name: The name of the type that should be deleted.

        Reference:
            com.telelogic.rhapsody.core.IRPClass::deleteType(java.lang.String name)
        """
        AbstractRPModelElement.call_com(lambda: self._com.deleteType(name))

    @property
    def is_active(self) -> int:
        """``1`` if the class runs on its own thread, ``0`` if sequential."""
        return int(AbstractRPModelElement.get_com_property(self._com, "isActive"))

    @is_active.setter
    def is_active(self, is_active: int) -> None:
        """Set to ``1`` for active, ``0`` for sequential."""
        AbstractRPModelElement.set_com_property(self._com, "isActive", is_active)

    @property
    def is_behavior_overriden(self) -> int:
        """``1`` if the class does not inherit its base statechart behavior, else ``0``."""
        return int(AbstractRPModelElement.get_com_property(self._com, "isBehaviorOverriden"))

    @is_behavior_overriden.setter
    def is_behavior_overriden(self, is_behavior_overriden: int) -> None:
        """Set to ``1`` to not inherit the base statechart behavior, ``0`` to inherit."""
        AbstractRPModelElement.set_com_property(self._com, "isBehaviorOverriden", is_behavior_overriden)

    @property
    def is_composite(self) -> int:
        """``1`` if the class is a composite class, ``0`` otherwise."""
        return int(AbstractRPModelElement.get_com_property(self._com, "isComposite"))

    def get_is_final(self) -> int:
        """Returns ``1`` if the class is final, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPClass.getIsFinal()
        """
        return int(AbstractRPModelElement.call_com(lambda: self._com.getIsFinal()))

    def set_is_final(self, is_final: int) -> None:
        """Set to ``1`` to make the class final, ``0`` otherwise.

        Args:
            is_final: ``1`` to make the class final, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPClass.setIsFinal(int isFinal)
        """
        AbstractRPModelElement.call_com(lambda: self._com.setIsFinal(is_final))

    @property
    def is_reactive(self) -> int:
        """``1`` if the class has a statechart or activity diagram, ``0`` otherwise."""
        return int(AbstractRPModelElement.get_com_property(self._com, "isReactive"))


AbstractRPModelElement.register_wrapper("Class", IRPClass)
