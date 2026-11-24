"""Tests for graphics package — IRPGraphElement, IRPGraphEdge, and 12 other classes (Task 15)."""

from rhapsody_cli.models.com.telelogic.rhapsody.core import (
    IRPConditionMark,
    IRPConnector,
    IRPGraphEdge,
    IRPGraphElement,
    IRPGraphicalProperty,
    IRPGraphNode,
    IRPImageMap,
    IRPLink,
    IRPMatrixLayout,
    IRPMatrixView,
    IRPMessagePoint,
    IRPPin,
    IRPTableLayout,
    IRPTableView,
)
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


class TestRPGraphElementTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("GraphElement", properties={"name": "ge1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPGraphElement)

    def test_get_interface_name_returns_str(self) -> None:
        # Pattern A — no-arg getter returning primitive
        fake = make_fake_element("GraphElement")
        fake.interfaceName = "IFoo"
        ge = IRPGraphElement(fake)
        assert ge.get_interface_name() == "IFoo"

    def test_get_model_object_wraps_result(self) -> None:
        # Pattern B — no-arg getter returning wrapped element
        fake = make_fake_element("GraphElement")
        model_obj = make_fake_element("Class", properties={"name": "Widget"})
        fake.getModelObject.return_value = model_obj
        ge = IRPGraphElement(fake)
        wrapped = ge.get_model_object()
        assert wrapped is not None and wrapped.name == "Widget"

    def test_get_all_graphical_properties_returns_collection(self) -> None:
        # Pattern C — no-arg getter returning collection
        fake = make_fake_element("GraphElement")
        prop = make_fake_element("GraphicalProperty", properties={"name": "p1"})
        fake.getAllGraphicalProperties.return_value = make_fake_collection([prop])
        ge = IRPGraphElement(fake)
        result = ge.get_all_graphical_properties()
        assert isinstance(result, IRPCollection)

    def test_set_associated_image_delegates(self) -> None:
        # Pattern D — single-arg setter (str)
        fake = make_fake_element("GraphElement")
        fake.setAssociatedImage.return_value = None
        ge = IRPGraphElement(fake)
        ge.set_associated_image("img.png")
        fake.setAssociatedImage.assert_called_once_with("img.png")

    def test_add_property_delegates(self) -> None:
        # Pattern F — multi-arg void method (3 str args)
        fake = make_fake_element("GraphElement")
        fake.addProperty.return_value = None
        ge = IRPGraphElement(fake)
        ge.add_property("key", "type", "value")
        fake.addProperty.assert_called_once_with("key", "type", "value")

    def test_get_graphical_property_uses_call_com_directly(self) -> None:
        # Parameterized getter — must use call_com (not _get_method_or_property)
        fake = make_fake_element("GraphElement")
        prop = make_fake_element("GraphicalProperty", properties={"name": "FillColor"})
        fake.getGraphicalProperty.return_value = prop
        ge = IRPGraphElement(fake)
        wrapped = ge.get_graphical_property("FillColor")
        assert wrapped.name == "FillColor"
        fake.getGraphicalProperty.assert_called_once_with("FillColor")

    def test_remove_property_delegates(self) -> None:
        # Pattern F — single-arg void method (str)
        fake = make_fake_element("GraphElement")
        fake.removeProperty.return_value = None
        ge = IRPGraphElement(fake)
        ge.remove_property("key")
        fake.removeProperty.assert_called_once_with("key")

    def test_get_diagram_wraps_result(self) -> None:
        # Pattern B — no-arg getter returning wrapped element
        fake = make_fake_element("GraphElement")
        diagram = make_fake_element("ObjectModelDiagram", properties={"name": "Diagram1"})
        fake.getDiagram.return_value = diagram
        ge = IRPGraphElement(fake)
        wrapped = ge.get_diagram()
        assert wrapped.name == "Diagram1"

    def test_get_graphical_parent_wraps_result(self) -> None:
        # Pattern B — no-arg getter returning wrapped element
        fake = make_fake_element("GraphElement")
        parent = make_fake_element("GraphNode", properties={"name": "Parent"})
        fake.getGraphicalParent.return_value = parent
        ge = IRPGraphElement(fake)
        wrapped = ge.get_graphical_parent()
        assert wrapped.name == "Parent"

    def test_get_property_value_parameterized(self) -> None:
        # Parameterized getter — must use call_com
        fake = make_fake_element("GraphElement")
        fake.getPropertyValue.return_value = "someValue"
        ge = IRPGraphElement(fake)
        result = ge.get_property_value("myKey")
        assert result == "someValue"
        fake.getPropertyValue.assert_called_once_with("myKey")

    def test_set_property_value_parameterized(self) -> None:
        # Parameterized setter — must use call_com
        fake = make_fake_element("GraphElement")
        fake.setPropertyValue.return_value = None
        ge = IRPGraphElement(fake)
        ge.set_property_value("key", "value")
        fake.setPropertyValue.assert_called_once_with("key", "value")


class TestRPGraphEdgeTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("GraphEdge", properties={"name": "edge1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPGraphEdge)

    def test_is_graph_element(self) -> None:
        # IRPGraphEdge extends IRPGraphElement
        fake = make_fake_element("GraphEdge", properties={"name": "edge1"})
        edge = IRPGraphEdge(fake)
        assert isinstance(edge, IRPGraphElement)

    def test_get_source_wraps_result(self) -> None:
        # Pattern B — no-arg getter returning wrapped element
        fake = make_fake_element("GraphEdge")
        src = make_fake_element("GraphNode", properties={"name": "src"})
        fake.getSource.return_value = src
        edge = IRPGraphEdge(fake)
        wrapped = edge.get_source()
        assert wrapped.name == "src"

    def test_get_target_wraps_result(self) -> None:
        # Pattern B
        fake = make_fake_element("GraphEdge")
        tgt = make_fake_element("GraphNode", properties={"name": "tgt"})
        fake.getTarget.return_value = tgt
        edge = IRPGraphEdge(fake)
        wrapped = edge.get_target()
        assert wrapped.name == "tgt"

    def test_embed_new_flow_returns_self(self) -> None:
        # Pattern E — no-arg method returning wrapped element (self)
        fake = make_fake_element("GraphEdge")
        fake.embedNewFlow.return_value = fake  # returns the same edge
        edge = IRPGraphEdge(fake)
        result = edge.embed_new_flow()
        fake.embedNewFlow.assert_called_once_with()
        assert result is not None

    def test_get_containing_arrow_wraps_result(self) -> None:
        # Pattern B
        fake = make_fake_element("GraphEdge")
        arrow = make_fake_element("GraphEdge", properties={"name": "arrow"})
        fake.getContainingArrow.return_value = arrow
        edge = IRPGraphEdge(fake)
        wrapped = edge.get_containing_arrow()
        assert wrapped.name == "arrow"


class TestRPGraphNodeTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("GraphNode", properties={"name": "node1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPGraphNode)

    def test_is_graph_element(self) -> None:
        fake = make_fake_element("GraphNode", properties={"name": "node1"})
        node = IRPGraphNode(fake)
        assert isinstance(node, IRPGraphElement)

    def test_bring_to_front_delegates(self) -> None:
        # Pattern F — void method
        fake = make_fake_element("GraphNode")
        fake.bringToFront.return_value = None
        node = IRPGraphNode(fake)
        node.bring_to_front()
        fake.bringToFront.assert_called_once_with()

    def test_send_to_back_delegates(self) -> None:
        # Pattern F — void method
        fake = make_fake_element("GraphNode")
        fake.sendToBack.return_value = None
        node = IRPGraphNode(fake)
        node.send_to_back()
        fake.sendToBack.assert_called_once_with()

    def test_hide_all_ports_delegates(self) -> None:
        # Pattern F — void method
        fake = make_fake_element("GraphNode")
        fake.hideAllPorts.return_value = None
        node = IRPGraphNode(fake)
        node.hide_all_ports()
        fake.hideAllPorts.assert_called_once_with()

    def test_show_all_ports_delegates(self) -> None:
        # Pattern F — void method
        fake = make_fake_element("GraphNode")
        fake.showAllPorts.return_value = None
        node = IRPGraphNode(fake)
        node.show_all_ports()
        fake.showAllPorts.assert_called_once_with()

    def test_get_is_panel_widget_returns_int(self) -> None:
        # Pattern G — returns 0/1 int
        fake = make_fake_element("GraphNode")
        fake.getIsPanelWidget.return_value = 1
        node = IRPGraphNode(fake)
        assert node.get_is_panel_widget() == 1


class TestRPConnectorTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("Connector", properties={"name": "conn1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPConnector)

    def test_is_condition_connector_returns_int(self) -> None:
        # Pattern G — returns 0/1 int
        fake = make_fake_element("Connector")
        fake.isConditionConnector.return_value = 1
        conn = IRPConnector(fake)
        assert conn.is_condition_connector() == 1
        fake.isConditionConnector.assert_called_once_with()

    def test_is_fork_connector_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Connector")
        fake.isForkConnector.return_value = 1
        conn = IRPConnector(fake)
        assert conn.is_fork_connector() == 1
        fake.isForkConnector.assert_called_once_with()

    def test_is_join_connector_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("Connector")
        fake.isJoinConnector.return_value = 0
        conn = IRPConnector(fake)
        assert conn.is_join_connector() == 0
        fake.isJoinConnector.assert_called_once_with()

    def test_get_connector_type_returns_str(self) -> None:
        # Pattern A — returns str
        fake = make_fake_element("Connector")
        fake.getConnectorType.return_value = "Fork"
        conn = IRPConnector(fake)
        assert conn.get_connector_type() == "Fork"

    def test_get_derived_in_edges_returns_collection(self) -> None:
        # Pattern C — returns collection
        fake = make_fake_element("Connector")
        trans = make_fake_element("Transition", properties={"name": "T1"})
        fake.getDerivedInEdges.return_value = make_fake_collection([trans])
        conn = IRPConnector(fake)
        result = conn.get_derived_in_edges()
        assert isinstance(result, IRPCollection)

    def test_get_of_state_wraps_result(self) -> None:
        # Pattern B — returns wrapped IRPState
        fake = make_fake_element("Connector")
        state = make_fake_element("State", properties={"name": "S1"})
        fake.getOfState.return_value = state
        conn = IRPConnector(fake)
        wrapped = conn.get_of_state()
        assert wrapped.name == "S1"

    def test_set_of_state_delegates(self) -> None:
        # Pattern F — setter with wrapped element
        fake = make_fake_element("Connector")
        state = make_fake_element("State", properties={"name": "S1"})
        fake.setOfState.return_value = None
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_statemachine import IRPState

        conn = IRPConnector(fake)
        conn.set_of_state(IRPState(state))
        fake.setOfState.assert_called_once_with(state)


class TestRPPinTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("Pin", properties={"name": "pin1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPPin)

    def test_is_connector(self) -> None:
        fake = make_fake_element("Pin", properties={"name": "pin1"})
        pin = IRPPin(fake)
        assert isinstance(pin, IRPConnector)

    def test_get_pin_direction_returns_str(self) -> None:
        # Pattern A
        fake = make_fake_element("Pin")
        fake.getPinDirection.return_value = "In"
        pin = IRPPin(fake)
        assert pin.get_pin_direction() == "In"

    def test_get_pin_type_wraps_result(self) -> None:
        # Pattern B — returns wrapped IRPClassifier
        fake = make_fake_element("Pin")
        classifier = make_fake_element("Class", properties={"name": "DataType"})
        fake.getPinType.return_value = classifier
        pin = IRPPin(fake)
        wrapped = pin.get_pin_type()
        assert wrapped.name == "DataType"

    def test_set_pin_type_delegates(self) -> None:
        # Pattern F — setter with wrapped element
        fake = make_fake_element("Pin")
        classifier = make_fake_element("Class", properties={"name": "DataType"})
        fake.setPinType.return_value = None
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass

        pin = IRPPin(fake)
        pin.set_pin_type(IRPClass(classifier))
        fake.setPinType.assert_called_once_with(classifier)


class TestRPConditionMarkTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("ConditionMark", properties={"name": "cm1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPConditionMark)

    def test_is_message(self) -> None:
        fake = make_fake_element("ConditionMark", properties={"name": "cm1"})
        cm = IRPConditionMark(fake)
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interactions import IRPMessage

        assert isinstance(cm, IRPMessage)


class TestRPGraphicalPropertyTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("GraphicalProperty", properties={"name": "gp1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPGraphicalProperty)

    def test_get_key_returns_str(self) -> None:
        # Pattern A
        fake = make_fake_element("GraphicalProperty")
        fake.getKey.return_value = "FillColor"
        gp = IRPGraphicalProperty(fake)
        assert gp.get_key() == "FillColor"

    def test_get_value_returns_str(self) -> None:
        # Pattern A
        fake = make_fake_element("GraphicalProperty")
        fake.getValue.return_value = "255,0,0"
        gp = IRPGraphicalProperty(fake)
        assert gp.get_value() == "255,0,0"


class TestRPImageMapTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("ImageMap", properties={"name": "im1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPImageMap)

    def test_get_name_returns_str(self) -> None:
        # Pattern A
        fake = make_fake_element("ImageMap")
        fake.name = "MyImageMap"
        im = IRPImageMap(fake)
        assert im.get_name() == "MyImageMap"

    def test_get_shape_returns_str(self) -> None:
        # Pattern A
        fake = make_fake_element("ImageMap")
        fake.getShape.return_value = "rect"
        im = IRPImageMap(fake)
        assert im.get_shape() == "rect"

    def test_get_is_guid_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("ImageMap")
        fake.getIsGUID.return_value = 1
        im = IRPImageMap(fake)
        assert im.get_is_guid() == 1


class TestRPLinkTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("Link", properties={"name": "link1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPLink)

    def test_get_end1_name_returns_str(self) -> None:
        # Pattern A
        fake = make_fake_element("Link")
        fake.getEnd1Name.return_value = "End1"
        link = IRPLink(fake)
        assert link.get_end1_name() == "End1"

    def test_get_from_wraps_result(self) -> None:
        # Pattern B — returns wrapped IRPInstance
        fake = make_fake_element("Link")
        instance = make_fake_element("Instance", properties={"name": "Inst1"})
        fake.getFrom.return_value = instance
        link = IRPLink(fake)
        wrapped = link.get_from()
        assert wrapped.name == "Inst1"

    def test_get_instantiates_wraps_result(self) -> None:
        # Pattern B — returns wrapped IRPRelation
        fake = make_fake_element("Link")
        relation = make_fake_element("Association", properties={"name": "Assoc1"})
        fake.getInstantiates.return_value = relation
        link = IRPLink(fake)
        wrapped = link.get_instantiates()
        assert wrapped.name == "Assoc1"

    def test_set_end1_name_delegates(self) -> None:
        # Pattern D
        fake = make_fake_element("Link")
        fake.setEnd1Name.return_value = None
        link = IRPLink(fake)
        link.set_end1_name("NewEnd1")
        fake.setEnd1Name.assert_called_once_with("NewEnd1")


class TestRPMessagePointTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("MessagePoint", properties={"name": "mp1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPMessagePoint)

    def test_get_type_returns_str(self) -> None:
        # Pattern A
        fake = make_fake_element("MessagePoint")
        fake.getType.return_value = "Send"
        mp = IRPMessagePoint(fake)
        assert mp.get_type() == "Send"

    def test_get_message_wraps_result(self) -> None:
        # Pattern B — returns wrapped IRPMessage
        fake = make_fake_element("MessagePoint")
        message = make_fake_element("Message", properties={"name": "Msg1"})
        fake.getMessage.return_value = message
        mp = IRPMessagePoint(fake)
        wrapped = mp.get_message()
        assert wrapped.name == "Msg1"


class TestRPTableLayoutTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("TableLayout", properties={"name": "tl1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPTableLayout)

    def test_get_collapse_first_column_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("TableLayout")
        fake.getCollapseFirstColumn.return_value = 1
        tl = IRPTableLayout(fake)
        assert tl.get_collapse_first_column() == 1

    def test_get_column_name_parameterized(self) -> None:
        # Parameterized getter — must use call_com
        fake = make_fake_element("TableLayout")
        fake.getColumnName.return_value = "Col1"
        tl = IRPTableLayout(fake)
        assert tl.get_column_name(0) == "Col1"
        fake.getColumnName.assert_called_once_with(0)

    def test_add_column_delegates(self) -> None:
        # Pattern F — multi-arg void
        fake = make_fake_element("TableLayout")
        fake.addColumn.return_value = None
        tl = IRPTableLayout(fake)
        tl.add_column("GENERAL_ATTRIBUTE", "NAME", "Name")
        fake.addColumn.assert_called_once_with("GENERAL_ATTRIBUTE", "NAME", "Name")

    def test_get_element_types_returns_collection(self) -> None:
        # Pattern C
        fake = make_fake_element("TableLayout")
        fake.getElementTypes.return_value = make_fake_collection([])
        tl = IRPTableLayout(fake)
        result = tl.get_element_types()
        assert isinstance(result, IRPCollection)

    def test_get_relation_table_returns_int(self) -> None:
        # Pattern G
        fake = make_fake_element("TableLayout")
        fake.getRelationTable.return_value = 1
        tl = IRPTableLayout(fake)
        assert tl.get_relation_table() == 1


class TestRPTableViewTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("TableView", properties={"name": "tv1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPTableView)

    def test_get_row_count_returns_int(self) -> None:
        # Pattern A (int)
        fake = make_fake_element("TableView")
        fake.getRowCount.return_value = 5
        tv = IRPTableView(fake)
        assert tv.get_row_count() == 5

    def test_get_cell_string_parameterized(self) -> None:
        # Parameterized getter — must use call_com
        fake = make_fake_element("TableView")
        fake.getCellString.return_value = "CellText"
        tv = IRPTableView(fake)
        assert tv.get_cell_string(0, 0) == "CellText"
        fake.getCellString.assert_called_once_with(0, 0)

    def test_get_its_table_layout_wraps_result(self) -> None:
        # Pattern B
        fake = make_fake_element("TableView")
        layout = make_fake_element("TableLayout", properties={"name": "TL1"})
        fake.getItsTableLayout.return_value = layout
        tv = IRPTableView(fake)
        wrapped = tv.get_its_table_layout()
        assert wrapped.name == "TL1"

    def test_open_delegates(self) -> None:
        # Pattern F — void method
        fake = make_fake_element("TableView")
        fake.open.return_value = None
        tv = IRPTableView(fake)
        tv.open()
        fake.open.assert_called_once_with()


class TestRPMatrixLayoutTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("MatrixLayout", properties={"name": "ml1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPMatrixLayout)

    def test_get_from_element_types_returns_collection(self) -> None:
        # Pattern C
        fake = make_fake_element("MatrixLayout")
        fake.getFromElementTypes.return_value = make_fake_collection([])
        ml = IRPMatrixLayout(fake)
        result = ml.get_from_element_types()
        assert isinstance(result, IRPCollection)


class TestRPMatrixViewTask15:
    def test_is_registered(self) -> None:
        fake = make_fake_element("MatrixView", properties={"name": "mv1"})
        wrapped = IRPModelElement.wrap(fake)
        assert isinstance(wrapped, IRPMatrixView)

    def test_get_column_count_returns_int(self) -> None:
        # Pattern A (int)
        fake = make_fake_element("MatrixView")
        fake.getColumnCount.return_value = 3
        mv = IRPMatrixView(fake)
        assert mv.get_column_count() == 3

    def test_get_cell_elements_parameterized(self) -> None:
        # Parameterized getter returning collection — must use call_com
        fake = make_fake_element("MatrixView")
        el = make_fake_element("Class", properties={"name": "C1"})
        fake.getCellElements.return_value = make_fake_collection([el])
        mv = IRPMatrixView(fake)
        result = mv.get_cell_elements(0, 0)
        assert isinstance(result, IRPCollection)
        fake.getCellElements.assert_called_once_with(0, 0)

    def test_open_delegates(self) -> None:
        # Pattern F — void method
        fake = make_fake_element("MatrixView")
        fake.open.return_value = None
        mv = IRPMatrixView(fake)
        mv.open()
        fake.open.assert_called_once_with()
