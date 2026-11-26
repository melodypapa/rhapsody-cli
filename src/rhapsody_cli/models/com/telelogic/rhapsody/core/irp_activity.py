"""Activity model-element wrappers (auto-generated stubs)."""

from typing import Optional, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState


class IRPFlowItem(IRPClassifier):
    """Wraps ``IRPFlowItem``: represents item flows in Rhapsody models."""

    # IRPFlowItem method parity checklist:
    # [x] add_represented               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_represented               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove_represented            [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_classifier methods (covered by rp_classifier checklist)
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_unit methods (covered by rp_unit checklist)
    # No deprecated IRPFlowItem methods.

    def add_represented(self, p_element: "IRPModelElement") -> None:
        """Adds an element to the collection of information elements that are represented by the item flow.

        Args:
            p_element: The element to add to the collection.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowItem::addRepresented(com.telelogic.rhapsody.core.IRPModelElement pElement)
        """
        self.call_com(lambda: self._com.addRepresented(p_element._com))

    def get_represented(self) -> "IRPCollection":
        """Returns a collection of all the information elements that are represented by the item flow.

        Returns:
            IRPCollection: All the information elements that are represented by the item flow.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowItem::getRepresented()
        """
        return IRPCollection(self.call_com(lambda: self._com.getRepresented()))

    def remove_represented(self, p_element: "IRPModelElement") -> None:
        """Removes the specified element from the collection of information elements that are represented by the item flow.

        Args:
            p_element: The element that should be removed from the collection.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowItem::removeRepresented(com.telelogic.rhapsody.core.IRPModelElement pElement)
        """
        self.call_com(lambda: self._com.removeRepresented(p_element._com))


class IRPObjectNode(IRPState):
    """Wraps ``IRPObjectNode``: represents Object Node elements in activity diagrams."""

    # IRPObjectNode method parity checklist:
    # [x] add_in_state                   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_in_state                   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_in_state_list               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_represents                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove_in_state                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_in_state                   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_represents                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # [inherited] irp_state methods (covered by rp_state checklist)
    # [inherited] irp_state_vertex methods (covered by rp_state_vertex checklist)
    # [deprecated] get_in_state  - skipped (deprecated in Rhapsody Java API)
    # [deprecated] set_in_state  - skipped (deprecated in Rhapsody Java API)
    # No non-deprecated IRPObjectNode methods.

    def add_in_state(self, val: "IRPModelElement") -> None:
        """Adds the specified state to the list of "In State" states for the object node.

        Args:
            val: The state to add to the list of "In State" states.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::addInState(com.telelogic.rhapsody.core.IRPModelElement val)
        """
        self.call_com(lambda: self._com.addInState(val._com))

    def get_in_state(self) -> str:
        """Returns the "In State" of the object node. Deprecated: use getInStateList() instead.

        Returns:
            str: The "In State" of the object node.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::getInState()
        """
        return str(self._get_method_or_property(self._com, "getInState", "inState"))

    def get_in_state_list(self) -> "IRPCollection":
        """Returns a collection of the "In State" states for the object node.

        Returns:
            IRPCollection: The "In State" states defined for the object node.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::getInStateList()
        """
        return IRPCollection(self.call_com(lambda: self._com.getInStateList()))

    def get_represents(self) -> "Optional[IRPModelElement]":
        """Returns the class/type that this object node represents.

        Returns:
            The class/type that this object node represents, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::getRepresents()
        """
        return self.wrap(self.call_com(lambda: self._com.getRepresents()))

    def remove_in_state(self, val: "IRPModelElement") -> None:
        """Removes the specified state from the list of "In State" states for the object node.

        Args:
            val: The state to remove from the list.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::removeInState(com.telelogic.rhapsody.core.IRPModelElement val)
        """
        self.call_com(lambda: self._com.removeInState(val._com))

    def set_in_state(self, in_state: str) -> None:
        """Sets the "In State" of the object node. Deprecated: use addInState instead.

        Args:
            in_state: The "In State" value to set.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::setInState(java.lang.String inState)
        """
        self._set_method_or_property(self._com, "setInState", "inState", in_state)

    def set_represents(self, represents: "IRPModelElement") -> None:
        """Specifies the class/type that this object node should represent.

        Args:
            represents: The class/type that this object node should represent.

        Reference:
            com.telelogic.rhapsody.core.IRPObjectNode::setRepresents(com.telelogic.rhapsody.core.IRPModelElement represents)
        """
        self._set_method_or_property(self._com, "setRepresents", "represents", represents._com)


class IRPSwimlane(IRPModelElement):
    """Wraps ``IRPSwimlane``: represents swimlanes in an activity diagram."""

    # IRPSwimlane method parity checklist:
    # [x] add_swimlane                  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_contents                  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_represents                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_swimlanes                 [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_represents                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_model_element methods (covered by rp_model_element checklist)
    # No deprecated IRPSwimlane methods.

    def add_swimlane(self, name: str) -> "IRPSwimlane":
        """For internal use only.

        Args:
            name: The name to use for the new swimlane.

        Returns:
            IRPSwimlane: The swimlane that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::addSwimlane(java.lang.String name)
        """
        return cast("IRPSwimlane", self.wrap(self.call_com(lambda: self._com.addSwimlane(name))))

    def get_contents(self) -> "IRPCollection":
        """Returns a collection of the elements contained in the swimlane.

        Returns:
            IRPCollection: The elements contained in the swimlane.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::getContents()
        """
        return IRPCollection(self.call_com(lambda: self._com.getContents()))

    def get_represents(self) -> "Optional[IRPModelElement]":
        """Returns the model element that the swimlane represents.

        Returns:
            The model element that the swimlane represents, or None if not set.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::getRepresents()
        """
        return self.wrap(self.call_com(lambda: self._com.getRepresents()))

    def get_swimlanes(self) -> "IRPCollection":
        """Returns a collection of the swimlanes that are nested under this swimlane.

        Returns:
            IRPCollection: The swimlanes nested under this swimlane.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::getSwimlanes()
        """
        return IRPCollection(self.call_com(lambda: self._com.getSwimlanes()))

    def set_represents(self, represents: "IRPModelElement") -> None:
        """Specifies the model element that the swimlane is to represent.

        Args:
            represents: The model element that the swimlane is to represent.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPSwimlane::setRepresents(com.telelogic.rhapsody.core.IRPModelElement represents)
        """
        self._set_method_or_property(self._com, "setRepresents", "represents", represents._com)


# Register wrappers for meta classes
IRPModelElement.register_wrapper("FlowItem", IRPFlowItem)
IRPModelElement.register_wrapper("ObjectNode", IRPObjectNode)
IRPModelElement.register_wrapper("Swimlane", IRPSwimlane)
