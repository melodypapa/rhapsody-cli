"""Tests for rhapsody_cli.elements.classifier.IRPClassifier."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPFlow, IRPFlowItem, IRPRelation, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute import IRPAttribute
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_classifier_is_a_unit() -> None:
    fake = make_fake_element("Class", properties={"name": "Widget"})
    classifier = IRPClassifier(fake)

    assert isinstance(classifier, IRPUnit)
    assert classifier.name == "Widget"


def test_classifier_add_attribute_wraps_result() -> None:
    fake = make_fake_element("Class")
    attr = make_fake_element("Attribute", properties={"name": "count"})
    fake.addAttribute.return_value = attr
    classifier = IRPClassifier(fake)

    result = classifier.add_attribute("count")

    fake.addAttribute.assert_called_once_with("count")
    assert result.name == "count"


def test_classifier_add_operation_wraps_result() -> None:
    fake = make_fake_element("Class")
    op = make_fake_element("Operation", properties={"name": "doIt"})
    fake.addOperation.return_value = op
    classifier = IRPClassifier(fake)

    result = classifier.add_operation("doIt")

    fake.addOperation.assert_called_once_with("doIt")
    assert result.name == "doIt"


def test_classifier_get_attributes_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.attributes = make_fake_collection([make_fake_element("Attribute", properties={"name": "count"})])
    classifier = IRPClassifier(fake)

    attributes = classifier.attributes

    assert len(attributes) == 1
    assert attributes[0].name == "count"


def test_classifier_get_operations_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.operations = make_fake_collection([make_fake_element("Operation", properties={"name": "doIt"})])
    classifier = IRPClassifier(fake)

    operations = classifier.operations

    assert len(operations) == 1
    assert operations[0].name == "doIt"


def test_classifier_add_generalization_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    base = make_fake_element("Class", properties={"name": "Base"})
    classifier = IRPClassifier(fake)

    classifier.add_generalization(IRPClassifier(base))

    fake.addGeneralization.assert_called_once_with(base)


def test_classifier_add_statechart_wraps_result() -> None:
    fake = make_fake_element("Class")
    statechart = make_fake_element("Statechart", properties={"name": "Behavior"})
    fake.addStatechart.return_value = statechart
    classifier = IRPClassifier(fake)

    result = classifier.add_statechart()

    fake.addStatechart.assert_called_once_with()
    assert result.name == "Behavior"


def test_classifier_add_activity_diagram_wraps_result() -> None:
    fake = make_fake_element("Class")
    diagram = make_fake_element("ActivityDiagram", properties={"name": "Act"})
    fake.addActivityDiagram.return_value = diagram
    classifier = IRPClassifier(fake)

    result = classifier.add_activity_diagram()

    fake.addActivityDiagram.assert_called_once_with()
    assert result.name == "Act"


def test_classifier_add_flow_items_wraps_result() -> None:
    fake = make_fake_element("Class")
    item = make_fake_element("FlowItem", properties={"name": "flowItem"})
    fake.addFlowItems.return_value = item
    classifier = IRPClassifier(fake)

    result = classifier.add_flow_items("flowItem")

    fake.addFlowItems.assert_called_once_with("flowItem")
    assert result.name == "flowItem"


def test_classifier_add_flows_wraps_result() -> None:
    fake = make_fake_element("Class")
    flow = make_fake_element("Flow", properties={"name": "flow"})
    fake.addFlows.return_value = flow
    classifier = IRPClassifier(fake)

    result = classifier.add_flows("flow")

    fake.addFlows.assert_called_once_with("flow")
    assert result.name == "flow"


def test_classifier_add_relation_wraps_result() -> None:
    fake = make_fake_element("Class")
    relation = make_fake_element("Relation", properties={"name": "assoc"})
    fake.addRelation.return_value = relation
    classifier = IRPClassifier(fake)

    result = classifier.add_relation("Other", "Pkg", "r1", "Association", "1", "r2", "Association", "*", "Link")

    fake.addRelation.assert_called_once_with("Other", "Pkg", "r1", "Association", "1", "r2", "Association", "*", "Link")
    assert result.name == "assoc"


def test_classifier_add_relation_to_unwraps_classifier_and_wraps_result() -> None:
    fake = make_fake_element("Class")
    other_fake = make_fake_element("Class", properties={"name": "Other"})
    relation = make_fake_element("Relation", properties={"name": "assoc"})
    fake.addRelationTo.return_value = relation
    classifier = IRPClassifier(fake)

    result = classifier.add_relation_to(IRPClassifier(other_fake), "r1", "Association", "1", "r2", "Association", "*", "Link")

    fake.addRelationTo.assert_called_once_with(other_fake, "r1", "Association", "1", "r2", "Association", "*", "Link")
    assert result.name == "assoc"


def test_classifier_add_unidirectional_relation_wraps_result() -> None:
    fake = make_fake_element("Class")
    relation = make_fake_element("Relation", properties={"name": "assoc"})
    fake.addUnidirectionalRelation.return_value = relation
    classifier = IRPClassifier(fake)

    result = classifier.add_unidirectional_relation("Other", "Pkg", "r1", "Association", "1", "Link")

    fake.addUnidirectionalRelation.assert_called_once_with("Other", "Pkg", "r1", "Association", "1", "Link")
    assert result.name == "assoc"


def test_classifier_add_unidirectional_relation_to_unwraps_classifier_and_wraps_result() -> None:
    fake = make_fake_element("Class")
    other_fake = make_fake_element("Class", properties={"name": "Other"})
    relation = make_fake_element("Relation", properties={"name": "assoc"})
    fake.addUnidirectionalRelationTo.return_value = relation
    classifier = IRPClassifier(fake)

    result = classifier.add_unidirectional_relation_to(IRPClassifier(other_fake), "r1", "Association", "1", "Link")

    fake.addUnidirectionalRelationTo.assert_called_once_with(other_fake, "r1", "Association", "1", "Link")
    assert result.name == "assoc"


def test_classifier_delete_attribute_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    attr_fake = make_fake_element("Attribute", properties={"name": "count"})
    classifier = IRPClassifier(fake)

    classifier.delete_attribute(cast(IRPAttribute, IRPModelElement(attr_fake)))

    fake.deleteAttribute.assert_called_once_with(attr_fake)


def test_classifier_delete_flow_items_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    item_fake = make_fake_element("FlowItem", properties={"name": "flowItem"})
    classifier = IRPClassifier(fake)

    classifier.delete_flow_items(cast(IRPFlowItem, IRPModelElement(item_fake)))

    fake.deleteFlowItems.assert_called_once_with(item_fake)


def test_classifier_delete_flows_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    flow_fake = make_fake_element("Flow", properties={"name": "flow"})
    classifier = IRPClassifier(fake)

    classifier.delete_flows(cast(IRPFlow, IRPModelElement(flow_fake)))

    fake.deleteFlows.assert_called_once_with(flow_fake)


def test_classifier_delete_generalization_unwraps_classifier() -> None:
    fake = make_fake_element("Class")
    base_fake = make_fake_element("Class", properties={"name": "Base"})
    classifier = IRPClassifier(fake)

    classifier.delete_generalization(IRPClassifier(base_fake))

    fake.deleteGeneralization.assert_called_once_with(base_fake)


def test_classifier_delete_operation_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    op_fake = make_fake_element("Operation", properties={"name": "doIt"})
    classifier = IRPClassifier(fake)

    classifier.delete_operation(cast(IRPOperation, IRPModelElement(op_fake)))

    fake.deleteOperation.assert_called_once_with(op_fake)


def test_classifier_delete_relation_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    rel_fake = make_fake_element("Relation", properties={"name": "assoc"})
    classifier = IRPClassifier(fake)

    classifier.delete_relation(cast(IRPRelation, IRPModelElement(rel_fake)))

    fake.deleteRelation.assert_called_once_with(rel_fake)


def test_classifier_find_attribute_wraps_result() -> None:
    fake = make_fake_element("Class")
    attr = make_fake_element("Attribute", properties={"name": "count"})
    fake.findAttribute.return_value = attr
    classifier = IRPClassifier(fake)

    result = classifier.find_attribute("count")

    fake.findAttribute.assert_called_once_with("count")
    assert result.name == "count"


def test_classifier_find_base_classifier_wraps_result() -> None:
    fake = make_fake_element("Class")
    base = make_fake_element("Class", properties={"name": "Base"})
    fake.findBaseClassifier.return_value = base
    classifier = IRPClassifier(fake)

    result = classifier.find_base_classifier("Base")

    fake.findBaseClassifier.assert_called_once_with("Base")
    assert result.name == "Base"


def test_classifier_find_derived_classifier_wraps_result() -> None:
    fake = make_fake_element("Class")
    derived = make_fake_element("Class", properties={"name": "Derived"})
    fake.findDerivedClassifier.return_value = derived
    classifier = IRPClassifier(fake)

    result = classifier.find_derived_classifier("Derived")

    fake.findDerivedClassifier.assert_called_once_with("Derived")
    assert result.name == "Derived"


def test_classifier_find_generalization_wraps_result() -> None:
    fake = make_fake_element("Class")
    gen = make_fake_element("Generalization", properties={"name": "gen"})
    fake.findGeneralization.return_value = gen
    classifier = IRPClassifier(fake)

    result = classifier.find_generalization("Base")

    fake.findGeneralization.assert_called_once_with("Base")
    assert result.name == "gen"


def test_classifier_find_interface_item_wraps_result() -> None:
    fake = make_fake_element("Class")
    item = make_fake_element("Operation", properties={"name": "doIt"})
    fake.findInterfaceItem.return_value = item
    classifier = IRPClassifier(fake)

    result = classifier.find_interface_item("doIt()")

    fake.findInterfaceItem.assert_called_once_with("doIt()")
    assert result.name == "doIt"


def test_classifier_find_nested_classifier_wraps_result() -> None:
    fake = make_fake_element("Class")
    nested = make_fake_element("Class", properties={"name": "Nested"})
    fake.findNestedClassifier.return_value = nested
    classifier = IRPClassifier(fake)

    result = classifier.find_nested_classifier("Nested")

    fake.findNestedClassifier.assert_called_once_with("Nested")
    assert result.name == "Nested"


def test_classifier_find_nested_classifier_recursive_wraps_result() -> None:
    fake = make_fake_element("Class")
    nested = make_fake_element("Class", properties={"name": "Nested"})
    fake.findNestedClassifierRecursive.return_value = nested
    classifier = IRPClassifier(fake)

    result = classifier.find_nested_classifier_recursive("Nested")

    fake.findNestedClassifierRecursive.assert_called_once_with("Nested")
    assert result is not None and result.name == "Nested"


def test_classifier_find_relation_wraps_result() -> None:
    fake = make_fake_element("Class")
    rel = make_fake_element("Relation", properties={"name": "assoc"})
    fake.findRelation.return_value = rel
    classifier = IRPClassifier(fake)

    result = classifier.find_relation("assoc")

    fake.findRelation.assert_called_once_with("assoc")
    assert result.name == "assoc"


def test_classifier_find_trigger_wraps_result() -> None:
    fake = make_fake_element("Class")
    trigger = make_fake_element("Trigger", properties={"name": "trig"})
    fake.findTrigger.return_value = trigger
    classifier = IRPClassifier(fake)

    result = classifier.find_trigger("trig")

    fake.findTrigger.assert_called_once_with("trig")
    assert result.name == "trig"


def test_classifier_get_activity_diagram_wraps_result() -> None:
    fake = make_fake_element("Class")
    diagram = make_fake_element("ActivityDiagram", properties={"name": "Act"})
    fake.activityDiagram = diagram
    classifier = IRPClassifier(fake)

    result = classifier.activity_diagram
    assert result.name == "Act"


def test_classifier_get_statechart_wraps_result() -> None:
    fake = make_fake_element("Class")
    statechart = make_fake_element("Statechart", properties={"name": "Behavior"})
    fake.statechart = statechart
    classifier = IRPClassifier(fake)

    result = classifier.statechart
    assert result.name == "Behavior"


def test_classifier_get_attributes_including_bases_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.getAttributesIncludingBases.return_value = make_fake_collection([make_fake_element("Attribute", properties={"name": "count"})])
    classifier = IRPClassifier(fake)

    result = classifier.get_attributes_including_bases()

    assert len(result) == 1
    assert result[0].name == "count"


def test_classifier_get_base_classifiers_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.baseClassifiers = make_fake_collection([make_fake_element("Class", properties={"name": "Base"})])
    classifier = IRPClassifier(fake)

    result = classifier.base_classifiers

    assert len(result) == 1
    assert result[0].name == "Base"


def test_classifier_get_behavioral_diagrams_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.behavioralDiagrams = make_fake_collection([make_fake_element("Statechart", properties={"name": "Behavior"})])
    classifier = IRPClassifier(fake)

    result = classifier.behavioral_diagrams

    assert len(result) == 1
    assert result[0].name == "Behavior"


def test_classifier_get_derived_classifiers_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.derivedClassifiers = make_fake_collection([make_fake_element("Class", properties={"name": "Derived"})])
    classifier = IRPClassifier(fake)

    result = classifier.derived_classifiers

    assert len(result) == 1
    assert result[0].name == "Derived"


def test_classifier_get_flow_items_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.flowItems = make_fake_collection([make_fake_element("FlowItem", properties={"name": "flowItem"})])
    classifier = IRPClassifier(fake)

    result = classifier.flow_items

    assert len(result) == 1
    assert result[0].name == "flowItem"


def test_classifier_get_flows_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.flows = make_fake_collection([make_fake_element("Flow", properties={"name": "flow"})])
    classifier = IRPClassifier(fake)

    result = classifier.flows

    assert len(result) == 1
    assert result[0].name == "flow"


def test_classifier_get_generalizations_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.generalizations = make_fake_collection([make_fake_element("Generalization", properties={"name": "gen"})])
    classifier = IRPClassifier(fake)

    result = classifier.generalizations

    assert len(result) == 1
    assert result[0].name == "gen"


def test_classifier_get_interface_items_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.interfaceItems = make_fake_collection([make_fake_element("Operation", properties={"name": "doIt"})])
    classifier = IRPClassifier(fake)

    result = classifier.interface_items

    assert len(result) == 1
    assert result[0].name == "doIt"


def test_classifier_get_interface_items_including_bases_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.getInterfaceItemsIncludingBases.return_value = make_fake_collection([make_fake_element("Operation", properties={"name": "doIt"})])
    classifier = IRPClassifier(fake)

    result = classifier.get_interface_items_including_bases()

    assert len(result) == 1
    assert result[0].name == "doIt"


def test_classifier_get_links_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.links = make_fake_collection([make_fake_element("Link", properties={"name": "link"})])
    classifier = IRPClassifier(fake)

    result = classifier.links

    assert len(result) == 1
    assert result[0].name == "link"


def test_classifier_get_nested_classifiers_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.nestedClassifiers = make_fake_collection([make_fake_element("Class", properties={"name": "Nested"})])
    classifier = IRPClassifier(fake)

    result = classifier.nested_classifiers

    assert len(result) == 1
    assert result[0].name == "Nested"


def test_classifier_get_ports_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.ports = make_fake_collection([make_fake_element("Port", properties={"name": "port"})])
    classifier = IRPClassifier(fake)

    result = classifier.ports

    assert len(result) == 1
    assert result[0].name == "port"


def test_classifier_get_relations_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.relations = make_fake_collection([make_fake_element("Relation", properties={"name": "assoc"})])
    classifier = IRPClassifier(fake)

    result = classifier.relations

    assert len(result) == 1
    assert result[0].name == "assoc"


def test_classifier_get_relations_including_bases_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.getRelationsIncludingBases.return_value = make_fake_collection([make_fake_element("Relation", properties={"name": "assoc"})])
    classifier = IRPClassifier(fake)

    result = classifier.get_relations_including_bases()

    assert len(result) == 1
    assert result[0].name == "assoc"


def test_classifier_get_sequence_diagrams_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.sequenceDiagrams = make_fake_collection([make_fake_element("SequenceDiagram", properties={"name": "seq"})])
    classifier = IRPClassifier(fake)

    result = classifier.sequence_diagrams

    assert len(result) == 1
    assert result[0].name == "seq"


def test_classifier_get_source_artifacts_returns_collection() -> None:
    fake = make_fake_element("Class")
    fake.sourceArtifacts = make_fake_collection([make_fake_element("File", properties={"name": "file"})])
    classifier = IRPClassifier(fake)

    result = classifier.source_artifacts

    assert len(result) == 1
    assert result[0].name == "file"
