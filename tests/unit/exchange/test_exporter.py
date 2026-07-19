"""Tests for RhapsodyExporter.

UTS_XCH_00065: export returns dict with version, project, rhapsody-model keys
UTS_XCH_00066: export includes project name from container
UTS_XCH_00067: _export_element dispatches Package
UTS_XCH_00068: _export_element dispatches Class
UTS_XCH_00069: _export_operation emits return_type, is_static, arguments
UTS_XCH_00070: _export_argument emits data_type and direction
UTS_XCH_00071: _export_attribute emits data_type, visibility, multiplicity, is_static
UTS_XCH_00072: _export_type emits kind and enumeration literals
UTS_XCH_00073: _export_type emits children for Structure kind
UTS_XCH_00074: _export_object emits classifier
UTS_XCH_00075: _export_enumeration_literal emits name only
UTS_XCH_00076: _export_stereotypes returns names
UTS_XCH_00077: _export_tags returns name/value dict
UTS_XCH_00078: _export_element skips unsupported metaclass
UTS_XCH_00079: _export_element attaches stereotypes and tags
"""

from unittest.mock import MagicMock

from rhapsody_cli.exchange.exporter import RhapsodyExporter


def _make_exporter(project: object = None) -> RhapsodyExporter:
    """Build a RhapsodyExporter with mocked app and project."""
    exporter = RhapsodyExporter.__new__(RhapsodyExporter)
    exporter.app = MagicMock()
    exporter.project = project
    return exporter


class TestExport:
    """UTS_XCH_00065, UTS_XCH_00066: export() top-level dict shape."""

    def test_returns_dict_with_required_keys(self) -> None:
        project = MagicMock()
        project.get_meta_class.return_value = "Project"
        project.get_name.return_value = "MyProject"
        project.get_nested_elements.return_value = []
        exporter = _make_exporter()

        result = exporter.export(project)

        assert result["version"] == 1
        assert result["project"] == "MyProject"
        assert result["rhapsody-model"] == []

    def test_includes_project_name_from_container(self) -> None:
        project = MagicMock()
        project.get_meta_class.return_value = "Project"
        project.get_name.return_value = "TopLevel"
        pkg = MagicMock()
        pkg.get_meta_class.return_value = "Package"
        pkg.get_name.return_value = "Sub"
        pkg.get_owner.return_value = project
        pkg.get_nested_elements.return_value = []
        exporter = _make_exporter()

        result = exporter.export(pkg)

        assert result["project"] == "TopLevel"

    def test_includes_exported_children(self) -> None:
        cls = MagicMock()
        cls.get_meta_class.return_value = "Class"
        cls.get_name.return_value = "Widget"
        cls.get_nested_elements.return_value = []
        cls.get_stereotypes.return_value = []
        cls.get_all_tags.return_value = []
        project = MagicMock()
        project.get_meta_class.return_value = "Project"
        project.get_name.return_value = "P"
        project.get_nested_elements.return_value = [cls]
        exporter = _make_exporter()

        result = exporter.export(project)

        assert len(result["rhapsody-model"]) == 1
        assert result["rhapsody-model"][0]["name"] == "Widget"
        assert result["rhapsody-model"][0]["type"] == "Class"


class TestExportPackage:
    """UTS_XCH_00067: _export_package."""

    def test_emits_name_type_and_children(self) -> None:
        child = MagicMock()
        child.get_meta_class.return_value = "Class"
        child.get_name.return_value = "Inner"
        child.get_nested_elements.return_value = []
        child.get_stereotypes.return_value = []
        child.get_all_tags.return_value = []
        pkg = MagicMock()
        pkg.get_meta_class.return_value = "Package"
        pkg.get_name.return_value = "Outer"
        pkg.get_nested_elements.return_value = [child]
        pkg.get_stereotypes.return_value = []
        pkg.get_all_tags.return_value = []
        exporter = _make_exporter()

        result = exporter._export_element(pkg)

        assert result["name"] == "Outer"
        assert result["type"] == "Package"
        assert "children" in result
        assert result["children"][0]["name"] == "Inner"


class TestExportClass:
    """UTS_XCH_00068: _export_class."""

    def test_emits_name_type(self) -> None:
        cls = MagicMock()
        cls.get_meta_class.return_value = "Class"
        cls.get_name.return_value = "Widget"
        cls.get_nested_elements.return_value = []
        cls.get_stereotypes.return_value = []
        cls.get_all_tags.return_value = []
        exporter = _make_exporter()

        result = exporter._export_element(cls)

        assert result["name"] == "Widget"
        assert result["type"] == "Class"


class TestExportOperation:
    """UTS_XCH_00069: _export_operation."""

    def test_emits_return_type_is_static_and_arguments(self) -> None:
        return_classifier = MagicMock()
        return_classifier.get_name.return_value = "int"
        arg = MagicMock()
        arg.get_meta_class.return_value = "Argument"
        arg.get_name.return_value = "x"
        arg.get_type.return_value = return_classifier
        arg.get_argument_direction.return_value = "in"
        arg.get_stereotypes.return_value = []
        arg.get_all_tags.return_value = []
        op = MagicMock()
        op.get_meta_class.return_value = "Operation"
        op.get_name.return_value = "reset"
        op.get_returns.return_value = return_classifier
        op.get_is_static.return_value = True
        op.get_arguments.return_value = [arg]
        op.get_stereotypes.return_value = []
        op.get_all_tags.return_value = []
        exporter = _make_exporter()

        result = exporter._export_element(op)

        assert result["return_type"] == "int"
        assert result["is_static"] is True
        assert len(result["arguments"]) == 1
        assert result["arguments"][0]["name"] == "x"
        assert result["arguments"][0]["data_type"] == "int"
        assert result["arguments"][0]["direction"] == "in"


class TestExportArgument:
    """UTS_XCH_00070: _export_argument."""

    def test_emits_data_type_and_direction(self) -> None:
        classifier = MagicMock()
        classifier.get_name.return_value = "String"
        arg = MagicMock()
        arg.get_meta_class.return_value = "Argument"
        arg.get_name.return_value = "name"
        arg.get_type.return_value = classifier
        arg.get_argument_direction.return_value = "in"
        arg.get_stereotypes.return_value = []
        arg.get_all_tags.return_value = []
        exporter = _make_exporter()

        result = exporter._export_element(arg)

        assert result["name"] == "name"
        assert result["type"] == "Argument"
        assert result["data_type"] == "String"
        assert result["direction"] == "in"


class TestExportAttribute:
    """UTS_XCH_00071: _export_attribute."""

    def test_emits_all_fields(self) -> None:
        classifier = MagicMock()
        classifier.get_name.return_value = "int"
        attr = MagicMock()
        attr.get_meta_class.return_value = "Attribute"
        attr.get_name.return_value = "count"
        attr.get_type.return_value = classifier
        attr.get_visibility.return_value = "public"
        attr.get_multiplicity.return_value = "1"
        attr.get_is_static.return_value = False
        attr.get_stereotypes.return_value = []
        attr.get_all_tags.return_value = []
        exporter = _make_exporter()

        result = exporter._export_element(attr)

        assert result["data_type"] == "int"
        assert result["visibility"] == "public"
        assert result["multiplicity"] == "1"
        assert result["is_static"] is False


class TestExportType:
    """UTS_XCH_00072, UTS_XCH_00073: _export_type."""

    def test_emits_kind_and_enumeration_literals(self) -> None:
        literal = MagicMock()
        literal.get_meta_class.return_value = "EnumerationLiteral"
        literal.get_name.return_value = "RED"
        literal.get_stereotypes.return_value = []
        literal.get_all_tags.return_value = []
        type_element = MagicMock()
        type_element.get_meta_class.return_value = "Type"
        type_element.get_name.return_value = "Color"
        type_element.get_kind.return_value = "Enumeration"
        type_element.get_enumeration_literals.return_value = [literal]
        type_element.get_nested_elements.return_value = []
        type_element.get_stereotypes.return_value = []
        type_element.get_all_tags.return_value = []
        exporter = _make_exporter()

        result = exporter._export_element(type_element)

        assert result["kind"] == "Enumeration"
        assert "literals" in result
        assert result["literals"][0]["name"] == "RED"

    def test_emits_children_for_structure_kind(self) -> None:
        child = MagicMock()
        child.get_meta_class.return_value = "Attribute"
        child.get_name.return_value = "x"
        child.get_type.return_value = None
        child.get_visibility.return_value = None
        child.get_multiplicity.return_value = None
        child.get_is_static.return_value = None
        child.get_stereotypes.return_value = []
        child.get_all_tags.return_value = []
        type_element = MagicMock()
        type_element.get_meta_class.return_value = "Type"
        type_element.get_name.return_value = "Point"
        type_element.get_kind.return_value = "Structure"
        type_element.get_nested_elements.return_value = [child]
        type_element.get_stereotypes.return_value = []
        type_element.get_all_tags.return_value = []
        exporter = _make_exporter()

        result = exporter._export_element(type_element)

        assert result["kind"] == "Structure"
        assert "children" in result
        assert result["children"][0]["name"] == "x"


class TestExportObject:
    """UTS_XCH_00074: _export_object."""

    def test_emits_classifier(self) -> None:
        classifier = MagicMock()
        classifier.get_name.return_value = "MyClass"
        obj = MagicMock()
        obj.get_meta_class.return_value = "Object"
        obj.get_name.return_value = "myObj"
        obj.get_classifier.return_value = classifier
        obj.get_stereotypes.return_value = []
        obj.get_all_tags.return_value = []
        exporter = _make_exporter()

        result = exporter._export_element(obj)

        assert result["classifier"] == "MyClass"


class TestExportEnumerationLiteral:
    """UTS_XCH_00075: _export_enumeration_literal."""

    def test_emits_name_only(self) -> None:
        literal = MagicMock()
        literal.get_meta_class.return_value = "EnumerationLiteral"
        literal.get_name.return_value = "RED"
        literal.get_stereotypes.return_value = []
        literal.get_all_tags.return_value = []
        exporter = _make_exporter()

        result = exporter._export_element(literal)

        assert result == {"name": "RED", "type": "EnumerationLiteral"}


class TestExportStereotypesAndTags:
    """UTS_XCH_00076, UTS_XCH_00077, UTS_XCH_00079: common property exporters."""

    def test_export_stereotypes_returns_names(self) -> None:
        st1 = MagicMock()
        st1.get_name.return_value = "Interface"
        st2 = MagicMock()
        st2.get_name.return_value = "SwComponent"
        element = MagicMock()
        element.get_stereotypes.return_value = [st1, st2]
        exporter = _make_exporter()

        result = exporter._export_stereotypes(element)

        assert result == ["Interface", "SwComponent"]

    def test_export_tags_returns_name_value_dict(self) -> None:
        tag1 = MagicMock()
        tag1.get_name.return_value = "status"
        tag1.get_value.return_value = "active"
        tag2 = MagicMock()
        tag2.get_name.return_value = "count"
        tag2.get_value.return_value = "3"
        element = MagicMock()
        element.get_all_tags.return_value = [tag1, tag2]
        exporter = _make_exporter()

        result = exporter._export_tags(element)

        assert result == {"status": "active", "count": "3"}

    def test_export_element_attaches_stereotypes_and_tags(self) -> None:
        st = MagicMock()
        st.get_name.return_value = "Interface"
        tag = MagicMock()
        tag.get_name.return_value = "status"
        tag.get_value.return_value = "active"
        cls = MagicMock()
        cls.get_meta_class.return_value = "Class"
        cls.get_name.return_value = "Widget"
        cls.get_nested_elements.return_value = []
        cls.get_stereotypes.return_value = [st]
        cls.get_all_tags.return_value = [tag]
        exporter = _make_exporter()

        result = exporter._export_element(cls)

        assert result["stereotypes"] == ["Interface"]
        assert result["tags"] == {"status": "active"}


class TestExportElementSkipUnsupported:
    """UTS_XCH_00078: _export_element skips unsupported metaclass."""

    def test_returns_none_for_unknown_metaclass(self) -> None:
        element = MagicMock()
        element.get_meta_class.return_value = "SomeUnknownType"
        element.get_name.return_value = "x"
        exporter = _make_exporter()

        result = exporter._export_element(element)

        assert result is None

    def test_returns_none_for_none_input(self) -> None:
        exporter = _make_exporter()

        result = exporter._export_element(None)

        assert result is None
