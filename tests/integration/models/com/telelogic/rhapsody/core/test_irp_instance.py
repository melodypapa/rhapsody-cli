"""Integration tests for IRPInstance's own members with a live instance.

``add_new_aggr`` is an IRPModelElement method used only to build the fixture;
every assertion below targets an IRPInstance-owned member. ``add_link``-based
fixtures live in test_irp_package.py; here the link is asserted through the
instance-side ``get_in_links``/``get_out_links`` members.
"""

import uuid

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPInstance, IRPRelation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class import IRPClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject


@pytest.mark.integration
class TestIRPInstanceIntegration:
    """Integration tests for IRPInstance's own members with a live instance."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_instance(test_project: IRPProject, pkg_name: str, cls_name: str, inst_name: str) -> tuple[IRPPackage, IRPClass, IRPInstance]:
        pkg = test_project.add_package(pkg_name)
        cls = pkg.add_class(cls_name)
        object_element = pkg.add_global_object(inst_name, cls.name, pkg.name)
        instance = IRPInstance(object_element._com)
        return pkg, cls, instance

    def test_get_all_nested_elements_is_documented_unavailable(self, test_project: IRPProject) -> None:
        pkg, _cls, instance = self._create_instance(test_project, self._unique("StubPkg"), self._unique("StubCls"), self._unique("StubInst"))
        try:
            with pytest.raises(NotImplementedError):
                instance.get_all_nested_elements()
        finally:
            pkg.delete_from_project()

    def test_update_contained_diagrams_on_server_is_documented_unavailable(self, test_project: IRPProject) -> None:
        pkg, _cls, instance = self._create_instance(test_project, self._unique("StubPkg"), self._unique("StubCls"), self._unique("StubInst"))
        try:
            with pytest.raises(NotImplementedError):
                instance.update_contained_diagrams_on_server(1)
        finally:
            pkg.delete_from_project()

    def test_attribute_value_roundtrip(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("AttrValPkg"))
        cls = pkg.add_class(self._unique("AttrValCls"))
        try:
            attribute_name = self._unique("count")
            cls.add_attribute(attribute_name)
            object_element = pkg.add_global_object(self._unique("AttrValInst"), cls.name, pkg.name)
            instance = IRPInstance(object_element._com)

            instance.set_attribute_value(attribute_name, "42")

            assert instance.get_attribute_value(attribute_name) == "42"
        finally:
            pkg.delete_from_project()

    def test_get_in_links_and_get_out_links(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("InstLinksPkg"))
        try:
            from_class = pkg.add_class(self._unique("LinkFrom"))
            to_class = pkg.add_class(self._unique("LinkTo"))
            association = from_class.add_relation_to(to_class, self._unique("FromRole"), "Association", "1", self._unique("ToRole"), "Association", "1", self._unique("LinkAssociation"))
            from_object = pkg.add_global_object(self._unique("FromObject"), from_class.name, pkg.name)
            to_object = pkg.add_global_object(self._unique("ToObject"), to_class.name, pkg.name)
            from_part = IRPInstance(from_object._com)
            to_part = IRPInstance(to_object._com)
            link = pkg.add_link(from_part, to_part, association, None, None)

            out_links = from_part.get_out_links()
            in_links = to_part.get_in_links()
            assert isinstance(out_links, IRPCollection)
            assert isinstance(in_links, IRPCollection)
            assert link in list(out_links)
            assert link in list(in_links)
        finally:
            pkg.delete_from_project()

    @pytest.mark.skip(reason="Approved live blocker (#202): addRelationToTheWhole returns None for a global object created from its classifier.")
    def test_add_relation_to_the_whole(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("WholePkg"))
        cls = pkg.add_class(self._unique("WholeCls"))
        try:
            object_element = pkg.add_global_object(self._unique("WholeObject"), cls.name, pkg.name)
            instance = IRPInstance(object_element._com)
            relation = instance.add_relation_to_the_whole(self._unique("WholeRel"))
            assert isinstance(relation, IRPRelation)
        finally:
            pkg.delete_from_project()

    @pytest.mark.skip(reason="Approved live blocker (#202): setInstantiatedBy does not persist; getter remains None on a global object.")
    def test_instantiated_by_roundtrip(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("InstByPkg"))
        cls = pkg.add_class(self._unique("InstByCls"))
        try:
            operation = cls.add_constructor("")
            assert isinstance(operation, IRPOperation)
            object_element = pkg.add_global_object(self._unique("InstByInst"), cls.name, pkg.name)
            instance = IRPInstance(object_element._com)

            instance.instantiated_by = operation

            result = instance.instantiated_by
            assert result is not None
            assert result._com is operation._com
        finally:
            pkg.delete_from_project()

    def test_get_list_of_initializer_arguments(self, test_project: IRPProject) -> None:
        pkg, _cls, instance = self._create_instance(test_project, self._unique("InitArgsPkg"), self._unique("InitArgsCls"), self._unique("InitArgsInst"))
        try:
            arguments = instance.get_list_of_initializer_arguments()
            assert isinstance(arguments, IRPCollection)
            assert len(list(arguments)) == 0
        finally:
            pkg.delete_from_project()

    def test_set_explicit_and_set_implicit(self, test_project: IRPProject) -> None:
        pkg, _cls, instance = self._create_instance(test_project, self._unique("ExplicitPkg"), self._unique("ExplicitCls"), self._unique("ExplicitInst"))
        try:
            assert instance.set_explicit() is None  # type: ignore[func-returns-value]
            assert instance.set_implicit() is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()
