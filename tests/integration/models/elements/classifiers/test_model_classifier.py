"""Integration tests for RPClassifier with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import uuid
from typing import cast

import pytest

from rhapsody_cli.models.elements.classifiers import RPClass, RPClassifier
from rhapsody_cli.models.elements.containment import RPPackage, RPProject


@pytest.mark.integration
class TestRPClassifierIntegration:
    """Integration tests for RPClassifier with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: RPProject, name: str) -> RPPackage:
        pkg = project.add_package(name)
        assert pkg is not None and isinstance(pkg, RPPackage)
        return pkg

    def test_find_attribute_and_delete_attribute(self, test_project: RPProject) -> None:
        pkg_name = self._unique("AttrPkg")
        class_name = self._unique("AttrCls")
        attr_name = self._unique("myAttr")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            attribute = classifier.add_attribute(attr_name)
            found = classifier.find_attribute(attr_name)
            assert found is not None
            assert found.get_name() == attr_name
            classifier.delete_attribute(attribute)
            attrs_after = [a.get_name() for a in classifier.get_attributes()]
            assert attr_name not in attrs_after
        finally:
            classifier.delete_from_project()

    def test_find_interface_item(self, test_project: RPProject) -> None:
        pkg_name = self._unique("IfPkg")
        class_name = self._unique("IfCls")
        op_name = self._unique("myOp")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            op = classifier.add_operation(op_name)
            assert op is not None
            found = classifier.find_interface_item(f"{op_name}()")
            assert found is not None
            assert found.get_name() == op_name
        finally:
            classifier.delete_from_project()

    def test_add_port_and_get_ports(self, test_project: RPProject) -> None:
        pkg_name = self._unique("PortPkg")
        class_name = self._unique("PortCls")
        port_name = self._unique("myPort")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            port = classifier.add_port(port_name)
            assert port is not None
            ports = list(classifier.get_ports())
            assert port in ports
        finally:
            classifier.delete_from_project()

    def test_get_source_artifacts_empty(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SrcArtPkg")
        class_name = self._unique("SrcArtCls")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            artifacts = list(classifier.get_source_artifacts())
            assert artifacts == []
        finally:
            classifier.delete_from_project()

    def test_get_sequence_diagrams_empty(self, test_project: RPProject) -> None:
        pkg_name = self._unique("SeqDiagPkg")
        class_name = self._unique("SeqDiagCls")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            diagrams = list(classifier.get_sequence_diagrams())
            assert diagrams == []
        finally:
            classifier.delete_from_project()

    def test_get_links_empty(self, test_project: RPProject) -> None:
        pkg_name = self._unique("LinksPkg")
        class_name = self._unique("LinksCls")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            links = list(classifier.get_links())
            assert links == []
        finally:
            classifier.delete_from_project()

    def test_delete_operation(self, test_project: RPProject) -> None:
        pkg_name = self._unique("DelOpPkg")
        class_name = self._unique("DelOpCls")
        op_name = self._unique("toBeDeleted")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            op = classifier.add_operation(op_name)
            assert op is not None
            ops = list(classifier.get_operations())
            assert op in ops
            classifier.delete_operation(op)
            ops_after = list(classifier.get_operations())
            assert op not in ops_after
        finally:
            classifier.delete_from_project()

    def test_get_interface_items(self, test_project: RPProject) -> None:
        pkg_name = self._unique("IfItemsPkg")
        class_name = self._unique("IfItemsCls")
        op_name = self._unique("ifItemOp")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            op = classifier.add_operation(op_name)
            items = list(classifier.get_interface_items())
            assert op in items
            inherited = list(classifier.get_interface_items_including_bases())
            assert len(inherited) >= len(items)
        finally:
            classifier.delete_from_project()

    def test_add_relation_to_and_find_and_delete(self, test_project: RPProject) -> None:
        pkg_name = self._unique("RelPkg")
        class_a_name = self._unique("ClsA")
        class_b_name = self._unique("ClsB")
        role1 = self._unique("roleA")
        role2 = self._unique("roleB")
        pkg = self._create_package(test_project, pkg_name)
        class_a = pkg.add_class(class_a_name)
        class_b = pkg.add_class(class_b_name)
        try:
            relation = class_a.add_relation_to(class_b, role1, "Association", "1", role2, "Association", "1", "")
            assert relation is not None
            found = class_a.find_relation(relation.get_name())
            assert found is not None
            relations = list(class_a.get_relations())
            assert relation in relations
            class_a.delete_relation(relation)
            relations_after = list(class_a.get_relations())
            assert relation not in relations_after
        finally:
            class_a.delete_from_project()
            class_b.delete_from_project()

    def test_add_relation_by_name(self, test_project: RPProject) -> None:
        pkg_name = self._unique("RelNmPkg")
        class_a_name = self._unique("ClsANm")
        class_b_name = self._unique("ClsBNm")
        role = self._unique("roleA")
        pkg = self._create_package(test_project, pkg_name)
        class_a = pkg.add_class(class_a_name)
        class_b = pkg.add_class(class_b_name)
        try:
            relation = class_a.add_relation(class_b_name, pkg_name, role, "Association", "1", role, "Association", "1", "")
            assert relation is not None
            relations = list(class_a.get_relations())
            assert relation in relations
        finally:
            class_a.delete_from_project()
            class_b.delete_from_project()

    def test_add_unidirectional_relation_to(self, test_project: RPProject) -> None:
        pkg_name = self._unique("UniRelPkg")
        class_a_name = self._unique("ClsAUni")
        class_b_name = self._unique("ClsBUni")
        role = self._unique("target")
        pkg = self._create_package(test_project, pkg_name)
        class_a = pkg.add_class(class_a_name)
        class_b = pkg.add_class(class_b_name)
        try:
            relation = class_a.add_unidirectional_relation_to(class_b, role, "Association", "1", "")
            assert relation is not None
            relations = list(class_a.get_relations())
            assert relation in relations
        finally:
            class_a.delete_from_project()
            class_b.delete_from_project()

    def test_add_unidirectional_relation_by_name(self, test_project: RPProject) -> None:
        pkg_name = self._unique("UniNmPkg")
        class_a_name = self._unique("ClsAUniNm")
        class_b_name = self._unique("ClsBUniNm")
        role = self._unique("target")
        pkg = self._create_package(test_project, pkg_name)
        class_a = pkg.add_class(class_a_name)
        class_b = pkg.add_class(class_b_name)
        try:
            relation = class_a.add_unidirectional_relation(class_b_name, pkg_name, role, "Association", "1", "")
            assert relation is not None
            relations = list(class_a.get_relations())
            assert relation in relations
        finally:
            class_a.delete_from_project()
            class_b.delete_from_project()

    def test_generalization_hierarchy(self, test_project: RPProject) -> None:
        pkg_name = self._unique("GenPkg")
        base_name = self._unique("BaseCls")
        derived_name = self._unique("DerivedCls")
        pkg = self._create_package(test_project, pkg_name)
        base = pkg.add_class(base_name)
        derived = pkg.add_class(derived_name)
        try:
            derived.add_generalization(base)
            base_classifiers = list(derived.get_base_classifiers())
            assert base in base_classifiers
            derived_classifiers = list(base.get_derived_classifiers())
            assert derived in derived_classifiers
            found_base = derived.find_base_classifier(base_name)
            assert found_base is not None and found_base.get_name() == base_name
            found_derived = base.find_derived_classifier(derived_name)
            assert found_derived is not None and found_derived.get_name() == derived_name
            generalizations = list(derived.get_generalizations())
            assert len(generalizations) >= 1
            derived.delete_generalization(base)
            base_classifiers_after = list(derived.get_base_classifiers())
            assert base not in base_classifiers_after
        finally:
            derived.delete_from_project()
            base.delete_from_project()

    def test_get_relations_including_bases(self, test_project: RPProject) -> None:
        pkg_name = self._unique("RelIncPkg")
        base_name = self._unique("BaseClsRel")
        derived_name = self._unique("DerClsRel")
        other_name = self._unique("OtherCls")
        role = self._unique("relRole")
        pkg = self._create_package(test_project, pkg_name)
        base = pkg.add_class(base_name)
        derived = pkg.add_class(derived_name)
        other = pkg.add_class(other_name)
        try:
            derived.add_generalization(base)
            rel = base.add_unidirectional_relation_to(other, role, "Association", "1", "")
            derived_rels = list(derived.get_relations())
            assert rel not in derived_rels
            derived_rels_incl = list(derived.get_relations_including_bases())
            assert rel in derived_rels_incl
        finally:
            derived.delete_from_project()
            base.delete_from_project()
            other.delete_from_project()

    def test_add_activity_diagram_and_get_behavioral_diagrams(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ActDiagPkg")
        class_name = self._unique("ActDiagCls")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            activity_diagram = classifier.add_activity_diagram()
            assert activity_diagram is not None
            fetched = classifier.get_activity_diagram()
            assert fetched is not None
            behavioral = list(classifier.get_behavioral_diagrams())
            assert len(behavioral) >= 1
        finally:
            classifier.delete_from_project()

    def test_get_statechart(self, test_project: RPProject) -> None:
        pkg_name = self._unique("ScPkg")
        class_name = self._unique("ScCls")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            sc = classifier.add_statechart()
            assert sc is not None
            fetched = classifier.get_statechart()
            assert fetched is not None
            assert fetched.get_name() == sc.get_name()
        finally:
            classifier.delete_from_project()

    def test_add_flow_items_and_delete(self, test_project: RPProject) -> None:
        pkg_name = self._unique("FlowItPkg")
        class_name = self._unique("FlowItCls")
        flow_item_name = self._unique("myFlowItem")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            flow_item = classifier.add_flow_items(flow_item_name)
            assert flow_item is not None
            items = list(classifier.get_flow_items())
            assert flow_item in items
            classifier.delete_flow_items(flow_item)
            items_after = list(classifier.get_flow_items())
            assert flow_item not in items_after
        finally:
            classifier.delete_from_project()

    def test_add_flows_and_delete(self, test_project: RPProject) -> None:
        pkg_name = self._unique("FlowPkg")
        class_name = self._unique("FlowCls")
        flow_name = self._unique("myFlow")
        pkg = self._create_package(test_project, pkg_name)
        classifier: RPClassifier = pkg.add_class(class_name)
        try:
            flow = classifier.add_flows(flow_name)
            assert flow is not None
            flows = list(classifier.get_flows())
            assert flow in flows
            classifier.delete_flows(flow)
            flows_after = list(classifier.get_flows())
            assert flow not in flows_after
        finally:
            classifier.delete_from_project()

    def test_nested_classifiers_and_find(self, test_project: RPProject) -> None:
        pkg_name = self._unique("NestPkg")
        outer_name = self._unique("OuterCls")
        inner_name = self._unique("InnerCls")
        deep_name = self._unique("DeepCls")
        pkg = self._create_package(test_project, pkg_name)
        outer: RPClassifier = pkg.add_class(outer_name)
        try:
            inner = cast(RPClass, outer).add_class(inner_name)
            assert inner is not None
            nested = list(outer.get_nested_classifiers())
            assert inner in nested
            found = outer.find_nested_classifier(inner_name)
            assert found is not None and found.get_name() == inner_name
            deep = cast(RPClass, inner).add_class(deep_name)
            assert deep is not None
            found_deep = outer.find_nested_classifier_recursive(deep_name)
            assert found_deep is not None and found_deep.get_name() == deep_name
        finally:
            outer.delete_from_project()
