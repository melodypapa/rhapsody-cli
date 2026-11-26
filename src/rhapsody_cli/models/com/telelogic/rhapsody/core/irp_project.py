"""Wrappers for ``com.telelogic.rhapsody.core.IRPProject``.

Canonical module for :class:`IRPProject`; see the class requirement document at
``docs/requirements/com/telelogic/rhapsody/core/irp_project.md``.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, cast

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage

if TYPE_CHECKING:
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collaboration import IRPCollaboration
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_configuration import IRPConfiguration
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_diagrams import IRPDiagram
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_ide import IRPProgressBar


class IRPProject(IRPPackage):
    """Wraps ``IRPProject``: represents the top-level project container."""

    # Inherited members such as IRPPackage.add_actor/add_class/add_node/find_node,
    # IRPPackage.nodes/packages, and IRPUnit methods are not duplicated here.
    # IRPProject.save overrides IRPUnit.save(int) with its zero-argument COM shape.
    # JavaDoc-only/pywin32-absent methods are documented NotImplementedError stubs;
    # deprecated Design Manager methods retain their exact catalog bindings.

    def add_package(self, name: str) -> IRPPackage:
        """Adds a new package to the project.

        Args:
            name: The name of the new package.

        Returns:
            The wrapped ``IRPPackage`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addPackage(java.lang.String name)
        """
        return cast(IRPPackage, self.wrap(self.call_com(lambda: self._com.addPackage(name))))

    def close(self) -> None:
        """Closes the project.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::close()
        """
        self.call_com(lambda: self._com.close())

    def become_active_project(self) -> None:
        """Makes this project the active project in Rhapsody.

        Used when you have multiple projects open in Rhapsody.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::becomeActiveProject()
        """
        self.call_com(lambda: self._com.becomeActiveProject())

    def find_component(self, name: str) -> IRPComponent:
        """Finds a component in the project by name.

        Args:
            name: The name of the component to find.

        Returns:
            The wrapped component element if found, otherwise empty wrapper.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findComponent(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent

        return cast(IRPComponent, self.wrap(self.call_com(lambda: self._com.findComponent(name))))

    @property
    def components(self) -> IRPCollection:
        """Returns all components in the project.

        Returns:
            An ``IRPCollection`` of component elements.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getComponents()
        """
        return IRPCollection(self.get_com_property(self._com, "components"))

    def find_element_by_guid(self, guid: str) -> IRPModelElement | None:
        """Finds an element in the project by GUID.

        Args:
            guid: The GUID of the element to find.

        Returns:
            The wrapped element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findElementByGUID(java.lang.String theGUID)
        """
        return self.wrap(self.call_com(lambda: self._com.findElementByGUID(guid)))

    # --- Component methods ---
    def add_component(self, name: str) -> IRPComponent:
        """Adds a new component to the project.

        Args:
            name: The name of the new component.

        Returns:
            The wrapped ``IRPComponent`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addComponent(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent

        return cast(IRPComponent, self.wrap(self.call_com(lambda: self._com.addComponent(name))))

    def delete_component(self, component: IRPModelElement) -> None:
        """Deletes a component from the project.

        Args:
            component: The component to delete.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::deleteComponent(com.telelogic.rhapsody.core.IRPComponent component)
        """
        self.call_com(lambda: self._com.deleteComponent(component._com))

    # --- Configuration methods ---
    @property
    def active_configuration(self) -> IRPConfiguration:
        """Returns the active configuration of the project.

        Returns:
            The wrapped ``IRPConfiguration`` that is currently active.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getActiveConfiguration()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_configuration import IRPConfiguration

        return cast(IRPConfiguration, self.wrap(self.get_com_property(self._com, "activeConfiguration")))

    def set_active_configuration(self, name: str) -> None:
        """Sets the active configuration by name.

        The configuration must belong to the active component.

        Args:
            name: The name of the configuration to activate.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setActiveConfiguration(java.lang.String name)
        """
        self.call_com(lambda: self._com.setActiveConfiguration(name))

    @property
    def active_component(self) -> IRPComponent:
        """Returns the active component of the project.

        Returns:
            The wrapped ``IRPComponent`` that is currently active.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getActiveComponent()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent

        return cast(IRPComponent, self.wrap(self.get_com_property(self._com, "activeComponent")))

    def set_active_component(self, name: str) -> None:
        """Sets the active component by its project-qualified name.

        A component nested in a package or component is named by joining its
        location in the project hierarchy with ``::`` (for example,
        ``Default::subpackage::component``).

        Args:
            name: The name or project-qualified path of the component to activate.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setActiveComponent(java.lang.String name)
        """
        self.call_com(lambda: self._com.setActiveComponent(name))

    # --- Stereotype methods ---
    @property
    def all_stereotypes(self) -> IRPCollection:
        """Returns all stereotypes in the project.

        Returns:
            An ``IRPCollection`` of ``IRPStereotype`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getAllStereotypes()
        """
        return IRPCollection(self.get_com_property(self._com, "allStereotypes"))

    def get_new_collaboration(self) -> IRPCollaboration:
        """Returns a new collaboration object.

        Returns:
            The wrapped ``IRPCollaboration`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getNewCollaboration()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collaboration import IRPCollaboration

        return cast(IRPCollaboration, self.wrap(self.call_com(lambda: self._com.getNewCollaboration())))

    # --- Profile methods ---
    def add_profile(self, name: str) -> IRPModelElement:
        """Adds a new profile to the project.

        Args:
            name: The name of the new profile.

        Returns:
            The wrapped profile element created.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addProfile(java.lang.String name)
        """
        return cast(IRPModelElement, self.wrap(self.call_com(lambda: self._com.addProfile(name))))

    @property
    def profiles(self) -> IRPCollection:
        """Returns all profiles in the project.

        Returns:
            An ``IRPCollection`` of profile elements.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getProfiles()
        """
        return IRPCollection(self.get_com_property(self._com, "profiles"))

    # --- Save methods ---
    def save(self) -> None:  # type: ignore[override]
        """Saves the project.

        This zero-argument project method overrides ``IRPUnit.save(with_subs)``;
        pywin32 exposes ``IRPProject.save`` with no arguments.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::save()
        """
        self.call_com(lambda: self._com.save())

    def save_as(self, file_path: str) -> None:
        """Saves the project to a new file path.

        Args:
            file_path: The path to save the project to.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::saveAs(java.lang.String filePath)
        """
        self.call_com(lambda: self._com.saveAs(file_path))

    # --- Find by binary ID ---
    def find_element_by_binary_id(self, binary_id: bytes) -> IRPModelElement | None:
        """Finds an element in the project by binary ID.

        Args:
            binary_id: The binary ID of the element to find; pywin32 exposes
                this as a VT_UI1 SAFEARRAY, so pass the raw ``bytes`` from an
                element's ``binary_id`` property.

        Returns:
            The wrapped element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findElementByBinaryID(java.lang.String binaryID)
        """
        return self.wrap(self.call_com(lambda: self._com.findElementByBinaryID(binary_id)))

    def find_element_by_file_name(self, folder_name: str, file_name: str) -> IRPModelElement | None:
        """Finds the top-level element stored in the specified Rhapsody unit file.

        Args:
            folder_name: The folder that contains the unit file.
            file_name: The name of the unit file.

        Returns:
            The wrapped top-level element if found, otherwise ``None``.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findElementByFileName(java.lang.String theFolderName, java.lang.String theFileName)
            pywin32 IRPProject.findElementByFileName(theFolderName: str, theFileName: str) -> IRPModelElement
        """
        return self.wrap(self.call_com(lambda: self._com.findElementByFileName(folder_name, file_name)))

    # --- Code generation methods ---
    def get_code_generated_files(self) -> IRPCollection:
        """Returns all code-generated files in the project.

        Returns:
            An ``IRPCollection`` of file elements.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getCodeGeneratedFiles()
        """
        return IRPCollection(self.call_com(lambda: self._com.getCodeGeneratedFiles()))

    # --- Other methods ---
    def allow_auto_save(self, allow: int) -> None:
        """Sets whether auto-save is allowed for the project.

        Args:
            allow: ``1`` to allow auto-save, ``0`` to disallow.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::allowAutoSave(int allow)
        """
        self.call_com(lambda: self._com.allowAutoSave(allow))

    def allow_non_unique_names(self, allow: int) -> None:
        """Sets whether non-unique names are allowed for elements.

        Args:
            allow: ``1`` to allow non-unique names, ``0`` to disallow.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::allowNonUniqueNames(int allow)
        """
        self.call_com(lambda: self._com.allowNonUniqueNames(allow))

    @property
    def cg_simplified_model_package(self) -> IRPPackage:
        """Returns the code generation simplified model package.

        Returns:
            The wrapped ``IRPPackage`` for the simplified model.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getCgSimplifiedModelPackage()
        """
        return cast(IRPPackage, self.wrap(self.get_com_property(self._com, "cgSimplifiedModelPackage")))

    def locate_in_ide(self, configuration: IRPConfiguration, file_name: str, line_number: int) -> None:
        """Asks the configured IDE to highlight a line in a source file.

        Args:
            configuration: The configuration whose IDE integration is used.
            file_name: The path of the source file to open.
            line_number: The line number to highlight.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::locateInIDE(IRPConfiguration config, java.lang.String filename, int lineNumber)
            pywin32 IRPProject.locateInIDE(config: IRPConfiguration, filename: str, lineNumber: int)
        """
        self.call_com(lambda: self._com.locateInIDE(configuration._com, file_name, line_number))

    def is_modified_recursive(self) -> bool:
        """Checks whether the project or any of its contents have unsaved changes.

        Returns:
            ``True`` if modified, ``False`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::isModifiedRecursive()
        """
        return bool(self.call_com(lambda: self._com.isModifiedRecursive()))

    def highlight_from_code(self, file_path: str, line_number: int) -> None:
        """Highlights the element in Rhapsody based on code location.

        Args:
            file_path: The path of the source file.
            line_number: The line number in the source file.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::highlightFromCode(java.lang.String filePath, int lineNumber)
        """
        self.call_com(lambda: self._com.highlightFromCode(file_path, line_number))

    # --- Gateway/Report methods ---
    def gateway_export_to_xml(self, file_path: str, parameters: str) -> None:
        """Exports the project to an XML file using the Gateway tool.

        Args:
            file_path: The path of the XML file to create.
            parameters: The Gateway parameters to pass.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::gatewayExportToXML(java.lang.String filename, java.lang.String params)
            pywin32 IRPProject.GatewayExportToXML(filename: str, params: str)
        """
        self.call_com(lambda: self._com.GatewayExportToXML(file_path, parameters))

    def gateway_export_to_xml2(self, file_path: str, parameters: str, project: IRPProject) -> None:
        """Exports a project to an XML file using the Gateway tool with parameters.

        Args:
            file_path: The path of the XML file to create.
            parameters: The Gateway parameters to pass.
            project: The project whose model is exported.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::gatewayExportToXML2(java.lang.String filename, java.lang.String params, IRPProject proj)
            pywin32 IRPProject.GatewayExportToXML2(filename: str, params: str, proj: IRPProject)
        """
        self.call_com(lambda: self._com.GatewayExportToXML2(file_path, parameters, project._com))

    def generate_report(self, model_scope: str, template_name: str, doc_type: str, file_path: str, show_document: int, silent_mode: int) -> None:
        """Generates a ReporterPLUS report for the project.

        Args:
            model_scope: The name of the package for which the report is generated.
            template_name: The path of the ReporterPLUS template.
            doc_type: The output document type, for example ``"html"``.
            file_path: The path of the report file to create.
            show_document: ``1`` to open the report after generation, ``0`` otherwise.
            silent_mode: ``1`` to suppress dialogs, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::generateReport(java.lang.String modelscope, java.lang.String templatename,
            java.lang.String docType, java.lang.String filename, int showDocument, int silentMode)
            pywin32 IRPProject.GenerateReport(modelscope: str, templatename: str, docType: str, filename: str, showDocument: int, silentMode: int)
        """
        self.call_com(lambda: self._com.GenerateReport(model_scope, template_name, doc_type, file_path, show_document, silent_mode))

    # --- Custom Views methods ---
    def add_custom_view_on_browser(self, view: IRPModelElement) -> None:
        """Adds a custom view to be applied on the Rhapsody browser.

        Args:
            view: The wrapped custom view to add.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addCustomViewOnBrowser(com.telelogic.rhapsody.core.IRPCustomView view)
        """
        self.call_com(lambda: self._com.addCustomViewOnBrowser(view._com))

    def add_custom_view_on_diagram(self, diagram: IRPDiagram, view: IRPModelElement) -> None:
        """Applies a custom view to a diagram.

        Args:
            diagram: The diagram to which the custom view is applied.
            view: The wrapped custom view package to apply.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addCustomViewOnDiagram(IRPDiagram diagram, IRPPackage customView)
            pywin32 IRPProject.addCustomViewOnDiagram(diagram: IRPDiagram, customView: IRPPackage)
        """
        self.call_com(lambda: self._com.addCustomViewOnDiagram(diagram._com, view._com))

    def apply_browser_custom_views_on_diagrams(self, enabled: int) -> None:
        """Applies the browser custom views to all diagrams.

        Args:
            enabled: ``1`` to apply the custom views to all diagrams, ``0`` to remove them.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::applyBrowserCustomViewsOnDiagrams(int newVal)
            pywin32 IRPProject.applyBrowserCustomViewsOnDiagrams(newVal: int)
        """
        self.call_com(lambda: self._com.applyBrowserCustomViewsOnDiagrams(enabled))

    def get_active_custom_views_on_browser(self) -> IRPCollection:
        """Returns the active custom views applied on the browser.

        Returns:
            An ``IRPCollection`` of active browser custom views.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getActiveCustomViewsOnBrowser()
        """
        return IRPCollection(self.call_com(lambda: self._com.getActiveCustomViewsOnBrowser()))

    def get_active_custom_views_on_diagram(self, diagram: IRPDiagram) -> IRPCollection:
        """Returns the custom views currently applied to a diagram.

        Args:
            diagram: The diagram whose custom views are returned.

        Returns:
            An ``IRPCollection`` of active diagram custom views.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getActiveCustomViewsOnDiagram(IRPDiagram diagram)
            pywin32 IRPProject.getActiveCustomViewsOnDiagram(diagram: IRPDiagram) -> IRPCollection
        """
        return IRPCollection(self.call_com(lambda: self._com.getActiveCustomViewsOnDiagram(diagram._com)))

    def remove_custom_view_on_browser(self, view: IRPModelElement) -> None:
        """Removes a custom view from the browser.

        Args:
            view: The wrapped custom view to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::removeCustomViewOnBrowser(com.telelogic.rhapsody.core.IRPCustomView view)
        """
        self.call_com(lambda: self._com.removeCustomViewOnBrowser(view._com))

    def remove_custom_view_on_diagram(self, diagram: IRPDiagram, view: IRPModelElement) -> None:
        """Removes a custom view from a diagram.

        Args:
            diagram: The diagram from which the custom view is removed.
            view: The wrapped custom view package to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::removeCustomViewOnDiagram(IRPDiagram diagram, IRPPackage customView)
            pywin32 IRPProject.removeCustomViewOnDiagram(diagram: IRPDiagram, customView: IRPPackage)
        """
        self.call_com(lambda: self._com.removeCustomViewOnDiagram(diagram._com, view._com))

    # --- CSV methods ---
    def close_csv_file(self, file_path: str) -> None:
        """Closes the Output window tab of the specified CSV file.

        Args:
            file_path: The path of the CSV file to close.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::closeCSVFile(java.lang.String fullCSVFileName)
            pywin32 IRPProject.closeCSVFile(fullCSVFileName: str)
        """
        self.call_com(lambda: self._com.closeCSVFile(file_path))

    def open_csv_file(self, file_path: str, mode: int) -> None:
        """Opens a CSV file for requirements import.

        Args:
            file_path: The path of the CSV file to open.
            mode: The mode in which to open the file.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::openCSVFile(java.lang.String filePath, int mode)
        """
        self.call_com(lambda: self._com.openCSVFile(file_path, mode))

    def reload_csv_file(self, file_path: str) -> None:
        """Reloads the specified CSV file in its Output window tab.

        Args:
            file_path: The path of the CSV file to reload.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::reloadCSVFile(java.lang.String fullCSVFileName)
            pywin32 IRPProject.reloadCSVFile(fullCSVFileName: str)
        """
        self.call_com(lambda: self._com.reloadCSVFile(file_path))

    # --- Remote/Roundtrip methods ---
    def apply_roundtrip_diff_merge(self, magic_number: int, shadow_model: IRPModelElement, files_to_update: IRPCollection) -> None:
        """Applies the roundtrip diff merge for the project.

        Args:
            magic_number: The roundtrip magic number supplied by Rhapsody.
            shadow_model: The roundtrip shadow model element.
            files_to_update: The collection of files to update.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::applyRoundtripDiffMerge(int magicNumber, IRPProject shadowModel, IRPCollection filesToUpdate)
            pywin32 IRPProject.applyRoundtripDiffMerge(magicNumber: int, shadowModel: IRPProject, filesToUpdate: IRPCollection)
        """
        self.call_com(lambda: self._com.applyRoundtripDiffMerge(magic_number, shadow_model._com, files_to_update._com))

    def enable_rhapsody_model_manager(self) -> None:
        """Enable Rhapsody Model Manager for the project.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::enableRhapsodyModelManager()
        """
        raise NotImplementedError("enableRhapsodyModelManager is not exposed in the Rhapsody COM automation type library.")

    def find_elements_with_oslc_link(self, link_type: str, purl: str) -> IRPCollection:
        """Returns the elements that have an OSLC link of a type to a target.

        Args:
            link_type: The OSLC link type to search for.
            purl: The purl of the OSLC target element.

        Returns:
            An ``IRPCollection`` of elements with the matching OSLC link.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findElementsWithOSLCLink(java.lang.String type, java.lang.String purl)
            pywin32 IRPProject.findElementsWithOSLCLink(type: str, purl: str) -> IRPCollection
        """
        return IRPCollection(self.call_com(lambda: self._com.findElementsWithOSLCLink(link_type, purl)))

    def get_remote_resource_packages(self) -> IRPCollection:
        """Returns the remote resource packages of the project.

        Returns:
            An ``IRPCollection`` of remote resource packages.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getRemoteResourcePackages()
        """
        return IRPCollection(self.call_com(lambda: self._com.getRemoteResourcePackages()))

    def get_roundtrip_shadow_model(self, magic_number: int) -> IRPModelElement | None:
        """Returns the roundtrip shadow model for a magic number.

        Args:
            magic_number: The roundtrip magic number supplied by Rhapsody.

        Returns:
            The wrapped roundtrip shadow model if available.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getRoundtripShadowModel(int magicNumber)
            pywin32 IRPProject.getRoundtripShadowModel(magicNumber: int) -> IRPProject
        """
        return self.wrap(self.call_com(lambda: self._com.getRoundtripShadowModel(magic_number)))

    def is_actively_managed(self) -> int:
        """Checks whether the project is actively managed by Rhapsody Model Manager.

        Returns:
            ``1`` if the project is actively managed, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::isActivelyManaged()
        """
        return int(self.call_com(lambda: self._com.isActivelyManaged()))

    def is_resolve_on_demand(self) -> int:
        """Checks whether remote artifacts are resolved on demand.

        Returns:
            ``1`` if remote artifacts are resolved on demand, ``0`` otherwise.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::isResolveOnDemand()
        """
        raise NotImplementedError("isResolveOnDemand is not exposed in the Rhapsody COM automation type library.")

    def migrate_design_manager_links(self) -> None:
        """Migrate Design Manager links to Rhapsody Model Manager links.

        Ensure the OSLC links are imported, Model Manager is enabled, and any
        required global configuration is set before calling this method.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::migrateDesignManagerLinks()
        """
        raise NotImplementedError("migrateDesignManagerLinks is not exposed in the Rhapsody COM automation type library.")

    def move_to_design_manager(self, user_name: str, password: str, server_url: str, project_area_name: str, stream_name: str) -> None:
        """Moves the project to Design Manager.

        Deprecated: Rhapsody removed Design Manager support in release 8.4.
        The binding remains available because this member is exposed by pywin32.

        Args:
            user_name: The Design Manager user name.
            password: The Design Manager password.
            server_url: The Design Manager server URL.
            project_area_name: The Design Manager project area name.
            stream_name: The Design Manager stream name.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::moveToDesignManager(
                java.lang.String userName, java.lang.String password, java.lang.String serverURL, java.lang.String projectAreaName, java.lang.String streamName)
        """
        self.call_com(lambda: self._com.moveToDesignManager(user_name, password, server_url, project_area_name, stream_name))

    def move_to_design_manager_after_login(self, server_url: str, project_area_name: str, stream_name: str) -> None:
        """Moves the project to Design Manager after login.

        Deprecated: Rhapsody removed Design Manager support in release 8.4.
        The binding remains available because this member is exposed by pywin32.

        Args:
            server_url: The Design Manager server URL.
            project_area_name: The Design Manager project area name.
            stream_name: The Design Manager stream name.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::moveToDesignManagerAfterLogin(java.lang.String serverURL, java.lang.String projectAreaName, java.lang.String streamName)
        """
        self.call_com(lambda: self._com.moveToDesignManagerAfterLogin(server_url, project_area_name, stream_name))

    # --- Rose Import methods ---
    def import_package_from_rose(self, project_name: str, package_name: str, log_file_name: str) -> IRPPackage:
        """Imports a package from a Rational Rose project.

        Args:
            project_name: The Rose project to import the package from.
            package_name: The name of the Rose package to import.
            log_file_name: The path of the log file to write.

        Returns:
            The wrapped ``IRPPackage`` created from the import.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::importPackageFromRose(java.lang.String projectName, java.lang.String packageName, java.lang.String logFileName)
            pywin32 IRPProject.importPackageFromRose(projectName: str, packageName: str, logFileName: str)
        """
        return cast(IRPPackage, self.wrap(self.call_com(lambda: self._com.importPackageFromRose(project_name, package_name, log_file_name))))

    def import_project_from_rose(self, project_name: str, log_file_name: str) -> None:
        """Imports a Rational Rose project.

        Args:
            project_name: The Rose project to import.
            log_file_name: The path of the log file to write.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::importProjectFromRose(java.lang.String projectName, java.lang.String logFileName)
            pywin32 IRPProject.importProjectFromRose(projectName: str, logFileName: str)
        """
        self.call_com(lambda: self._com.importProjectFromRose(project_name, log_file_name))

    # --- Events methods ---
    def check_events_base_ids_solve_collisions(self) -> None:
        """Checks events base IDs and solves collisions.

        The pywin32 member is ``checkEventsBaseIdsSolveCollisions`` (capital ``I`` in
        ``Ids``); a live probe on 2026-11-25 confirmed the call returns ``None``,
        matching the JavaDoc's void contract.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::checkEventsBaseIdsSolveCollisions()
        """
        self.call_com(lambda: self._com.checkEventsBaseIdsSolveCollisions())

    def recalculate_events_base_ids(self) -> None:
        """Recalculates the events base IDs for the project.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::recalculateEventsBaseIds()
        """
        self.call_com(lambda: self._com.recalculateEventsBaseIds())

    # --- Misc methods ---
    def add_spell_checker_result(self, value: str) -> None:
        """Adds a spell checker result.

        Args:
            value: The misspelled word reported by the spell checker.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addSpellCheckerResult(java.lang.String value)
            pywin32 IRPProject.addSpellCheckerResult(value: str)
        """
        self.call_com(lambda: self._com.addSpellCheckerResult(value))

    def clean_unresolved_elements(self, root_element: IRPModelElement) -> None:
        """Removes unresolved elements below the specified element.

        Args:
            root_element: The element below which Rhapsody cleans unresolved elements.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::cleanUnresolvedElements(IRPModelElement rootElement)
            pywin32 IRPProject.cleanUnresolvedElements(rootElement: IRPModelElement)
        """
        self.call_com(lambda: self._com.cleanUnresolvedElements(root_element._com))

    def end_transaction_of_no_cg_interest(self) -> None:
        """Ends a transaction of no code generation interest.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::endTransactionOfNoCGInterest()
        """
        self.call_com(lambda: self._com.endTransactionOfNoCGInterest())

    @property
    def default_directory_scheme(self) -> str:
        """Returns the default directory scheme of the project.

        Returns:
            The default directory scheme (for example ``"Flat"`` or ``"Nested"``).

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getDefaultDirectoryScheme()
        """
        return str(self.get_com_property(self._com, "defaultDirectoryScheme"))

    @default_directory_scheme.setter
    def default_directory_scheme(self, scheme: str) -> None:
        """Sets the default directory scheme of the project.

        Args:
            scheme: The default directory scheme to set, e.g. ``"Flat"``.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setDefaultDirectoryScheme(java.lang.String scheme)
        """
        self.set_com_property(self._com, "defaultDirectoryScheme", scheme)

    def get_new_progress_bar(self, amount: int, name: str) -> IRPProgressBar:
        """Returns a new progress bar.

        Args:
            amount: The maximum value of the progress bar.
            name: The title of the progress bar.

        Returns:
            The wrapped ``IRPProgressBar`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getNewProgressBar(int amount, java.lang.String name)
            pywin32 IRPProject.getNewProgressBar(amount: int, name: str) -> IRPProgressBar
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_ide import IRPProgressBar

        return cast(IRPProgressBar, self.wrap(self.call_com(lambda: self._com.getNewProgressBar(amount, name))))

    def get_notify_plugin_on_elements_changed(self) -> int:
        """Checks whether plugins are notified when elements change.

        Returns:
            ``1`` if plugins are notified, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getNotifyPluginOnElementsChanged()
        """
        return int(self.call_com(lambda: self._com.getNotifyPluginOnElementsChanged()))

    def get_requirements_by_id(self, requirement_id: str, return_first_found_only: int) -> IRPCollection:
        """Returns the requirements matching the specified ID.

        Args:
            requirement_id: The requirement ID to search for.
            return_first_found_only: ``1`` to stop at the first match, ``0`` to return all matches.

        Returns:
            An ``IRPCollection`` of matching requirements.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getRequirementsByID(java.lang.String requirementID, int returnFirstFoundOnly)
            pywin32 IRPProject.getRequirementsByID(requirementID: str, returnFirstFoundOnly: int) -> IRPCollection
        """
        return IRPCollection(self.call_com(lambda: self._com.getRequirementsByID(requirement_id, return_first_found_only)))

    def remove(self) -> None:
        """Removes the project.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::remove()
        """
        self.call_com(lambda: self._com.remove())

    def save_as_prev_version(self, file_name: str, previous_version: str) -> None:
        """Saves the project using the format of a previous Rhapsody version.

        Args:
            file_name: The path to use for saving the project.
            previous_version: The Rhapsody version whose file format is used.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::saveAsPrevVersion(java.lang.String filename, java.lang.String prevVersion)
            pywin32 IRPProject.saveAsPrevVersion(filename: str, prevVersion: str)
        """
        self.call_com(lambda: self._com.saveAsPrevVersion(file_name, previous_version))

    def set_resolve_on_demand(self, resolve_on_demand: int) -> None:
        """Sets whether remote artifacts should be resolved on demand.

        Args:
            resolve_on_demand: ``1`` to enable on-demand resolution, ``0`` to disable it.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setResolveOnDemand(int resolveOnDemand)
        """
        raise NotImplementedError("setResolveOnDemand is not exposed in the Rhapsody COM automation type library.")

    def set_global_configuration(self, gc_uri: str, name: str) -> int:
        """Set the global configuration used for the project.

        Args:
            gc_uri: The URI of the global configuration.
            name: The name of the global configuration.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setGlobalConfiguration(java.lang.String GCUri, java.lang.String name)
        """
        raise NotImplementedError("setGlobalConfiguration is not exposed in the Rhapsody COM automation type library.")

    def set_notify_plugin_on_elements_changed(self, enabled: int) -> None:
        """Sets whether plugins are notified when elements change.

        Args:
            enabled: ``1`` to notify plugins, ``0`` to not notify.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setNotifyPluginOnElementsChanged(int enabled)
        """
        self.call_com(lambda: self._com.setNotifyPluginOnElementsChanged(enabled))

    def set_object_explicit(self, obj: IRPModelElement) -> None:
        """Sets the specified object as explicit.

        Args:
            obj: The wrapped model element to set as explicit.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setObjectExplicit(com.telelogic.rhapsody.core.IRPModelElement obj)
        """
        self.call_com(lambda: self._com.setObjectExplicit(obj._com))

    def set_object_implicit(self, obj: IRPModelElement) -> None:
        """Sets the specified object as implicit.

        Args:
            obj: The wrapped model element to set as implicit.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setObjectImplicit(com.telelogic.rhapsody.core.IRPModelElement obj)
        """
        self.call_com(lambda: self._com.setObjectImplicit(obj._com))

    _use_unique_stereotype_and_ref_cache = property(
        None,
        doc="Sets whether to use the unique stereotype and reference cache; the pywin32 property is write-only.",
    )

    @_use_unique_stereotype_and_ref_cache.setter
    def use_unique_stereotype_and_ref_cache(self, enabled: int) -> None:
        """Sets whether to use a unique stereotype and reference cache.

        Args:
            enabled: ``1`` to use the unique cache, ``0`` to not use it.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setUseUniqueStereotypeAndRefCache(int enabled)
        """
        self.set_com_property(self._com, "UseUniqueStereotypeAndRefCache", enabled)

    def set_wait_dialog_watchdog_value(self, value: str) -> None:
        """Reports whether an external process is still running.

        Pass a non-blank string while the external process is running and call
        again with an empty string when it completes. Rhapsody assumes the
        process has crashed if it receives no update for two minutes.

        Args:
            value: A non-blank running marker or an empty string on completion.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setWaitDialogWatchdogValue(java.lang.String value)
        """
        self.call_com(lambda: self._com.setWaitDialogWatchdogValue(value))

    def start_transaction_of_no_cg_interest(self) -> None:
        """Starts a transaction of no code generation interest.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::startTransactionOfNoCGInterest()
        """
        self.call_com(lambda: self._com.startTransactionOfNoCGInterest())


IRPModelElement.register_wrapper("Project", IRPProject)
