"""Fake-COM unit tests for the IRPComponent wrapper."""

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPComponent, IRPConfiguration, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_component_is_registered() -> None:
    fake = make_fake_element("Component", properties={"name": "Comp1"})
    wrapped = IRPModelElement.wrap(fake)
    assert isinstance(wrapped, IRPComponent)
    assert wrapped.name == "Comp1"


def test_additional_sources_returns_string() -> None:
    fake = make_fake_element("Component", properties={"additionalSources": "value"})
    assert IRPComponent(fake).additional_sources == "value"


def test_additional_sources_setter() -> None:
    fake = make_fake_element("Component")
    IRPComponent(fake).additional_sources = "updated"
    assert fake.additionalSources == "updated"


def test_build_type_returns_string() -> None:
    fake = make_fake_element("Component", properties={"buildType": "value"})
    assert IRPComponent(fake).build_type == "value"


def test_build_type_setter() -> None:
    fake = make_fake_element("Component")
    IRPComponent(fake).build_type = "updated"
    assert fake.buildType == "updated"


def test_configurations_returns_collection() -> None:
    fake = make_fake_element("Component", properties={"configurations": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPComponent(fake).configurations) == 1


def test_files_returns_collection() -> None:
    fake = make_fake_element("Component", properties={"files": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPComponent(fake).files) == 1


def test_include_path_returns_string() -> None:
    fake = make_fake_element("Component", properties={"includePath": "value"})
    assert IRPComponent(fake).include_path == "value"


def test_include_path_setter() -> None:
    fake = make_fake_element("Component")
    IRPComponent(fake).include_path = "updated"
    assert fake.includePath == "updated"


def test_libraries_returns_string() -> None:
    fake = make_fake_element("Component", properties={"libraries": "value"})
    assert IRPComponent(fake).libraries == "value"


def test_libraries_setter() -> None:
    fake = make_fake_element("Component")
    IRPComponent(fake).libraries = "updated"
    assert fake.libraries == "updated"


def test_nested_components_returns_collection() -> None:
    fake = make_fake_element("Component", properties={"nestedComponents": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPComponent(fake).nested_components) == 1


def test_panel_diagrams_returns_collection() -> None:
    fake = make_fake_element("Component", properties={"panelDiagrams": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPComponent(fake).panel_diagrams) == 1


def test_scope_by_selected_elements_returns_collection() -> None:
    fake = make_fake_element("Component", properties={"scopeBySelectedElements": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPComponent(fake).scope_by_selected_elements) == 1


def test_scope_by_selected_elements_setter() -> None:
    fake = make_fake_element("Component")
    collection = make_fake_collection([make_fake_element("Unit")])
    IRPComponent(fake).scope_by_selected_elements = IRPCollection(collection)
    assert fake.scopeBySelectedElements is collection


def test_scope_elements_returns_collection() -> None:
    fake = make_fake_element("Component", properties={"scopeElements": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPComponent(fake).scope_elements) == 1


def test_standard_headers_returns_string() -> None:
    fake = make_fake_element("Component", properties={"standardHeaders": "value"})
    assert IRPComponent(fake).standard_headers == "value"


def test_standard_headers_setter() -> None:
    fake = make_fake_element("Component")
    IRPComponent(fake).standard_headers = "updated"
    assert fake.standardHeaders == "updated"


def test_variation_points_returns_collection() -> None:
    fake = make_fake_element("Component", properties={"variationPoints": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPComponent(fake).variation_points) == 1


def test_add_configuration_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    name = "value"
    result_obj = make_fake_element("Configuration", properties={"name": "R1"})
    fake.addConfiguration.return_value = result_obj
    result = component.add_configuration(name)
    assert result.name == "R1"


def test_add_file_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    name = "value"
    result_obj = make_fake_element("Unit", properties={"name": "R1"})
    fake.addFile.return_value = result_obj
    result = component.add_file(name)
    assert result.name == "R1"


def test_add_folder_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    name = "value"
    result_obj = make_fake_element("Unit", properties={"name": "R1"})
    fake.addFolder.return_value = result_obj
    result = component.add_folder(name)
    assert result.name == "R1"


def test_add_nested_component_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    name = "value"
    result_obj = make_fake_element("Unit", properties={"name": "R1"})
    fake.addNestedComponent.return_value = result_obj
    result = component.add_nested_component(name)
    assert result.name == "R1"


def test_add_scope_element_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    element = IRPUnit(make_fake_element("Unit"))
    component.add_scope_element(element)
    fake.addScopeElement.assert_called_once_with(element._com)


def test_add_scope_element_without_aggregates_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    element = IRPUnit(make_fake_element("Unit"))
    component.add_scope_element_without_aggregates(element)
    fake.addScopeElementWithoutAggregates.assert_called_once_with(element._com)


def test_add_to_scope_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    element = IRPUnit(make_fake_element("Unit"))
    component.add_to_scope(element)
    fake.addToScope.assert_called_once_with(element._com)


def test_all_elements_in_scope_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    fake.allElementsInScope.return_value = make_fake_collection([make_fake_element("Unit", properties={"name": "U1"})])
    result = component.all_elements_in_scope()
    assert isinstance(result, IRPCollection)
    assert len(result) == 1


def test_delete_configuration_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    configuration = IRPConfiguration(make_fake_element("Configuration"))
    component.delete_configuration(configuration)
    fake.deleteConfiguration.assert_called_once_with(configuration._com)


def test_delete_file_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    file = IRPUnit(make_fake_element("Unit"))
    component.delete_file(file)
    fake.deleteFile.assert_called_once_with(file._com)


def test_find_configuration_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    name = "value"
    result_obj = make_fake_element("Configuration", properties={"name": "R1"})
    fake.findConfiguration.return_value = result_obj
    result = component.find_configuration(name)
    assert result is not None
    assert result.name == "R1"


def test_get_config_by_dependency_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)

    result_obj = make_fake_element("Configuration", properties={"name": "R1"})
    fake.getConfigByDependency.return_value = result_obj
    result = component.get_config_by_dependency()
    assert result is not None
    assert result.name == "R1"


def test_get_file_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    name = "value"
    result_obj = make_fake_element("Unit", properties={"name": "R1"})
    fake.getFile.return_value = result_obj
    result = component.get_file(name)
    assert result.name == "R1"


def test_get_file_name_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    fake.getFileName.return_value = "value"
    assert component.get_file_name() == "value"


def test_get_model_element_file_name_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    fake.getModelElementFileName.return_value = "value"
    assert component.get_model_element_file_name() == "value"


def test_get_package_file_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    fake.getPackageFile.return_value = "value"
    assert component.get_package_file() == "value"


def test_get_possible_variants_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    fake.getPossibleVariants.return_value = make_fake_collection([make_fake_element("Unit", properties={"name": "U1"})])
    result = component.get_possible_variants()
    assert isinstance(result, IRPCollection)
    assert len(result) == 1


def test_get_scope_elements_by_category_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    category = "value"
    fake.getScopeElementsByCategory.return_value = make_fake_collection([make_fake_element("Unit", properties={"name": "U1"})])
    result = component.get_scope_elements_by_category(category)
    assert isinstance(result, IRPCollection)
    assert len(result) == 1


def test_get_variant_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    fake.getVariant.return_value = "value"
    assert component.get_variant() == "value"


def test_is_directory_per_model_component_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    fake.isDirectoryPerModelComponent.return_value = 1
    assert component.is_directory_per_model_component() == 1


def test_remove_scope_element_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    element = IRPUnit(make_fake_element("Unit"))
    component.remove_scope_element(element)
    fake.removeScopeElement.assert_called_once_with(element._com)


def test_set_variant_delegates() -> None:
    fake = make_fake_element("Component")
    component = IRPComponent(fake)
    value = "value"
    component.set_variant(value)
    fake.setVariant.assert_called_once_with(value)


def test_unavailable_members_raise_before_dispatch() -> None:
    component = IRPComponent(make_fake_element("Component"))
    with pytest.raises(NotImplementedError):
        component.get_path()
    with pytest.raises(NotImplementedError):
        component.set_path("value")
    with pytest.raises(NotImplementedError):
        component.update_contained_diagrams_on_server()
