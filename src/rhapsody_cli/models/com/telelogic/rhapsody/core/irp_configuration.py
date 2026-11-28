"""Wraps ``com.telelogic.rhapsody.core.IRPConfiguration``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_instance import IRPInstance


class IRPConfiguration(IRPUnit):
    """Wraps ``IRPConfiguration``: a configuration that extends ``IRPUnit``."""

    # IRPConfiguration method parity checklist:
    # [x] add_initial_instance  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] add_package_to_instrumentation_scope  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] add_to_instrumentation_scope  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] delete_initial_instance  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_additional_sources  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_all_elements_in_instrumentation_scope  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_build_set  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_compiler_switches  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_directory  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_executable_name  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_generate_code_for_actors  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_include_path  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_initial_instances  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_initialization_code  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_instrumentation_scope  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_instrumentation_type  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_its_component  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_libraries  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_link_switches  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_main_name  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_makefile_name  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_path  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_scope_type  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_standard_headers  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_statechart_implementation  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_target_name  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] get_time_model  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] needs_code_generation  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] remove_from_instrumentation_scope  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] remove_package_from_instrumentation_scope  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_additional_sources  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_all_elements_in_instrumentation_scope  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_build_set  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_compiler_switches  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] set_directory  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] set_generate_code_for_actors  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_include_path  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_initialization_code  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_instrumentation_type  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] set_its_component  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] set_libraries  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_link_switches  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_scope_type  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_standard_headers  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_statechart_implementation  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] set_time_model  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [inherited] irp_unit / irp_model_element methods (covered by rp_unit / rp_model_element checklists)
    # No deprecated IRPConfiguration methods.

    def add_initial_instance(self, instance: IRPInstance) -> None:
        """Adds an initial instance to the configuration.

        Args:
            instance: The instance to add.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::addInitialInstance(IRPInstance instance)
        """
        self.call_com(lambda: self._com.addInitialInstance(instance._com))

    def add_package_to_instrumentation_scope(self, package: IRPUnit) -> None:
        """Adds a package to the instrumentation scope.

        Args:
            package: The package to add to instrumentation scope.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::addPackageToInstrumentationScope(IRPPackage package)
        """
        self.call_com(lambda: self._com.addPackageToInstrumentationScope(package._com))

    def add_to_instrumentation_scope(self, element: IRPUnit) -> None:
        """Adds an element to the instrumentation scope.

        Args:
            element: The element to add to instrumentation scope.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::addToInstrumentationScope(IRPModelElement element)
        """
        self.call_com(lambda: self._com.addToInstrumentationScope(element._com))

    def delete_initial_instance(self, instance: IRPInstance) -> None:
        """Deletes an initial instance from the configuration.

        Args:
            instance: The instance to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::deleteInitialInstance(IRPInstance instance)
        """
        self.call_com(lambda: self._com.deleteInitialInstance(instance._com))

    @property
    def additional_sources(self) -> str:
        """COM-backed ``additionalSources`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_additional_sources()
        """
        return str(self.get_com_property(self._com, "additionalSources"))

    @additional_sources.setter
    def additional_sources(self, value: str) -> None:
        """Writes the COM-backed ``additionalSources`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setAdditionalSources(value)
        """
        self.set_com_property(self._com, "additionalSources", value)

    @property
    def all_elements_in_instrumentation_scope(self) -> int:
        """Checks whether instrumentation applies to all or selected elements.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getAllElementsInInstrumentationScope()
        """
        return int(self.get_com_property(self._com, "allElementsInInstrumentationScope"))

    @all_elements_in_instrumentation_scope.setter
    def all_elements_in_instrumentation_scope(self, all_elements_in_instrumentation_scope: int) -> None:
        """Specifies whether instrumentation applies to all elements.

        Args:
            all_elements_in_instrumentation_scope: ``1`` to apply instrumentation to all elements, ``0`` for selected elements.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setAllElementsInInstrumentationScope(int allElementsInInstrumentationScope)
        """
        self.set_com_property(self._com, "allElementsInInstrumentationScope", all_elements_in_instrumentation_scope)

    @property
    def build_set(self) -> str:
        """COM-backed ``buildSet`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_build_set()
        """
        return str(self.get_com_property(self._com, "buildSet"))

    @build_set.setter
    def build_set(self, value: str) -> None:
        """Writes the COM-backed ``buildSet`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setBuildSet(value)
        """
        self.set_com_property(self._com, "buildSet", value)

    @property
    def compiler_switches(self) -> str:
        """COM-backed ``compilerSwitches`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_compiler_switches()
        """
        return str(self.get_com_property(self._com, "compilerSwitches"))

    @compiler_switches.setter
    def compiler_switches(self, value: str) -> None:
        """Writes the COM-backed ``compilerSwitches`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setCompilerSwitches(value)
        """
        self.set_com_property(self._com, "compilerSwitches", value)

    def get_directory(self) -> str:
        """Returns the directory for the configuration.

        Returns:
            The directory string.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getDirectory()
        """
        return str(self.call_com(lambda: self._com.getDirectory()))

    def get_executable_name(self) -> str:
        """Returns the executable name for the configuration.

        Returns:
            The executable name string.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getExecutableName()
        """
        return str(self.call_com(lambda: self._com.getExecutableName()))

    @property
    def generate_code_for_actors(self) -> int:
        """COM-backed ``generateCodeForActors`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_generate_code_for_actors()
        """
        return int(self.get_com_property(self._com, "generateCodeForActors"))

    @generate_code_for_actors.setter
    def generate_code_for_actors(self, value: int) -> None:
        """Writes the COM-backed ``generateCodeForActors`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setGenerateCodeForActors(value)
        """
        self.set_com_property(self._com, "generateCodeForActors", value)

    @property
    def include_path(self) -> str:
        """COM-backed ``includePath`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_include_path()
        """
        return str(self.get_com_property(self._com, "includePath"))

    @include_path.setter
    def include_path(self, value: str) -> None:
        """Writes the COM-backed ``includePath`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setIncludePath(value)
        """
        self.set_com_property(self._com, "includePath", value)

    @property
    def initial_instances(self) -> IRPCollection:
        """COM-backed ``initialInstances`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_initial_instances()
        """
        return IRPCollection(self.get_com_property(self._com, "initialInstances"))

    @property
    def initialization_code(self) -> str:
        """COM-backed ``initializationCode`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_initialization_code()
        """
        return str(self.get_com_property(self._com, "initializationCode"))

    @initialization_code.setter
    def initialization_code(self, value: str) -> None:
        """Writes the COM-backed ``initializationCode`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setInitializationCode(value)
        """
        self.set_com_property(self._com, "initializationCode", value)

    @property
    def instrumentation_scope(self) -> IRPCollection:
        """COM-backed ``instrumentationScope`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_instrumentation_scope()
        """
        return IRPCollection(self.get_com_property(self._com, "instrumentationScope"))

    @property
    def instrumentation_type(self) -> str:
        """Returns the instrumentation type for the configuration.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getInstrumentationType()
        """
        return str(self.get_com_property(self._com, "instrumentationType"))

    @instrumentation_type.setter
    def instrumentation_type(self, value: str) -> None:
        """Specifies the instrumentation type for the configuration.

        Args:
            value: The instrumentation type.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setInstrumentationType(java.lang.String instrumentationType)
        """
        self.set_com_property(self._com, "instrumentationType", value)

    def get_its_component(self) -> IRPComponent:
        """Returns the component for this configuration.

        Returns:
            The wrapped ``IRPComponent``.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getItsComponent()
        """
        return cast("IRPComponent", self.wrap(self.call_com(lambda: self._com.getItsComponent())))

    @property
    def libraries(self) -> str:
        """COM-backed ``libraries`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_libraries()
        """
        return str(self.get_com_property(self._com, "libraries"))

    @libraries.setter
    def libraries(self, value: str) -> None:
        """Writes the COM-backed ``libraries`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setLibraries(value)
        """
        self.set_com_property(self._com, "libraries", value)

    @property
    def link_switches(self) -> str:
        """COM-backed ``linkSwitches`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_link_switches()
        """
        return str(self.get_com_property(self._com, "linkSwitches"))

    @link_switches.setter
    def link_switches(self, value: str) -> None:
        """Writes the COM-backed ``linkSwitches`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setLinkSwitches(value)
        """
        self.set_com_property(self._com, "linkSwitches", value)

    def get_main_name(self) -> str:
        """Returns the main name for the configuration.

        Returns:
            The main name string.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getMainName()
        """
        return str(self.call_com(lambda: self._com.getMainName()))

    def get_makefile_name(self) -> str:
        """Returns the makefile name for the configuration.

        Returns:
            The makefile name string.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getMakefileName()
        """
        return str(self.call_com(lambda: self._com.getMakefileName()))

    def get_path(self) -> str:
        """JavaDoc ``getPath``; absent from pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getPath()
        """
        raise NotImplementedError("getPath is not exposed by pywin32")

    def set_path(self, value: str) -> None:
        """JavaDoc ``setPath``; absent from pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setPath(java.lang.String path)
        """
        raise NotImplementedError("setPath is not exposed by pywin32")

    @property
    def scope_type(self) -> str:
        """Returns the scope type for the configuration.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getScopeType()
        """
        return str(self.get_com_property(self._com, "scopeType"))

    @scope_type.setter
    def scope_type(self, value: str) -> None:
        """Specifies the scope type for the configuration.

        Args:
            value: The scope type.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setScopeType(java.lang.String scopeType)
        """
        self.set_com_property(self._com, "scopeType", value)

    @property
    def standard_headers(self) -> str:
        """COM-backed ``standardHeaders`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::get_standard_headers()
        """
        return str(self.get_com_property(self._com, "standardHeaders"))

    @standard_headers.setter
    def standard_headers(self, value: str) -> None:
        """Writes the COM-backed ``standardHeaders`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setStandardHeaders(value)
        """
        self.set_com_property(self._com, "standardHeaders", value)

    @property
    def statechart_implementation(self) -> str:
        """Returns the statechart implementation for the configuration.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getStatechartImplementation()
        """
        return str(self.get_com_property(self._com, "statechartImplementation"))

    @statechart_implementation.setter
    def statechart_implementation(self, value: str) -> None:
        """Specifies the statechart implementation for the configuration.

        Args:
            value: The statechart implementation, such as ``flat`` or ``reusable``.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setStatechartImplementation(java.lang.String statechartImplementation)
        """
        self.set_com_property(self._com, "statechartImplementation", value)

    def get_target_name(self) -> str:
        """Returns the target name for the configuration.

        Returns:
            The target name string.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getTargetName()
        """
        return str(self.call_com(lambda: self._com.getTargetName()))

    @property
    def time_model(self) -> str:
        """Returns the time model for the configuration.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::getTimeModel()
        """
        return str(self.get_com_property(self._com, "timeModel"))

    @time_model.setter
    def time_model(self, value: str) -> None:
        """Specifies the time model for the configuration.

        Args:
            value: The time model, such as ``real`` or ``simulated``.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setTimeModel(java.lang.String timeModel)
        """
        self.set_com_property(self._com, "timeModel", value)

    def needs_code_generation(self) -> int:
        """Returns whether code generation is needed.

        Returns:
            1 if needed, 0 if not.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::needsCodeGeneration()
        """
        return int(self.call_com(lambda: self._com.needsCodeGeneration()))

    def remove_from_instrumentation_scope(self, element: IRPUnit) -> None:
        """Removes an element from instrumentation scope.

        Args:
            element: The element to remove from instrumentation scope.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::removeFromInstrumentationScope(IRPModelElement element)
        """
        self.call_com(lambda: self._com.removeFromInstrumentationScope(element._com))

    def remove_package_from_instrumentation_scope(self, package: IRPUnit) -> None:
        """Removes a package from instrumentation scope.

        Args:
            package: The package to remove from instrumentation scope.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::removePackageFromInstrumentationScope(IRPPackage package)
        """
        self.call_com(lambda: self._com.removePackageFromInstrumentationScope(package._com))

    def set_directory(self, value: str) -> None:
        """Sets the directory for the configuration.

        Args:
            value: The directory string.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setDirectory(java.lang.String value)
        """
        self.call_com(lambda: self._com.setDirectory(value))

    def set_its_component(self, component: IRPComponent) -> None:
        """Sets the component for this configuration.

        Args:
            component: The component to set.

        Reference:
            com.telelogic.rhapsody.core.IRPConfiguration::setItsComponent(IRPComponent component)
        """
        self.call_com(lambda: self._com.setItsComponent(component._com))


IRPModelElement.register_wrapper("Configuration", IRPConfiguration)
