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
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actor import IRPActor
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collaboration import IRPCollaboration
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_component import IRPComponent
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_configuration import IRPConfiguration
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_ide import IRPProgressBar
    from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_node import IRPNode


class IRPProject(IRPPackage):
    """Wraps ``IRPProject``: represents the top-level project container."""

    # IRPProject method parity checklist:
    # [x] gateway_export_to_xml  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] gateway_export_to_xml2  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] generate_report  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_component  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [x] add_custom_view_on_browser  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_custom_view_on_diagram  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] add_package  [x] impl  [x] docstring  [x] unit test  [x] integration test
    # [ ] add_profile  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] add_spell_checker_result  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] allow_auto_save  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] allow_non_unique_names  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] apply_browser_custom_views_on_diagrams  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] apply_roundtrip_diff_merge  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] become_active_project  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] check_events_base_ids_solve_collisions  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] clean_unresolved_elements  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] close  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] close_csv_file  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] delete_component  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] enable_rhapsody_model_manager  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] end_transaction_of_no_cg_interest  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] find_component  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] find_element_by_binary_id  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] find_element_by_file_name  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] find_element_by_guid  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] find_elements_with_oslc_link  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] active_component  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] active_configuration  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_active_custom_views_on_browser  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_active_custom_views_on_diagram  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] all_stereotypes  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] cg_simplified_model_package  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] get_code_generated_files  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] components  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] default_directory_scheme  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_new_collaboration  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_new_progress_bar  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_notify_plugin_on_elements_changed  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] profiles  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] nodes  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] packages  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] use_unique_stereotype_and_ref_cache  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] get_remote_resource_packages  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_requirements_by_id  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] get_roundtrip_shadow_model  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] highlight_from_code  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] import_package_from_rose  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] import_project_from_rose  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] is_actively_managed  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] is_modified_recursive  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [ ] locate_in_ide  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] migrate_design_manager_links  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [deprecated] move_to_design_manager  - skipped (deprecated in Rhapsody Java API; see deprecated-list.html)
    # [deprecated] move_to_design_manager_after_login  - skipped (deprecated in Rhapsody Java API; see deprecated-list.html)
    # [x] open_csv_file  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] recalculate_events_base_ids  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] reload_csv_file  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove_custom_view_on_browser  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] remove_custom_view_on_diagram  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [ ] save  [x] impl  [x] docstring  [ ] unit test  [ ] integration test   (inherited from rp_unit)
    # [x] save_as  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] save_as_prev_version  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_active_component  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] set_active_configuration  [x] impl  [x] docstring  [ ] unit test  [ ] integration test
    # [x] set_default_directory_scheme (via default_directory_scheme setter)  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_global_configuration  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_notify_plugin_on_elements_changed  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_object_explicit  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_object_implicit  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] set_wait_dialog_watchdog_value  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [x] start_transaction_of_no_cg_interest  [x] impl  [x] docstring  [x] unit test  [ ] integration test
    # [inherited] irp_package / irp_unit / irp_model_element methods (covered by rp_package / rp_unit / rp_model_element checklists)
    # Deprecated IRPProject methods listed above.
    #
    # Audit 2026-07-18: methods implemented in IRPProject but NOT declared on IRPProject in the Java API (docs/java_api HTML).
    # The following [not-in-api] methods were REMOVED from IRPProject (they did not exist on any IRP* interface in Java API):
    #   find_by_name (findByName), find_by_meta_class (findByMetaClass),
    #   get_is_dirty (getIsDirty), set_dirty (setDirty),
    #   add_collaboration (addCollaboration), get_collaborations (getCollaborations),
    #   find_collaboration (findCollaboration), delete_collaboration (deleteCollaboration)
    # The following [wrong-interface] methods were REMOVED from IRPProject (they exist on IRPComponent, not IRPProject - use IRPComponent instead):
    #   add_configuration (addConfiguration), get_configurations (getConfigurations),
    #   find_configuration (findConfiguration), delete_configuration (deleteConfiguration)

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
    def packages(self) -> IRPCollection:
        """Returns all top-level packages in the project.

        Returns:
            An ``IRPCollection`` of ``IRPPackage`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::getPackages()
        """
        return IRPCollection(self.get_com_property(self._com, "packages"))

    def add_class(self, name: str) -> IRPClass:
        """Adds a new class to the project's top level.

        Args:
            name: The name of the new class.

        Returns:
            The wrapped ``IRPClass`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addClass(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass

        return cast(IRPClass, self.wrap(self.call_com(lambda: self._com.addClass(name))))

    def add_actor(self, name: str) -> IRPActor:
        """Adds a new actor to the project's top level.

        Args:
            name: The name of the new actor.

        Returns:
            The wrapped ``IRPActor`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPPackage::addActor(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_actor import IRPActor

        return cast(IRPActor, self.wrap(self.call_com(lambda: self._com.addActor(name))))

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

    # --- Node methods ---
    def add_node(self, name: str) -> IRPNode:
        """Adds a new node to the project.

        Args:
            name: The name of the new node.

        Returns:
            The wrapped ``IRPNode`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addNode(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_node import IRPNode

        return cast(IRPNode, self.wrap(self.call_com(lambda: self._com.addNode(name))))

    @property
    def nodes(self) -> IRPCollection:
        """Returns all nodes in the project.

        Returns:
            An ``IRPCollection`` of ``IRPNode`` objects.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getNodes()
        """
        return IRPCollection(self.get_com_property(self._com, "nodes"))

    def find_node(self, name: str) -> IRPNode:
        """Finds a node in the project by name.

        Args:
            name: The name of the node to find.

        Returns:
            The wrapped ``IRPNode`` if found, otherwise empty wrapper.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findNode(java.lang.String name)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_node import IRPNode

        return cast(IRPNode, self.wrap(self.call_com(lambda: self._com.findNode(name))))

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

    def set_active_configuration(self, config: IRPModelElement) -> None:
        """Sets the active configuration of the project.

        Args:
            config: The configuration to set as active.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setActiveConfiguration(com.telelogic.rhapsody.core.IRPConfiguration config)
        """
        self.call_com(lambda: self._com.setActiveConfiguration(config._com))

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

    def set_active_component(self, component: IRPModelElement) -> None:
        """Sets the active component of the project.

        Args:
            component: The component to set as active.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setActiveComponent(com.telelogic.rhapsody.core.IRPComponent component)
        """
        self.call_com(lambda: self._com.setActiveComponent(component._com))

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
    def save_as(self, file_path: str) -> None:
        """Saves the project to a new file path.

        Args:
            file_path: The path to save the project to.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::saveAs(java.lang.String filePath)
        """
        self.call_com(lambda: self._com.saveAs(file_path))

    # --- Find by binary ID ---
    def find_element_by_binary_id(self, binary_id: str) -> IRPModelElement | None:
        """Finds an element in the project by binary ID.

        Args:
            binary_id: The binary ID of the element to find.

        Returns:
            The wrapped element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findElementByBinaryID(java.lang.String binaryID)
        """
        return self.wrap(self.call_com(lambda: self._com.findElementByBinaryID(binary_id)))

    def find_element_by_file_name(self, file_name: str) -> IRPModelElement | None:
        """Finds an element in the project by file name.

        Args:
            file_name: The file name to search for.

        Returns:
            The wrapped element if found.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findElementByFileName(java.lang.String fileName)
        """
        return self.wrap(self.call_com(lambda: self._com.findElementByFileName(file_name)))

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

    def locate_in_ide(self) -> None:
        """Locates this project in the Rhapsody IDE.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::locateInIDE()
        """
        self.call_com(lambda: self._com.locateInIDE())

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
    def gateway_export_to_xml(self, file_path: str) -> None:
        """Exports the project to an XML file using the Gateway tool.

        Args:
            file_path: The path of the XML file to create.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::gatewayExportToXML(java.lang.String filePath)
        """
        self.call_com(lambda: self._com.GatewayExportToXML(file_path))

    def gateway_export_to_xml2(self, file_path: str, options: str) -> None:
        """Exports the project to an XML file using the Gateway tool with options.

        Args:
            file_path: The path of the XML file to create.
            options: The options string to pass to the Gateway tool.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::gatewayExportToXML2(java.lang.String filePath, java.lang.String options)
        """
        self.call_com(lambda: self._com.GatewayExportToXML2(file_path, options))

    def generate_report(self, template_path: str, output_path: str) -> None:
        """Generates a report from the project using the specified template.

        Args:
            template_path: The path of the report template file.
            output_path: The path of the output report file to create.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::generateReport(java.lang.String templatePath, java.lang.String outputPath)
        """
        self.call_com(lambda: self._com.GenerateReport(template_path, output_path))

    # --- Custom Views methods ---
    def add_custom_view_on_browser(self, view: IRPModelElement) -> None:
        """Adds a custom view to be applied on the Rhapsody browser.

        Args:
            view: The wrapped custom view to add.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addCustomViewOnBrowser(com.telelogic.rhapsody.core.IRPCustomView view)
        """
        self.call_com(lambda: self._com.addCustomViewOnBrowser(view._com))

    def add_custom_view_on_diagram(self, view: IRPModelElement) -> None:
        """Adds a custom view to be applied on diagrams.

        Args:
            view: The wrapped custom view to add.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addCustomViewOnDiagram(com.telelogic.rhapsody.core.IRPCustomView view)
        """
        self.call_com(lambda: self._com.addCustomViewOnDiagram(view._com))

    def apply_browser_custom_views_on_diagrams(self) -> None:
        """Applies the browser custom views on diagrams.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::applyBrowserCustomViewsOnDiagrams()
        """
        self.call_com(lambda: self._com.applyBrowserCustomViewsOnDiagrams())

    def get_active_custom_views_on_browser(self) -> IRPCollection:
        """Returns the active custom views applied on the browser.

        Returns:
            An ``IRPCollection`` of active browser custom views.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getActiveCustomViewsOnBrowser()
        """
        return IRPCollection(self.call_com(lambda: self._com.getActiveCustomViewsOnBrowser()))

    def get_active_custom_views_on_diagram(self) -> IRPCollection:
        """Returns the active custom views applied on diagrams.

        Returns:
            An ``IRPCollection`` of active diagram custom views.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getActiveCustomViewsOnDiagram()
        """
        return IRPCollection(self.call_com(lambda: self._com.getActiveCustomViewsOnDiagram()))

    def remove_custom_view_on_browser(self, view: IRPModelElement) -> None:
        """Removes a custom view from the browser.

        Args:
            view: The wrapped custom view to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::removeCustomViewOnBrowser(com.telelogic.rhapsody.core.IRPCustomView view)
        """
        self.call_com(lambda: self._com.removeCustomViewOnBrowser(view._com))

    def remove_custom_view_on_diagram(self, view: IRPModelElement) -> None:
        """Removes a custom view from diagrams.

        Args:
            view: The wrapped custom view to remove.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::removeCustomViewOnDiagram(com.telelogic.rhapsody.core.IRPCustomView view)
        """
        self.call_com(lambda: self._com.removeCustomViewOnDiagram(view._com))

    # --- CSV methods ---
    def close_csv_file(self) -> None:
        """Closes the CSV file currently open in the project.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::closeCSVFile()
        """
        self.call_com(lambda: self._com.closeCSVFile())

    def open_csv_file(self, file_path: str, mode: int) -> None:
        """Opens a CSV file for requirements import.

        Args:
            file_path: The path of the CSV file to open.
            mode: The mode in which to open the file.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::openCSVFile(java.lang.String filePath, int mode)
        """
        self.call_com(lambda: self._com.openCSVFile(file_path, mode))

    def reload_csv_file(self) -> None:
        """Reloads the CSV file currently open in the project.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::reloadCSVFile()
        """
        self.call_com(lambda: self._com.reloadCSVFile())

    # --- Remote/Roundtrip methods ---
    def apply_roundtrip_diff_merge(self) -> None:
        """Applies the roundtrip diff merge for the project.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::applyRoundtripDiffMerge()
        """
        self.call_com(lambda: self._com.applyRoundtripDiffMerge())

    def enable_rhapsody_model_manager(self) -> None:
        """Enable Rhapsody Model Manager for the project.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::enableRhapsodyModelManager()
        """
        raise NotImplementedError("enableRhapsodyModelManager is not exposed in the Rhapsody COM automation type library.")

    def find_elements_with_oslc_link(self, link: str) -> IRPCollection:
        """Returns the elements that have an OSLC link matching the specified link.

        Args:
            link: The OSLC link to search for.

        Returns:
            An ``IRPCollection`` of elements with the matching OSLC link.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::findElementsWithOSLCLink(java.lang.String link)
        """
        return IRPCollection(self.call_com(lambda: self._com.findElementsWithOSLCLink(link)))

    def get_remote_resource_packages(self) -> IRPCollection:
        """Returns the remote resource packages of the project.

        Returns:
            An ``IRPCollection`` of remote resource packages.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getRemoteResourcePackages()
        """
        return IRPCollection(self.call_com(lambda: self._com.getRemoteResourcePackages()))

    def get_roundtrip_shadow_model(self) -> object:
        """Returns the roundtrip shadow model of the project.

        Returns:
            The wrapped roundtrip shadow model.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getRoundtripShadowModel()
        """
        return self.wrap(self.call_com(lambda: self._com.getRoundtripShadowModel()))

    def is_actively_managed(self) -> int:
        """Checks whether the project is actively managed by Rhapsody Model Manager.

        Returns:
            ``1`` if the project is actively managed, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::isActivelyManaged()
        """
        return int(self.call_com(lambda: self._com.isActivelyManaged()))

    def migrate_design_manager_links(self) -> None:
        """Migrate Design Manager links for the project.

        Raises:
            NotImplementedError: This Java API method is not exposed by pywin32.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::migrateDesignManagerLinks()
        """
        raise NotImplementedError("migrateDesignManagerLinks is not exposed in the Rhapsody COM automation type library.")

    # --- Rose Import methods ---
    def import_package_from_rose(self, file_path: str) -> IRPPackage:
        """Imports a package from a Rational Rose model file.

        Args:
            file_path: The path of the Rose model file to import from.

        Returns:
            The wrapped ``IRPPackage`` created from the import.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::importPackageFromRose(java.lang.String filePath)
        """
        return cast(IRPPackage, self.wrap(self.call_com(lambda: self._com.importPackageFromRose(file_path))))

    def import_project_from_rose(self, file_path: str) -> None:
        """Imports a project from a Rational Rose model file.

        Args:
            file_path: The path of the Rose model file to import from.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::importProjectFromRose(java.lang.String filePath)
        """
        self.call_com(lambda: self._com.importProjectFromRose(file_path))

    # --- Events methods ---
    def check_events_base_ids_solve_collisions(self) -> int:
        """Checks events base IDs and solves collisions.

        Returns:
            The number of collisions solved.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::checkEventsBaseIdsSolveCollisions()
        """
        return int(self.call_com(lambda: self._com.checkEventsBaseIdsSolveCollisions()))

    def recalculate_events_base_ids(self) -> None:
        """Recalculates the events base IDs for the project.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::recalculateEventsBaseIds()
        """
        self.call_com(lambda: self._com.recalculateEventsBaseIds())

    # --- Misc methods ---
    def add_spell_checker_result(self, word: str, suggestion: str) -> None:
        """Adds a spell checker result with a suggestion.

        Args:
            word: The misspelled word.
            suggestion: The suggested correction.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::addSpellCheckerResult(java.lang.String word, java.lang.String suggestion)
        """
        self.call_com(lambda: self._com.addSpellCheckerResult(word, suggestion))

    def clean_unresolved_elements(self) -> None:
        """Cleans unresolved elements from the project.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::cleanUnresolvedElements()
        """
        self.call_com(lambda: self._com.cleanUnresolvedElements())

    def end_transaction_of_no_cg_interest(self) -> None:
        """Ends a transaction of no code generation interest.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::endTransactionOfNoCGInterest()
        """
        self.call_com(lambda: self._com.endTransactionOfNoCGInterest())

    @property
    def default_directory_scheme(self) -> int:
        """Returns the default directory scheme of the project.

        Returns:
            The default directory scheme as an int.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getDefaultDirectoryScheme()
        """
        return int(self.get_com_property(self._com, "defaultDirectoryScheme"))

    @default_directory_scheme.setter
    def default_directory_scheme(self, scheme: int) -> None:
        """Sets the default directory scheme of the project.

        Args:
            scheme: The default directory scheme to set.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setDefaultDirectoryScheme(int scheme)
        """
        self.set_com_property(self._com, "defaultDirectoryScheme", scheme)

    def get_new_progress_bar(self) -> IRPProgressBar:
        """Returns a new progress bar.

        Returns:
            The wrapped ``IRPProgressBar`` created.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getNewProgressBar()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_ide import IRPProgressBar

        return cast(IRPProgressBar, self.wrap(self.call_com(lambda: self._com.getNewProgressBar())))

    def get_notify_plugin_on_elements_changed(self) -> int:
        """Checks whether plugins are notified when elements change.

        Returns:
            ``1`` if plugins are notified, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getNotifyPluginOnElementsChanged()
        """
        return int(self.call_com(lambda: self._com.getNotifyPluginOnElementsChanged()))

    def get_requirements_by_id(self, id: str) -> IRPCollection:
        """Returns the requirements matching the specified ID.

        Args:
            id: The requirement ID to search for.

        Returns:
            An ``IRPCollection`` of matching requirements.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::getRequirementsByID(java.lang.String id)
        """
        return IRPCollection(self.call_com(lambda: self._com.getRequirementsByID(id)))

    def remove(self) -> None:
        """Removes the project.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::remove()
        """
        self.call_com(lambda: self._com.remove())

    def save_as_prev_version(self, file_path: str) -> None:
        """Saves the project to a previous version file path.

        Args:
            file_path: The path to save the project to.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::saveAsPrevVersion(java.lang.String filePath)
        """
        self.call_com(lambda: self._com.saveAsPrevVersion(file_path))

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

    @property
    def use_unique_stereotype_and_ref_cache(self) -> int:
        """Returns whether a unique stereotype and reference cache is used.

        Returns:
            ``1`` if the unique cache is used, ``0`` otherwise.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setUseUniqueStereotypeAndRefCache(int enabled)
        """
        return int(self.get_com_property(self._com, "UseUniqueStereotypeAndRefCache"))

    @use_unique_stereotype_and_ref_cache.setter
    def use_unique_stereotype_and_ref_cache(self, enabled: int) -> None:
        """Sets whether to use a unique stereotype and reference cache.

        Args:
            enabled: ``1`` to use the unique cache, ``0`` to not use it.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setUseUniqueStereotypeAndRefCache(int enabled)
        """
        self.set_com_property(self._com, "UseUniqueStereotypeAndRefCache", enabled)

    def set_wait_dialog_watchdog_value(self, value: int) -> None:
        """Sets the wait dialog watchdog value.

        Args:
            value: The wait dialog watchdog value to set.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::setWaitDialogWatchdogValue(int value)
        """
        self.call_com(lambda: self._com.setWaitDialogWatchdogValue(value))

    def start_transaction_of_no_cg_interest(self) -> None:
        """Starts a transaction of no code generation interest.

        Reference:
            com.telelogic.rhapsody.core.IRPProject::startTransactionOfNoCGInterest()
        """
        self.call_com(lambda: self._com.startTransactionOfNoCGInterest())


IRPModelElement.register_wrapper("Project", IRPProject)
