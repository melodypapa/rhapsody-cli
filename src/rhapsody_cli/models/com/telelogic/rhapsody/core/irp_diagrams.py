"""Diagram-family wrappers: mirrors IRPDiagram from com.telelogic.rhapsody.core."""

from typing import TYPE_CHECKING, Optional, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphEdge, IRPGraphElement, IRPGraphNode


class IRPDiagram(IRPUnit):
    """Wraps ``IRPDiagram``: represents a diagram in the model."""

    # IRPDiagram method parity checklist:
    # [x] add_free_shape_by_type  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_image  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_new_edge_by_type  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_new_edge_for_element  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_new_node_by_type  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_new_node_for_element  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_text_box  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] create_diagram_view  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_custom_views  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_diagram_view_of  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_diagram_views  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_diagram_view  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] open_diagram_view  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] rearrange_ports  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_custom_views  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] update_view_on_server  [x] stub  [x] docstring  [x] unit test  [ ] integration test
    # [x] close_diagram  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] complete_relations  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_corresponding_graphic_elements  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_elements_in_diagram  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] graphical_elements  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_last_visualization_modified_time  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] get_picture  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_picture_as  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_picture_as_divided_metafiles  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_picture_ex  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_pictures_with_image_map  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_open  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] is_show_diagram_frame  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] open_diagram  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] populate_diagram  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] remove_graph_elements  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] set_show_diagram_frame  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [inherited] irp_unit / irp_model_element methods (covered by rp_unit / rp_model_element checklists)
    # No deprecated IRPDiagram methods.

    def close_diagram(self) -> None:
        """Closes the diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::closeDiagram()
        """
        self.call_com(lambda: self._com.closeDiagram())

    def add_text_box(self, text: str, x_position: int, y_position: int, width: int, height: int) -> "IRPGraphElement":
        """Adds a text box using the specified text, starting point, width, and height.

        Args:
            text: The text content for the box.
            x_position: The X coordinate for the text box.
            y_position: The Y coordinate for the text box.
            width: The width of the text box.
            height: The height of the text box.

        Returns:
            The wrapped text box element created.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::AddTextBox(java.lang.String text, int xPosition, int yPosition, int nWidth, int nHeight)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphElement

        return IRPGraphElement(self.call_com(lambda: self._com.AddTextBox(text, x_position, y_position, width, height)))

    def get_custom_views(self) -> IRPCollection:
        """Gets the custom views that were applied to this diagram view.

        Returns:
            An ``IRPCollection`` of custom view elements.

        Raises:
            NotImplementedError: ``getCustomViews`` is absent from the
                registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getCustomViews()
        """
        raise NotImplementedError("getCustomViews is not exposed by the registered pywin32 interface.")

    def get_corresponding_graphic_elements(self, model_element: IRPModelElement) -> IRPCollection:
        """Returns the graphical elements that represent the specified model element.

        In cases where the same model element appears multiple times in a single
        diagram, the collection returned will contain more than one graphical element.

        Args:
            model_element: The model element to find graphic representations for.

        Returns:
            An ``IRPCollection`` of graphic elements.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getCorrespondingGraphicElements(com.telelogic.rhapsody.core.IRPModelElement modelElement)
        """
        return IRPCollection(self.call_com(lambda: self._com.getCorrespondingGraphicElements(model_element._com)))

    def add_free_shape_by_type(self, type_: str, x_points: IRPCollection, y_points: IRPCollection) -> "IRPGraphElement":
        """Adds a free shape using its x and y coordinate collections.

        Args:
            type_: The shape type, such as ``Polygon`` or ``Rectangle``.
            x_points: Collection of integer x coordinates.
            y_points: Collection of integer y coordinates.

        Returns:
            The wrapped graph element created.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::addFreeShapeByType(java.lang.String metaType, com.telelogic.rhapsody.core.IRPCollection xPoints, com.telelogic.rhapsody.core.IRPCollection yPoints)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphElement

        return IRPGraphElement(self.call_com(lambda: self._com.AddFreeShapeByType(type_, x_points._com, y_points._com)))

    def add_image(self, image_path: str, x: int, y: int, width: int, height: int) -> "IRPGraphElement":
        """Adds an image to the diagram.

        Args:
            image_path: The path to the image file.
            x: The X coordinate.
            y: The Y coordinate.
            width: The width.
            height: The height.

        Returns:
            The wrapped graph element created.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::AddImage(java.lang.String imagePath, int x, int y, int width, int height)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphElement

        return IRPGraphElement(self.call_com(lambda: self._com.AddImage(image_path, x, y, width, height)))

    def add_new_edge_by_type(self, type_: str, source: "IRPGraphElement", source_x: int, source_y: int, target: "IRPGraphElement", target_x: int, target_y: int) -> "IRPGraphEdge":
        """Adds a graphical-only connector between two graph elements.

        Args:
            type_: The connector type.
            source: The source graph element.
            source_x: The source attachment x coordinate.
            source_y: The source attachment y coordinate.
            target: The target graph element.
            target_x: The target attachment x coordinate.
            target_y: The target attachment y coordinate.

        Returns:
            The wrapped graph edge created.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::addNewEdgeByType(
                java.lang.String metaType, com.telelogic.rhapsody.core.IRPGraphElement src,
                int xSrcPosition, int ySrcPosition, com.telelogic.rhapsody.core.IRPGraphElement trg,
                int xTrgPosition, int yTrgPosition)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphEdge

        return IRPGraphEdge(self.call_com(lambda: self._com.AddNewEdgeByType(type_, source._com, source_x, source_y, target._com, target_x, target_y)))

    def add_new_edge_for_element(self, element: IRPModelElement, source: "IRPGraphNode", source_x: int, source_y: int, target: "IRPGraphNode", target_x: int, target_y: int) -> "IRPGraphEdge":
        """Adds a connector representation for a model element between two graph nodes.

        Args:
            element: The model element to represent.
            source: The source graph node.
            source_x: The source attachment x coordinate.
            source_y: The source attachment y coordinate.
            target: The target graph node.
            target_x: The target attachment x coordinate.
            target_y: The target attachment y coordinate.

        Returns:
            The wrapped graph edge created.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::addNewEdgeForElement(
                com.telelogic.rhapsody.core.IRPModelElement element, com.telelogic.rhapsody.core.IRPGraphNode src,
                int xSrcPosition, int ySrcPosition, com.telelogic.rhapsody.core.IRPGraphNode trg,
                int xTrgPosition, int yTrgPosition)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphEdge

        return IRPGraphEdge(self.call_com(lambda: self._com.AddNewEdgeForElement(element._com, source._com, source_x, source_y, target._com, target_x, target_y)))

    def add_new_node_by_type(self, type_: str, x: int, y: int, width: int, height: int) -> "IRPGraphNode":
        """Adds a new node to the diagram by type.

        Args:
            type_: The type of node to add.
            x: The X coordinate.
            y: The Y coordinate.
            width: The width.
            height: The height.

        Returns:
            The wrapped graph element created.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::AddNewNodeByType(java.lang.String type, int x, int y, int width, int height)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphNode

        return IRPGraphNode(self.call_com(lambda: self._com.AddNewNodeByType(type_, x, y, width, height)))

    def add_new_node_for_element(self, element: IRPModelElement, x: int, y: int, width: int, height: int) -> "IRPGraphNode":
        """Adds a new node for the specified element.

        Args:
            element: The model element.
            x: The X coordinate.
            y: The Y coordinate.
            width: The width.
            height: The height.

        Returns:
            The wrapped graph element created.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::AddNewNodeForElement(com.telelogic.rhapsody.core.IRPModelElement element, int x, int y, int width, int height)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_graphics import IRPGraphNode

        return IRPGraphNode(self.call_com(lambda: self._com.AddNewNodeForElement(element._com, x, y, width, height)))

    def create_diagram_view(self, name: str) -> "IRPGraphElement":
        """Creates a diagram view with the specified name.

        Args:
            name: The name of the diagram view.

        Returns:
            The wrapped graph element created.

        Raises:
            NotImplementedError: ``createDiagramView`` is absent from the
                registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::createDiagramView(java.lang.String name)
        """
        raise NotImplementedError("createDiagramView is not exposed by the registered pywin32 interface.")

    def get_diagram_view_of(self, name: str) -> Optional["IRPGraphElement"]:
        """Returns the diagram view with the specified name.

        Args:
            name: The name of the diagram view.

        Returns:
            The wrapped graph element, or None if not found.

        Raises:
            NotImplementedError: ``getDiagramViewOf`` is absent from the
                registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getDiagramViewOf(java.lang.String name)
        """
        raise NotImplementedError("getDiagramViewOf is not exposed by the registered pywin32 interface.")

    def get_diagram_views(self) -> IRPCollection:
        """Returns the diagram views for this diagram.

        Returns:
            An ``IRPCollection`` of diagram views.

        Raises:
            NotImplementedError: ``getDiagramViews`` is absent from the
                registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getDiagramViews()
        """
        raise NotImplementedError("getDiagramViews is not exposed by the registered pywin32 interface.")

    def is_diagram_view(self) -> int:
        """Checks if this is a diagram view.

        Returns:
            1 if this is a diagram view, 0 otherwise.

        Raises:
            NotImplementedError: ``isDiagramView`` is absent from the
                registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::isDiagramView()
        """
        raise NotImplementedError("isDiagramView is not exposed by the registered pywin32 interface.")

    def open_diagram_view(self, name: str) -> None:
        """Opens the diagram view with the specified name.

        Args:
            name: The name of the diagram view to open.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::openDiagramView(java.lang.String name)
        """
        self.call_com(lambda: self._com.openDiagramView(name))

    def rearrange_ports(self) -> None:
        """Rearranges the ports on the diagram.

        Raises:
            NotImplementedError: ``rearrangePorts`` is absent from the
                registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::rearrangePorts()
        """
        raise NotImplementedError("rearrangePorts is not exposed by the registered pywin32 interface.")

    def set_custom_views(self, views: IRPCollection) -> None:
        """Sets the custom views for this diagram.

        Args:
            views: The collection of custom views.

        Raises:
            NotImplementedError: ``setCustomViews`` is absent from the
                registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::setCustomViews(com.telelogic.rhapsody.core.IRPCollection views)
        """
        raise NotImplementedError("setCustomViews is not exposed by the registered pywin32 interface.")

    def update_view_on_server(self) -> None:
        """Updates the view on the server.

        Raises:
            NotImplementedError: ``updateViewOnServer`` is absent from the
                registered pywin32 interface.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::updateViewOnServer()
        """
        raise NotImplementedError("updateViewOnServer is not exposed by the registered pywin32 interface.")

    def complete_relations(self, graph_elements: IRPCollection, selected_to_all: int) -> None:
        """Adds connectors for relations between the specified graph elements.

        Args:
            graph_elements: Graph elements whose relations should be displayed.
            selected_to_all: Use 0 for relations among the specified elements;
                use 1 to include their relations to other elements on the diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::completeRelations(com.telelogic.rhapsody.core.IRPCollection graphElements, int selectedToAll)
        """
        self.call_com(lambda: self._com.completeRelations(graph_elements._com, selected_to_all))

    def get_elements_in_diagram(self) -> IRPCollection:
        """Returns the model elements in this diagram.

        Returns:
            An ``IRPCollection`` of model elements.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getElementsInDiagram()
        """
        return IRPCollection(self.call_com(lambda: self._com.getElementsInDiagram()))

    @property
    def graphical_elements(self) -> IRPCollection:
        """Returns the graphical elements in this diagram.

        Returns:
            An ``IRPCollection`` of graphical elements.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::graphicalElements (property)
        """
        return IRPCollection(self.get_com_property(self._com, "graphicalElements"))

    def get_last_visualization_modified_time(self) -> str:
        """Returns the last visualization modified time.

        Returns:
            The last visualization modified time as a string.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getLastVisualizationModifiedTime()
        """
        return str(self.call_com(lambda: self._com.getLastVisualizationModifiedTime()))

    def get_picture(self) -> "IRPGraphElement":
        """Returns the picture for this diagram.

        Returns:
            The wrapped graph element representing the picture.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getPicture()
        """
        return cast("IRPGraphElement", self.wrap(self.call_com(lambda: self._com.getPicture())))

    def get_picture_as(self, format_: str) -> "IRPGraphElement":
        """Returns the picture in the specified format.

        Args:
            format_: The format for the picture.

        Returns:
            The wrapped graph element representing the picture.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getPictureAs(java.lang.String format)
        """
        return cast("IRPGraphElement", self.wrap(self.call_com(lambda: self._com.getPictureAs(format_))))

    def get_picture_as_divided_metafiles(self, first_file_name: str) -> IRPCollection:
        """Saves the diagram as one or more EMF metafiles.

        Args:
            first_file_name: The name for the first file. Additional split
                files use the documented `firstFileNameZ_X_Y` convention.

        Returns:
            An ``IRPCollection`` containing the names of the files created.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getPictureAsDividedMetafiles(java.lang.String firstFileName)
        """
        return IRPCollection(self.call_com(lambda: self._com.getPictureAsDividedMetafiles(first_file_name)))

    def get_picture_ex(self, x: int, y: int, width: int, height: int) -> "IRPGraphElement":
        """Returns a picture for the specified region.

        Args:
            x: The X coordinate.
            y: The Y coordinate.
            width: The width.
            height: The height.

        Returns:
            The wrapped graph element representing the picture.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getPictureEx(int x, int y, int width, int height)
        """
        return cast("IRPGraphElement", self.wrap(self.call_com(lambda: self._com.getPictureEx(x, y, width, height))))

    def get_pictures_with_image_map(self, first_file_name: str, diagram_map: "IRPCollection") -> "IRPCollection":
        """Saves the diagram as EMF file(s) and populates the given collection with image-map info.

        Saves the diagram as an EMF format file, breaking the diagram into a number of
        files if necessary (based on the ``General:Graphics:ExportedDiagramScale`` property).
        The ``diagram_map`` collection is populated with ``IRPImageMap`` objects containing
        the information needed to construct an HTML image map.

        Args:
            first_file_name: The base name for the created EMF file(s). If multiple files
                are created, names follow the convention ``firstFileNameZ_X_Y``.
            diagram_map: An empty ``IRPCollection`` (obtainable via
                ``RhapsodyApplication.create_new_collection()``) that will be populated
                with ``IRPImageMap`` objects.

        Returns:
            An ``IRPCollection`` containing the names of the files that were created.

        Raises:
            RhapsodyRuntimeException: If the operation fails.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::getPicturesWithImageMap(
                java.lang.String firstFileName, com.telelogic.rhapsody.core.IRPCollection diagrammap)
        """
        result = self.call_com(lambda: self._com.getPicturesWithImageMap(first_file_name, diagram_map._com))
        file_names, _ = cast(tuple[object, object], result)
        return IRPCollection(file_names)

    def is_open(self) -> int:
        """Checks if the diagram is open.

        Returns:
            1 if the diagram is open, 0 otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::isOpen()
        """
        return int(self.call_com(lambda: self._com.isOpen()))

    def is_show_diagram_frame(self) -> int:
        """Checks if the diagram frame is shown.

        Returns:
            1 if the diagram frame is shown, 0 otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::isShowDiagramFrame()
        """
        return int(self.call_com(lambda: self._com.isShowDiagramFrame()))

    def open_diagram(self) -> None:
        """Opens the diagram.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::openDiagram()
        """
        self.call_com(lambda: self._com.openDiagram())

    def populate_diagram(self, elements_to_populate: IRPCollection, relations_types: IRPCollection, create_content: str) -> None:
        """Populates the diagram with the specified elements and relation types.

        Args:
            elements_to_populate: The model elements to add to the diagram.
            relations_types: Relation-type strings to display, such as ``AllRelations``.
            create_content: One of ``among``, ``from``, ``to``, or ``fromto``.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::populateDiagram(
                com.telelogic.rhapsody.core.IRPCollection elementsToPopulate,
                com.telelogic.rhapsody.core.IRPCollection relationsTypes, java.lang.String createContent)
        """
        self.call_com(lambda: self._com.populateDiagram(elements_to_populate._com, relations_types._com, create_content))

    def remove_graph_elements(self, elements: IRPCollection) -> None:
        """Removes the specified graph elements from the diagram.

        Args:
            elements: The collection of graph elements to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::removeGraphElements(com.telelogic.rhapsody.core.IRPCollection elements)
        """
        self.call_com(lambda: self._com.removeGraphElements(elements._com))

    def set_show_diagram_frame(self, show: int) -> None:
        """Sets whether to show the diagram frame.

        Args:
            show: 1 to show the frame, 0 to hide it.

        Reference:
            com.telelogic.rhapsody.core.IRPDiagram::setShowDiagramFrame(int show)
        """
        self.call_com(lambda: self._com.setShowDiagramFrame(show))


IRPModelElement.register_wrapper("ActivityDiagram", IRPDiagram)
