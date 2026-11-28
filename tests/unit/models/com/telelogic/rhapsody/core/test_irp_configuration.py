"""Fake-COM unit tests for the IRPConfiguration wrapper."""

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPComponent, IRPConfiguration, IRPInstance, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_configuration_is_registered() -> None:
    fake = make_fake_element("Configuration", properties={"name": "C1"})
    assert isinstance(IRPModelElement.wrap(fake), IRPConfiguration)


def test_additional_sources() -> None:
    fake = make_fake_element("Configuration", properties={"additionalSources": "value"})
    assert IRPConfiguration(fake).additional_sources == "value"


def test_additional_sources_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "updated"
    IRPConfiguration(fake).additional_sources = value
    assert fake.additionalSources == value


def test_all_elements_in_instrumentation_scope() -> None:
    fake = make_fake_element("Configuration", properties={"allElementsInInstrumentationScope": 1})
    assert IRPConfiguration(fake).all_elements_in_instrumentation_scope == 1


def test_all_elements_in_instrumentation_scope_setter() -> None:
    fake = make_fake_element("Configuration")
    IRPConfiguration(fake).all_elements_in_instrumentation_scope = 1
    assert fake.allElementsInInstrumentationScope == 1


def test_build_set() -> None:
    fake = make_fake_element("Configuration", properties={"buildSet": "value"})
    assert IRPConfiguration(fake).build_set == "value"


def test_build_set_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "updated"
    IRPConfiguration(fake).build_set = value
    assert fake.buildSet == value


def test_compiler_switches() -> None:
    fake = make_fake_element("Configuration", properties={"compilerSwitches": "value"})
    assert IRPConfiguration(fake).compiler_switches == "value"


def test_compiler_switches_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "updated"
    IRPConfiguration(fake).compiler_switches = value
    assert fake.compilerSwitches == value


def test_generate_code_for_actors() -> None:
    fake = make_fake_element("Configuration", properties={"generateCodeForActors": 1})
    assert IRPConfiguration(fake).generate_code_for_actors == 1


def test_generate_code_for_actors_setter() -> None:
    fake = make_fake_element("Configuration")
    value = 1
    IRPConfiguration(fake).generate_code_for_actors = value
    assert fake.generateCodeForActors == value


def test_include_path() -> None:
    fake = make_fake_element("Configuration", properties={"includePath": "value"})
    assert IRPConfiguration(fake).include_path == "value"


def test_include_path_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "updated"
    IRPConfiguration(fake).include_path = value
    assert fake.includePath == value


def test_initial_instances() -> None:
    fake = make_fake_element("Configuration", properties={"initialInstances": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPConfiguration(fake).initial_instances) == 1


def test_initialization_code() -> None:
    fake = make_fake_element("Configuration", properties={"initializationCode": "value"})
    assert IRPConfiguration(fake).initialization_code == "value"


def test_initialization_code_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "updated"
    IRPConfiguration(fake).initialization_code = value
    assert fake.initializationCode == value


def test_instrumentation_scope() -> None:
    fake = make_fake_element("Configuration", properties={"instrumentationScope": make_fake_collection([make_fake_element("Unit")])})
    assert len(IRPConfiguration(fake).instrumentation_scope) == 1


def test_instrumentation_type() -> None:
    fake = make_fake_element("Configuration", properties={"instrumentationType": "none"})
    assert IRPConfiguration(fake).instrumentation_type == "none"


def test_instrumentation_type_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "none"
    IRPConfiguration(fake).instrumentation_type = value
    assert fake.instrumentationType == value


def test_libraries() -> None:
    fake = make_fake_element("Configuration", properties={"libraries": "value"})
    assert IRPConfiguration(fake).libraries == "value"


def test_libraries_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "updated"
    IRPConfiguration(fake).libraries = value
    assert fake.libraries == value


def test_link_switches() -> None:
    fake = make_fake_element("Configuration", properties={"linkSwitches": "value"})
    assert IRPConfiguration(fake).link_switches == "value"


def test_link_switches_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "updated"
    IRPConfiguration(fake).link_switches = value
    assert fake.linkSwitches == value


def test_scope_type() -> None:
    fake = make_fake_element("Configuration", properties={"scopeType": "explicit"})
    assert IRPConfiguration(fake).scope_type == "explicit"


def test_scope_type_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "explicit"
    IRPConfiguration(fake).scope_type = value
    assert fake.scopeType == value


def test_standard_headers() -> None:
    fake = make_fake_element("Configuration", properties={"standardHeaders": "value"})
    assert IRPConfiguration(fake).standard_headers == "value"


def test_standard_headers_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "updated"
    IRPConfiguration(fake).standard_headers = value
    assert fake.standardHeaders == value


def test_statechart_implementation() -> None:
    fake = make_fake_element("Configuration", properties={"statechartImplementation": "flat"})
    assert IRPConfiguration(fake).statechart_implementation == "flat"


def test_statechart_implementation_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "flat"
    IRPConfiguration(fake).statechart_implementation = value
    assert fake.statechartImplementation == value


def test_time_model() -> None:
    fake = make_fake_element("Configuration", properties={"timeModel": "real"})
    assert IRPConfiguration(fake).time_model == "real"


def test_time_model_setter() -> None:
    fake = make_fake_element("Configuration")
    value = "real"
    IRPConfiguration(fake).time_model = value
    assert fake.timeModel == value


def test_add_initial_instance() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    instance = IRPInstance(make_fake_element("Instance"))
    fake.addInitialInstance.return_value = None
    coll.add_initial_instance(instance)
    fake.addInitialInstance.assert_called_once_with(instance._com)


def test_add_package_to_instrumentation_scope() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    package = IRPUnit(make_fake_element("Unit"))
    fake.addPackageToInstrumentationScope.return_value = None
    coll.add_package_to_instrumentation_scope(package)
    fake.addPackageToInstrumentationScope.assert_called_once_with(package._com)


def test_add_to_instrumentation_scope() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    element = IRPUnit(make_fake_element("Unit"))
    fake.addToInstrumentationScope.return_value = None
    coll.add_to_instrumentation_scope(element)
    fake.addToInstrumentationScope.assert_called_once_with(element._com)


def test_delete_initial_instance() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    instance = IRPInstance(make_fake_element("Instance"))
    fake.deleteInitialInstance.return_value = None
    coll.delete_initial_instance(instance)
    fake.deleteInitialInstance.assert_called_once_with(instance._com)


def test_get_directory() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    fake.getDirectory.return_value = "value"
    assert coll.get_directory() == "value"


def test_get_executable_name() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    fake.getExecutableName.return_value = "value"
    assert coll.get_executable_name() == "value"


def test_get_its_component() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    fake.getItsComponent.return_value = make_fake_element("Unit", properties={"name": "R1"})
    assert coll.get_its_component().name == "R1"


def test_get_main_name() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    fake.getMainName.return_value = "value"
    assert coll.get_main_name() == "value"


def test_get_makefile_name() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    fake.getMakefileName.return_value = "value"
    assert coll.get_makefile_name() == "value"


def test_get_target_name() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    fake.getTargetName.return_value = "value"
    assert coll.get_target_name() == "value"


def test_needs_code_generation() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    fake.needsCodeGeneration.return_value = 1
    assert coll.needs_code_generation() == 1


def test_remove_from_instrumentation_scope() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    element = IRPUnit(make_fake_element("Unit"))
    fake.removeFromInstrumentationScope.return_value = None
    coll.remove_from_instrumentation_scope(element)
    fake.removeFromInstrumentationScope.assert_called_once_with(element._com)


def test_remove_package_from_instrumentation_scope() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    package = IRPUnit(make_fake_element("Unit"))
    fake.removePackageFromInstrumentationScope.return_value = None
    coll.remove_package_from_instrumentation_scope(package)
    fake.removePackageFromInstrumentationScope.assert_called_once_with(package._com)


def test_set_directory() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    value = "V"
    fake.setDirectory.return_value = None
    coll.set_directory(value)
    fake.setDirectory.assert_called_once_with(value)


def test_set_its_component() -> None:
    fake = make_fake_element("Configuration")
    coll = IRPConfiguration(fake)
    component = IRPComponent(make_fake_element("Component"))
    fake.setItsComponent.return_value = None
    coll.set_its_component(component)
    fake.setItsComponent.assert_called_once_with(component._com)


def test_get_path() -> None:
    configuration = IRPConfiguration(make_fake_element("Configuration"))
    with pytest.raises(NotImplementedError):
        configuration.get_path()


def test_set_path() -> None:
    configuration = IRPConfiguration(make_fake_element("Configuration"))
    with pytest.raises(NotImplementedError):
        configuration.set_path("path")
