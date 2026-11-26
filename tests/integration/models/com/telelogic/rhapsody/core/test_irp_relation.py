import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPRelation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPRelationIntegration:
    """Integration tests for IRPRelation's own members with a live association."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_association(test_project: IRPProject, pkg_name: str, link_name: str) -> tuple[IRPPackage, IRPClass, IRPClass, IRPRelation]:
        pkg = test_project.add_package(pkg_name)
        source = pkg.add_class(TestIRPRelationIntegration._unique("RelSrc"))
        target = pkg.add_class(TestIRPRelationIntegration._unique("RelTgt"))
        end1 = IRPRelation(source.add_relation_to(target, "targets", "Association", "1", "sources", "Association", "1", link_name)._com)
        return pkg, source, target, end1

    def test_relation_type(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            assert end1.relation_type == "Association"
        finally:
            pkg.delete_from_project()

    def test_relation_role_name(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            assert end1.relation_role_name == "targets"
        finally:
            pkg.delete_from_project()

    def test_relation_link_name(self, test_project: IRPProject) -> None:
        link_name = self._unique("Link")
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), link_name)
        try:
            assert end1.relation_link_name == link_name
        finally:
            pkg.delete_from_project()

    def test_of_class(self, test_project: IRPProject) -> None:
        pkg, source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            assert end1.of_class is not None and end1.of_class.name == source.name
        finally:
            pkg.delete_from_project()

    def test_other_class(self, test_project: IRPProject) -> None:
        pkg, _source, target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            assert end1.other_class is not None and end1.other_class.name == target.name
        finally:
            pkg.delete_from_project()

    def test_inverse(self, test_project: IRPProject) -> None:
        pkg, _source, target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            inverse = end1.inverse
            assert isinstance(inverse, IRPRelation)
            assert inverse.relation_role_name == "sources"
            assert inverse.of_class is not None and inverse.of_class.name == target.name
        finally:
            pkg.delete_from_project()

    def test_is_symmetric(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            assert end1.is_symmetric is True
        finally:
            pkg.delete_from_project()

    def test_visibility(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            assert end1.visibility == "Protected"
        finally:
            pkg.delete_from_project()

    def test_is_typeless_object_is_false_for_a_typed_association_end(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            assert end1.is_typeless_object() is False
        finally:
            pkg.delete_from_project()

    def test_multiplicity(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            end1.multiplicity = "0..*"
            assert end1.multiplicity == "0..*"
        finally:
            pkg.delete_from_project()

    def test_is_navigable(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            end1.is_navigable = False
            assert end1.is_navigable is False
            end1.is_navigable = True
            assert end1.is_navigable is True
        finally:
            pkg.delete_from_project()

    def test_relation_label(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            end1.relation_label = "owns"
            assert end1.relation_label == "owns"
        finally:
            pkg.delete_from_project()

    def test_add_qualifier_is_listed_by_get_qualifiers_and_removed(self, test_project: IRPProject) -> None:
        pkg, source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            qualifier = source.add_attribute(self._unique("Key"))
            end1.add_qualifier(qualifier)
            assert qualifier.name in [element.name for element in end1.get_qualifiers()]
            end1.remove_qualifier(qualifier)
            assert len(end1.get_qualifiers()) == 0
        finally:
            pkg.delete_from_project()

    def test_qualifier_type_round_trips_through_the_setter(self, test_project: IRPProject) -> None:
        pkg, _source, target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            end1.set_qualifier_type(target)
            qualifier_type = end1.get_qualifier_type()
            assert qualifier_type is not None and qualifier_type.name == target.name
        finally:
            pkg.delete_from_project()

    def test_make_unidirect_returns_none(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            assert end1.make_unidirect() is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_set_inverse_updates_the_inverse_role_name(self, test_project: IRPProject) -> None:
        pkg, _source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            end1.set_inverse("renamedRole", "Association")
            inverse = end1.inverse
            assert inverse is not None and inverse.relation_role_name == "renamedRole"
        finally:
            pkg.delete_from_project()

    def test_get_association_class_returns_the_linked_association_class(self, test_project: IRPProject) -> None:
        pkg, source, _target, end1 = self._create_association(test_project, self._unique("RelPkg"), self._unique("Link"))
        try:
            inverse = end1.inverse
            assert inverse is not None
            assoc_name = self._unique("AssocCls")
            source.add_association(end1, inverse, assoc_name)
            association_class = end1.get_association_class()
            assert association_class is not None and association_class.name == assoc_name
        finally:
            pkg.delete_from_project()
