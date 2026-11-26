"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPFlowchart``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statechart import IRPStatechart
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions import IRPAcceptEventAction, IRPAcceptTimeEvent, IRPCallOperation
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_activity import IRPObjectNode, IRPSwimlane
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPActivityDiagram
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPPin
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation


class IRPFlowchart(IRPStatechart):
    """Wraps ``IRPFlowchart``: represents activities in Rhapsody models.

    JavaDoc accessors exposed by pywin32 as properties are surfaced as
    ``@property`` members; the remaining JavaDoc methods use ``call_com``.
    """

    # IRPFlowchart method parity checklist:
    # [x] is_analysis_only               [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] its_owner                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] swimlanes                      [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_accept_event_action        [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_accept_time_event          [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_activity_parameter         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_call_behavior              [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_call_operation             [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_object_node                [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_reference_activity         [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_swimlane                   [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_flowchart_diagram          [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_class methods (covered by irp_class checklist)
    # [inherited] irp_classifier methods (covered by irp_classifier checklist)
    # [inherited] irp_model_element methods (covered by irp_model_element checklist)
    # [inherited] irp_statechart methods (covered by irp_statechart checklist)
    # [inherited] irp_unit methods (covered by irp_unit checklist)

    @property
    def is_analysis_only(self) -> int:
        """Checks whether the activity is analysis-only.

        Returns:
            1 if the activity is analysis-only, 0 otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::getIsAnalysisOnly()
        """
        return int(self.get_com_property(self._com, "isAnalysisOnly"))

    @is_analysis_only.setter
    def is_analysis_only(self, is_analysis_only: int) -> None:
        """Specifies whether the activity is analysis-only.

        Args:
            is_analysis_only: 1 to make the activity analysis-only, 0 otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::setIsAnalysisOnly(int isAnalysisOnly)
        """
        self.set_com_property(self._com, "isAnalysisOnly", is_analysis_only)

    @property
    def its_owner(self) -> IRPOperation | None:
        """Returns the operation that owns the activity.

        Deprecated in the Java API: use ``owner`` instead.

        Returns:
            The owning operation, or None if the activity has no owner.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::getItsOwner()
        """
        return self.wrap(self.get_com_property(self._com, "itsOwner"))

    @its_owner.setter
    def its_owner(self, its_owner: IRPOperation) -> None:
        """Sets the operation that owns the activity.

        Deprecated in the Java API: use ``owner`` instead.

        Args:
            its_owner: The operation that should own the activity.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::setItsOwner(com.telelogic.rhapsody.core.IRPOperation itsOwner)
        """
        self.set_com_property(self._com, "itsOwner", its_owner._com)

    @property
    def swimlanes(self) -> IRPCollection:
        """Returns all swimlanes in the activity.

        Returns:
            A collection of ``IRPSwimlane`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::getSwimlanes()
        """
        return IRPCollection(self.get_com_property(self._com, "swimlanes"))

    def add_accept_event_action(self, name: str, parent: IRPState) -> IRPAcceptEventAction:
        """Adds a new Accept Event Action element to the activity.

        Args:
            name: The name of the new element.
            parent: The diagram element to which the new element should be
                added; for an Action Block use the block, otherwise use the
                root state of the diagram.

        Returns:
            The Accept Event Action that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::addAcceptEventAction(java.lang.String name, com.telelogic.rhapsody.core.IRPState parent)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions import IRPAcceptEventAction

        return cast(IRPAcceptEventAction, self.wrap(self.call_com(lambda: self._com.addAcceptEventAction(name, parent._com))))

    def add_accept_time_event(self, name: str, parent: IRPState) -> IRPAcceptTimeEvent:
        """Adds a new Accept Time Event element to the activity.

        Args:
            name: The name of the new element.
            parent: The diagram element to which the new element should be
                added; for an Action Block use the block, otherwise use the
                root state of the diagram.

        Returns:
            The Accept Time Event that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::addAcceptTimeEvent(java.lang.String name, com.telelogic.rhapsody.core.IRPState parent)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions import IRPAcceptTimeEvent

        return cast(IRPAcceptTimeEvent, self.wrap(self.call_com(lambda: self._com.addAcceptTimeEvent(name, parent._com))))

    def add_activity_parameter(self, name: str) -> IRPPin:
        """Adds an activity parameter to the frame of the activity.

        Args:
            name: The name of the new activity parameter.

        Returns:
            The activity parameter that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::addActivityParameter(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPPin

        return cast(IRPPin, self.wrap(self.call_com(lambda: self._com.addActivityParameter(name))))

    def add_call_behavior(self, referenced: IRPModelElement) -> IRPState:
        """Adds a new Call Behavior element to the activity.

        Args:
            referenced: The activity that the new element should invoke.

        Returns:
            The Call Behavior element that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::addCallBehavior(com.telelogic.rhapsody.core.IRPModelElement referenced)
        """
        return cast(IRPState, self.wrap(self.call_com(lambda: self._com.addCallBehavior(referenced._com))))

    def add_call_operation(self, name: str, parent: IRPState) -> IRPCallOperation:
        """Adds a new Call Operation element to the activity.

        Args:
            name: The name of the new element.
            parent: The diagram element to which the new element should be
                added; for an Action Block use the block, otherwise use the
                root state of the diagram.

        Returns:
            The Call Operation element that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::addCallOperation(java.lang.String name, com.telelogic.rhapsody.core.IRPState parent)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions import IRPCallOperation

        return cast(IRPCallOperation, self.wrap(self.call_com(lambda: self._com.addCallOperation(name, parent._com))))

    def add_object_node(self, name: str, parent: IRPState) -> IRPObjectNode:
        """Adds a new Object Node element to the activity.

        Args:
            name: The name of the new element.
            parent: The diagram element to which the new element should be
                added; for an Action Block use the block, otherwise use the
                root state of the diagram.

        Returns:
            The Object Node that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::addObjectNode(java.lang.String name, com.telelogic.rhapsody.core.IRPState parent)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_activity import IRPObjectNode

        return cast(IRPObjectNode, self.wrap(self.call_com(lambda: self._com.addObjectNode(name, parent._com))))

    def add_reference_activity(self, referenced: IRPModelElement) -> IRPState:
        """Adds a referenced activity; performs the same action as ``add_call_behavior``.

        Args:
            referenced: The activity that the new element should invoke.

        Returns:
            The Call Behavior element that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::addReferenceActivity(com.telelogic.rhapsody.core.IRPModelElement referenced)
        """
        return cast(IRPState, self.wrap(self.call_com(lambda: self._com.addReferenceActivity(referenced._com))))

    def add_swimlane(self, name: str) -> IRPSwimlane:
        """Adds a new swimlane to the activity.

        Args:
            name: The name of the new swimlane.

        Returns:
            The swimlane that was created.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::addSwimlane(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_activity import IRPSwimlane

        return cast(IRPSwimlane, self.wrap(self.call_com(lambda: self._com.addSwimlane(name))))

    def get_flowchart_diagram(self) -> IRPActivityDiagram:
        """Returns the activity diagram associated with the activity.

        Returns:
            The associated ``IRPActivityDiagram``.

        Reference:
            com.telelogic.rhapsody.core.IRPFlowchart::getFlowchartDiagram()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPActivityDiagram

        return cast(IRPActivityDiagram, self.wrap(self.call_com(lambda: self._com.getFlowchartDiagram())))


IRPModelElement.register_wrapper("Flowchart", IRPFlowchart)
