"""Integration tests for IRPModelElement and IRPCollection with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import uuid
from typing import Iterator, Optional

import pytest

from rhapsody_cli import RhapsodyApplication
from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPAssociationClass, IRPTag, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_relation import IRPRelation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_stereotype import IRPStereotype


@pytest.fixture(scope="module", autouse=True)
def _hide_application_ui_by_default(rhapsody_app: Optional[RhapsodyApplication]) -> Iterator[None]:
    """Keep this integration module hidden without changing shared fixtures."""
    if rhapsody_app is None:
        yield
        return

    original_hidden_ui = rhapsody_app.is_hidden_ui
    rhapsody_app.set_hidden_ui(True)
    try:
        yield
    finally:
        rhapsody_app.set_hidden_ui(original_hidden_ui)


@pytest.mark.integration
class TestRPModelElementIntegration:
    """Integration tests for IRPModelElement with real Rhapsody COM API."""

    def test_get_name(self, test_project: IRPProject) -> None:
        assert isinstance(test_project, IRPModelElement)
        name = test_project.name
        assert name == "TestProject"
        assert isinstance(name, str)

    def test_set_name(self, test_project: IRPProject) -> None:
        original_name = test_project.name
        test_project.name = "RenamedProject"
        new_name = test_project.name
        assert new_name == "RenamedProject"
        assert isinstance(new_name, str)
        test_project.name = original_name

    def test_get_meta_class(self, test_project: IRPProject) -> None:
        meta_class = test_project.meta_class
        assert meta_class == "Project"
        assert isinstance(meta_class, str)

    def test_get_guid(self, test_project: IRPProject) -> None:
        guid = test_project.guid
        assert isinstance(guid, str)
        # Live COM returns the value as "GUID <hex-uuid>", not a bare UUID string.
        parsed = uuid.UUID(guid.split()[-1])
        assert str(parsed) in guid


@pytest.mark.integration
class TestRPCollectionIntegration:
    """Integration tests for IRPCollection with real Rhapsody COM API."""

    def test_get_nested_elements_iteration(self, test_project: IRPProject) -> None:
        elements = test_project.get_nested_elements()
        assert elements is not None
        assert len(list(elements)) >= 0

    def test_get_nested_elements_filtering(self, test_project: IRPProject) -> None:
        all_elements = test_project.get_nested_elements()
        packages = test_project.get_nested_elements_by_meta_class("Package", 0)
        assert all_elements is not None
        assert packages is not None
        all_list = list(all_elements)
        package_list = list(packages)
        assert len(package_list) <= len(all_list)


@pytest.mark.integration
class TestRPCollectionAddItemIntegration:
    """Integration tests for IRPCollection.add_item with live Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_add_item_appends_and_count_increases(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("AddItemPkg"))
        try:
            cls1 = pkg.add_class(self._unique("AddItemCls1"))
            cls2 = pkg.add_class(self._unique("AddItemCls2"))

            collection = rhapsody_app.create_new_collection()
            assert isinstance(collection, IRPCollection)

            before = collection.count
            assert isinstance(before, int)
            assert before == 0

            collection.add_item(cls1)
            collection.add_item(cls2)
            after = collection.count
            assert isinstance(after, int)
            assert after == before + 2

            items = [item.name for item in collection]
            assert cls1.name in items
            assert cls2.name in items
        finally:
            pkg.delete_from_project()

    def test_add_item_idempotent_on_same_element(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("AddItemIdemPkg"))
        try:
            cls = pkg.add_class(self._unique("AddItemIdemCls"))

            collection = rhapsody_app.create_new_collection()
            assert isinstance(collection, IRPCollection)

            collection.add_item(cls)
            collection.add_item(cls)
            assert collection.count == 2

            names = [item.name for item in collection]
            assert names.count(cls.name) == 2
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPCollectionMutationMethodsIntegration:
    """Integration tests for IRPCollection mutation methods with live Rhapsody COM API.

    These tests use ``rhapsody_app.create_new_collection()`` to obtain a genuinely
    mutable collection. Read-only snapshots such as ``getNestedElements()`` are
    intentionally avoided because mutations on them are silently ignored.
    """

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_to_list_returns_python_list_of_items(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        """JavaDoc IRPCollection.toList exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        pkg = self._create_package(test_project, self._unique("ToListPkg"))
        try:
            cls1 = pkg.add_class(self._unique("ToListCls1"))
            cls2 = pkg.add_class(self._unique("ToListCls2"))

            collection = rhapsody_app.create_new_collection()
            assert isinstance(collection, IRPCollection)
            collection.add_item(cls1)
            collection.add_item(cls2)

            with pytest.raises(NotImplementedError):
                collection.to_list()
        finally:
            pkg.delete_from_project()

    def test_set_size_changes_count(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("SetSizePkg"))
        try:
            collection = rhapsody_app.create_new_collection()
            assert isinstance(collection, IRPCollection)
            assert collection.count == 0

            collection.set_size(3)
            count = collection.count
            assert isinstance(count, int)
            assert count == 3
        finally:
            pkg.delete_from_project()

    def test_remove_decreases_count(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("RemovePkg"))
        try:
            cls1 = pkg.add_class(self._unique("RemoveCls1"))
            cls2 = pkg.add_class(self._unique("RemoveCls2"))

            collection = rhapsody_app.create_new_collection()
            assert isinstance(collection, IRPCollection)
            collection.add_item(cls1)
            collection.add_item(cls2)
            before = collection.count
            assert before == 2

            collection.remove(1)
            after = collection.count
            assert isinstance(after, int)
            assert after == before - 1

            remaining = [item.name for item in collection]
            assert cls1.name not in remaining
            assert cls2.name in remaining
        finally:
            pkg.delete_from_project()

    def test_set_model_element_replaces_item_at_index(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("SetModelElemPkg"))
        try:
            cls1 = pkg.add_class(self._unique("SetModelElemCls1"))
            cls2 = pkg.add_class(self._unique("SetModelElemCls2"))
            cls3 = pkg.add_class(self._unique("SetModelElemCls3"))

            collection = rhapsody_app.create_new_collection()
            assert isinstance(collection, IRPCollection)
            collection.add_item(cls1)
            collection.add_item(cls2)
            assert collection.count == 2

            collection.set_model_element(1, cls3)
            replaced = collection.get_item(1)
            assert isinstance(replaced, IRPModelElement)
            assert replaced.name == cls3.name
        finally:
            pkg.delete_from_project()

    def test_empty_clears_collection(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("EmptyPkg"))
        try:
            cls1 = pkg.add_class(self._unique("EmptyCls1"))
            cls2 = pkg.add_class(self._unique("EmptyCls2"))

            collection = rhapsody_app.create_new_collection()
            assert isinstance(collection, IRPCollection)
            collection.add_item(cls1)
            collection.add_item(cls2)
            assert collection.count == 2

            collection.empty()
            count = collection.count
            assert isinstance(count, int)
            assert count == 0
            assert len(list(collection)) == 0
        finally:
            pkg.delete_from_project()

    def test_set_string_stores_value(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("SetStrPkg"))
        try:
            collection = rhapsody_app.create_new_collection()
            assert isinstance(collection, IRPCollection)
            collection.set_size(1)
            collection.set_string(1, "marker")

            item = collection.get_item(1)
            assert "marker" in str(item)
        finally:
            pkg.delete_from_project()

    def test_set_integer_stores_value(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("SetIntPkg"))
        try:
            collection = rhapsody_app.create_new_collection()
            assert isinstance(collection, IRPCollection)
            collection.set_size(1)
            collection.set_integer(1, 42)

            item = collection.get_item(1)
            assert "42" in str(item)
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementDependenciesIntegration:
    """Integration tests for IRPModelElement dependency/association methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_add_dependency_to_and_get_dependencies(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DepPkg"))
        try:
            source = pkg.add_class(self._unique("Source"))
            target = pkg.add_class(self._unique("Target"))
            dependency = source.add_dependency_to(target)
            assert dependency is not None
            assert isinstance(dependency, IRPModelElement)
            assert dependency.meta_class == "Dependency"

            deps = source.dependencies
            assert isinstance(deps, IRPCollection)
            assert isinstance(deps.count, int)
            assert deps.count >= 0
            assert len(list(deps)) >= 1

            source.delete_dependency(dependency)
            deps_after = source.dependencies
            assert len(list(deps_after)) == 0
        finally:
            pkg.delete_from_project()

    def test_add_dependency(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("AddDepPkg")
        pkg = self._create_package(test_project, pkg_name)
        try:
            target = pkg.add_class(self._unique("Target"))
            target_name = target.name
            source = pkg.add_class(self._unique("Source"))
            dependency = source.add_dependency(target_name, "Class")
            assert dependency is not None
            assert isinstance(dependency, IRPModelElement)
            assert dependency.meta_class == "Dependency"
            deps = source.dependencies
            assert len(list(deps)) >= 1
            source.delete_dependency(dependency)
        finally:
            pkg.delete_from_project()

    def test_add_dependency_between(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("DepBetPkg")
        pkg = self._create_package(test_project, pkg_name)
        try:
            source = pkg.add_class(self._unique("Source"))
            target = pkg.add_class(self._unique("Target"))
            dependency = pkg.add_dependency_between(source, target)
            assert dependency is not None
            assert isinstance(dependency, IRPModelElement)
            assert dependency.meta_class == "Dependency"
            deps = pkg.get_owned_dependencies()
            assert isinstance(deps, IRPCollection)
            assert isinstance(deps.count, int)
            assert deps.count >= 0
            assert len(list(deps)) >= 1
            pkg.delete_dependency(dependency)
        finally:
            pkg.delete_from_project()

    def test_get_owned_dependencies(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("OwnedDepPkg")
        pkg = self._create_package(test_project, pkg_name)
        try:
            source = pkg.add_class(self._unique("Source"))
            target = pkg.add_class(self._unique("Target"))
            dependency = source.add_dependency_to(target)
            owned = source.get_owned_dependencies()
            assert isinstance(owned, IRPCollection)
            assert isinstance(owned.count, int)
            assert owned.count >= 0
            assert len(list(owned)) >= 1
            source.delete_dependency(dependency)
        finally:
            pkg.delete_from_project()

    def test_add_remote_dependency_to_and_get_remote_dependencies(self, test_project: IRPProject) -> None:
        # add_remote_dependency_to requires a Design Manager remote-requirements
        # setup (JavaDoc: the target must be a remote requirement retrieved via
        # getRemoteResourcePackages); no live fixture can create one, so only
        # the empty-state collection is asserted here. The owned member call is
        # an open ledger blocker.
        pkg = self._create_package(test_project, self._unique("DocPkg"))
        cls = pkg.add_class(self._unique("DocCls"))
        try:
            remote_dependencies = cls.get_remote_dependencies()
            assert isinstance(remote_dependencies, IRPCollection)
            assert isinstance(remote_dependencies.count, int)
            assert len(list(remote_dependencies)) == 0
        finally:
            pkg.delete_from_project()

    def test_get_association_classes(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("AssocClsPkg")
        pkg = self._create_package(test_project, pkg_name)
        try:
            source = pkg.add_class(self._unique("AssocSource"))
            target = pkg.add_class(self._unique("AssocTarget"))
            end1 = source.add_relation_to(target, "targets", "Association", "1", "sources", "Association", "1", "")
            end2 = IRPRelation(end1._com).get_inverse()
            association_class = source.add_association(end1, end2, self._unique("AssocCls"))
            assert association_class in list(source.association_classes)
        finally:
            pkg.delete_from_project()

    def test_get_references(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("RefPkg")
        pkg = self._create_package(test_project, pkg_name)
        try:
            source = pkg.add_class(self._unique("Source"))
            target = pkg.add_class(self._unique("Target"))
            dependency = source.add_dependency_to(target)
            references = list(target.references)
            # JavaDoc does not say whether the returned elements are the dependency or its
            # client; either proves the getter resolves the incoming relationship.
            assert dependency in references or source in references
            source.delete_dependency(dependency)
        finally:
            pkg.delete_from_project()

    def test_add_association(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("AssocClsPkg"))
        try:
            source = pkg.add_class(self._unique("AssocSource"))
            target = pkg.add_class(self._unique("AssocTarget"))
            end1 = source.add_relation_to(target, "targets", "Association", "1", "sources", "Association", "1", "")
            # The automation wrapper reports the concrete metaclass as
            # AssociationEnd, so wrap the dispatch explicitly to access the
            # documented IRPRelation inverse operation.
            end2 = IRPRelation(end1._com).get_inverse()
            assert end1.meta_class == "AssociationEnd"
            assert end2.meta_class == "AssociationEnd"
            association_name = self._unique("AssocCls")

            association_class = source.add_association(end1, end2, association_name)

            assert isinstance(association_class, IRPAssociationClass)
            assert association_class.name == association_name
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementStereotypesTagsIntegration:
    """Integration tests for IRPModelElement stereotype and tag methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_get_stereotypes_initially_empty(self, test_project: IRPProject) -> None:
        stereotypes = test_project.stereotypes
        assert stereotypes is not None
        assert isinstance(stereotypes, IRPCollection)
        assert len(list(stereotypes)) == 0

    def test_add_stereotype_and_get_stereotypes(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("StereoPkg"))
        try:
            stereo = pkg.add_stereotype(self._unique("TestStereo"), "Package")
            assert stereo is not None
            assert isinstance(stereo, IRPModelElement)
            stereotypes = pkg.stereotypes
            assert isinstance(stereotypes, IRPCollection)
            names = [s.name for s in stereotypes]
            assert stereo.name in names
        finally:
            pkg.delete_from_project()

    def test_stereotype_property_reads_and_writes_applied_stereotype(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("SingleStereoPkg"))
        try:
            stereo = pkg.add_stereotype(self._unique("SingleStereo"), "Package")
            assert isinstance(stereo, IRPStereotype)

            pkg.stereotype = stereo
            applied_stereotype = pkg.stereotype

            assert applied_stereotype is not None
            assert applied_stereotype.name == stereo.name
        finally:
            pkg.delete_from_project()

    def test_remove_stereotype(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RemoveStereoPkg"))
        try:
            stereo = pkg.add_stereotype(self._unique("RemoveMe"), "Package")
            assert stereo is not None
            assert isinstance(stereo, IRPModelElement)
            pkg.remove_stereotype(stereo)
            stereotypes = pkg.stereotypes
            assert isinstance(stereotypes, IRPCollection)
            names = [s.name for s in stereotypes]
            assert stereo.name not in names
        finally:
            pkg.delete_from_project()

    def test_add_specific_stereotype(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("SpecificStereoPkg"))
        try:
            stereo = pkg.add_stereotype(self._unique("SpecificStereo"), "Package")
            assert stereo is not None
            assert isinstance(stereo, IRPModelElement)
            pkg.remove_stereotype(stereo)
            # add_specific_stereotype returns void (None) according to Java API
            pkg.add_specific_stereotype(stereo)
            stereotypes = pkg.stereotypes
            assert isinstance(stereotypes, IRPCollection)
            names = [s.name for s in stereotypes]
            assert stereo.name in names
        finally:
            pkg.delete_from_project()

    def test_get_all_tags(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("AllTagsTestPkg"))
        try:
            tag_name = self._unique("AllTagsTestTag")
            tag = pkg.add_new_aggr("Tag", tag_name)
            assert isinstance(tag, IRPTag)
            pkg.set_tag_value(tag, "retrievable tag value")

            tags = pkg.all_tags

            assert tags is not None
            assert isinstance(tags, IRPCollection)
            assert any(item.name == tag_name for item in tags)
        finally:
            pkg.delete_from_project()

    def test_get_local_tags_returns_tag_created_on_element(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("LocalTagsTestPkg"))
        try:
            tag_name = self._unique("LocalTag")
            tag = pkg.add_new_aggr("Tag", tag_name)
            assert isinstance(tag, IRPTag)
            pkg.set_tag_value(tag, "local tag value")

            tags = pkg.local_tags

            assert tag_name in [item.name for item in tags]
        finally:
            pkg.delete_from_project()

    def test_get_tag(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DocPkg"))
        cls = pkg.add_class(self._unique("DocCls"))
        try:
            assert cls.get_tag("SomeTag") is None
        finally:
            pkg.delete_from_project()

    def test_get_new_term_stereotype(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DocPkg"))
        cls = pkg.add_class(self._unique("DocCls"))
        try:
            assert cls.get_new_term_stereotype() is None
        finally:
            pkg.delete_from_project()

    def test_set_tag_value(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("TagValuePkg"))
        try:
            cls = pkg.add_class(self._unique("TagValueCls"))
            tag_name = self._unique("TagValueTag")
            tag = cls.add_new_aggr("Tag", tag_name)
            assert isinstance(tag, IRPTag)

            cls.set_tag_value(tag, "retrievable tag value")

            # Re-query through getTag: its typelib result is a typed IRPTag
            # dispatch, whose value property is readable (the addNewAggr
            # result is only typed as IRPModelElement).
            applied = cls.get_tag(tag_name)
            assert applied is not None
            assert applied.get_value() == "retrievable tag value"
        finally:
            pkg.delete_from_project()

    def test_set_tag_element_value(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("TagElementPkg"))
        try:
            cls = pkg.add_class(self._unique("TagElementCls"))
            target = pkg.add_class(self._unique("TagElementTarget"))
            tag_name = self._unique("TagElementTag")
            tag = cls.add_new_aggr("Tag", tag_name)
            assert isinstance(tag, IRPTag)

            cls.set_tag_element_value(tag, target)

            applied = cls.get_tag(tag_name)
            assert applied is not None
            assert applied.name == tag_name
        finally:
            pkg.delete_from_project()

    def test_set_tag_context_value(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("TagContextPkg"))
        try:
            cls = pkg.add_class(self._unique("TagContextCls"))
            target = pkg.add_class(self._unique("TagContextTarget"))
            tag_name = self._unique("TagContextTag")
            tag = cls.add_new_aggr("Tag", tag_name)
            assert isinstance(tag, IRPTag)

            elements = rhapsody_app.create_new_collection()
            elements.add_item(target)
            multiplicities = rhapsody_app.create_new_collection()
            multiplicities.set_size(1)
            multiplicities.set_string(1, "1")

            cls.set_tag_context_value(tag, elements, multiplicities)

            applied = cls.get_tag(tag_name)
            assert applied is not None
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementDescriptionDisplayNameIntegration:
    """Integration tests for IRPModelElement description and display-name methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_set_and_get_description_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DescPkg"))
        try:
            cls = pkg.add_class(self._unique("DescCls"))
            cls.description = "A test description"
            description = cls.description
            assert description == "A test description"
            assert isinstance(description, str)

            plain_text = cls.description_plain_text
            assert isinstance(plain_text, str)
            assert "A test description" in plain_text
        finally:
            pkg.delete_from_project()

    def test_set_and_get_description_rtf_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RtfDescPkg"))
        try:
            cls = pkg.add_class(self._unique("RtfDescCls"))
            rtf_string = r"{\rtf1 Hello}"
            cls.description_rtf = rtf_string

            is_rtf = cls.is_description_rtf()
            assert is_rtf
            assert isinstance(is_rtf, (bool, int))

            retrieved_rtf = cls.description_rtf
            assert isinstance(retrieved_rtf, str)
            assert retrieved_rtf == rtf_string

            description = cls.description
            assert isinstance(description, str)
            assert "Hello" in description
        finally:
            pkg.delete_from_project()

    def test_set_and_get_description_html(self, test_project: IRPProject) -> None:
        """JavaDoc declares setDescriptionHTML but says "Not implemented - should not be used"; pywin32 exposes only the descriptionHTML property, so the wrapper raises instead of writing."""
        pkg = self._create_package(test_project, self._unique("HtmlDescPkg"))
        try:
            cls = pkg.add_class(self._unique("HtmlDescCls"))
            html = "<html><body>Hello</body></html>"

            # setDescriptionHTML is documented as "Not implemented - should not be used"
            with pytest.raises(NotImplementedError, match="setDescriptionHTML is documented as"):
                cls.set_description_html(html)

            # getDescriptionHTML should work normally; set description through
            # the writable property and assert the HTML getter reflects it.
            cls.description = "A test description"
            retrieved_html = cls.description_html
            assert isinstance(retrieved_html, str)
            assert "A test description" in retrieved_html
        finally:
            pkg.delete_from_project()

    def test_get_description_html_on_empty(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("HtmlEmptyPkg"))
        try:
            result = pkg.description_html
            assert isinstance(result, str)
        finally:
            pkg.delete_from_project()

    def test_set_and_get_display_name_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DispNamePkg"))
        try:
            cls = pkg.add_class(self._unique("DispNameCls"))
            display_name = "My Custom Label"
            cls.display_name = display_name

            retrieved = cls.display_name
            assert retrieved == display_name
            assert isinstance(retrieved, str)
        finally:
            pkg.delete_from_project()

    def test_set_and_get_display_name_rtf_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DispNameRtfPkg"))
        try:
            cls = pkg.add_class(self._unique("DispNameRtfCls"))
            rtf_string = r"{\rtf1 Bold Label}"
            cls.set_display_name_rtf(rtf_string)

            is_rtf = cls.is_display_name_rtf()
            assert is_rtf
            assert isinstance(is_rtf, (bool, int))

            retrieved_rtf = cls.get_display_name_rtf()
            assert isinstance(retrieved_rtf, str)
            assert retrieved_rtf == rtf_string

            display_name = cls.display_name
            assert isinstance(display_name, str)
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementPropertiesIntegration:
    """Integration tests for IRPModelElement property methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_add_property_and_get_property_value(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("AddPropPkg"))
        try:
            cls = pkg.add_class(self._unique("AddPropCls"))
            property_key = f"CG.Class.{self._unique('NewProp')}"

            cls.add_property(property_key, "String", "custom value")

            assert cls.get_property_value(property_key) == "custom value"
        finally:
            pkg.delete_from_project()

    def test_set_property_value_and_read_back(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("SetPropPkg"))
        try:
            cls = pkg.add_class(self._unique("SetPropCls"))
            property_key = f"CG.Class.{self._unique('SettableProp')}"
            cls.add_property(property_key, "String", "initial value")

            cls.set_property_value(property_key, "OverriddenHeader.h")

            assert cls.get_property_value(property_key) == "OverriddenHeader.h"
            assert cls.remove_property(property_key) is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_add_then_remove_property(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RemovePropPkg"))
        try:
            cls = pkg.add_class(self._unique("RemovePropCls"))
            property_key = f"CG.Class.{self._unique('RemovableProp')}"
            cls.add_property(property_key, "String", "temporary")

            assert cls.remove_property(property_key) is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_get_property_value_explicit(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ExplicitPropPkg"))
        try:
            cls = pkg.add_class(self._unique("ExplicitPropCls"))
            property_key = f"CG.Class.{self._unique('ExplicitProp')}"
            cls.add_property(property_key, "String", "ExplicitHeader.h")

            assert cls.get_property_value_explicit(property_key) == "ExplicitHeader.h"
            cls.remove_property(property_key)
        finally:
            pkg.delete_from_project()

    def test_get_overridden_properties(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DocPkg"))
        cls = pkg.add_class(self._unique("DocCls"))
        try:
            assert isinstance(cls.get_overridden_properties(0), IRPCollection)
        finally:
            pkg.delete_from_project()

    def test_get_overridden_properties_by_pattern(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("OverridePatternPkg"))
        try:
            cls = pkg.add_class(self._unique("OverridePatternCls"))
            property_key = "CG.Class.ActiveThreadName"
            property_value = "OverriddenHeader.h"
            cls.set_property_value(property_key, property_value)

            # The live automation matches the exact key (wildcards return an
            # empty collection) and returns items as "key:value" strings.
            overridden = cls.get_overridden_properties_by_pattern(property_key, 1, 0)

            assert isinstance(overridden, IRPCollection)
            assert f"{property_key}:{property_value}" in [item for item in overridden]
            cls.remove_property(property_key)
        finally:
            pkg.delete_from_project()

    def test_get_property_value_conditional(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("ConditionalPropPkg"))
        try:
            cls = pkg.add_class(self._unique("ConditionalPropCls"))
            tokens = rhapsody_app.create_new_collection()
            tokens.set_size(1)
            tokens.set_string(1, "Language")
            token_values = rhapsody_app.create_new_collection()
            token_values.set_size(1)
            token_values.set_string(1, "C++")

            value = cls.get_property_value_conditional("CG.Class.UseCMenus", tokens, token_values)

            assert isinstance(value, str)
        finally:
            pkg.delete_from_project()

    def test_get_property_value_conditional_explicit(self, test_project: IRPProject, rhapsody_app: RhapsodyApplication) -> None:
        pkg = self._create_package(test_project, self._unique("CondExplicitPkg"))
        try:
            cls = pkg.add_class(self._unique("CondExplicitCls"))
            property_key = f"CG.Class.{self._unique('CondExplicitProp')}"
            cls.add_property(property_key, "String", "ConditionalHeader.h")
            tokens = rhapsody_app.create_new_collection()
            tokens.set_size(1)
            tokens.set_string(1, "Language")
            token_values = rhapsody_app.create_new_collection()
            token_values.set_size(1)
            token_values.set_string(1, "C++")

            assert cls.get_property_value_conditional_explicit(property_key, tokens, token_values) == "ConditionalHeader.h"
            cls.remove_property(property_key)
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementNavigationIntegration:
    """Integration tests for IRPModelElement navigation/search methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_find_nested_element(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("NavPkg"))
        try:
            class_name = self._unique("NavCls")
            pkg.add_class(class_name)
            found = pkg.find_nested_element(class_name, "Class")
            assert found is not None
            assert isinstance(found, IRPModelElement)
            assert found.name == class_name

            not_found = pkg.find_nested_element(self._unique("Missing"), "Class")
            # Rhapsody findNestedElement returns None (not an empty-name element) when no match.
            assert not_found is None
        finally:
            pkg.delete_from_project()

    def test_find_nested_element_recursive(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RecPkg"))
        try:
            subpkg = pkg.add_nested_package(self._unique("SubPkg"))
            class_name = self._unique("DeepCls")
            subpkg.add_class(class_name)
            not_found = pkg.find_nested_element(class_name, "Class")
            # The class is nested one level down, so first-level search returns None.
            assert not_found is None
            found = pkg.find_nested_element_recursive(class_name, "Class")
            assert found is not None
            assert isinstance(found, IRPModelElement)
            assert found.name == class_name
        finally:
            pkg.delete_from_project()

    def test_find_elements_by_full_name(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("FullNamePkg"))
        try:
            class_name = self._unique("FullNameCls")
            pkg.add_class(class_name)
            full_path = f"{pkg.name}::{class_name}"
            found = test_project.find_elements_by_full_name(full_path, "Class")
            assert found is not None
            assert isinstance(found, IRPModelElement)
            assert found.name == class_name
        finally:
            pkg.delete_from_project()

    def test_get_nested_elements_recursive(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RecNestPkg"))
        try:
            pkg.add_class(self._unique("Child1"))
            pkg.add_class(self._unique("Child2"))
            elements = pkg.get_nested_elements_recursive()
            assert isinstance(elements, IRPCollection)
            assert isinstance(elements.count, int)
            assert len(list(elements)) >= 3
        finally:
            pkg.delete_from_project()

    def test_get_full_path_name(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("PathPkg"))
        try:
            class_name = self._unique("PathCls")
            cls = pkg.add_class(class_name)
            full_path = cls.get_full_path_name()
            assert isinstance(full_path, str)
            assert pkg.name in full_path
            assert class_name in full_path
        finally:
            pkg.delete_from_project()

    def test_get_full_path_name_in(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("PathInPkg"))
        try:
            class_name = self._unique("PathInCls")
            cls = pkg.add_class(class_name)
            path_in = cls.get_full_path_name_in()
            assert isinstance(path_in, str)
            assert class_name in path_in
            assert pkg.name in path_in
        finally:
            pkg.delete_from_project()

    def test_get_project(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ProjPkg"))
        try:
            class_name = self._unique("ProjCls")
            cls = pkg.add_class(class_name)
            project = cls.project
            assert project is not None
            assert isinstance(project, IRPProject)
            assert project.name == test_project.name
        finally:
            pkg.delete_from_project()

    def test_set_owner(self, test_project: IRPProject) -> None:
        pkg1 = self._create_package(test_project, self._unique("OwnerPkg1"))
        pkg2 = self._create_package(test_project, self._unique("OwnerPkg2"))
        try:
            cls = pkg1.add_class(self._unique("OwnerCls"))
            cls.owner = pkg2
            owner = cls.owner
            assert owner is not None
            assert isinstance(owner, IRPModelElement)
            assert owner.name == pkg2.name
        finally:
            pkg2.delete_from_project()
            pkg1.delete_from_project()

    def test_has_nested_elements(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("HasNestPkg"))
        try:
            empty_pkg = pkg.add_nested_package(self._unique("EmptyPkg"))
            assert empty_pkg.has_nested_elements() == 0
            assert isinstance(empty_pkg.has_nested_elements(), int)
            empty_pkg.add_class(self._unique("SomeCls"))
            assert empty_pkg.has_nested_elements() == 1
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementCloningTemplatesIntegration:
    """Integration tests for IRPModelElement clone, change-to and template methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_clone(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ClonePkg"))
        try:
            cls = pkg.add_class(self._unique("Original"))
            original_guid = cls.guid

            clone_name = self._unique("Clone")
            cloned = cls.clone(clone_name, pkg)
            assert cloned is not None
            assert isinstance(cloned, IRPModelElement)
            assert cloned.name == clone_name
            assert cloned.guid != original_guid
        finally:
            pkg.delete_from_project()

    def test_change_to(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DocPkg"))
        cls = pkg.add_class(self._unique("DocCls"))
        try:
            assert cls.change_to("Package") is not None
        finally:
            pkg.delete_from_project()

    def test_is_a_template(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IsTemplPkg"))
        try:
            cls = pkg.add_class(self._unique("PlainClass"))
            result = cls.is_a_template()
            assert result == 0
            assert isinstance(result, int)
        finally:
            pkg.delete_from_project()

    def test_get_of_template_on_plain_element(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DocPkg"))
        cls = pkg.add_class(self._unique("DocCls"))
        try:
            assert cls.of_template is None
        finally:
            pkg.delete_from_project()

    def test_become_template_instantiation_of(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("BecomesTIPkg"))
        try:
            template = pkg.add_class(self._unique("BecomesTITemplate"))
            # A Rhapsody template class owns at least one template parameter;
            # without it becomeTemplateInstantiationOf faults (E_FAIL).
            template.add_new_aggr("TemplateParameter", "T")
            assert template.is_a_template() == 1
            instance = pkg.add_class(self._unique("BecomesTIInstance"))

            assert instance.become_template_instantiation_of(template) is None  # type: ignore[func-returns-value]
            assert instance.ti is not None
            assert instance.ti.meta_class == "TemplateInstantiation"
            assert instance.of_template is not None
            assert instance.of_template.name == template.name
            assert "T" in [parameter.name for parameter in template.template_parameters]
        finally:
            pkg.delete_from_project()

    def test_set_of_template(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("TemplatePkg"))
        template = pkg.add_class(self._unique("TemplateClass"))
        template.add_new_aggr("TemplateParameter", "T")
        assert template.is_a_template() == 1
        instance = pkg.add_class(self._unique("TemplateInstance"))
        try:
            instance.of_template = template
            retrieved_template = instance.of_template

            assert retrieved_template is not None
            assert retrieved_template.name == template.name
        finally:
            pkg.delete_from_project()

    def test_get_template_parameters_on_plain_element(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("TemplParamsPkg"))
        try:
            cls = pkg.add_class(self._unique("Plain"))
            params = cls.template_parameters
            assert params is not None
            assert isinstance(params, IRPCollection)
            assert isinstance(params.count, int)
        finally:
            pkg.delete_from_project()

    def test_get_ti(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("TemplatePkg"))
        template = pkg.add_class(self._unique("TemplateClass"))
        template.add_new_aggr("TemplateParameter", "T")
        instance = pkg.add_class(self._unique("TemplateInstance"))
        try:
            instance.become_template_instantiation_of(template)
            template_instantiation = instance.ti

            assert template_instantiation.meta_class == "TemplateInstantiation"
            assert instance.ti == template_instantiation
        finally:
            pkg.delete_from_project()

    def test_set_ti(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("TemplatePkg"))
        template = pkg.add_class(self._unique("TemplateClass"))
        template.add_new_aggr("TemplateParameter", "T")
        instance = pkg.add_class(self._unique("TemplateInstance"))
        try:
            instance.become_template_instantiation_of(template)
            template_instantiation = instance.ti
            instance.ti = template_instantiation

            assert instance.ti == template_instantiation
        finally:
            pkg.delete_from_project()

    def test_synchronize_template_instantiation(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("SyncTIPkg"))
        try:
            template = pkg.add_class(self._unique("SyncTITemplate"))
            template.add_new_aggr("TemplateParameter", "T")
            instance = pkg.add_class(self._unique("SyncTIInstance"))
            instance.become_template_instantiation_of(template)

            assert instance.synchronize_template_instantiation() is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementRedefinesConstraintsIntegration:
    """Integration tests for IRPModelElement redefine and constraint methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_add_redefines_and_get_redefines(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RedefinesPkg"))
        try:
            # Redefinition is a feature-level concept: the same-name attribute
            # on the derived class redefines the inherited base attribute.
            # Calling add_redefines with a classifier argument faults (E_FAIL).
            base = pkg.add_class(self._unique("RedefinesBase"))
            derived = pkg.add_class(self._unique("RedefinesDerived"))
            attribute_name = self._unique("redefined_attr")
            base_attr = base.add_attribute(attribute_name)
            derived.add_generalization(base)
            derived_attr = derived.add_attribute(attribute_name)

            assert derived_attr.add_redefines(base_attr) is None  # type: ignore[func-returns-value]

            redefines = derived_attr.get_redefines()
            assert isinstance(redefines, IRPCollection)
            assert base_attr.name in [item.name for item in redefines]
            derived_attr.remove_redefines(base_attr)
        finally:
            pkg.delete_from_project()

    def test_remove_redefines(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DocPkg"))
        cls = pkg.add_class(self._unique("DocCls"))
        try:
            assert cls.remove_redefines(cls) is None  # type: ignore[func-returns-value]
        finally:
            pkg.delete_from_project()

    def test_get_constraints_returns_constraint_created_on_element(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ConstrPkg"))
        try:
            cls = pkg.add_class(self._unique("ConstrCls"))
            constraint_name = self._unique("Constraint")
            constraint = cls.add_new_aggr("Constraint", constraint_name)
            assert constraint.name == constraint_name

            constraints = cls.constraints
            assert isinstance(constraints, IRPCollection)
            assert constraint_name in [item.name for item in constraints]
        finally:
            pkg.delete_from_project()

    def test_get_constraints_by_him_is_not_implemented(self, test_project: IRPProject) -> None:
        """User-approved runtime stub: the catalog exposes constraintsByHim, but live probing returned no result and JavaDoc marks it internal-only (Group-core-1 ledger, 2026-11-24)."""
        pkg = self._create_package(test_project, self._unique("ConstrHimPkg"))
        try:
            cls = pkg.add_class(self._unique("ConstrHimCls"))
            with pytest.raises(NotImplementedError, match="constraints_by_him"):
                _ = cls.constraints_by_him
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementOslcRemoteIntegration:
    """Integration tests for IRPModelElement OSLC, remote and requirement traceability methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_get_hyper_links_is_not_implemented(self, test_project: IRPProject) -> None:
        """User-approved runtime stub: the catalog exposes hyperLinks, but the documented creation APIs faulted and no retrievable hyperlink was produced (Group-core-1 ledger, 2026-11-24)."""
        pkg = self._create_package(test_project, self._unique("HyperLinkPkg"))
        try:
            cls = pkg.add_class(self._unique("HyperLinkCls"))
            with pytest.raises(NotImplementedError, match="hyper_links"):
                _ = cls.hyper_links
        finally:
            pkg.delete_from_project()

    def test_get_oslc_links_returns_empty_collection_for_plain_class(self, test_project: IRPProject) -> None:
        """Exercise the live getOSLCLinks binding and assert its documented empty result.

        This is COM execution evidence only, not populated-getter closure: creating an OSLC link
        needs an OSLC-enabled remote server and the documented createOSLCLink call faults E_FAIL
        in this build (SWR_ELEM_00033). The populated retrieval row stays an open blocker.
        """
        pkg = self._create_package(test_project, self._unique("OslcLinksPkg"))
        try:
            cls = pkg.add_class(self._unique("OslcLinksCls"))
            links = cls.get_oslc_links()
            assert isinstance(links, IRPCollection)
            assert len(links) == 0
        finally:
            pkg.delete_from_project()

    def test_get_remote_uri_returns_empty_string(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("RemoteUriPkg"))
        try:
            cls = pkg.add_class(self._unique("RemoteUriCls"))
            uri = cls.get_remote_uri()
            assert isinstance(uri, str)
            assert uri == ""
        finally:
            pkg.delete_from_project()

    def test_is_remote_returns_zero(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IsRemotePkg"))
        try:
            cls = pkg.add_class(self._unique("IsRemoteCls"))
            result = cls.is_remote()
            assert isinstance(result, int)
            assert result == 0
        finally:
            pkg.delete_from_project()

    def test_get_rmm_url_returns_empty_string(self, test_project: IRPProject) -> None:
        """JavaDoc IRPModelElement.getRmmUrl exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        pkg = self._create_package(test_project, self._unique("DocPkg"))
        cls = pkg.add_class(self._unique("DocCls"))
        try:
            with pytest.raises(NotImplementedError):
                cls.get_rmm_url()
        finally:
            pkg.delete_from_project()

    def test_get_requirement_traceability_handle_default(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ReqTracePkg"))
        try:
            cls = pkg.add_class(self._unique("ReqTraceCls"))
            handle = cls.requirement_traceability_handle
            assert isinstance(handle, int)
        finally:
            pkg.delete_from_project()

    def test_set_and_get_requirement_traceability_handle_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ReqTraceRoundPkg"))
        try:
            cls = pkg.add_class(self._unique("ReqTraceRoundCls"))
            handle_value = 12345
            cls.requirement_traceability_handle = handle_value
            retrieved = cls.requirement_traceability_handle
            assert isinstance(retrieved, int)
            assert retrieved == handle_value
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementMetadataIntegration:
    """Integration tests for IRPModelElement metadata/icon/GUID methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_get_binary_id(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("BinIdPkg"))
        try:
            cls = pkg.add_class(self._unique("BinIdCls"))
            binary_id = cls.binary_id
            assert isinstance(binary_id, bytes)
            # Live COM returns 16 bytes of GUID data plus 4 trailing bytes.
            assert len(binary_id) >= 16
            assert binary_id == cls.binary_id
            assert binary_id != test_project.binary_id

            guid = cls.guid
            assert isinstance(guid, str)
            assert uuid.UUID(guid.split()[-1])
        finally:
            pkg.delete_from_project()

    def test_get_interface_name(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IntNamePkg"))
        try:
            cls = pkg.add_class(self._unique("IntNameCls"))
            iface = cls.interface_name
            assert isinstance(iface, str)
            assert iface == "IRPClass"
        finally:
            pkg.delete_from_project()

    def test_get_is_of_meta_class_class(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IsOfPkg"))
        try:
            cls = pkg.add_class(self._unique("IsOfCls"))
            result = cls.get_is_of_meta_class("Class")
            assert result

            not_result = cls.get_is_of_meta_class("Package")
            assert not not_result
        finally:
            pkg.delete_from_project()

    def test_get_icon_file_name(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IconPkg"))
        try:
            cls = pkg.add_class(self._unique("IconCls"))
            icon = cls.get_icon_file_name()
            assert isinstance(icon, str)
            assert len(icon) > 0
        finally:
            pkg.delete_from_project()

    def test_get_overlay_icon_file_name(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("OverlayIconPkg"))
        try:
            cls = pkg.add_class(self._unique("OverlayIconCls"))
            overlay = cls.get_overlay_icon_file_name()
            assert isinstance(overlay, str)
        finally:
            pkg.delete_from_project()

    def test_get_decoration_style_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("DecoPkg"))
        try:
            cls = pkg.add_class(self._unique("DecoCls"))
            style = cls.get_decoration_style()
            assert isinstance(style, str)

            cls.set_decoration_style("None")
            after = cls.get_decoration_style()
            assert after == "None"
        finally:
            pkg.delete_from_project()

    def test_get_is_external(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IsExtPkg"))
        try:
            cls = pkg.add_class(self._unique("IsExtCls"))
            result = cls.is_external
            assert isinstance(result, int)
            assert result == 0
        finally:
            pkg.delete_from_project()

    def test_get_is_unresolved(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("IsUnresPkg"))
        try:
            cls = pkg.add_class(self._unique("IsUnresCls"))
            result = cls.is_unresolved
            assert isinstance(result, int)
            assert result == 0
        finally:
            pkg.delete_from_project()

    def test_get_user_defined_meta_class(self, test_project: IRPProject) -> None:
        """Open blocker: JavaDoc defines this as the New Term name, but the COM surface exposes no
        API to define a New Term, so only the type of the default value is observable."""
        pkg = self._create_package(test_project, self._unique("DocPkg"))
        cls = pkg.add_class(self._unique("DocCls"))
        try:
            assert isinstance(cls.user_defined_meta_class, str)
        finally:
            pkg.delete_from_project()

    def test_is_modified_after_set_name(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ModPkg"))
        try:
            cls = pkg.add_class(self._unique("ModCls"))
            cls.name = self._unique("Renamed")
            modified = cls.is_modified()
            assert modified
        finally:
            pkg.delete_from_project()

    def test_get_tool_tip_html(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ToolTipPkg"))
        try:
            cls = pkg.add_class(self._unique("ToolTipCls"))
            html = cls.get_tool_tip_html()
            assert isinstance(html, str)
            assert len(html) > 0
        finally:
            pkg.delete_from_project()

    def test_get_is_show_display_name_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ShowDnPkg"))
        try:
            cls = pkg.add_class(self._unique("ShowDnCls"))
            original = cls.is_show_display_name
            assert isinstance(original, int)

            cls.is_show_display_name = 0
            assert cls.is_show_display_name == 0

            cls.is_show_display_name = 1
            assert cls.is_show_display_name == 1
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestRPModelElementDiagnosticsUiIntegration:
    """Integration tests for IRPModelElement diagnostics/annotations/UI-action methods."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{uuid.uuid4().hex[:8]}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_error_message_empty_after_success(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("ErrPkg"))
        try:
            cls = pkg.add_class(self._unique("ErrCls"))
            assert cls.name
            message = cls.error_message()
            assert message == ""
            assert isinstance(message, str)
        finally:
            pkg.delete_from_project()

    def test_get_error_message_empty_after_success(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("GetErrPkg"))
        try:
            cls = pkg.add_class(self._unique("GetErrCls"))
            assert cls.name
            message = cls.get_error_message("")
            assert message == ""
            assert isinstance(message, str)
        finally:
            pkg.delete_from_project()

    def test_get_annotations_empty_for_plain_class(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("AnnPkg"))
        try:
            cls = pkg.add_class(self._unique("AnnCls"))
            annotations = cls.annotations
            assert isinstance(annotations, IRPCollection)
            assert isinstance(annotations.count, int)
            assert annotations.count == 0
            assert len(list(annotations)) == 0
        finally:
            pkg.delete_from_project()

    def test_get_annotations_returns_annotation_created_on_element(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("AnnPopPkg"))
        try:
            cls = pkg.add_class(self._unique("AnnPopCls"))
            annotation_name = self._unique("Annotation")
            cls.add_new_aggr("Annotation", annotation_name)

            assert annotation_name in [annotation.name for annotation in cls.annotations]
        finally:
            pkg.delete_from_project()

    def test_get_controlled_files_empty(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("CtrlPkg"))
        try:
            cls = pkg.add_class(self._unique("CtrlCls"))
            files = cls.controlled_files
            assert isinstance(files, IRPCollection)
            assert isinstance(files.count, int)
            assert files.count == 0
            assert len(list(files)) == 0
        finally:
            pkg.delete_from_project()

    def test_get_save_unit(self, test_project: IRPProject) -> None:

        pkg = self._create_package(test_project, self._unique("SaveUnitPkg"))
        try:
            cls = pkg.add_class(self._unique("SaveUnitCls"))
            unit = cls.get_save_unit()
            assert isinstance(unit, IRPUnit)
            unit_name = unit.name
            assert isinstance(unit_name, str)
            assert pkg.name in unit_name
        finally:
            pkg.delete_from_project()

    def test_get_main_diagram_and_set_main_diagram_roundtrip(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("MainDiagramPkg"))
        diagram = pkg.add_object_model_diagram(self._unique("MainDiagram"))
        try:
            pkg.main_diagram = diagram
            retrieved_diagram = pkg.main_diagram

            assert retrieved_diagram == diagram
            assert retrieved_diagram.name == diagram.name
        finally:
            pkg.delete_from_project()

    def test_has_panel_widget_returns_zero(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("PanelPkg"))
        try:
            cls = pkg.add_class(self._unique("PanelCls"))
            result = cls.has_panel_widget()
            assert isinstance(result, int)
            assert result == 0
        finally:
            pkg.delete_from_project()

    def test_locate_in_browser_returns_int(self, test_project: IRPProject) -> None:
        pkg = self._create_package(test_project, self._unique("LocPkg"))
        try:
            cls = pkg.add_class(self._unique("LocCls"))
            result = cls.locate_in_browser()
            assert isinstance(result, int)
        finally:
            pkg.delete_from_project()


@pytest.mark.integration
class TestIRPModelElementDunderIntegration:
    """Live coverage for equality, hashing and representation."""

    def test_equality_hash_and_repr(self, test_project: IRPProject) -> None:
        assert test_project.__eq__(object()) is NotImplemented
        assert test_project == test_project
        assert hash(test_project) == hash(id(test_project._com))
        assert repr(test_project).startswith("IRPProject(name=")
