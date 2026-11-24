"""Wraps ``com.telelogic.rhapsody.core.IRPStatechart``."""

from typing import TYPE_CHECKING, Optional, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPStatechartDiagram
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphEdge, IRPGraphNode


class IRPStatechart(IRPClass):
    """Wraps ``IRPStatechart``: represents a statechart behavior."""

    # IRPStatechart method parity checklist:
    # [ ] add_free_shape_by_type  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_image  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_new_edge_by_type  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_new_edge_for_element  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] add_new_node_by_type  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] add_new_node_for_element  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_text_box  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] open_diagram_view  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_new_accept_event_action  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_new_accept_time_event  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] close_diagram  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] create_graphics  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] delete_state  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] find_trigger  [x] impl  [x] docstring  [x] unit test  [ ] integration test   (inherited from rp_classifier)
    # [ ] get_all_triggers  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_elements_in_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_graphical_elements  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_inherits_from  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_is_main_behavior  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_is_overridden  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_its_class  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_picture  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_picture_as  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_picture_as_divided_metafiles  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_pictures_with_image_map  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_root_state  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_statechart_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] override_inheritance  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] populate_diagram  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_as_main_behavior  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_show_diagram_frame  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] unoverride_inheritance  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [inherited] irp_class / irp_classifier / irp_unit / irp_model_element methods (covered by rp_class / rp_classifier / rp_unit / rp_model_element checklists)
    # No deprecated IRPStatechart methods.

    def add_new_node_by_type(self, meta_type: str, x_position: int, y_position: int, width: int, height: int) -> "IRPGraphNode":
        """Adds a statechart element of the specified type to the statechart.

        The element is placed at the given position with the given dimensions.
        This method works only for elements that have purely graphical
        representations and are not actual model elements. To add an "ordinary"
        model element to a statechart, first add the element to your model and
        then add its graphical representation via ``add_new_node_for_element``.

        Args:
            meta_type: The type of node to create (e.g., 'State', 'Junction').
            x_position: The X coordinate for the node.
            y_position: The Y coordinate for the node.
            width: The width of the node.
            height: The height of the node.

        Returns:
            The wrapped node element created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewNodeByType(java.lang.String metaType, int xPosition, int yPosition, int nWidth, int nHeight)
        """
        return cast("IRPGraphNode", self.wrap(self.call_com(lambda: self._com.addNewNodeByType(meta_type, x_position, y_position, width, height))))

    def create_graphics(self) -> None:
        """Creates the graphical representation of the statechart's elements.

        When a statechart is created through the API, its graphical
        representation is not created by default; the first time you open it in
        Rhapsody you would be prompted whether to create the graphics. Calling
        this method creates the graphical representation directly.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::createGraphics()
        """
        self.call_com(lambda: self._com.createGraphics())

    def close_diagram(self) -> None:
        """Closes the statechart diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::closeDiagram()
        """
        self.call_com(lambda: self._com.closeDiagram())

    def delete_state(self, state: IRPModelElement) -> None:
        """Deletes a state from the statechart.

        Args:
            state: The state element to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::deleteState(com.telelogic.rhapsody.core.IRPState state)
        """
        self.call_com(lambda: self._com.deleteState(state._com))

    def add_free_shape_by_type(self, meta_type: str, x_position: int, y_position: int, width: int, height: int) -> "IRPGraphNode":
        """Adds a free shape to the statechart.

        Args:
            meta_type: The type of shape to add.
            x_position: The X coordinate for the shape.
            y_position: The Y coordinate for the shape.
            width: The width of the shape.
            height: The height of the shape.

        Returns:
            The wrapped graph node created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addFreeShapeByType(java.lang.String metaType, int xPosition, int yPosition, int nWidth, int nHeight)
        """
        return cast("IRPGraphNode", self.wrap(self.call_com(lambda: self._com.addFreeShapeByType(meta_type, x_position, y_position, width, height))))

    def add_image(self, x_position: int, y_position: int, width: int, height: int) -> "IRPGraphNode":
        """Adds an image to the statechart.

        Args:
            x_position: The X coordinate for the image.
            y_position: The Y coordinate for the image.
            width: The width of the image.
            height: The height of the image.

        Returns:
            The wrapped graph node created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addImage(int xPosition, int yPosition, int nWidth, int nHeight)
        """
        return cast("IRPGraphNode", self.wrap(self.call_com(lambda: self._com.addImage(x_position, y_position, width, height))))

    def add_new_edge_by_type(self, meta_type: str, source: IRPModelElement, target: IRPModelElement) -> "IRPGraphEdge":
        """Adds a transition edge of the specified type to the statechart.

        Args:
            meta_type: The type of edge to create (e.g., 'Transition').
            source: The source node for the edge.
            target: The target node for the edge.

        Returns:
            The wrapped graph edge created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewEdgeByType(
                java.lang.String metaType, IRPModelElement source, IRPModelElement target)
        """
        return cast("IRPGraphEdge", self.wrap(self.call_com(lambda: self._com.addNewEdgeByType(meta_type, source._com, target._com))))

    def add_new_edge_for_element(self, element: IRPModelElement, source: IRPModelElement, target: IRPModelElement) -> "IRPGraphEdge":
        """Adds a graphical edge for an existing model element to the statechart.

        Args:
            element: The existing model element to add an edge for.
            source: The source node for the edge.
            target: The target node for the edge.

        Returns:
            The wrapped graph edge created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewEdgeForElement(
                IRPModelElement element, IRPModelElement source, IRPModelElement target)
        """
        return cast("IRPGraphEdge", self.wrap(self.call_com(lambda: self._com.addNewEdgeForElement(element._com, source._com, target._com))))

    def add_new_node_for_element(self, element: IRPModelElement, x_position: int, y_position: int, width: int, height: int) -> "IRPGraphNode":
        """Adds a graphical node for an existing model element to the statechart.

        Args:
            element: The existing model element to add a node for.
            x_position: The X coordinate for the node.
            y_position: The Y coordinate for the node.
            width: The width of the node.
            height: The height of the node.

        Returns:
            The wrapped graph node created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewNodeForElement(com.telelogic.rhapsody.core.IRPModelElement element, int xPosition, int yPosition, int nWidth, int nHeight)
        """
        return cast("IRPGraphNode", self.wrap(self.call_com(lambda: self._com.addNewNodeForElement(element._com, x_position, y_position, width, height))))

    def add_text_box(self, x_position: int, y_position: int, width: int, height: int) -> "IRPGraphNode":
        """Adds a text box to the statechart.

        Args:
            x_position: The X coordinate for the text box.
            y_position: The Y coordinate for the text box.
            width: The width of the text box.
            height: The height of the text box.

        Returns:
            The wrapped graph node created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addTextBox(int xPosition, int yPosition, int nWidth, int nHeight)
        """
        return cast("IRPGraphNode", self.wrap(self.call_com(lambda: self._com.addTextBox(x_position, y_position, width, height))))

    def open_diagram_view(self) -> None:
        """Opens the statechart diagram view in the Rhapsody GUI.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::openDiagramView()
        """
        self.call_com(lambda: self._com.openDiagramView())

    def add_new_accept_event_action(self, name: str) -> Optional["IRPModelElement"]:
        """Adds a new accept event action to the statechart.

        Args:
            name: The name for the new accept event action.

        Returns:
            The wrapped accept event action created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewAcceptEventAction(java.lang.String name)
        """
        return self.wrap(self.call_com(lambda: self._com.addNewAcceptEventAction(name)))

    def add_new_accept_time_event(self, name: str) -> Optional["IRPModelElement"]:
        """Adds a new accept time event to the statechart.

        Args:
            name: The name for the new accept time event.

        Returns:
            The wrapped accept time event created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewAcceptTimeEvent(java.lang.String name)
        """
        return self.wrap(self.call_com(lambda: self._com.addNewAcceptTimeEvent(name)))

    def get_all_triggers(self) -> IRPCollection:
        """Returns all triggers defined in the statechart.

        Returns:
            An ``IRPCollection`` of triggers.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getAllTriggers()
        """
        return IRPCollection(self._get_method_or_property(self._com, "getAllTriggers", "allTriggers"))

    def get_elements_in_diagram(self) -> IRPCollection:
        """Returns all model elements displayed in the statechart diagram.

        Returns:
            An ``IRPCollection`` of model elements in the diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getElementsInDiagram()
        """
        return IRPCollection(self._get_method_or_property(self._com, "getElementsInDiagram", "elementsInDiagram"))

    def get_graphical_elements(self) -> IRPCollection:
        """Returns all graphical elements in the statechart.

        Returns:
            An ``IRPCollection`` of graphical elements.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getGraphicalElements()
        """
        return IRPCollection(self._get_method_or_property(self._com, "getGraphicalElements", "graphicalElements"))

    def get_inherits_from(self) -> "IRPStatechart":
        """Returns the statechart that this statechart inherits from.

        Returns:
            The wrapped inherited statechart, or None if not inherited.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getInheritsFrom()
        """
        return cast("IRPStatechart", self.wrap(self._get_method_or_property(self._com, "getInheritsFrom", "inheritsFrom")))

    def get_is_main_behavior(self) -> int:
        """Checks whether this statechart is the main behavior of its owning class.

        Returns:
            ``1`` if this is the main behavior, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getIsMainBehavior()
        """
        return int(self._get_method_or_property(self._com, "getIsMainBehavior", "isMainBehavior"))

    def get_is_overridden(self) -> int:
        """Checks whether this statechart overrides an inherited statechart.

        Returns:
            ``1`` if this statechart is overridden, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getIsOverridden()
        """
        return int(self._get_method_or_property(self._com, "getIsOverridden", "isOverridden"))

    def get_its_class(self) -> "IRPClass":
        """Returns the class that owns this statechart.

        Returns:
            The wrapped owning class.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getItsClass()
        """
        return cast("IRPClass", self.wrap(self._get_method_or_property(self._com, "getItsClass", "itsClass")))

    def get_picture(self) -> object:
        """Returns the picture representation of the statechart.

        Returns:
            The picture representation.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getPicture()
        """
        return self._get_method_or_property(self._com, "getPicture", "picture")

    def get_picture_as(self, format: str) -> object:
        """Returns the picture representation in the specified format.

        Args:
            format: The format for the picture (e.g., 'BMP', 'PNG').

        Returns:
            The picture representation in the specified format.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getPictureAs(java.lang.String format)
        """
        return self.call_com(lambda: self._com.getPictureAs(format))

    def get_picture_as_divided_metafiles(self) -> IRPCollection:
        """Returns the picture as divided metafiles.

        Returns:
            An ``IRPCollection`` of divided metafiles.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getPictureAsDividedMetafiles()
        """
        return IRPCollection(self.call_com(lambda: self._com.getPictureAsDividedMetafiles()))

    def get_pictures_with_image_map(self, first_file_name: str, diagram_map: "IRPCollection") -> "IRPCollection":
        """Saves the statechart as EMF file(s) and populates the given collection with image-map info.

        Same semantics as ``IRPDiagram.getPicturesWithImageMap`` -- saves the statechart
        diagram as EMF file(s) and populates ``diagram_map`` with ``IRPImageMap`` objects.

        Args:
            first_file_name: The base name for the created EMF file(s).
            diagram_map: An empty ``IRPCollection`` that will be populated with ``IRPImageMap`` objects.

        Returns:
            An ``IRPCollection`` containing the names of the files that were created.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getPicturesWithImageMap(
                java.lang.String firstFileName, com.telelogic.rhapsody.core.IRPCollection diagrammap)
        """
        return IRPCollection(self.call_com(lambda: self._com.getPicturesWithImageMap(first_file_name, diagram_map._com)))

    def get_root_state(self) -> Optional["IRPModelElement"]:
        """Returns the root state of the statechart.

        Returns:
            The wrapped root state.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getRootState()
        """
        return self.wrap(self._get_method_or_property(self._com, "getRootState", "rootState"))

    def get_statechart_diagram(self) -> "IRPStatechartDiagram":
        """Returns the statechart diagram associated with this statechart.

        Returns:
            The wrapped statechart diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getStatechartDiagram()
        """
        return cast("IRPStatechartDiagram", self.wrap(self._get_method_or_property(self._com, "getStatechartDiagram", "statechartDiagram")))

    def override_inheritance(self) -> None:
        """Overrides the inherited statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::overrideInheritance()
        """
        self.call_com(lambda: self._com.overrideInheritance())

    def populate_diagram(self) -> None:
        """Populates the diagram with elements.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::populateDiagram()
        """
        self.call_com(lambda: self._com.populateDiagram())

    def set_as_main_behavior(self, is_main: int) -> None:
        """Sets whether this statechart is the main behavior.

        Args:
            is_main: ``1`` to set as main behavior, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::setAsMainBehavior(int isMain)
        """
        self.call_com(lambda: self._com.setAsMainBehavior(is_main))

    def set_show_diagram_frame(self, show_frame: int) -> None:
        """Sets whether to show the diagram frame.

        Args:
            show_frame: ``1`` to show the frame, ``0`` to hide it.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::setShowDiagramFrame(int showFrame)
        """
        self.call_com(lambda: self._com.setShowDiagramFrame(show_frame))

    def unoverride_inheritance(self) -> None:
        """Removes the override of the inherited statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::unoverrideInheritance()
        """
        self.call_com(lambda: self._com.unoverrideInheritance())


IRPModelElement.register_wrapper("Statechart", IRPStatechart)
