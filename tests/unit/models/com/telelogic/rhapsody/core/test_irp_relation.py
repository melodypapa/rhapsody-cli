"""Tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPRelation."""

from typing import cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPRelation, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_relation_is_a_unit() -> None:
    fake = make_fake_element("Relation", properties={"name": "assoc1"})
    relation = IRPRelation(fake)

    assert isinstance(relation, IRPUnit)
    assert relation.name == "assoc1"


def test_relation_add_qualifier_delegates_to_com() -> None:
    fake = make_fake_element("Relation")
    qualifier = make_fake_element("Class", properties={"name": "Key"})
    relation = IRPRelation(fake)

    relation.add_qualifier(cast(IRPModelElement, IRPModelElement.wrap(qualifier)))

    fake.addQualifier.assert_called_once_with(qualifier)


def test_relation_get_association_class_wraps_result() -> None:
    fake = make_fake_element("Relation")
    assoc_class = make_fake_element("AssociationClass", properties={"name": "LinkClass"})
    fake.getAssociationClass.return_value = assoc_class
    relation = IRPRelation(fake)

    result = relation.get_association_class()
    assert result is not None
    assert result.name == "LinkClass"


def test_relation_get_association_class_is_none_without_association_class() -> None:
    fake = make_fake_element("Relation")
    fake.getAssociationClass.return_value = None
    relation = IRPRelation(fake)

    assert relation.get_association_class() is None


def test_relation_inverse_property_returns_relation_even_for_association_end_metaclass() -> None:
    inverse = make_fake_element("AssociationEnd", properties={"name": "inverseAssoc"})
    fake = make_fake_element("AssociationEnd", properties={"inverse": inverse})
    relation = IRPRelation(fake)

    result = relation.inverse

    assert isinstance(result, IRPRelation)
    assert result.name == "inverseAssoc"


def test_relation_inverse_property_is_none_without_inverse() -> None:
    fake = make_fake_element("Relation", properties={"inverse": None})
    relation = IRPRelation(fake)

    assert relation.inverse is None


def test_relation_is_navigable_property_reads_bool() -> None:
    fake = make_fake_element("Relation", properties={"isNavigable": 1})
    relation = IRPRelation(fake)

    assert relation.is_navigable is True


def test_relation_is_navigable_property_writes_com_flag() -> None:
    fake = make_fake_element("Relation", properties={"isNavigable": 0})
    relation = IRPRelation(fake)

    relation.is_navigable = True

    assert fake.isNavigable == 1
    fake.setIsNavigable.assert_not_called()


def test_relation_is_symmetric_property_reads_bool() -> None:
    fake = make_fake_element("Relation", properties={"isSymmetric": 0})
    relation = IRPRelation(fake)

    assert relation.is_symmetric is False


def test_relation_multiplicity_property_round_trips() -> None:
    fake = make_fake_element("Relation", properties={"multiplicity": "0..*"})
    relation = IRPRelation(fake)

    assert relation.multiplicity == "0..*"
    relation.multiplicity = "1"

    assert fake.multiplicity == "1"
    fake.setMultiplicity.assert_not_called()


def test_relation_object_as_object_type_property_wraps_result() -> None:
    klass = make_fake_element("Class", properties={"name": "Widget"})
    fake = make_fake_element("Relation", properties={"ObjectAsObjectType": klass})
    relation = IRPRelation(fake)

    result = relation.object_as_object_type

    assert result.name == "Widget"
    fake.getObjectAsObjectType.assert_not_called()


def test_relation_of_class_property_wraps_result_and_writes_com_object() -> None:
    klass_fake = make_fake_element("Class", properties={"name": "Widget"})
    fake = make_fake_element("Relation", properties={"ofClass": klass_fake})
    relation = IRPRelation(fake)

    assert relation.of_class.name == "Widget"
    relation.of_class = IRPClassifier(klass_fake)

    assert fake.ofClass is klass_fake
    fake.setOfClass.assert_not_called()


def test_relation_other_class_property_wraps_result_and_writes_com_object() -> None:
    klass_fake = make_fake_element("Class", properties={"name": "Other"})
    fake = make_fake_element("Relation", properties={"otherClass": klass_fake})
    relation = IRPRelation(fake)

    assert relation.other_class.name == "Other"
    relation.other_class = IRPClassifier(klass_fake)

    assert fake.otherClass is klass_fake
    fake.setOtherClass.assert_not_called()


def test_relation_qualifier_property_round_trips() -> None:
    fake = make_fake_element("Relation", properties={"qualifier": "key"})
    relation = IRPRelation(fake)

    assert relation.qualifier == "key"
    relation.qualifier = "other"

    assert fake.qualifier == "other"
    fake.setQualifier.assert_not_called()


def test_relation_get_qualifiers_returns_collection() -> None:
    inner = make_fake_element("Class", properties={"name": "Key"})
    fake = make_fake_element("Relation")
    fake.getQualifiers.return_value = make_fake_collection([inner])
    relation = IRPRelation(fake)

    result = relation.get_qualifiers()

    assert isinstance(result, IRPCollection)
    assert len(result) == 1


def test_relation_get_qualifier_type_wraps_result() -> None:
    fake = make_fake_element("Relation")
    klass = make_fake_element("Class", properties={"name": "KeyType"})
    fake.getQualifierType.return_value = klass
    relation = IRPRelation(fake)

    result = relation.get_qualifier_type()
    assert result.name == "KeyType"


def test_relation_relation_label_property_round_trips() -> None:
    fake = make_fake_element("Relation", properties={"relationLabel": "owns"})
    relation = IRPRelation(fake)

    assert relation.relation_label == "owns"
    relation.relation_label = "contains"

    assert fake.relationLabel == "contains"
    fake.setRelationLabel.assert_not_called()


def test_relation_relation_link_name_property_round_trips() -> None:
    fake = make_fake_element("Relation", properties={"relationLinkName": "Ownership"})
    relation = IRPRelation(fake)

    assert relation.relation_link_name == "Ownership"
    relation.relation_link_name = "Link2"

    assert fake.relationLinkName == "Link2"
    fake.setRelationLinkName.assert_not_called()


def test_relation_relation_role_name_property_round_trips() -> None:
    fake = make_fake_element("Relation", properties={"relationRoleName": "owner"})
    relation = IRPRelation(fake)

    assert relation.relation_role_name == "owner"
    relation.relation_role_name = "items"

    assert fake.relationRoleName == "items"
    fake.setRelationRoleName.assert_not_called()


def test_relation_relation_type_property_round_trips() -> None:
    fake = make_fake_element("Relation", properties={"relationType": "Association"})
    relation = IRPRelation(fake)

    assert relation.relation_type == "Association"
    relation.relation_type = "Aggregation"

    assert fake.relationType == "Aggregation"
    fake.setRelationType.assert_not_called()


def test_relation_visibility_property_reads_string() -> None:
    fake = make_fake_element("Relation", properties={"visibility": "public"})
    relation = IRPRelation(fake)

    assert relation.visibility == "public"


def test_relation_is_typeless_object_delegates_to_com() -> None:
    fake = make_fake_element("Relation", isTypelessObject=1)
    relation = IRPRelation(fake)

    assert relation.is_typeless_object() is True


def test_relation_make_unidirect_delegates_to_com() -> None:
    fake = make_fake_element("Relation")
    relation = IRPRelation(fake)

    relation.make_unidirect()

    fake.makeUnidirect.assert_called_once_with()


def test_relation_remove_qualifier_delegates_to_com() -> None:
    fake = make_fake_element("Relation")
    qualifier = make_fake_element("Class", properties={"name": "Key"})
    relation = IRPRelation(fake)

    relation.remove_qualifier(cast(IRPModelElement, IRPModelElement.wrap(qualifier)))

    fake.removeQualifier.assert_called_once_with(qualifier)


def test_relation_set_inverse_delegates_to_com() -> None:
    fake = make_fake_element("Relation")
    relation = IRPRelation(fake)

    relation.set_inverse("owner", "Association")

    fake.setInverse.assert_called_once_with("owner", "Association")


def test_relation_set_qualifier_type_delegates_to_com() -> None:
    fake = make_fake_element("Relation")
    klass_fake = make_fake_element("Class", properties={"name": "KeyType"})
    relation = IRPRelation(fake)

    relation.set_qualifier_type(cast(IRPClassifier, IRPModelElement.wrap(klass_fake)))

    fake.setQualifierType.assert_called_once_with(klass_fake)


def test_relation_legacy_accessor_methods_are_removed() -> None:
    relation = IRPRelation(make_fake_element("Relation"))

    legacy_names = (
        "get_inverse",
        "get_is_navigable",
        "set_is_navigable",
        "get_multiplicity",
        "set_multiplicity",
        "get_visibility",
        "get_of_class",
        "set_of_class",
        "get_relation_type",
        "set_relation_type",
    )
    for legacy in legacy_names:
        assert not hasattr(relation, legacy), legacy
