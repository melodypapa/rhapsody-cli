"""Wrapper for the Java interface ``com.telelogic.rhapsody.core.IRPComponent``."""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_configuration import IRPConfiguration


class IRPComponent(IRPUnit):
    """Wraps ``IRPComponent``: a component that extends ``IRPUnit``.

    JavaDoc accessor pairs that pywin32 exposes as properties are surfaced as
    ``@property`` members. ``get_path``, ``set_path`` and
    ``update_contained_diagrams_on_server`` are JavaDoc-declared but absent from
    the pywin32 catalog, so they are documented pre-dispatch stubs.
    """

    # IRPComponent method parity checklist: properties, methods and unavailable
    # stubs are all reconciled against the committed API report.

    @property
    def additional_sources(self) -> str:
        """COM-backed ``additionalSources`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::additionalSources()
        """
        return str(self.get_com_property(self._com, "additionalSources"))

    @additional_sources.setter
    def additional_sources(self, value: str) -> None:
        """Writes the COM-backed ``additionalSources`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::setAdditionalSources(value)
        """
        self.set_com_property(self._com, "additionalSources", value)

    @property
    def build_type(self) -> str:
        """COM-backed ``buildType`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::buildType()
        """
        return str(self.get_com_property(self._com, "buildType"))

    @build_type.setter
    def build_type(self, value: str) -> None:
        """Writes the COM-backed ``buildType`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::setBuildType(value)
        """
        self.set_com_property(self._com, "buildType", value)

    @property
    def configurations(self) -> IRPCollection:
        """COM-backed ``configurations`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::configurations()
        """
        return IRPCollection(self.get_com_property(self._com, "configurations"))

    @property
    def files(self) -> IRPCollection:
        """COM-backed ``files`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::files()
        """
        return IRPCollection(self.get_com_property(self._com, "files"))

    @property
    def include_path(self) -> str:
        """COM-backed ``includePath`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::includePath()
        """
        return str(self.get_com_property(self._com, "includePath"))

    @include_path.setter
    def include_path(self, value: str) -> None:
        """Writes the COM-backed ``includePath`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::setIncludePath(value)
        """
        self.set_com_property(self._com, "includePath", value)

    @property
    def libraries(self) -> str:
        """COM-backed ``libraries`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::libraries()
        """
        return str(self.get_com_property(self._com, "libraries"))

    @libraries.setter
    def libraries(self, value: str) -> None:
        """Writes the COM-backed ``libraries`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::setLibraries(value)
        """
        self.set_com_property(self._com, "libraries", value)

    @property
    def nested_components(self) -> IRPCollection:
        """COM-backed ``nestedComponents`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::nestedComponents()
        """
        return IRPCollection(self.get_com_property(self._com, "nestedComponents"))

    @property
    def panel_diagrams(self) -> IRPCollection:
        """COM-backed ``panelDiagrams`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::panelDiagrams()
        """
        return IRPCollection(self.get_com_property(self._com, "panelDiagrams"))

    @property
    def scope_by_selected_elements(self) -> IRPCollection:
        """COM-backed ``scopeBySelectedElements`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::scopeBySelectedElements()
        """
        return IRPCollection(self.get_com_property(self._com, "scopeBySelectedElements"))

    @scope_by_selected_elements.setter
    def scope_by_selected_elements(self, elements: IRPCollection) -> None:
        """Writes the COM-backed ``scopeBySelectedElements`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::setScopeBySelectedElements(elements)
        """
        self.set_com_property(self._com, "scopeBySelectedElements", elements._com)

    @property
    def scope_elements(self) -> IRPCollection:
        """COM-backed ``scopeElements`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::scopeElements()
        """
        return IRPCollection(self.get_com_property(self._com, "scopeElements"))

    @property
    def standard_headers(self) -> str:
        """COM-backed ``standardHeaders`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::standardHeaders()
        """
        return str(self.get_com_property(self._com, "standardHeaders"))

    @standard_headers.setter
    def standard_headers(self, value: str) -> None:
        """Writes the COM-backed ``standardHeaders`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::setStandardHeaders(value)
        """
        self.set_com_property(self._com, "standardHeaders", value)

    @property
    def variation_points(self) -> IRPCollection:
        """COM-backed ``variationPoints`` property.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::variationPoints()
        """
        return IRPCollection(self.get_com_property(self._com, "variationPoints"))

    def add_configuration(self, name: str) -> IRPConfiguration:
        """JavaDoc ``addConfiguration`` forwarded to the catalog member ``addConfiguration``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::addConfiguration
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_configuration import IRPConfiguration

        return cast(IRPConfiguration, self.wrap(self.call_com(lambda: self._com.addConfiguration(name))))

    def add_file(self, name: str) -> IRPUnit:
        """JavaDoc ``addFile`` forwarded to the catalog member ``addFile``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::addFile
        """
        return cast(IRPUnit, self.wrap(self.call_com(lambda: self._com.addFile(name))))

    def add_folder(self, name: str) -> IRPUnit:
        """JavaDoc ``addFolder`` forwarded to the catalog member ``addFolder``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::addFolder
        """
        return cast(IRPUnit, self.wrap(self.call_com(lambda: self._com.addFolder(name))))

    def add_nested_component(self, name: str) -> IRPComponent:
        """JavaDoc ``addNestedComponent`` forwarded to the catalog member ``addNestedComponent``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::addNestedComponent
        """
        return cast(IRPComponent, self.wrap(self.call_com(lambda: self._com.addNestedComponent(name))))

    def add_scope_element(self, element: IRPUnit) -> None:
        """JavaDoc ``addScopeElement`` forwarded to the catalog member ``addScopeElement``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::addScopeElement
        """
        self.call_com(lambda: self._com.addScopeElement(element._com))

    def add_scope_element_without_aggregates(self, element: IRPUnit) -> None:
        """JavaDoc ``addScopeElementWithoutAggregates`` forwarded to the catalog member ``addScopeElementWithoutAggregates``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::addScopeElementWithoutAggregates
        """
        self.call_com(lambda: self._com.addScopeElementWithoutAggregates(element._com))

    def add_to_scope(self, element: IRPUnit) -> None:
        """JavaDoc ``addToScope`` forwarded to the catalog member ``addToScope``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::addToScope
        """
        self.call_com(lambda: self._com.addToScope(element._com))

    def all_elements_in_scope(self) -> IRPCollection:
        """JavaDoc ``allElementsInScope`` forwarded to the catalog member ``allElementsInScope``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::allElementsInScope
        """
        return IRPCollection(self.call_com(lambda: self._com.allElementsInScope()))

    def delete_configuration(self, configuration: IRPConfiguration) -> None:
        """JavaDoc ``deleteConfiguration`` forwarded to the catalog member ``deleteConfiguration``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::deleteConfiguration
        """
        self.call_com(lambda: self._com.deleteConfiguration(configuration._com))

    def delete_file(self, file: IRPUnit) -> None:
        """JavaDoc ``deleteFile`` forwarded to the catalog member ``deleteFile``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::deleteFile
        """
        self.call_com(lambda: self._com.deleteFile(file._com))

    def find_configuration(self, name: str) -> IRPConfiguration | None:
        """JavaDoc ``findConfiguration`` forwarded to the catalog member ``findConfiguration``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::findConfiguration
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_configuration import IRPConfiguration

        return cast(IRPConfiguration, self.wrap(self.call_com(lambda: self._com.findConfiguration(name))))

    def get_config_by_dependency(self) -> IRPConfiguration:
        """JavaDoc ``getConfigByDependency`` forwarded to the catalog member ``getConfigByDependency``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::getConfigByDependency
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_configuration import IRPConfiguration

        return cast(IRPConfiguration, self.wrap(self.call_com(lambda: self._com.getConfigByDependency())))

    def get_file(self, name: str) -> IRPUnit:
        """JavaDoc ``getFile`` forwarded to the catalog member ``getFile``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::getFile
        """
        return cast(IRPUnit, self.wrap(self.call_com(lambda: self._com.getFile(name))))

    def get_file_name(self) -> str:
        """JavaDoc ``getFileName`` forwarded to the catalog member ``getFileName``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::getFileName
        """
        return str(self.call_com(lambda: self._com.getFileName()))

    def get_model_element_file_name(self) -> str:
        """JavaDoc ``getModelElementFileName`` forwarded to the catalog member ``getModelElementFileName``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::getModelElementFileName
        """
        return str(self.call_com(lambda: self._com.getModelElementFileName()))

    def get_package_file(self) -> str:
        """JavaDoc ``getPackageFile`` forwarded to the catalog member ``getPackageFile``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::getPackageFile
        """
        return str(self.call_com(lambda: self._com.getPackageFile()))

    def get_possible_variants(self) -> IRPCollection:
        """JavaDoc ``getPossibleVariants`` forwarded to the catalog member ``getPossibleVariants``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::getPossibleVariants
        """
        return IRPCollection(self.call_com(lambda: self._com.getPossibleVariants()))

    def get_scope_elements_by_category(self, category: str) -> IRPCollection:
        """JavaDoc ``getScopeElementsByCategory`` forwarded to the catalog member ``getScopeElementsByCategory``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::getScopeElementsByCategory
        """
        return IRPCollection(self.call_com(lambda: self._com.getScopeElementsByCategory(category)))

    def get_variant(self) -> str:
        """JavaDoc ``getVariant`` forwarded to the catalog member ``getVariant``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::getVariant
        """
        return str(self.call_com(lambda: self._com.getVariant()))

    def is_directory_per_model_component(self) -> int:
        """JavaDoc ``isDirectoryPerModelComponent`` forwarded to the catalog member ``isDirectoryPerModelComponent``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::isDirectoryPerModelComponent
        """
        return int(self.call_com(lambda: self._com.isDirectoryPerModelComponent()))

    def remove_scope_element(self, element: IRPUnit) -> None:
        """JavaDoc ``removeScopeElement`` forwarded to the catalog member ``removeScopeElement``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::removeScopeElement
        """
        self.call_com(lambda: self._com.removeScopeElement(element._com))

    def set_variant(self, value: str) -> None:
        """JavaDoc ``setVariant`` forwarded to the catalog member ``setVariant``.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::setVariant
        """
        self.call_com(lambda: self._com.setVariant(value))

    def get_path(self) -> str:
        """JavaDoc ``getPath``; pywin32 exposes no such member.

        Raises:
            NotImplementedError: Always; the member is unavailable in pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::getPath()
        """
        raise NotImplementedError("getPath is not exposed by pywin32")

    def set_path(self, value: str) -> None:
        """JavaDoc ``setPath``; pywin32 exposes no such member.

        Raises:
            NotImplementedError: Always; the member is unavailable in pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::setPath(java.lang.String path)
        """
        raise NotImplementedError("setPath is not exposed by pywin32")

    def update_contained_diagrams_on_server(self) -> None:
        """JavaDoc ``updateContainedDiagramsOnServer``; absent from pywin32.

        Raises:
            NotImplementedError: Always; the member is unavailable in pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPComponent::updateContainedDiagramsOnServer()
        """
        raise NotImplementedError("updateContainedDiagramsOnServer is not exposed by pywin32")


IRPModelElement.register_wrapper("Component", IRPComponent)
