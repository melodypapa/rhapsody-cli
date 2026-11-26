"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPObjectNode``."""

from __future__ import annotations

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState


class IRPObjectNode(IRPState):
    """Wraps ``IRPObjectNode``: an Object Node in an activity diagram.

    JavaDoc accessors exposed by pywin32 as properties are surfaced as
    ``@property`` members; ``add_in_state`` and ``remove_in_state`` remain
    methods.
    """

    # IRPObjectNode method parity checklist:
    # [x] in_state                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] in_state_list                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] represents                    [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_in_state                  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove_in_state               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)
    # [inherited] irp_state methods (covered by irp_state checklist)
    # [inherited] irp_state_vertex methods (covered by irp_state_vertex checklist)

    @property
    def in_state(self) -> str:
        """Returns the "In State" of the object node.

        Deprecated in the Java API: use ``in_state_list`` instead.

        Returns:
            The "In State" value.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::getInState()
        """
        return str(self.get_com_property(self._com, "inState"))

    @in_state.setter
    def in_state(self, in_state: str) -> None:
        """Sets the "In State" of the object node.

        Deprecated in the Java API: use ``add_in_state`` instead.

        Args:
            in_state: The "In State" value to set.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::setInState(java.lang.String inState)
        """
        self.set_com_property(self._com, "inState", in_state)

    @property
    def in_state_list(self) -> IRPCollection:
        """Returns the "In State" states defined for the object node.

        Returns:
            The states as an ``IRPCollection``.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::getInStateList()
        """
        return IRPCollection(self.get_com_property(self._com, "inStateList"))

    @property
    def represents(self) -> IRPModelElement | None:
        """Returns the class or type represented by this object node.

        Returns:
            The represented element, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::getRepresents()
        """
        return self.wrap(self.get_com_property(self._com, "represents"))

    @represents.setter
    def represents(self, represents: IRPModelElement) -> None:
        """Specifies the class or type represented by this object node.

        Args:
            represents: The element to represent.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::setRepresents(com.telelogic.rhapsody.core.IRPModelElement represents)
        """
        self.set_com_property(self._com, "represents", represents._com)

    def add_in_state(self, val: IRPModelElement) -> None:
        """Adds a state to the "In State" list of the object node.

        Args:
            val: The state to add.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::addInState(com.telelogic.rhapsody.core.IRPModelElement val)
        """
        self.call_com(lambda: self._com.addInState(val._com))

    def remove_in_state(self, val: IRPModelElement) -> None:
        """Removes a state from the "In State" list of the object node.

        Args:
            val: The state to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::removeInState(com.telelogic.rhapsody.core.IRPModelElement val)
        """
        self.call_com(lambda: self._com.removeInState(val._com))


IRPModelElement.register_wrapper("ObjectNode", IRPObjectNode)
