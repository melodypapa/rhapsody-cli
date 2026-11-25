"""Wraps ``com.telelogic.rhapsody.core.IRPStatechart``."""

from __future__ import annotations

from typing import TYPE_CHECKING, Optional, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_ide import IRPAXViewCtrl
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actions import IRPAcceptEventAction, IRPAcceptTimeEvent
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPStatechartDiagram
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphEdge, IRPGraphElement, IRPGraphNode
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item import IRPInterfaceItem
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState


class IRPStatechart(IRPClass):
    """Represents the statechart elements underlying a statechart diagram.

    The diagram itself is represented by :class:`IRPStatechartDiagram`; a
    statechart object is created through :meth:`IRPClass.add_statechart`.
    """

    # JavaDoc-owned methods are implemented below. The five property-shaped
    # pywin32 members are exposed as Python properties, not duplicate get_* APIs.

    def add_free_shape_by_type(self, meta_type: str, x_points: IRPCollection, y_points: IRPCollection) -> IRPGraphElement:
        """Adds a free shape using collections of its x and y coordinates.

        Args:
            meta_type: Shape type: ``Polyline``, ``Polygon``, ``Rectangle``,
                ``Polycurve``, ``Closed Curve``, or ``Ellipse``.
            x_points: Collection of integer x coordinates.
            y_points: Collection of integer y coordinates.

        Returns:
            The new graphical shape.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addFreeShapeByType(
            java.lang.String metaType, IRPCollection xPoints, IRPCollection yPoints)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphElement

        raw_shape = self.call_com(lambda: self._com.AddFreeShapeByType(meta_type, x_points._com, y_points._com))
        return IRPGraphElement(raw_shape)

    def add_image(self, filename: str, x_position: int, y_position: int, width: int, height: int) -> IRPGraphElement:
        """Adds an image from a file at the specified diagram position and size.

        Args:
            filename: Full path to the image file.
            x_position: X coordinate of the image's top-left corner, in pixels.
            y_position: Y coordinate of the image's top-left corner, in pixels.
            width: Image width, in pixels.
            height: Image height, in pixels.

        Returns:
            The new image graphical element.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addImage(
            java.lang.String filename, int xPosition, int yPosition, int nWidth, int nHeight)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphElement

        raw_image = self.call_com(lambda: self._com.AddImage(filename, x_position, y_position, width, height))
        return IRPGraphElement(raw_image)

    def add_new_accept_event_action(self, name: str, parent: IRPState) -> IRPAcceptEventAction:
        """Adds an Accept Event Action element to the statechart.

        The parent is the diagram element to contain the action; use the root
        state for an action on the main diagram canvas. JavaDoc declares this
        API, but the registered pywin32 interface has no corresponding member,
        so the wrapper raises before attempting COM dispatch.

        Args:
            name: Name for the Accept Event Action element.
            parent: Parent state or diagram element.

        Returns:
            The created Accept Event Action element.

        Raises:
            NotImplementedError: The registered pywin32 interface does not
                expose ``addNewAcceptEventAction``.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewAcceptEventAction(
            java.lang.String name, IRPState parent)
        """
        raise NotImplementedError("addNewAcceptEventAction is not exposed by the registered pywin32 interface.")

    def add_new_accept_time_event(self, name: str, parent: IRPState) -> IRPAcceptTimeEvent:
        """Adds an Accept Time Event element to the statechart.

        The parent is the diagram element to contain the event; use the root
        state for an event on the main diagram canvas. JavaDoc declares this
        API, but the registered pywin32 interface has no corresponding member,
        so the wrapper raises before attempting COM dispatch.

        Args:
            name: Name for the Accept Time Event element.
            parent: Parent state or diagram element.

        Returns:
            The created Accept Time Event element.

        Raises:
            NotImplementedError: The registered pywin32 interface does not
                expose ``addNewAcceptTimeEvent``.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewAcceptTimeEvent(
            java.lang.String name, IRPState parent)
        """
        raise NotImplementedError("addNewAcceptTimeEvent is not exposed by the registered pywin32 interface.")

    def add_new_edge_by_type(
        self,
        meta_type: str,
        source: IRPGraphElement,
        x_source_position: int,
        y_source_position: int,
        target: IRPGraphElement,
        x_target_position: int,
        y_target_position: int,
    ) -> IRPGraphEdge:
        """Adds a graphical-only connector between two diagram elements.

        Args:
            meta_type: Connector type: ``anchor``, ``compRealization``,
                ``Containment Arrow``, or ``communication path``.
            source: Graphical source element.
            x_source_position: Source point's horizontal position in pixels.
            y_source_position: Source point's vertical position in pixels.
            target: Graphical target element.
            x_target_position: Target point's horizontal position in pixels.
            y_target_position: Target point's vertical position in pixels.

        Returns:
            The connector graphical element added to the statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewEdgeByType(
            java.lang.String metaType, IRPGraphElement src, int xSrcPosition,
            int ySrcPosition, IRPGraphElement trg, int xTrgPosition, int yTrgPosition)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphEdge

        raw_edge = self.call_com(
            lambda: self._com.AddNewEdgeByType(
                meta_type,
                source._com,
                x_source_position,
                y_source_position,
                target._com,
                x_target_position,
                y_target_position,
            )
        )
        return IRPGraphEdge(raw_edge)

    def add_new_edge_for_element(
        self,
        element: IRPModelElement,
        source: IRPGraphNode,
        x_source_position: int,
        y_source_position: int,
        target: IRPGraphNode,
        x_target_position: int,
        y_target_position: int,
    ) -> IRPGraphEdge:
        """Adds a connector representation for an existing model element.

        Args:
            element: Model element represented by the connector.
            source: Graphical source node.
            x_source_position: Source point's horizontal position in pixels.
            y_source_position: Source point's vertical position in pixels.
            target: Graphical target node.
            x_target_position: Target point's horizontal position in pixels.
            y_target_position: Target point's vertical position in pixels.

        Returns:
            The connector graphical element added to the statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewEdgeForElement(
            IRPModelElement element, IRPGraphNode src, int xSrcPosition,
            int ySrcPosition, IRPGraphNode trg, int xTrgPosition, int yTrgPosition)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphEdge

        raw_edge = self.call_com(
            lambda: self._com.AddNewEdgeForElement(
                element._com,
                source._com,
                x_source_position,
                y_source_position,
                target._com,
                x_target_position,
                y_target_position,
            )
        )
        return IRPGraphEdge(raw_edge)

    def add_new_node_by_type(self, meta_type: str, x_position: int, y_position: int, width: int, height: int) -> IRPGraphNode:
        """Adds a graphical-only statechart node of the specified type.

        Args:
            meta_type: Node type, such as ``OrState`` or ``Note``.
            x_position: Left-edge position in pixels relative to the diagram.
            y_position: Top-edge position in pixels relative to the diagram.
            width: Node width in pixels.
            height: Node height in pixels.

        Returns:
            The graphical node added to the statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewNodeByType(
            java.lang.String metaType, int xPosition, int yPosition,
            int nWidth, int nHeight)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphNode

        raw_node = self.call_com(lambda: self._com.AddNewNodeByType(meta_type, x_position, y_position, width, height))
        return IRPGraphNode(raw_node)

    def add_new_node_for_element(self, element: IRPModelElement, x_position: int, y_position: int, width: int, height: int) -> IRPGraphNode:
        """Adds a graphical representation of an existing model element.

        Args:
            element: Model element to represent in the statechart.
            x_position: Left-edge position in pixels relative to the diagram.
            y_position: Top-edge position in pixels relative to the diagram.
            width: Graphical node width in pixels.
            height: Graphical node height in pixels.

        Returns:
            The graphical node added to the statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addNewNodeForElement(
            IRPModelElement element, int xPosition, int yPosition,
            int nWidth, int nHeight)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphNode

        raw_node = self.call_com(lambda: self._com.AddNewNodeForElement(element._com, x_position, y_position, width, height))
        return IRPGraphNode(raw_node)

    def add_text_box(self, text: str, x_position: int, y_position: int, width: int, height: int) -> IRPGraphElement:
        """Adds a text box with the specified content and geometry.

        Args:
            text: Text displayed in the box.
            x_position: Top-left x coordinate in pixels.
            y_position: Top-left y coordinate in pixels.
            width: Text-box width in pixels.
            height: Text-box height in pixels.

        Returns:
            The new text-box graphical element.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::addTextBox(
            java.lang.String text, int xPosition, int yPosition,
            int nWidth, int nHeight)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphElement

        raw_text_box = self.call_com(lambda: self._com.AddTextBox(text, x_position, y_position, width, height))
        return IRPGraphElement(raw_text_box)

    def open_diagram_view(self) -> IRPAXViewCtrl:
        """Opens the statechart view in the Rhapsody-Eclipse integration.

        Returns:
            The ActiveX view controller for the opened diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::openDiagramView()
        """
        return IRPAXViewCtrl(self.call_com(lambda: self._com.OpenDiagramView()))

    def close_diagram(self) -> None:
        """Closes the statechart diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::closeDiagram()
        """
        self.call_com(lambda: self._com.closeDiagram())

    def create_graphics(self) -> None:
        """Creates the graphical representation of statechart elements.

        When a statechart is created through the API, its graphical
        representation is not created by default. This method creates it
        without waiting for Rhapsody to prompt when the diagram is first opened.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::createGraphics()
        """
        self.call_com(lambda: self._com.createGraphics())

    def delete_state(self, state: IRPState) -> None:
        """Deletes the specified state from this statechart.

        Args:
            state: State element to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::deleteState(IRPState state)
        """
        self.call_com(lambda: self._com.deleteState(state._com))

    def find_trigger(self, item: IRPInterfaceItem) -> int:  # type: ignore[override]
        """Checks whether an interface item is a trigger of a statechart transition.

        Args:
            item: Interface item to check.

        Returns:
            ``1`` if the item serves as a transition trigger, otherwise ``0``.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::findTrigger(IRPInterfaceItem Item)
        """
        return int(self.call_com(lambda: self._com.findTrigger(item._com)))

    def get_all_triggers(self) -> IRPCollection:
        """Returns a collection of all triggers in the statechart.

        Returns:
            All triggers in the statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getAllTriggers()
        """
        return IRPCollection(self.call_com(lambda: self._com.getAllTriggers()))

    def get_elements_in_diagram(self) -> IRPCollection:
        """Returns all model elements displayed in the statechart diagram.

        Returns:
            All elements in the statechart diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getElementsInDiagram()
        """
        return IRPCollection(self.call_com(lambda: self._com.getElementsInDiagram()))

    @property
    def graphical_elements(self) -> IRPCollection:
        """Returns the graphical elements represented in this statechart.

        Returns:
            A collection of ``IRPGraphElement`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getGraphicalElements()
        """
        return IRPCollection(self.get_com_property(self._com, "graphicalElements"))

    def get_inherits_from(self) -> IRPStatechart | None:
        """Returns the statechart belonging to the base class.

        Returns:
            The base-class statechart, if available.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getInheritsFrom()
        """
        return cast(Optional[IRPStatechart], self.wrap(self.call_com(lambda: self._com.getInheritsFrom())))

    @property
    def is_main_behavior(self) -> int:
        """Checks whether this is the class's main behavior.

        Returns:
            ``1`` if this is the main behavior, otherwise ``0``.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getIsMainBehavior()
        """
        return int(self.get_com_property(self._com, "isMainBehavior"))

    @property
    def is_overridden(self) -> int:
        """Checks whether this statechart's inheritance relationship was overridden.

        Returns:
            ``1`` if overridden, otherwise ``0``.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getIsOverridden()
        """
        return int(self.get_com_property(self._com, "isOverridden"))

    @property
    def its_class(self) -> IRPClassifier:
        """Returns the classifier associated with this statechart.

        Returns:
            The class or classifier that owns the statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getItsClass()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier

        return cast(IRPClassifier, self.wrap(self.get_com_property(self._com, "itsClass")))

    def get_picture(self, filename: str) -> None:
        """Saves the statechart as an EMF file at the specified full path.

        Args:
            filename: Full path and filename for the EMF output.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getPicture(java.lang.String filename)
        """
        self.call_com(lambda: self._com.getPicture(filename))

    def get_picture_as(self, first_file_name: str, image_format: str, get_image_maps: int, diagram_map: IRPCollection) -> IRPCollection:
        """Saves the statechart in a graphic format and returns generated filenames.

        Args:
            first_file_name: Name/path for the first output file.
            image_format: Output format: EMF, BMP, JPEG, JPG, or TIFF.
            get_image_maps: ``1`` to request image-map information, otherwise ``0``.
            diagram_map: Collection used for the returned ``IRPImageMap`` objects.

        Returns:
            Collection containing the names of files created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getPictureAs(
            java.lang.String firstFileName, java.lang.String imageFormat,
            int getImageMaps, IRPCollection diagrammap)
        """
        filenames, returned_map = self.call_com(lambda: self._com.getPictureAs(first_file_name, image_format, get_image_maps, diagram_map._com))
        diagram_map._com = returned_map
        return IRPCollection(filenames)

    def get_picture_as_divided_metafiles(self, first_file_name: str) -> IRPCollection:
        """Saves the statechart as one or more EMF files.

        Args:
            first_file_name: Name/path to use for the first output file.

        Returns:
            Collection containing the names of files created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getPictureAsDividedMetafiles(
            java.lang.String firstFileName)
        """
        return IRPCollection(self.call_com(lambda: self._com.getPictureAsDividedMetafiles(first_file_name)))

    def get_pictures_with_image_map(self, first_file_name: str, diagram_map: IRPCollection) -> IRPCollection:
        """Saves the statechart as EMF files and returns image-map information.

        Args:
            first_file_name: Name/path for the first output file.
            diagram_map: Collection to receive ``IRPImageMap`` objects.

        Returns:
            Collection containing the names of files created.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getPicturesWithImageMap(
            java.lang.String firstFileName, IRPCollection diagrammap)
        """
        filenames, returned_map = self.call_com(lambda: self._com.getPicturesWithImageMap(first_file_name, diagram_map._com))
        diagram_map._com = returned_map
        return IRPCollection(filenames)

    @property
    def root_state(self) -> IRPState | None:
        """Returns the root state used to contain top-level statechart elements.

        Returns:
            The root state of the statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getRootState()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState

        return cast(Optional[IRPState], self.wrap(self.get_com_property(self._com, "rootState")))

    def get_statechart_diagram(self) -> IRPStatechartDiagram:
        """Returns the diagram object associated with the statechart.

        Returns:
            The statechart diagram associated with this statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::getStatechartDiagram()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagram_types import IRPStatechartDiagram

        return cast(IRPStatechartDiagram, self.wrap(self.call_com(lambda: self._com.getStatechartDiagram())))

    def override_inheritance(self) -> None:
        """Breaks the inheritance relationship with the base statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::overrideInheritance()
        """
        self.call_com(lambda: self._com.overrideInheritance())

    def populate_diagram(self, elements_to_populate: IRPCollection, relation_types: IRPCollection, create_content: str) -> None:
        """Populates the statechart with specified elements and relation types.

        Args:
            elements_to_populate: Collection of model elements to add as nodes.
            relation_types: Collection of relation types to draw, such as
                ``AllRelations``, ``Composition``, ``Association``, ``Link``,
                ``Dependency``, ``Inheritance``, ``Anchor``, or ``InformationFlow``.
            create_content: Additional related content: ``among``, ``from``,
                ``to``, or ``fromto``.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::populateDiagram(
            IRPCollection elementsToPopulate, IRPCollection relationsTypes,
            java.lang.String createContent)
        """
        self.call_com(lambda: self._com.populateDiagram(elements_to_populate._com, relation_types._com, create_content))

    def set_as_main_behavior(self) -> None:
        """Specifies that this statechart is the class's main behavior.

        Rhapsody may define multiple statecharts and activities, with one
        behavior defined as the main behavior for execution.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::setAsMainBehavior()
        """
        self.call_com(lambda: self._com.setAsMainBehavior())

    def set_show_diagram_frame(self, show_frame: int) -> None:
        """Shows or hides the statechart diagram frame.

        Args:
            show_frame: ``1`` to show the frame, ``0`` to hide it.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::setShowDiagramFrame(int bShow)
        """
        self.call_com(lambda: self._com.setShowDiagramFrame(show_frame))

    def unoverride_inheritance(self) -> None:
        """Restores the inheritance relationship with the base statechart.

        Reference:
            com.telelogic.rhapsody.core.IRPStatechart::unoverrideInheritance()
        """
        self.call_com(lambda: self._com.unoverrideInheritance())


IRPModelElement.register_wrapper("Statechart", IRPStatechart)
