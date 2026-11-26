"""Tests for rhapsody_cli._core class-based wrapping utilities."""

import re
from pathlib import Path
from typing import cast
from unittest.mock import MagicMock, call, patch

import pytest

import rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element as model_element_module
import rhapsody_cli.models.core as core_module
from rhapsody_cli.exceptions import RhapsodyRuntimeException
from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDependency, IRPDiagram, IRPGraphElement, IRPRelation, IRPStereotype, IRPTag, IRPTemplateInstantiation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_association_class import IRPAssociationClass
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_com_error, make_fake_collection, make_fake_element


class _FakeClassWrapper(IRPModelElement):
    pass


def test_call_com_returns_value_on_success() -> None:
    result = IRPModelElement.call_com(lambda: 42)

    assert result == 42


def test_call_com_translates_com_error() -> None:
    def failing() -> int:
        raise make_com_error("getName failed")

    with pytest.raises(RhapsodyRuntimeException, match="getName failed"):
        IRPModelElement.call_com(failing)


def test_call_com_does_not_translate_other_exceptions() -> None:
    def failing() -> int:
        raise ValueError("not a COM error")

    with pytest.raises(ValueError, match="not a COM error"):
        IRPModelElement.call_com(failing)


def test_get_com_property_reads_the_pywin32_property_directly() -> None:
    fake = MagicMock(spec=["isAbstract"])
    fake.isAbstract = 1

    assert IRPModelElement.get_com_property(fake, "isAbstract") == 1


def test_get_com_property_translates_com_error() -> None:
    class _FailingCom:
        @property
        def isAbstract(self) -> int:  # noqa: N802 - mirrors the camelCase COM identifier
            raise make_com_error("isAbstract read failed")

    with pytest.raises(RhapsodyRuntimeException, match="isAbstract read failed"):
        IRPModelElement.get_com_property(_FailingCom(), "isAbstract")


def test_set_com_property_writes_the_pywin32_property_directly() -> None:
    fake = MagicMock(spec=["isActive"])

    IRPModelElement.set_com_property(fake, "isActive", 0)

    assert fake.isActive == 0


def test_set_com_property_translates_com_error() -> None:
    class _FailingCom:
        @property
        def isActive(self) -> int:  # noqa: N802 - mirrors the camelCase COM identifier
            return 0

        @isActive.setter
        def isActive(self, value: int) -> None:  # noqa: N802 - mirrors the camelCase COM identifier
            raise make_com_error("isActive write failed")

    with pytest.raises(RhapsodyRuntimeException, match="isActive write failed"):
        IRPModelElement.set_com_property(_FailingCom(), "isActive", 1)


def test_core_module_no_longer_exports_backward_compatibility_wrappers() -> None:
    for wrapper_name in (
        "register_wrapper",
        "call_com",
        "_wrap_if_element",
        "wrap",
        "_get_method_or_property",
        "_set_method_or_property",
    ):
        assert not hasattr(core_module, wrapper_name)


def test_model_element_name_property_reads_pywin32_property() -> None:
    fake = make_fake_element("Class", properties={"name": "Widget"})
    element = IRPModelElement(fake)

    assert element.name == "Widget"
    fake.getName.assert_not_called()


def test_model_element_name_property_writes_pywin32_property() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.name = "NewName"

    assert fake.name == "NewName"
    fake.setName.assert_not_called()


def test_model_element_meta_class_property_reads_pywin32_property() -> None:
    fake = make_fake_element("Package")
    element = IRPModelElement(fake)

    assert element.meta_class == "Package"
    fake.getMetaClass.assert_not_called()


def test_wrap_uses_meta_class_property() -> None:
    fake = MagicMock(spec=["metaClass"])
    fake.metaClass = "Class"

    element = IRPModelElement.wrap(fake)

    assert element is not None and element.meta_class == "Class"


def test_model_element_guid_property_reads_pywin32_property() -> None:
    fake = make_fake_element("Class", properties={"GUID": "guid-123"})
    element = IRPModelElement(fake)

    assert element.guid == "guid-123"


def test_model_element_com_error_becomes_rhapsody_runtime_exception() -> None:
    class _FailingCom:
        @property
        def name(self) -> str:  # noqa: N802 - mirrors the camelCase COM identifier
            raise make_com_error("boom")

    element = IRPModelElement(_FailingCom())

    with pytest.raises(RhapsodyRuntimeException, match="boom"):
        _ = element.name


def test_model_element_equality_by_underlying_com_object() -> None:
    fake = make_fake_element("Class")

    assert IRPModelElement(fake) == IRPModelElement(fake)
    assert IRPModelElement(fake) != IRPModelElement(make_fake_element("Class"))


def test_model_element_eq_returns_not_implemented_for_unrelated_type() -> None:
    element = IRPModelElement(make_fake_element("Class"))

    assert element.__eq__(object()) is NotImplemented


def test_model_element_hash_is_derived_from_the_com_object() -> None:
    fake = make_fake_element("Class")

    assert hash(IRPModelElement(fake)) == hash(id(fake))


def test_model_element_repr_includes_name() -> None:
    fake = make_fake_element("Class", properties={"name": "MyClass"})

    assert repr(IRPModelElement(fake)) == "IRPModelElement(name='MyClass')"


def test_collection_len_delegates_to_count() -> None:
    fake = make_fake_collection([make_fake_element("Class")])
    collection = IRPCollection(fake)

    assert len(collection) == 1


def test_collection_getitem_wraps_model_elements() -> None:
    inner = make_fake_element("Class", properties={"name": "Widget"})
    fake = make_fake_collection([inner])
    collection = IRPCollection(fake)

    item = collection[0]

    assert isinstance(item, IRPModelElement)
    assert item.name == "Widget"
    fake.Item.assert_called_once_with(1)


def test_collection_getitem_passes_through_non_element_values() -> None:
    fake = make_fake_collection(["a plain string", 42])
    collection = IRPCollection(fake)

    assert collection[0] == "a plain string"
    assert collection[1] == 42


def test_collection_negative_index_raises_index_error() -> None:
    fake = make_fake_collection(["a plain string"])
    collection = IRPCollection(fake)

    with pytest.raises(IndexError, match="negative indices are not supported"):
        _ = collection[-1]


def test_collection_getitem_supports_slicing() -> None:
    fake = make_fake_collection(["a", "b", "c", "d"])
    collection = IRPCollection(fake)

    assert collection[:2] == ["a", "b"]
    assert collection[1:3] == ["b", "c"]
    assert collection[:] == ["a", "b", "c", "d"]


def test_collection_iter_yields_all_items() -> None:
    inner_a = make_fake_element("Class", properties={"name": "A"})
    inner_b = make_fake_element("Class", properties={"name": "B"})
    fake = make_fake_collection([inner_a, inner_b])
    collection = IRPCollection(fake)

    names = [item.name for item in collection]

    assert names == ["A", "B"]
    assert fake.Item.call_args_list == [call(1), call(2)]


def test_collection_add_item_delegates_to_com() -> None:
    fake = make_fake_collection([])
    collection = IRPCollection(fake)
    new_element = make_fake_element("Class")

    collection.add_item(IRPModelElement(new_element))

    fake.addItem.assert_called_once_with(new_element)


def test_collection_count_delegates_to_com() -> None:
    fake = make_fake_collection([make_fake_element("Class"), make_fake_element("Class")])
    collection = IRPCollection(fake)

    assert collection.count == 2


def test_collection_count_reads_the_count_property() -> None:
    """Some Rhapsody COM Prog IDs (e.g. Rhapsody2.Application.1) expose the
    collection size/item accessors via 'Count'/'Item' properties instead of
    getCount()/getItem() methods."""
    fake = MagicMock(spec=["Count"])
    fake.Count = 3
    collection = IRPCollection(fake)

    assert collection.count == 3


def test_collection_get_item_falls_back_to_item_property_when_method_missing() -> None:
    inner = make_fake_element("Class", properties={"name": "Widget"})
    fake = MagicMock(spec=["Item"])
    fake.Item.return_value = inner
    collection = IRPCollection(fake)

    item = collection.get_item(1)

    assert isinstance(item, IRPModelElement)
    assert item.name == "Widget"
    fake.Item.assert_called_once_with(1)


def test_collection_add_graphical_item_delegates_to_alias() -> None:
    fake = make_fake_collection([])
    collection = IRPCollection(fake)
    graph = IRPGraphElement(make_fake_element("GraphElement"))

    collection.add_graphical_item(graph)

    fake.addGraphicalElementItem.assert_called_once_with(graph._com)


def test_collection_to_list_raises_not_implemented() -> None:
    fake = make_fake_collection([make_fake_element("Class", properties={"name": "A"})])
    collection = IRPCollection(fake)

    with pytest.raises(NotImplementedError):
        collection.to_list()

    fake.Item.assert_not_called()


def test_collection_set_size_delegates_to_com() -> None:
    fake = make_fake_collection([])
    collection = IRPCollection(fake)

    collection.set_size(5)

    fake.setSize.assert_called_once_with(5)


def test_collection_remove_delegates_to_com() -> None:
    fake = make_fake_collection([])
    collection = IRPCollection(fake)

    collection.remove(1)

    fake.remove.assert_called_once_with(1)


def test_collection_set_string_delegates_to_com() -> None:
    fake = make_fake_collection([])
    collection = IRPCollection(fake)

    collection.set_string(1, "test")

    fake.setString.assert_called_once_with(1, "test")


def test_collection_set_model_element_delegates_to_com() -> None:
    fake = make_fake_collection([])
    collection = IRPCollection(fake)
    element = make_fake_element("Class")

    collection.set_model_element(1, IRPModelElement(element))

    fake.setModelElement.assert_called_once_with(1, element)


def test_collection_empty_delegates_to_com() -> None:
    fake = make_fake_collection([])
    collection = IRPCollection(fake)

    collection.empty()

    fake.empty.assert_called_once_with()


def test_collection_set_integer_delegates_to_com() -> None:
    fake = make_fake_collection([])
    collection = IRPCollection(fake)

    collection.set_integer(1, 42)

    fake.setInteger.assert_called_once_with(1, 42)


def test_wrap_dispatches_to_registered_wrapper() -> None:
    IRPModelElement.register_wrapper("FakeMetaType", _FakeClassWrapper)
    fake = make_fake_element("FakeMetaType", properties={"name": "Thing"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, _FakeClassWrapper)
    assert wrapped.name == "Thing"


def test_wrap_falls_back_to_model_element_for_unregistered_type() -> None:
    fake = make_fake_element("SomeUnmappedType", properties={"name": "Mystery"})

    wrapped = IRPModelElement.wrap(fake)

    assert type(wrapped) is IRPModelElement
    assert wrapped.name == "Mystery"


def test_wrap_handles_none_com_object() -> None:
    wrapped = IRPModelElement.wrap(None)

    assert wrapped is None


# ---------------------------------------------------------------------------
# IRPModelElement parity tests (Task 2): every non-deprecated method.
# ---------------------------------------------------------------------------


def test_model_element_add_association_unwraps_args_and_wraps_result() -> None:
    end1 = IRPModelElement(make_fake_element("Element"))
    end2 = IRPModelElement(make_fake_element("Element"))
    result_fake = make_fake_element("Association", properties={"name": "Assoc"})
    fake = make_fake_element("Class", addAssociation=result_fake)
    element = IRPModelElement(fake)

    result = element.add_association(cast(IRPRelation, end1), cast(IRPRelation, end2), "Assoc")

    assert isinstance(result, IRPAssociationClass)
    assert result._com is result_fake
    assert result.name == "Assoc"
    fake.addAssociation.assert_called_once_with(end1._com, end2._com, "Assoc")


def test_model_element_add_dependency_wraps_result() -> None:
    dep_fake = make_fake_element("Dependency", properties={"name": "Dep"})
    fake = make_fake_element("Class", addDependency=dep_fake)
    element = IRPModelElement(fake)

    result = element.add_dependency("Target", "Class")

    assert isinstance(result, IRPModelElement)
    assert result.name == "Dep"
    fake.addDependency.assert_called_once_with("Target", "Class")


def test_model_element_add_dependency_between_unwraps_args_and_wraps_result() -> None:
    dependent = IRPModelElement(make_fake_element("Element"))
    depends_on = IRPModelElement(make_fake_element("Element"))
    dep_fake = make_fake_element("Dependency", properties={"name": "Dep"})
    fake = make_fake_element("Class", addDependencyBetween=dep_fake)
    element = IRPModelElement(fake)

    result = element.add_dependency_between(dependent, depends_on)

    assert isinstance(result, IRPModelElement)
    assert result.name == "Dep"
    fake.addDependencyBetween.assert_called_once_with(dependent._com, depends_on._com)


def test_model_element_add_dependency_to_unwraps_argument_and_wraps_result() -> None:
    target = IRPModelElement(make_fake_element("Element"))
    dep_fake = make_fake_element("Dependency", properties={"name": "Dep"})
    fake = make_fake_element("Class", addDependencyTo=dep_fake)
    element = IRPModelElement(fake)

    result = element.add_dependency_to(target)

    assert isinstance(result, IRPModelElement)
    assert result.name == "Dep"
    fake.addDependencyTo.assert_called_once_with(target._com)


def test_model_element_add_link_to_element_unwraps_args_and_wraps_result() -> None:
    to_element = IRPModelElement(make_fake_element("Element"))
    assoc = IRPModelElement(make_fake_element("Element"))
    from_port = IRPModelElement(make_fake_element("Element"))
    to_port = IRPModelElement(make_fake_element("Element"))
    link_fake = make_fake_element("Link", properties={"name": "Link"})
    fake = make_fake_element("Class", addLinkToElement=link_fake)
    element = IRPModelElement(fake)

    result = element.add_link_to_element(to_element, cast(IRPRelation, assoc), from_port, to_port)

    assert isinstance(result, IRPModelElement)
    assert result.name == "Link"
    fake.addLinkToElement.assert_called_once_with(to_element._com, assoc._com, from_port._com, to_port._com)


def test_model_element_add_link_to_element_passes_none_ports_to_com() -> None:
    """JavaDoc: pass Null ports when the link represents an association."""
    to_element = IRPModelElement(make_fake_element("Element"))
    assoc = IRPModelElement(make_fake_element("Element"))
    link_fake = make_fake_element("Link", properties={"name": "Link"})
    fake = make_fake_element("Class", addLinkToElement=link_fake)
    element = IRPModelElement(fake)

    result = element.add_link_to_element(to_element, cast(IRPRelation, assoc), None, None)

    assert isinstance(result, IRPModelElement)
    fake.addLinkToElement.assert_called_once_with(to_element._com, assoc._com, None, None)


def test_model_element_add_new_aggr_wraps_result() -> None:
    new_fake = make_fake_element("Element", properties={"name": "NewElem"})
    fake = make_fake_element("Package", addNewAggr=new_fake)
    element = IRPModelElement(fake)

    result = element.add_new_aggr("Class", "NewElem")

    assert isinstance(result, IRPModelElement)
    assert result.name == "NewElem"
    fake.addNewAggr.assert_called_once_with("Class", "NewElem")


def test_model_element_add_property_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.add_property("key", "type", "value")

    fake.addProperty.assert_called_once_with("key", "type", "value")


def test_model_element_add_redefines_unwraps_argument() -> None:
    redefine = IRPModelElement(make_fake_element("Element"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.add_redefines(redefine)

    fake.addRedefines.assert_called_once_with(redefine._com)


def test_model_element_add_remote_dependency_to_unwraps_arg_and_wraps_result() -> None:
    target = IRPModelElement(make_fake_element("Element"))
    dep_fake = make_fake_element("Dependency", properties={"name": "Dep"})
    fake = make_fake_element("Class", addRemoteDependencyTo=dep_fake)
    element = IRPModelElement(fake)

    result = element.add_remote_dependency_to(target, "linkType")

    assert isinstance(result, IRPModelElement)
    assert result.name == "Dep"
    fake.addRemoteDependencyTo.assert_called_once_with(target._com, "linkType")


def test_model_element_add_specific_stereotype_unwraps_argument() -> None:
    stereotype = IRPModelElement(make_fake_element("Stereotype"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.add_specific_stereotype(cast(IRPStereotype, stereotype))

    fake.addSpecificStereotype.assert_called_once_with(stereotype._com)


def test_model_element_add_stereotype_wraps_result() -> None:
    st_fake = make_fake_element("Stereotype", properties={"name": "Ster"})
    fake = make_fake_element("Class", addStereotype=st_fake)
    element = IRPModelElement(fake)

    result = element.add_stereotype("Ster", "Class")

    assert isinstance(result, IRPModelElement)
    assert result.name == "Ster"
    fake.addStereotype.assert_called_once_with("Ster", "Class")


def test_model_element_become_template_instantiation_of_unwraps_argument() -> None:
    template = IRPModelElement(make_fake_element("Element"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.become_template_instantiation_of(template)

    fake.becomeTemplateInstantiationOf.assert_called_once_with(template._com)


def test_model_element_change_to_wraps_result() -> None:
    changed_fake = make_fake_element("Element", properties={"name": "Changed"})
    fake = make_fake_element("Class", changeTo=changed_fake)
    element = IRPModelElement(fake)

    result = element.change_to("Package")

    assert isinstance(result, IRPModelElement)
    assert result.name == "Changed"
    fake.changeTo.assert_called_once_with("Package")


def test_model_element_clone_unwraps_owner_and_wraps_result() -> None:
    new_owner = IRPModelElement(make_fake_element("Element"))
    cloned_fake = make_fake_element("Element", properties={"name": "Clone"})
    fake = make_fake_element("Class", clone=cloned_fake)
    element = IRPModelElement(fake)

    result = element.clone("Clone", new_owner)

    assert isinstance(result, IRPModelElement)
    assert result.name == "Clone"
    fake.clone.assert_called_once_with("Clone", new_owner._com)


def test_model_element_create_oslc_link_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)
    link_type = "http://jazz.net/ns/dm/linktypes#external"
    purl = "https://example.com/oslc/req/1"

    element.create_oslc_link(link_type, purl)

    fake.createOSLCLink.assert_called_once_with(link_type, purl)


def test_model_element_get_oslc_links_wraps_collection() -> None:
    link_text = "Type=external\nURL=https://example.com/oslc/req/1"
    links_com = make_fake_collection([link_text])
    fake = make_fake_element("Class", getOSLCLinks=links_com)
    element = IRPModelElement(fake)

    links = element.get_oslc_links()

    assert isinstance(links, IRPCollection)
    assert list(links) == [link_text]
    fake.getOSLCLinks.assert_called_once_with()


def test_model_element_delete_dependency_unwraps_argument() -> None:
    dependency = IRPModelElement(make_fake_element("Dependency"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.delete_dependency(cast(IRPDependency, dependency))

    fake.deleteDependency.assert_called_once_with(dependency._com)


def test_model_element_delete_from_project_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.delete_from_project()

    fake.deleteFromProject.assert_called_once_with()


def test_model_element_delete_oslc_link_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)
    link_type = "http://jazz.net/ns/dm/linktypes#external"
    purl = "https://example.com/oslc/req/1"

    element.delete_oslc_link(link_type, purl)

    fake.deleteOSLCLink.assert_called_once_with(link_type, purl)


def test_model_element_error_message_returns_str() -> None:
    fake = make_fake_element("Class", errorMessage="boom")
    element = IRPModelElement(fake)

    assert element.error_message() == "boom"
    fake.errorMessage.assert_called_once_with()


def test_model_element_find_elements_by_full_name_wraps_result() -> None:
    found_fake = make_fake_element("Element", properties={"name": "Found"})
    fake = make_fake_element("Package", findElementsByFullName=found_fake)
    element = IRPModelElement(fake)

    result = element.find_elements_by_full_name("Path::To::Found", "Class")

    assert isinstance(result, IRPModelElement)
    assert result.name == "Found"
    fake.findElementsByFullName.assert_called_once_with("Path::To::Found", "Class")


def test_model_element_find_nested_element_wraps_result() -> None:
    found_fake = make_fake_element("Element", properties={"name": "Found"})
    fake = make_fake_element("Package", findNestedElement=found_fake)
    element = IRPModelElement(fake)

    result = element.find_nested_element("Found", "Class")

    assert isinstance(result, IRPModelElement)
    assert result.name == "Found"
    fake.findNestedElement.assert_called_once_with("Found", "Class")


def test_model_element_find_nested_element_recursive_wraps_result() -> None:
    found_fake = make_fake_element("Element", properties={"name": "Found"})
    fake = make_fake_element("Package", findNestedElementRecursive=found_fake)
    element = IRPModelElement(fake)

    result = element.find_nested_element_recursive("Found", "Class")

    assert isinstance(result, IRPModelElement)
    assert result.name == "Found"
    fake.findNestedElementRecursive.assert_called_once_with("Found", "Class")


def test_model_element_all_tags_property_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"allTags": coll})
    element = IRPModelElement(fake)

    result = element.all_tags

    assert isinstance(result, IRPCollection)


def test_model_element_get_annotations_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"annotations": coll})
    element = IRPModelElement(fake)

    result = element.annotations

    assert isinstance(result, IRPCollection)


def test_model_element_get_association_classes_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"associationClasses": coll})
    element = IRPModelElement(fake)

    result = element.association_classes

    assert isinstance(result, IRPCollection)


def test_model_element_binary_id_property_reads_pywin32_property() -> None:
    fake = MagicMock(spec=["BinaryID"])
    fake.BinaryID = b"\x01\x02\x03"
    element = IRPModelElement(fake)

    assert element.binary_id == b"\x01\x02\x03"


def test_model_element_stereotype_property_wraps_and_unwraps_rps_stereotype() -> None:
    raw_stereotype = make_fake_element("Stereotype")
    fake = make_fake_element("Class", properties={"stereotype": raw_stereotype})
    element = IRPModelElement(fake)

    stereotype = element.stereotype
    assert isinstance(stereotype, IRPStereotype)
    assert stereotype._com is raw_stereotype

    element.stereotype = stereotype
    assert fake.stereotype is raw_stereotype


def test_model_element_stereotype_property_returns_none_when_unset() -> None:
    fake = make_fake_element("Class", properties={"stereotype": None})
    element = IRPModelElement(fake)

    assert element.stereotype is None


def test_model_element_get_constraints_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"constraints": coll})
    element = IRPModelElement(fake)

    result = element.constraints

    assert isinstance(result, IRPCollection)


def test_model_element_get_constraints_by_him_raises_not_implemented_without_com_access() -> None:
    fake = make_fake_element("Class", properties={"constraintsByHim": make_fake_collection([])})
    element = IRPModelElement(fake)

    with patch.object(core_module.ComHelper, "get_com_property") as get_com_property:
        with pytest.raises(NotImplementedError, match="constraints_by_him"):
            _ = element.constraints_by_him

    get_com_property.assert_not_called()


def test_model_element_get_controlled_files_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"controlledFiles": coll})
    element = IRPModelElement(fake)

    result = element.controlled_files

    assert isinstance(result, IRPCollection)


def test_model_element_get_decoration_style_returns_str() -> None:
    fake = make_fake_element("Class", getDecorationStyle="Bold")
    element = IRPModelElement(fake)

    assert element.get_decoration_style() == "Bold"


def test_model_element_get_dependencies_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"dependencies": coll})
    element = IRPModelElement(fake)

    result = element.dependencies

    assert isinstance(result, IRPCollection)


def test_model_element_get_description_returns_str() -> None:
    fake = make_fake_element("Class", properties={"description": "A description"})
    element = IRPModelElement(fake)

    assert element.description == "A description"


def test_model_element_get_description_html_returns_str() -> None:
    fake = make_fake_element("Class", properties={"descriptionHTML": "<p>desc</p>"})
    element = IRPModelElement(fake)

    assert element.description_html == "<p>desc</p>"


def test_model_element_get_description_plain_text_returns_str() -> None:
    fake = make_fake_element("Class", properties={"descriptionPlainText": "plain"})
    element = IRPModelElement(fake)

    assert element.description_plain_text == "plain"


def test_model_element_get_description_rtf_returns_str() -> None:
    fake = make_fake_element("Class", properties={"descriptionRTF": "{\\rtf}"})
    element = IRPModelElement(fake)

    assert element.description_rtf == "{\\rtf}"


def test_model_element_get_display_name_returns_str() -> None:
    fake = make_fake_element("Class", properties={"displayName": "Label"})
    element = IRPModelElement(fake)

    assert element.display_name == "Label"


def test_model_element_get_display_name_rtf_returns_str() -> None:
    fake = make_fake_element("Class", getDisplayNameRTF="{\\rtf}")
    element = IRPModelElement(fake)

    assert element.get_display_name_rtf() == "{\\rtf}"


def test_model_element_get_error_message_passes_required_midl_buffer() -> None:
    fake = make_fake_element("Class", getErrorMessage="boom")
    element = IRPModelElement(fake)

    # pywin32 requires the MIDL output buffer omitted from the JavaDoc signature.
    assert element.get_error_message("") == "boom"
    fake.getErrorMessage.assert_called_once_with("")


def test_model_element_get_full_path_name_returns_str() -> None:
    fake = make_fake_element("Class", getFullPathName="Pkg::Class")
    element = IRPModelElement(fake)

    assert element.get_full_path_name() == "Pkg::Class"


def test_model_element_get_full_path_name_in_returns_str() -> None:
    fake = make_fake_element("Class", getFullPathNameIn="Class in Pkg")
    element = IRPModelElement(fake)

    assert element.get_full_path_name_in() == "Class in Pkg"


def test_model_element_get_hyper_links_raises_not_implemented_without_com_access() -> None:
    fake = make_fake_element("Class", properties={"hyperLinks": make_fake_collection([])})
    element = IRPModelElement(fake)

    with patch.object(core_module.ComHelper, "get_com_property") as get_com_property:
        with pytest.raises(NotImplementedError, match="hyper_links"):
            _ = element.hyper_links

    get_com_property.assert_not_called()


def test_model_element_get_icon_file_name_returns_str() -> None:
    fake = make_fake_element("Class", getIconFileName="D:\\icons\\class.gif")
    element = IRPModelElement(fake)

    assert element.get_icon_file_name() == "D:\\icons\\class.gif"


def test_model_element_get_interface_name_returns_str() -> None:
    fake = make_fake_element("Class", properties={"interfaceName": "IRPClass"})
    element = IRPModelElement(fake)

    assert element.interface_name == "IRPClass"


def test_model_element_get_is_external_returns_int() -> None:
    fake = make_fake_element("Class", properties={"isExternal": 1})
    element = IRPModelElement(fake)

    assert element.is_external == 1


def test_model_element_get_is_of_meta_class_calls_pywin32_member() -> None:
    fake = MagicMock(spec=["isOfMetaClass"])
    fake.isOfMetaClass.return_value = 1
    element = IRPModelElement(fake)

    assert element.get_is_of_meta_class("Class") == 1
    fake.isOfMetaClass.assert_called_once_with("Class")


def test_model_element_get_is_show_display_name_returns_int() -> None:
    fake = make_fake_element("Class", properties={"isShowDisplayName": 0})
    element = IRPModelElement(fake)

    assert element.is_show_display_name == 0


def test_model_element_get_is_unresolved_returns_int() -> None:
    fake = make_fake_element("Class", properties={"isUnresolved": 0})
    element = IRPModelElement(fake)

    assert element.is_unresolved == 0


def test_model_element_get_local_tags_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"localTags": coll})
    element = IRPModelElement(fake)

    result = element.local_tags

    assert isinstance(result, IRPCollection)


def test_model_element_get_main_diagram_wraps_result() -> None:
    diagram_fake = make_fake_element("Diagram", properties={"name": "Main"})
    fake = make_fake_element("Class", properties={"mainDiagram": diagram_fake})
    element = IRPModelElement(fake)

    result = element.main_diagram

    assert isinstance(result, IRPModelElement)
    assert result.name == "Main"


def test_model_element_get_nested_elements_returns_collection() -> None:
    coll = make_fake_collection([make_fake_element("Class", properties={"name": "Child"})])
    fake = make_fake_element("Package", getNestedElements=coll)
    element = IRPModelElement(fake)

    result = element.get_nested_elements()

    assert isinstance(result, IRPCollection)
    assert result.count == 1


def test_model_element_get_nested_elements_by_meta_class_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Package", getNestedElementsByMetaClass=coll)
    element = IRPModelElement(fake)

    result = element.get_nested_elements_by_meta_class("Class", 1)

    assert isinstance(result, IRPCollection)
    fake.getNestedElementsByMetaClass.assert_called_once_with("Class", 1)


def test_model_element_get_nested_elements_recursive_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Package", getNestedElementsRecursive=coll)
    element = IRPModelElement(fake)

    result = element.get_nested_elements_recursive()

    assert isinstance(result, IRPCollection)


def test_model_element_get_new_term_stereotype_wraps_result() -> None:
    st_fake = make_fake_element("Stereotype", properties={"name": "NewTerm"})
    fake = make_fake_element("Class", getNewTermStereotype=st_fake)
    element = IRPModelElement(fake)

    result = element.get_new_term_stereotype()

    assert isinstance(result, IRPModelElement)
    assert result.name == "NewTerm"


def test_model_element_get_of_template_wraps_result() -> None:
    template_fake = make_fake_element("Element", properties={"name": "Template"})
    fake = make_fake_element("Class", properties={"ofTemplate": template_fake})
    element = IRPModelElement(fake)

    result = element.of_template

    assert isinstance(result, IRPModelElement)
    assert result.name == "Template"


def test_model_element_get_overlay_icon_file_name_returns_str() -> None:
    fake = make_fake_element("Class", getOverlayIconFileName="D:\\icons\\overlay.gif")
    element = IRPModelElement(fake)

    assert element.get_overlay_icon_file_name() == "D:\\icons\\overlay.gif"


def test_model_element_get_overridden_properties_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", getOverriddenProperties=coll)
    element = IRPModelElement(fake)

    result = element.get_overridden_properties(1)

    assert isinstance(result, IRPCollection)
    fake.getOverriddenProperties.assert_called_once_with(1)


def test_model_element_get_overridden_properties_by_pattern_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", getOverriddenPropertiesByPattern=coll)
    element = IRPModelElement(fake)

    result = element.get_overridden_properties_by_pattern("C++.*", 1, 0)

    assert isinstance(result, IRPCollection)
    fake.getOverriddenPropertiesByPattern.assert_called_once_with("C++.*", 1, 0)


def test_model_element_get_owned_dependencies_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", getOwnedDependencies=coll)
    element = IRPModelElement(fake)

    result = element.get_owned_dependencies()

    assert isinstance(result, IRPCollection)


def test_model_element_get_owner_wraps_result() -> None:
    owner_fake = make_fake_element("Element", properties={"name": "Owner"})
    fake = make_fake_element("Class", properties={"owner": owner_fake})
    element = IRPModelElement(fake)

    result = element.owner

    assert isinstance(result, IRPModelElement)
    assert result.name == "Owner"


def test_model_element_get_project_wraps_result() -> None:
    project_fake = make_fake_element("Element", properties={"name": "Project"})
    fake = make_fake_element("Class", properties={"project": project_fake})
    element = IRPModelElement(fake)

    result = element.project

    assert isinstance(result, IRPModelElement)
    assert result.name == "Project"


def test_model_element_get_property_value_returns_str() -> None:
    fake = make_fake_element("Class", getPropertyValue="value")
    element = IRPModelElement(fake)

    assert element.get_property_value("key") == "value"
    fake.getPropertyValue.assert_called_once_with("key")


def test_model_element_get_property_value_conditional_returns_str() -> None:
    formal = IRPCollection(make_fake_collection([]))
    actual = IRPCollection(make_fake_collection([]))
    fake = make_fake_element("Class", getPropertyValueConditional="value")
    element = IRPModelElement(fake)

    assert element.get_property_value_conditional("key", formal, actual) == "value"
    fake.getPropertyValueConditional.assert_called_once_with("key", formal._com, actual._com)


def test_model_element_get_property_value_conditional_explicit_returns_str() -> None:
    formal = IRPCollection(make_fake_collection([]))
    actual = IRPCollection(make_fake_collection([]))
    fake = make_fake_element("Class", getPropertyValueConditionalExplicit="value")
    element = IRPModelElement(fake)

    assert element.get_property_value_conditional_explicit("key", formal, actual) == "value"
    fake.getPropertyValueConditionalExplicit.assert_called_once_with("key", formal._com, actual._com)


def test_model_element_get_property_value_explicit_returns_str() -> None:
    fake = make_fake_element("Class", getPropertyValueExplicit="value")
    element = IRPModelElement(fake)

    assert element.get_property_value_explicit("key") == "value"
    fake.getPropertyValueExplicit.assert_called_once_with("key")


def test_model_element_get_redefines_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", getRedefines=coll)
    element = IRPModelElement(fake)

    result = element.get_redefines()

    assert isinstance(result, IRPCollection)


def test_model_element_get_references_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"references": coll})
    element = IRPModelElement(fake)

    result = element.references

    assert isinstance(result, IRPCollection)


def test_model_element_get_remote_dependencies_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", getRemoteDependencies=coll)
    element = IRPModelElement(fake)

    result = element.get_remote_dependencies()

    assert isinstance(result, IRPCollection)


def test_model_element_get_remote_uri_returns_str() -> None:
    fake = make_fake_element("Class", getRemoteURI="https://example.com/req/1")
    element = IRPModelElement(fake)

    assert element.get_remote_uri() == "https://example.com/req/1"


def test_model_element_get_requirement_traceability_handle_returns_int() -> None:
    fake = make_fake_element("Class", properties={"requirementTraceabilityHandle": 42})
    element = IRPModelElement(fake)

    assert element.requirement_traceability_handle == 42


def test_model_element_get_rmm_url_raises_not_implemented() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    with pytest.raises(NotImplementedError):
        element.get_rmm_url()

    fake.getRmmUrl.assert_not_called()


def test_model_element_get_save_unit_wraps_result() -> None:
    unit_fake = make_fake_element("Element", properties={"name": "Unit"})
    fake = make_fake_element("Class", getSaveUnit=unit_fake)
    element = IRPModelElement(fake)

    result = element.get_save_unit()

    assert isinstance(result, IRPModelElement)
    assert result.name == "Unit"


def test_model_element_get_stereotypes_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"stereotypes": coll})
    element = IRPModelElement(fake)

    result = element.stereotypes

    assert isinstance(result, IRPCollection)


def test_model_element_get_tag_wraps_result() -> None:
    tag_fake = make_fake_element("Tag", properties={"name": "MyTag"})
    fake = make_fake_element("Class", getTag=tag_fake)
    element = IRPModelElement(fake)

    result = element.get_tag("MyTag")

    assert isinstance(result, IRPModelElement)
    assert result.name == "MyTag"
    fake.getTag.assert_called_once_with("MyTag")


def test_model_element_get_template_parameters_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Class", properties={"templateParameters": coll})
    element = IRPModelElement(fake)

    result = element.template_parameters

    assert isinstance(result, IRPCollection)


def test_model_element_get_ti_wraps_result() -> None:
    ti_fake = make_fake_element("TemplateInstantiation", properties={"name": "TI"})
    fake = make_fake_element("Class", properties={"ti": ti_fake})
    element = IRPModelElement(fake)

    result = element.ti

    assert isinstance(result, IRPModelElement)
    assert result.name == "TI"


def test_model_element_get_tool_tip_html_returns_str() -> None:
    fake = make_fake_element("Class", getToolTipHTML="<b>tip</b>")
    element = IRPModelElement(fake)

    assert element.get_tool_tip_html() == "<b>tip</b>"


def test_model_element_get_user_defined_meta_class_returns_str() -> None:
    fake = make_fake_element("Class", properties={"userDefinedMetaClass": "NewTerm"})
    element = IRPModelElement(fake)

    assert element.user_defined_meta_class == "NewTerm"


def test_model_element_has_nested_elements_returns_int() -> None:
    fake = make_fake_element("Class", hasNestedElements=1)
    element = IRPModelElement(fake)

    assert element.has_nested_elements() == 1
    fake.hasNestedElements.assert_called_once_with()


def test_model_element_has_panel_widget_returns_int() -> None:
    fake = make_fake_element("Class", hasPanelWidget=0)
    element = IRPModelElement(fake)

    assert element.has_panel_widget() == 0
    fake.hasPanelWidget.assert_called_once_with()


def test_model_element_high_light_element_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.high_light_element()

    fake.highLightElement.assert_called_once_with()


def test_model_element_is_a_template_returns_int() -> None:
    fake = make_fake_element("Class", isATemplate=0)
    element = IRPModelElement(fake)

    assert element.is_a_template() == 0
    fake.isATemplate.assert_called_once_with()


def test_model_element_is_description_rtf_returns_int() -> None:
    fake = make_fake_element("Class", isDescriptionRTF=1)
    element = IRPModelElement(fake)

    assert element.is_description_rtf() == 1
    fake.isDescriptionRTF.assert_called_once_with()


def test_model_element_is_display_name_rtf_returns_int() -> None:
    fake = make_fake_element("Class", isDisplayNameRTF=0)
    element = IRPModelElement(fake)

    assert element.is_display_name_rtf() == 0
    fake.isDisplayNameRTF.assert_called_once_with()


def test_model_element_is_modified_returns_int() -> None:
    fake = make_fake_element("Class", isModified=1)
    element = IRPModelElement(fake)

    assert element.is_modified() == 1
    fake.isModified.assert_called_once_with()


def test_model_element_is_remote_returns_int() -> None:
    fake = make_fake_element("Class", isRemote=0)
    element = IRPModelElement(fake)

    assert element.is_remote() == 0
    fake.isRemote.assert_called_once_with()


def test_model_element_locate_in_browser_returns_int() -> None:
    fake = make_fake_element("Class", locateInBrowser=1)
    element = IRPModelElement(fake)

    assert element.locate_in_browser() == 1
    fake.locateInBrowser.assert_called_once_with()


def test_model_element_open_features_dialog_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.open_features_dialog(1)

    fake.openFeaturesDialog.assert_called_once_with(1)


def test_model_element_remove_property_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.remove_property("key")

    fake.removeProperty.assert_called_once_with("key")


def test_model_element_remove_redefines_unwraps_argument() -> None:
    redefine = IRPModelElement(make_fake_element("Element"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.remove_redefines(redefine)

    fake.removeRedefines.assert_called_once_with(redefine._com)


def test_model_element_remove_stereotype_unwraps_argument() -> None:
    stereotype = IRPModelElement(make_fake_element("Stereotype"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.remove_stereotype(cast(IRPStereotype, stereotype))

    fake.removeStereotype.assert_called_once_with(stereotype._com)


def test_model_element_set_decoration_style_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.set_decoration_style("Bold")

    fake.setDecorationStyle.assert_called_once_with("Bold")


def test_model_element_set_description_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.description = "A description"

    assert fake.description == "A description"


def test_model_element_set_description_and_hyperlinks_unwraps_targets() -> None:
    targets = IRPCollection(make_fake_collection([]))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.set_description_and_hyperlinks("{\\rtf}", targets)

    fake.setDescriptionAndHyperlinks.assert_called_once_with("{\\rtf}", targets._com)


def test_model_element_set_description_html_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    with pytest.raises(NotImplementedError):
        element.set_description_html("<p>desc</p>")


def test_model_element_set_description_rtf_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.description_rtf = "{\\rtf}"

    assert fake.descriptionRTF == "{\\rtf}"


def test_model_element_set_display_name_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.display_name = "Label"

    assert fake.displayName == "Label"


def test_model_element_set_display_name_rtf_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.set_display_name_rtf("{\\rtf}")

    fake.setDisplayNameRTF.assert_called_once_with("{\\rtf}")


def test_model_element_set_guid_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.guid = "new-guid"

    assert fake.GUID == "new-guid"


def test_model_element_set_is_show_display_name_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.is_show_display_name = 1

    assert fake.isShowDisplayName == 1


def test_model_element_set_main_diagram_unwraps_argument() -> None:
    diagram = IRPModelElement(make_fake_element("Diagram"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.main_diagram = cast(IRPDiagram, diagram)

    assert fake.mainDiagram == diagram._com


def test_model_element_set_of_template_unwraps_argument() -> None:
    template = IRPModelElement(make_fake_element("Element"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.of_template = template

    assert fake.ofTemplate == template._com


def test_model_element_set_owner_unwraps_argument() -> None:
    owner = IRPModelElement(make_fake_element("Element"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.owner = owner

    assert fake.owner == owner._com


def test_model_element_set_property_value_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.set_property_value("key", "value")

    fake.setPropertyValue.assert_called_once_with("key", "value")


def test_model_element_set_requirement_traceability_handle_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.requirement_traceability_handle = 42

    assert fake.requirementTraceabilityHandle == 42


def test_model_element_set_tag_context_value_unwraps_args_and_wraps_result() -> None:
    tag = IRPModelElement(make_fake_element("Tag"))
    elements = IRPCollection(make_fake_collection([]))
    multiplicities = IRPCollection(make_fake_collection([]))
    result_fake = make_fake_element("Tag", properties={"name": "CtxTag"})
    fake = make_fake_element("Class", setTagContextValue=result_fake)
    element = IRPModelElement(fake)

    result = element.set_tag_context_value(cast(IRPTag, tag), elements, multiplicities)

    assert isinstance(result, IRPModelElement)
    assert result.name == "CtxTag"
    fake.setTagContextValue.assert_called_once_with(tag._com, elements._com, multiplicities._com)


def test_model_element_set_tag_element_value_unwraps_args_and_wraps_result() -> None:
    tag = IRPModelElement(make_fake_element("Tag"))
    val = IRPModelElement(make_fake_element("Element"))
    result_fake = make_fake_element("Tag", properties={"name": "ElemTag"})
    fake = make_fake_element("Class", setTagElementValue=result_fake)
    element = IRPModelElement(fake)

    result = element.set_tag_element_value(cast(IRPTag, tag), val)

    assert isinstance(result, IRPModelElement)
    assert result.name == "ElemTag"
    fake.setTagElementValue.assert_called_once_with(tag._com, val._com)


def test_model_element_set_tag_value_unwraps_tag_and_wraps_result() -> None:
    tag = IRPModelElement(make_fake_element("Tag"))
    result_fake = make_fake_element("Tag", properties={"name": "ValTag"})
    fake = make_fake_element("Class", setTagValue=result_fake)
    element = IRPModelElement(fake)

    result = element.set_tag_value(cast(IRPTag, tag), "a value")

    assert isinstance(result, IRPModelElement)
    assert result.name == "ValTag"
    fake.setTagValue.assert_called_once_with(tag._com, "a value")


def test_model_element_set_ti_unwraps_argument() -> None:
    ti = IRPModelElement(make_fake_element("TemplateInstantiation"))
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.ti = cast(IRPTemplateInstantiation, ti)

    assert fake.ti == ti._com


def test_model_element_synchronize_template_instantiation_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    element = IRPModelElement(fake)

    element.synchronize_template_instantiation()

    fake.synchronizeTemplateInstantiation.assert_called_once_with()


def test_rp_model_element_uses_no_legacy_dual_binding_helpers() -> None:
    """IRPModelElement's own methods call exactly one pywin32 member — no name probing."""
    import ast as _ast

    sources = (
        Path(core_module.__file__).read_text(encoding="utf-8"),
        Path(model_element_module.__file__).read_text(encoding="utf-8"),
    )
    offenders: list[str] = []
    for source in sources:
        tree = _ast.parse(source)
        for node in tree.body:
            if not isinstance(node, _ast.ClassDef):
                continue
            if node.name not in ("IRPModelElement", "ComHelper"):
                continue
            for fn in node.body:
                if not isinstance(fn, _ast.FunctionDef):
                    continue
                if node.name == "ComHelper" and fn.name not in ("wrap",):
                    continue  # the legacy forwarder definitions stay until the last class migrates
                if fn.name == "get_rmm_url":
                    continue  # documented_unavailable: getRmmUrl/rmmUrl absent from the pywin32 catalog — site left unchanged
                for sub in _ast.walk(fn):
                    if isinstance(sub, _ast.Call) and isinstance(sub.func, _ast.Attribute):
                        if sub.func.attr in ("_get_method_or_property", "_set_method_or_property"):
                            offenders.append(f"{node.name}.{fn.name}:{sub.lineno}")
    assert offenders == []


def test_rp_collection_uses_no_legacy_dual_binding_helpers() -> None:
    """IRPCollection's own methods call exactly one pywin32 member — no name probing."""
    import ast as _ast

    from rhapsody_cli.models.com.telelogic.rhapsody.core import irp_collection as irp_collection_module

    source = Path(irp_collection_module.__file__).read_text(encoding="utf-8")
    tree = _ast.parse(source)
    collection_cls = next(node for node in tree.body if isinstance(node, _ast.ClassDef) and node.name == "IRPCollection")
    offenders: list[str] = []
    for fn in collection_cls.body:
        if not isinstance(fn, _ast.FunctionDef):
            continue
        for sub in _ast.walk(fn):
            if isinstance(sub, _ast.Call) and isinstance(sub.func, _ast.Attribute):
                if sub.func.attr in ("_get_method_or_property", "_set_method_or_property"):
                    offenders.append(f"{fn.name}:{sub.lineno}:legacy-helper")
    for fn in collection_cls.body:
        if not isinstance(fn, _ast.FunctionDef):
            continue
        for sub in _ast.walk(fn):
            if isinstance(sub, _ast.Call) and isinstance(sub.func, _ast.Name) and sub.func.id == "hasattr":
                offenders.append(f"{fn.name}:{sub.lineno}:hasattr-probe")
    assert offenders == []


def test_core_module_uses_future_annotations_and_unquoted_type_references() -> None:
    """Synced wrappers use `from __future__ import annotations` with unquoted type references."""
    source = Path(model_element_module.__file__).read_text(encoding="utf-8")

    assert "from __future__ import annotations" in source
    assert re.search(r'cast\("', source) is None
    assert re.search(r'(-> |: )"[A-Z][A-Za-z]*"', source) is None
