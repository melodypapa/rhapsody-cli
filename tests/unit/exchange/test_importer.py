"""Tests for RhapsodyImporter.

UTS_XCH_00037: import_template rejects wrong schema version
UTS_XCH_00038: import_template processes each top-level spec
UTS_XCH_00039: _process_element dispatches Package and recurses children
UTS_XCH_00040: _process_element dispatches Class
UTS_XCH_00041: _process_element dispatches Operation (on Class)
UTS_XCH_00042: _process_element dispatches Attribute
UTS_XCH_00043: _process_element dispatches Argument (via Operation extras)
UTS_XCH_00044: _process_element dispatches Type with kind
UTS_XCH_00045: _process_element dispatches Object
UTS_XCH_00046: _process_element dispatches EnumerationLiteral (via Type extras)
UTS_XCH_00047: _process_element applies stereotypes and tags
UTS_XCH_00048: _process_element skips unsupported type with warning
UTS_XCH_00049: _apply_operation_extras sets return_type
UTS_XCH_00050: _apply_operation_extras sets is_static
UTS_XCH_00051: _apply_operation_extras creates arguments
UTS_XCH_00052: _apply_argument_extras sets data_type
UTS_XCH_00053: _apply_argument_extras sets direction
UTS_XCH_00054: _apply_attribute_extras sets data_type, visibility, multiplicity, is_static
UTS_XCH_00055: _apply_type_extras creates enumeration literals
UTS_XCH_00056: _apply_object_extras sets classifier
UTS_XCH_00057: _apply_operation_extras warns on unresolvable return_type
UTS_XCH_00058: _apply_dependency_extras wires source/target
UTS_XCH_00059: _apply_generalization_extras wires derived/base
UTS_XCH_00060: _apply_relation_extras wires source/target and properties
UTS_XCH_00061: _apply_port_extras sets flags, contract, interfaces
UTS_XCH_00062: _apply_event_extras sets base_event and super_event
UTS_XCH_00063: _apply_event_reception_extras sets event reference
UTS_XCH_00064: _process_element dispatches 6 new element types
"""

from typing import TYPE_CHECKING, Dict, Optional, cast
from unittest.mock import MagicMock

import pytest

from rhapsody_cli.exceptions import CliExecutionError
from rhapsody_cli.exchange.importer import RhapsodyImporter
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


def _make_importer(project: Optional[IRPModelElement] = None) -> RhapsodyImporter:
    """Build a RhapsodyImporter with mocked app and project (skips connect)."""
    importer = RhapsodyImporter.__new__(RhapsodyImporter)
    importer.app = MagicMock()
    importer.project = cast(Optional["IRPProject"], project)
    return importer


class TestImportTemplateVersionCheck:
    """UTS_XCH_00037: import_template version validation."""

    def test_rejects_wrong_version(self) -> None:
        importer = _make_importer()
        root = MagicMock()

        with pytest.raises(CliExecutionError) as exc_info:
            importer.import_template({"version": 99, "rhapsody-model": []}, root)

        assert "version" in str(exc_info.value).lower()

    def test_accepts_version_one(self) -> None:
        importer = _make_importer()
        root = MagicMock()
        root.get_nested_elements.return_value = []

        importer.import_template({"version": 1, "rhapsody-model": []}, root)

        # No exception raised


class TestImportTemplateProcessesSpecs:
    """UTS_XCH_00038: import_template iterates rhapsody-model specs."""

    def test_processes_each_top_level_spec(self) -> None:
        importer = _make_importer()
        root = MagicMock()
        root.get_nested_elements.return_value = []
        new_pkg = MagicMock()
        root.add_new_aggr.return_value = new_pkg

        data = {
            "version": 1,
            "rhapsody-model": [
                {"name": "Pkg1", "type": "Package"},
                {"name": "Pkg2", "type": "Package"},
            ],
        }

        importer.import_template(data, root)

        assert root.add_new_aggr.call_count == 2


class TestProcessElementDispatch:
    """UTS_XCH_00039-00048: _process_element dispatch and common property application."""

    def test_dispatches_package_and_recurses_children(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_pkg = MagicMock()
        new_pkg.get_nested_elements.return_value = []
        parent.add_new_aggr.return_value = new_pkg

        spec: Dict[str, object] = {"name": "Pkg1", "type": "Package", "children": [{"name": "ChildCls", "type": "Class"}]}
        new_cls = MagicMock()
        new_cls.get_nested_elements.return_value = []
        new_pkg.add_new_aggr.return_value = new_cls

        importer._process_element(parent, spec)

        # Verify recursion: new_pkg.add_new_aggr called for the Class child
        new_pkg.add_new_aggr.assert_called_once_with("Class", "ChildCls")

    def test_dispatches_class(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_cls = MagicMock()
        new_cls.get_nested_elements.return_value = []
        parent.add_new_aggr.return_value = new_cls

        importer._process_element(parent, {"name": "Widget", "type": "Class"})

        parent.add_new_aggr.assert_called_once_with("Class", "Widget")

    def test_dispatches_operation_on_class(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.meta_class = "Class"
        parent.get_nested_elements.return_value = []
        new_op = MagicMock()
        parent.add_new_aggr.return_value = new_op

        importer._process_element(parent, {"name": "reset", "type": "Operation"})

        parent.add_new_aggr.assert_called_once_with("Operation", "reset")

    def test_dispatches_attribute(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_attr = MagicMock()
        parent.add_new_aggr.return_value = new_attr

        importer._process_element(parent, {"name": "count", "type": "Attribute"})

        parent.add_new_aggr.assert_called_once_with("Attribute", "count")

    def test_dispatches_type_with_kind(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_type = MagicMock()
        parent.add_new_aggr.return_value = new_type

        importer._process_element(parent, {"name": "Color", "type": "Type", "kind": "Enumeration"})

        parent.add_new_aggr.assert_called_once_with("Type", "Color")
        assert new_type.kind == "Enumeration"

    def test_dispatches_object(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_obj = MagicMock()
        parent.add_new_aggr.return_value = new_obj

        importer._process_element(parent, {"name": "myObj", "type": "Object"})

        parent.add_new_aggr.assert_called_once_with("Object", "myObj")

    def test_applies_stereotypes_and_tags(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_pkg = MagicMock()
        new_pkg.meta_class = "Package"
        new_pkg.stereotypes = []
        parent.add_new_aggr.return_value = new_pkg

        spec: Dict[str, object] = {
            "name": "Pkg1",
            "type": "Package",
            "stereotypes": ["SwComponent"],
            "tags": {"status": "active"},
        }

        importer._process_element(parent, spec)

        new_pkg.add_stereotype.assert_called_once_with("SwComponent", "Package")
        new_pkg.set_property_value.assert_called_once_with("status", "active")

    def test_skips_unsupported_type_with_warning(self) -> None:
        importer = _make_importer()
        parent = MagicMock()

        result = importer._process_element(parent, {"name": "Foo", "type": "Activity"})

        assert result is None
        parent.add_new_aggr.assert_not_called()


class TestApplyOperationExtras:
    """UTS_XCH_00049-00051, UTS_XCH_00057: _apply_operation_extras."""

    def test_sets_return_type_when_classifier_resolvable(self) -> None:
        classifier = MagicMock()
        classifier.name = "int"
        project = MagicMock()
        project.get_nested_elements.return_value = [classifier]
        importer = _make_importer(project=project)
        op = MagicMock()
        op.name = "reset"

        importer._apply_operation_extras(op, {"return_type": "int"})

        assert op.returns is classifier

    def test_warns_when_return_type_unresolvable(self) -> None:
        project = MagicMock()
        project.get_nested_elements.return_value = []
        importer = _make_importer(project=project)
        op = MagicMock()
        op.name = "reset"

        importer._apply_operation_extras(op, {"return_type": "Missing"})

        assert "returns" not in op.__dict__

    def test_sets_is_static(self) -> None:
        importer = _make_importer()
        op = MagicMock()

        importer._apply_operation_extras(op, {"is_static": True})

        assert op.is_static is True

    def test_creates_arguments(self) -> None:
        importer = _make_importer()
        op = MagicMock()
        op.get_nested_elements.return_value = []
        new_arg = MagicMock()
        op.add_argument.return_value = new_arg

        importer._apply_operation_extras(op, {"arguments": [{"name": "x", "data_type": "int"}]})

        op.add_argument.assert_called_once_with("x")


class TestApplyArgumentExtras:
    """UTS_XCH_00052, UTS_XCH_00053: _apply_argument_extras."""

    def test_sets_data_type(self) -> None:
        classifier = MagicMock()
        classifier.name = "int"
        project = MagicMock()
        project.get_nested_elements.return_value = [classifier]
        importer = _make_importer(project=project)
        arg = MagicMock()
        arg.name = "x"

        importer._apply_argument_extras(arg, {"data_type": "int"})

        arg.set_type.assert_called_once_with(classifier)

    def test_sets_direction(self) -> None:
        importer = _make_importer()
        arg = MagicMock()

        importer._apply_argument_extras(arg, {"direction": "in"})

        assert arg.argument_direction == "in"


class TestApplyAttributeExtras:
    """UTS_XCH_00054: _apply_attribute_extras."""

    def test_sets_all_fields(self) -> None:
        classifier = MagicMock()
        classifier.name = "int"
        project = MagicMock()
        project.get_nested_elements.return_value = [classifier]
        importer = _make_importer(project=project)
        attr = MagicMock()
        attr.name = "count"

        importer._apply_attribute_extras(
            attr,
            {
                "data_type": "int",
                "visibility": "public",
                "multiplicity": "1",
                "is_static": True,
            },
        )

        attr.set_type.assert_called_once_with(classifier)
        assert attr.visibility == "public"
        assert attr.multiplicity == "1"
        assert attr.is_static is True


class TestApplyTypeExtras:
    """UTS_XCH_00055: _apply_type_extras creates enumeration literals."""

    def test_creates_enumeration_literals(self) -> None:
        importer = _make_importer()
        type_element = MagicMock()
        type_element.get_nested_elements.return_value = []
        new_lit = MagicMock()
        type_element.add_new_aggr.return_value = new_lit

        importer._apply_type_extras(
            type_element,
            {"kind": "Enumeration", "literals": [{"name": "RED"}, {"name": "GREEN"}]},
        )

        assert type_element.add_new_aggr.call_count == 2
        type_element.add_new_aggr.assert_any_call("EnumerationLiteral", "RED")
        type_element.add_new_aggr.assert_any_call("EnumerationLiteral", "GREEN")


class TestApplyObjectExtras:
    """UTS_XCH_00056: _apply_object_extras."""

    def test_sets_classifier(self) -> None:
        classifier = MagicMock()
        classifier.name = "MyClass"
        project = MagicMock()
        project.get_nested_elements.return_value = [classifier]
        importer = _make_importer(project=project)
        obj = MagicMock()
        obj.name = "myObj"

        importer._apply_object_extras(obj, {"classifier": "MyClass"})

        obj.set_classifier.assert_called_once_with(classifier)


class TestApplyDependencyExtras:
    """UTS_XCH_00058: _apply_dependency_extras wires source/target."""

    def test_sets_dependent_and_depends_on(self) -> None:
        target = MagicMock()
        target.name = "OtherClass"
        project = MagicMock()
        project.get_nested_elements.return_value = [target]
        importer = _make_importer(project=project)
        dependency = MagicMock()
        dependency.name = "dep1"
        parent = MagicMock()
        parent.name = "MyClass"

        importer._apply_dependency_extras(dependency, {"depends_on": "OtherClass"}, parent)

        assert dependency.dependent is parent
        assert dependency.depends_on is target

    def test_warns_when_depends_on_unresolvable(self) -> None:
        project = MagicMock()
        project.get_nested_elements.return_value = []
        importer = _make_importer(project=project)
        dependency = MagicMock()
        dependency.name = "dep1"
        parent = MagicMock()
        parent.name = "MyClass"

        sentinel = object()
        dependency.depends_on = sentinel

        importer._apply_dependency_extras(dependency, {"depends_on": "Missing"}, parent)

        assert dependency.depends_on is sentinel
        # dependent is still set (source is always the parent)
        assert dependency.dependent is parent


class TestApplyGeneralizationExtras:
    """UTS_XCH_00059: _apply_generalization_extras wires derived/base."""

    def test_sets_derived_class_and_base_class(self) -> None:
        base = MagicMock()
        base.name = "BaseClass"
        project = MagicMock()
        project.get_nested_elements.return_value = [base]
        importer = _make_importer(project=project)
        generalization = MagicMock()
        generalization.name = "gen1"
        parent = MagicMock()
        parent.name = "MyClass"

        importer._apply_generalization_extras(
            generalization,
            {"base_class": "BaseClass", "visibility": "public", "is_virtual": True},
            parent,
        )

        generalization.set_derived_class.assert_called_once_with(parent)
        generalization.set_base_class.assert_called_once_with(base)
        generalization.set_visibility.assert_called_once_with("public")
        generalization.set_is_virtual.assert_called_once_with(True)


class TestApplyRelationExtras:
    """UTS_XCH_00060: _apply_relation_extras wires source/target and properties."""

    def test_sets_source_target_and_properties(self) -> None:
        target = MagicMock()
        target.name = "OtherClass"
        project = MagicMock()
        project.get_nested_elements.return_value = [target]
        importer = _make_importer(project=project)
        relation = MagicMock()
        relation.name = "assoc1"
        parent = MagicMock()
        parent.name = "MyClass"

        importer._apply_relation_extras(
            relation,
            {
                "relation_type": "Association",
                "to": "OtherClass",
                "multiplicity": "0..*",
                "is_navigable": True,
                "role": "items",
                "visibility": "public",
            },
            parent,
        )

        assert relation.of_class == parent
        assert relation.other_class == target
        assert relation.relation_type == "Association"
        assert relation.multiplicity == "0..*"
        assert relation.is_navigable is True
        assert relation.relation_role_name == "items"
        relation.set_visibility.assert_called_once_with("public")

    def test_uses_from_override_when_provided(self) -> None:
        source = MagicMock()
        source.name = "ExplicitSource"
        target = MagicMock()
        target.name = "Target"
        project = MagicMock()
        project.get_nested_elements.return_value = [source, target]
        importer = _make_importer(project=project)
        relation = MagicMock()
        relation.name = "assoc1"
        parent = MagicMock()
        parent.name = "MyClass"

        importer._apply_relation_extras(
            relation,
            {"from": "ExplicitSource", "to": "Target"},
            parent,
        )

        assert relation.of_class == source

    def test_falls_back_to_parent_when_from_unresolvable(self) -> None:
        target = MagicMock()
        target.name = "Target"
        project = MagicMock()
        project.get_nested_elements.return_value = [target]
        importer = _make_importer(project=project)
        relation = MagicMock()
        relation.name = "assoc1"
        parent = MagicMock()
        parent.name = "MyClass"

        importer._apply_relation_extras(
            relation,
            {"from": "Missing", "to": "Target"},
            parent,
        )

        assert relation.of_class == parent


class TestApplyPortExtras:
    """UTS_XCH_00061: _apply_port_extras sets flags, contract, interfaces."""

    def test_sets_flags_and_contract(self) -> None:
        contract = MagicMock()
        contract.name = "IFoo"
        project = MagicMock()
        project.get_nested_elements.return_value = [contract]
        importer = _make_importer(project=project)
        port = MagicMock()
        port.name = "p1"

        importer._apply_port_extras(
            port,
            {
                "is_behavioral": True,
                "is_reversed": False,
                "contract": "IFoo",
            },
        )

        assert port.is_behavioral is True
        assert port.is_reversed is False
        assert port.port_contract is contract

    def test_adds_provided_and_required_interfaces(self) -> None:
        iface1 = MagicMock()
        iface1.name = "IFoo"
        iface2 = MagicMock()
        iface2.name = "IBar"
        project = MagicMock()
        project.get_nested_elements.return_value = [iface1, iface2]
        importer = _make_importer(project=project)
        port = MagicMock()
        port.name = "p1"

        importer._apply_port_extras(
            port,
            {"provided_interfaces": ["IFoo"], "required_interfaces": ["IBar"]},
        )

        port.add_provided_interface.assert_called_once_with(iface1)
        port.add_required_interface.assert_called_once_with(iface2)


class TestApplyEventExtras:
    """UTS_XCH_00062: _apply_event_extras sets base_event and super_event."""

    def test_sets_base_and_super_event(self) -> None:
        base = MagicMock()
        base.name = "BaseEvent"
        sup = MagicMock()
        sup.name = "SuperEvent"
        project = MagicMock()
        project.get_nested_elements.return_value = [base, sup]
        importer = _make_importer(project=project)
        event = MagicMock()
        event.name = "TickEvent"

        importer._apply_event_extras(
            event,
            {"base_event": "BaseEvent", "super_event": "SuperEvent"},
        )

        event.set_base_event.assert_called_once_with(base)
        event.set_super_event.assert_called_once_with(sup)


class TestApplyEventReceptionExtras:
    """UTS_XCH_00063: _apply_event_reception_extras sets event reference."""

    def test_sets_event_reference(self) -> None:
        evt = MagicMock()
        evt.name = "TickEvent"
        project = MagicMock()
        project.get_nested_elements.return_value = [evt]
        importer = _make_importer(project=project)
        reception = MagicMock()
        reception.name = "onTick"

        importer._apply_event_reception_extras(reception, {"event": "TickEvent"})

        reception.set_event.assert_called_once_with(evt)


class TestProcessElementNewTypes:
    """UTS_XCH_00064: _process_element dispatches the 6 new element types."""

    def test_dispatches_dependency(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_dep = MagicMock()
        new_dep.name = "dep1"
        parent.add_new_aggr.return_value = new_dep

        result = importer._process_element(parent, {"name": "dep1", "type": "Dependency"})

        parent.add_new_aggr.assert_called_once_with("Dependency", "dep1")
        assert result is not None
        assert result.name == "dep1"

    def test_dispatches_generalization(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_gen = MagicMock()
        new_gen.name = "gen1"
        parent.add_new_aggr.return_value = new_gen

        result = importer._process_element(parent, {"name": "gen1", "type": "Generalization"})

        parent.add_new_aggr.assert_called_once_with("Generalization", "gen1")
        assert result is not None
        assert result.name == "gen1"

    def test_dispatches_relation(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_rel = MagicMock()
        parent.add_new_aggr.return_value = new_rel

        importer._process_element(parent, {"name": "assoc1", "type": "Relation"})

        parent.add_new_aggr.assert_called_once_with("Relation", "assoc1")

    def test_dispatches_port(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_port = MagicMock()
        parent.add_new_aggr.return_value = new_port

        importer._process_element(parent, {"name": "p1", "type": "Port"})

        parent.add_new_aggr.assert_called_once_with("Port", "p1")

    def test_dispatches_event(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_evt = MagicMock()
        parent.add_new_aggr.return_value = new_evt

        importer._process_element(parent, {"name": "TickEvent", "type": "Event"})

        parent.add_new_aggr.assert_called_once_with("Event", "TickEvent")

    def test_dispatches_event_reception(self) -> None:
        importer = _make_importer()
        parent = MagicMock()
        parent.get_nested_elements.return_value = []
        new_rec = MagicMock()
        parent.add_new_aggr.return_value = new_rec

        importer._process_element(parent, {"name": "onTick", "type": "EventReception"})

        parent.add_new_aggr.assert_called_once_with("EventReception", "onTick")
