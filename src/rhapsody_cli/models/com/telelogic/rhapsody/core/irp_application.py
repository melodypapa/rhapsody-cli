"""Wrappers for ``com.telelogic.rhapsody.core.IRPApplication``.

Canonical module for :class:`IRPApplication`; see the class requirement
document at ``docs/requirements/com/telelogic/rhapsody/core/irp_application.md``.
The connection lifecycle (attach/launch/connect/disconnect) intentionally lives
on the :class:`rhapsody_cli.RhapsodyApplication` facade, which subclasses this
wrapper — COM members belong here, orchestration belongs there.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit import IRPUnit

if TYPE_CHECKING:
    from rhapsody_cli.exceptions import RhapsodyRuntimeException  # noqa: F401
    from rhapsody_cli.models.com.telelogic.rhapsody.core import (
        IRPCodeGenSimplifiersRegistry,
        IRPDiagSynthAPI,
        IRPExternalCheckRegistry,
        IRPExternalIDERegistry,
        IRPExternalRoundtripInvoker,
        IRPowPaneMgr,
        IRPSearchManager,
        IRPSelection,
    )


class IRPApplication(IRPModelElement):
    """Wraps ``IRPApplication``: the Rhapsody application itself.

    The IRPApplication interface represents the Rhapsody application, and its
    methods reflect many of the commands that you can access from the Rhapsody
    menu bar.
    """

    def open_project(self, filename: str) -> IRPProject:
        """Open an existing Rhapsody project.

        Args:
            filename: The name of the .rpy file, including the full path.

        Returns:
            IRPProject: The opened Rhapsody project.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openProject(java.lang.String filename)
        """
        return IRPProject(self.call_com(lambda: self._com.openProject(filename)))

    def create_new_project(self, project_location: str, project_name: str) -> IRPProject | None:
        """Create a new Rhapsody project.

        Args:
            project_location: The directory where the project should be saved.
            project_name: The name to use for the project (used for the .rpy file).

        Returns:
            IRPProject | None: The newly created active project, or ``None`` if Rhapsody
                does not report an active project after creation.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::createNewProject(java.lang.String projectLocation, java.lang.String projectName)
        """
        self.call_com(lambda: self._com.createNewProject(project_location, project_name))
        return self.active_project()

    def active_project(self) -> IRPProject | None:
        """Return the active project, or ``None`` if no project is open.

        Returns:
            IRPProject | None: The currently open project, or ``None`` when the
                COM member reports no active project.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::activeProject()
        """
        result = self.call_com(lambda: self._com.activeProject())
        return IRPProject(result) if result is not None else None

    @property
    def projects(self) -> IRPCollection:
        """Return all open projects in Rhapsody.

        Returns:
            IRPCollection: A collection of the open IRPProject objects.

        Raises:
            RhapsodyRuntimeException: If the projects cannot be retrieved.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getProjects()
        """
        return IRPCollection(self.get_com_property(self._com, "projects"))

    def quit(self) -> None:
        """Quit the Rhapsody application.

        Closes all projects and exits the Rhapsody process.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::quit()
        """
        self.call_com(lambda: self._com.quit())

    @property
    def is_hidden_ui(self) -> bool:
        """Return whether the Rhapsody GUI is hidden.

        Mirrors ``IRPApplication.getIsHiddenUI()``.

        Returns:
            bool: True if the Rhapsody UI is hidden, False if it is visible.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getIsHiddenUI()
        """
        return bool(self.get_com_property(self._com, "isHiddenUI"))

    def set_hidden_ui(self, hidden: bool) -> None:
        """Set whether the Rhapsody GUI is hidden.

        Mirrors ``IRPApplication.setHiddenUI()``. Rhapsody instances launched via
        COM automation (``Dispatch()``) start with the UI hidden by default; call
        ``setHiddenUI(False)`` after connecting to make the window visible.

        Args:
            hidden: False to show the GUI window, True to hide it.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setHiddenUI(boolean pVal)
        """
        self.call_com(lambda: self._com.setHiddenUI(hidden))

    def bring_window_to_top(self) -> None:
        """Bring the Rhapsody application window to the top.

        Mirrors ``IRPApplication.bringWindowToTop()``. Brings an already-visible
        window to the foreground; it does not make a hidden window visible. Use
        :meth:`set_hidden_ui` with ``False`` to show the GUI first.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::bringWindowToTop()
        """
        self.call_com(lambda: self._com.bringWindowToTop())

    def save_all(self) -> None:
        """Save all open projects.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::saveAll()
        """
        self.call_com(lambda: self._com.saveAll())

    def version(self) -> str:
        """Get the Rhapsody version.

        Returns:
            str: The Rhapsody version string.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::version()
        """
        return str(self.call_com(lambda: self._com.version()))

    @property
    def build_no(self) -> str:
        """Return the Rhapsody build number.

        Returns:
            str: The build number.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getBuildNo() — the COM
            surface exposes the ``BuildNo`` property (COM shape is authoritative).
        """
        return str(self.get_com_property(self._com, "BuildNo"))

    @property
    def omroot(self) -> str:
        """Return the OMROOT directory path.

        Returns:
            str: The OMROOT path.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getOMROOT() — the COM
            surface exposes the ``OMROOT`` property (COM shape is authoritative).
        """
        return str(self.get_com_property(self._com, "OMROOT"))

    def create_new_collection(self) -> IRPCollection:
        """Create a new empty ``IRPCollection`` for use with COM calls that require a pre-allocated collection.

        Some Rhapsody COM methods (e.g. ``IRPDiagram.getPicturesWithImageMap``) populate a
        caller-provided collection rather than returning one. Use this method to create
        the empty collection, pass it to such methods, then read the results from it.

        Returns:
            IRPCollection: A new, empty collection.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::createNewCollection()
        """
        return IRPCollection(self.call_com(lambda: self._com.createNewCollection()))

    def get_search_manager(self) -> IRPSearchManager:
        """Return the Rhapsody search manager.

        Returns:
            IRPSearchManager: The search manager for finding model elements.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getSearchManager()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPSearchManager

        return IRPSearchManager(self.call_com(lambda: self._com.getSearchManager()))

    def get_selection(self) -> IRPSelection:
        """Return the current Rhapsody selection.

        Returns:
            IRPSelection: The current selection in the Rhapsody UI.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getSelection()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPSelection

        return IRPSelection(self.call_com(lambda: self._com.getSelection()))

    def get_code_gen_simplifiers_registry(self) -> IRPCodeGenSimplifiersRegistry:
        """Return the code-gen simplifiers registry.

        Returns:
            IRPCodeGenSimplifiersRegistry: The registry of code generation simplifiers.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getCodeGenSimplifiersRegistry()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPCodeGenSimplifiersRegistry

        return IRPCodeGenSimplifiersRegistry(self.call_com(lambda: self._com.getCodeGenSimplifiersRegistry()))

    def get_diag_synth_api(self, client_name: str) -> IRPDiagSynthAPI:
        """Return the diagram synthesis API for the given client.

        Args:
            client_name: The name of the client requesting the API.

        Returns:
            IRPDiagSynthAPI: The diagram synthesis API.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getDiagSynthAPI(java.lang.String clientName)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPDiagSynthAPI

        return IRPDiagSynthAPI(self.call_com(lambda: self._com.getDiagSynthAPI(client_name)))

    def get_external_checker_registry(self) -> IRPExternalCheckRegistry:
        """Return the external checker registry.

        Returns:
            IRPExternalCheckRegistry: The registry of external model checkers.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getExternalCheckerRegistry()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPExternalCheckRegistry

        return IRPExternalCheckRegistry(self.call_com(lambda: self._com.getExternalCheckerRegistry()))

    def get_external_ide_registry(self, client_id: str) -> IRPExternalIDERegistry:
        """Return the external IDE registry for the given client.

        Args:
            client_id: The ID of the client requesting the registry.

        Returns:
            IRPExternalIDERegistry: The external IDE registry.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getExternalIDERegistry(java.lang.String clientID)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPExternalIDERegistry

        return IRPExternalIDERegistry(self.call_com(lambda: self._com.getExternalIDERegistry(client_id)))

    def get_external_roundtrip_invoker(self) -> IRPExternalRoundtripInvoker:
        """Return the external roundtrip invoker.

        Returns:
            IRPExternalRoundtripInvoker: The external roundtrip invoker.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getExternalRoundtripInvoker()
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPExternalRoundtripInvoker

        return IRPExternalRoundtripInvoker(self.call_com(lambda: self._com.getExternalRoundtripInvoker()))

    def get_ow_pane_mgr(self, client_id: str) -> IRPowPaneMgr:
        """Return the output window pane manager for the given client.

        Args:
            client_id: The ID of the client requesting the pane manager.

        Returns:
            IRPowPaneMgr: The output window pane manager.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getOWPaneMgr(java.lang.String clientID)
        """
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPowPaneMgr

        return IRPowPaneMgr(self.call_com(lambda: self._com.getOWPaneMgr(client_id)))

    def generate(self) -> None:
        """Generate code for the entire project.

        Uses the active component and configuration. Use
        ``IRPProject.setActiveComponent`` and ``IRPProject.setActiveConfiguration``
        to change them first if necessary.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::generate()
        """
        self.call_com(lambda: self._com.generate())

    def generate_elements(self, elements: IRPCollection) -> None:
        """Generate code for the given elements.

        Args:
            elements: An IRPCollection of elements to generate code for.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::generateElements(com.telelogic.rhapsody.core.IRPCollection elements)
        """
        self.call_com(lambda: self._com.generateElements(elements._com))

    def generate_entire_project(self) -> None:
        """Generate code for the entire active project.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::generateEntireProject()
        """
        self.call_com(lambda: self._com.generateEntireProject())

    def regenerate(self) -> None:
        """Regenerate code for the active project (full regeneration).

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::regenerate()
        """
        self.call_com(lambda: self._com.regenerate())

    def add_to_model(self, filename: str, with_descendant: int) -> None:
        """Add a model element from a file to the model.

        Args:
            filename: Path to the file to add.
            with_descendant: 1 to also add descendants, 0 otherwise.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::addToModel(java.lang.String filename, int withDescendant)
        """
        self.call_com(lambda: self._com.addToModel(filename, with_descendant))

    def add_to_model_ex(self, filename: str, mode: int, add_sub_units: int, add_dependents: int) -> None:
        """Add a unit to the model with extended options.

        Args:
            filename: The full path to the file to add to the model.
            mode: How the unit should be added (see IRPApplication.AddToModel_Mode).
            add_sub_units: 1 to also add the unit's sub-units, 0 otherwise. Ignored
                when ``mode`` equals IRPApplication.AddToModel_Mode.AS_UNIT_WITHOUT_COPY.
            add_dependents: 1 to also add units that elements in the unit depend
                on, 0 otherwise. Ignored when ``mode`` equals
                IRPApplication.AddToModel_Mode.AS_UNIT_WITHOUT_COPY.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::addToModelEx(java.lang.String filename, int addToModelMode, int addSubUnits, int addDependents)
        """
        self.call_com(lambda: self._com.addToModelEx(filename, mode, add_sub_units, add_dependents))

    def set_log(self, full_pathname: str) -> None:
        """Set the log file path.

        Args:
            full_pathname: Full path to the log file.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setLog(java.lang.String logFile)
        """
        self.call_com(lambda: self._com.setLog(full_pathname))

    def check_model(self) -> None:
        """Run model checking on the active project.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::checkModel()
        """
        self.call_com(lambda: self._com.checkModel())

    def add_profile_to_model(self, profile_name: str) -> IRPUnit:
        """addProfileToModel

        Args:
            profile_name: See JavaDoc for profileName.

        Returns:
            IRPUnit: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::addProfileToModel
        """
        return IRPUnit(self.call_com(lambda: self._com.addProfileToModel(profile_name)))

    def add_selected_to_favorites(self) -> None:
        """Adds the currently selected item to the Favorites list

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::addSelectedToFavorites
        """
        self.call_com(lambda: self._com.addSelectedToFavorites())

    def add_to_model_by_reference(self, filename: str) -> None:
        """add To Model by reference

        Args:
            filename: See JavaDoc for filename.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::addToModelByReference
        """
        self.call_com(lambda: self._com.addToModelByReference(filename))

    def add_to_model_from_url(self, purl: str) -> None:
        """add To Model From URL

        Args:
            purl: See JavaDoc for purl.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::addToModelFromURL
        """
        self.call_com(lambda: self._com.addToModelFromURL(purl))

    def add_units_to_model(self, file_names_list: IRPCollection, add_to_model_mode: int, add_sub_units: int, add_dependents: int) -> IRPCollection:
        """Adds one or more units to the model

        Args:
            file_names_list: See JavaDoc for fileNamesList.
            add_to_model_mode: See JavaDoc for addToModelMode.
            add_sub_units: See JavaDoc for addSubUnits.
            add_dependents: See JavaDoc for addDependents.

        Returns:
            IRPCollection: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::addUnitsToModel
        """
        return IRPCollection(self.call_com(lambda: self._com.addUnitsToModel(file_names_list._com, add_to_model_mode, add_sub_units, add_dependents)))

    def allow_browser_refresh(self, should_refresh: int) -> None:
        """allowBrowserRefresh

        Args:
            should_refresh: See JavaDoc for shouldRefresh.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::allowBrowserRefresh
        """
        self.call_com(lambda: self._com.allowBrowserRefresh(should_refresh))

    def allow_ge_refresh(self, should_refresh: int) -> None:
        """allowGERefresh

        Args:
            should_refresh: See JavaDoc for shouldRefresh.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::allowGERefresh
        """
        self.call_com(lambda: self._com.allowGERefresh(should_refresh))

    def allow_rmm_remote_oslc_links_load(self, should_load: int) -> None:
        """allowRmmRemoteOslcLinksLoad

        Args:
            should_load: See JavaDoc for shouldLoad.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::allowRmmRemoteOslcLinksLoad
        """
        self.call_com(lambda: self._com.allowRmmRemoteOslcLinksLoad(should_load))

    def get_application_connection_string(self) -> str:
        """getApplicationConnectionString

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getApplicationConnectionString
        """
        return str(self.call_com(lambda: self._com.getApplicationConnectionString()))

    def get_application_name(self, application_name: str, product_rcp_name: str) -> None:
        """Get application name

        Args:
            application_name: See JavaDoc for applicationName.
            product_rcp_name: See JavaDoc for productRCPName.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getApplicationName
        """
        self.call_com(lambda: self._com.getApplicationName(application_name, product_rcp_name))

    @property
    def application_root(self) -> str:
        """Gets the full path of the Rhapsody installation folder

        Returns:
            str: Gets the full path of the Rhapsody installation folder.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getApplicationRoot
        """
        return str(self.get_com_property(self._com, "ApplicationRoot"))

    def get_application_status(self) -> int:
        """getApplicationStatus

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getApplicationStatus
        """
        return int(self.call_com(lambda: self._com.getApplicationStatus()))

    def set_application_status(self, n_status: int) -> None:
        """setApplicationStatus

        Args:
            n_status: See JavaDoc for nStatus.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setApplicationStatus
        """
        self.call_com(lambda: self._com.setApplicationStatus(n_status))

    def apply_new_terms_profile(self, profile_name: str) -> None:
        """Called to apply a NewTerms Profile to the active project

        Args:
            profile_name: See JavaDoc for profileName.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::applyNewTermsProfile
        """
        self.call_com(lambda: self._com.applyNewTermsProfile(profile_name))

    def apply_window_layout(self, layout_name: str) -> int:
        """Applies the layout provided in parameter

        Args:
            layout_name: See JavaDoc for layoutName.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::applyWindowLayout
        """
        return int(self.call_com(lambda: self._com.applyWindowLayout(layout_name)))

    def arc_check_out(self, filename: str, label: str, is_locked: int, is_recursive: int) -> None:
        """archive Check Out

        Args:
            filename: See JavaDoc for filename.
            label: See JavaDoc for label.
            is_locked: See JavaDoc for isLocked.
            is_recursive: See JavaDoc for isRecursive.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::arcCheckOut
        """
        self.call_com(lambda: self._com.arcCheckOut(filename, label, is_locked, is_recursive))

    def build(self) -> None:
        """Builds an application using the active component and configuration

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::build
        """
        self.call_com(lambda: self._com.build())

    def build_entire_project(self) -> None:
        """buildEntireProject

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::buildEntireProject
        """
        self.call_com(lambda: self._com.buildEntireProject())

    def build_with_dependencies(self) -> None:
        """buildWithDependencies

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::buildWithDependencies
        """
        self.call_com(lambda: self._com.buildWithDependencies())

    def can_redo(self) -> int:
        """Check if Redo action is available

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::canRedo
        """
        return int(self.call_com(lambda: self._com.canRedo()))

    def can_undo(self) -> int:
        """Check if Undo action is available

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::canUndo
        """
        return int(self.call_com(lambda: self._com.canUndo()))

    def check_in(self, unit_name: str, label: str, is_locked: int, is_recursive: int, description: str) -> None:
        """check In

        Args:
            unit_name: See JavaDoc for unitName.
            label: See JavaDoc for label.
            is_locked: See JavaDoc for isLocked.
            is_recursive: See JavaDoc for isRecursive.
            description: See JavaDoc for description.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::checkIn
        """
        self.call_com(lambda: self._com.checkIn(unit_name, label, is_locked, is_recursive, description))

    def check_out(self, unit_name: str, label: str, is_locked: int, is_recursive: int) -> None:
        """check Out

        Args:
            unit_name: See JavaDoc for unitName.
            label: See JavaDoc for label.
            is_locked: See JavaDoc for isLocked.
            is_recursive: See JavaDoc for isRecursive.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::checkOut
        """
        self.call_com(lambda: self._com.checkOut(unit_name, label, is_locked, is_recursive))

    def clean(self) -> None:
        """clean

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::clean
        """
        self.call_com(lambda: self._com.clean())

    def clear_output_window(self, title: str) -> None:
        """clear output window

        Args:
            title: See JavaDoc for title.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::clearOutputWindow
        """
        self.call_com(lambda: self._com.clearOutputWindow(title))

    def close_all_animated_sequence_diagrams(self, with_save: int) -> None:
        """Close All Animated Sequence diagrams without save

        Args:
            with_save: See JavaDoc for withSave.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::closeAllAnimatedSequenceDiagrams
        """
        self.call_com(lambda: self._com.closeAllAnimatedSequenceDiagrams(with_save))

    def compare_sequence_diagram(self, left_diagram: IRPModelElement, right_diagram: IRPModelElement) -> None:
        """Compares the two sequence diagrams specified as parameters

        Args:
            left_diagram: See JavaDoc for leftDiagram.
            right_diagram: See JavaDoc for rightDiagram.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::compareSequenceDiagram
        """
        self.call_com(lambda: self._com.compareSequenceDiagram(left_diagram._com, right_diagram._com))

    def set_component(self, component: str) -> None:
        """set Component

        Args:
            component: See JavaDoc for component.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setComponent
        """
        self.call_com(lambda: self._com.setComponent(component))

    def set_configuration(self, configuration: str) -> None:
        """set Configuration

        Args:
            configuration: See JavaDoc for configuration.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setConfiguration
        """
        self.call_com(lambda: self._com.setConfiguration(configuration))

    def connect_to_archive(self, archive_path: str) -> None:
        """connect To Archive

        Args:
            archive_path: See JavaDoc for archivePath.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::connectToArchive
        """
        self.call_com(lambda: self._com.connectToArchive(archive_path))

    def connect_to_imported_model(self, server_url: str, project_area_name: str, stream_name: str) -> None:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            server_url: See JavaDoc for serverURL.
            project_area_name: See JavaDoc for projectAreaName.
            stream_name: See JavaDoc for streamName.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::connectToImportedModel
        """
        self.call_com(lambda: self._com.connectToImportedModel(server_url, project_area_name, stream_name))

    def connect_to_target(self, target_name: str) -> None:
        """connectToTarget

        Args:
            target_name: See JavaDoc for targetName.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::connectToTarget
        """
        self.call_com(lambda: self._com.connectToTarget(target_name))

    def create_and_insert_project(self, project_location: str, project_name: str) -> int:
        """Create a new project and insert it into current workspace

        Args:
            project_location: See JavaDoc for projectLocation.
            project_name: See JavaDoc for projectName.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::createAndInsertProject
        """
        return int(self.call_com(lambda: self._com.createAndInsertProject(project_location, project_name)))

    def create_domain_from_profile(self, profile_arg: IRPModelElement, server_url: str) -> None:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            profile_arg: See JavaDoc for profileArg.
            server_url: See JavaDoc for serverURL.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::createDomainFromProfile
        """
        self.call_com(lambda: self._com.createDomainFromProfile(profile_arg._com, server_url))

    def create_embedded_web_view_window(self, html_file: str, window_kind: str, window_location: str) -> int:
        """creates new web viewer window when model is opened

        Args:
            html_file: See JavaDoc for htmlFile.
            window_kind: See JavaDoc for windowKind.
            window_location: See JavaDoc for windowLocation.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::createEmbeddedWebViewWindow
        """
        return int(self.call_com(lambda: self._com.createEmbeddedWebViewWindow(html_file, window_kind, window_location)))

    def create_progress_bar(self, name: str) -> object:
        """Creates a new progress bar with the specified name

        Args:
            name: See JavaDoc for name.

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::createProgressBar
        """
        return self.call_com(lambda: self._com.createProgressBar(name))

    def get_dm_bool_property(self, p_key: str) -> int:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            p_key: See JavaDoc for pKey.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getDMBoolProperty
        """
        return int(self.call_com(lambda: self._com.getDMBoolProperty(p_key)))

    def set_dm_bool_property(self, p_key: str, val: int) -> None:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            p_key: See JavaDoc for pKey.
            val: See JavaDoc for val.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setDMBoolProperty
        """
        self.call_com(lambda: self._com.setDMBoolProperty(p_key, val))

    def get_dm_model_workspace_folder(self) -> str:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getDMModelWorkspaceFolder
        """
        return str(self.call_com(lambda: self._com.getDMModelWorkspaceFolder()))

    def get_dm_property(self, p_key: str) -> str:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            p_key: See JavaDoc for pKey.

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getDMProperty
        """
        return str(self.call_com(lambda: self._com.getDMProperty(p_key)))

    def set_dm_property(self, p_key: str, val: str) -> None:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            p_key: See JavaDoc for pKey.
            val: See JavaDoc for val.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setDMProperty
        """
        self.call_com(lambda: self._com.setDMProperty(p_key, val))

    def d_m_refresh_recursive(self, p_unit: IRPUnit) -> None:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            p_unit: See JavaDoc for pUnit.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::dMRefreshRecursive
        """
        self.call_com(lambda: self._com.dMRefreshRecursive(p_unit._com))

    def d_m_sync_and_refresh(self, project_arg: IRPProject, sync: int, refresh: int) -> None:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            project_arg: See JavaDoc for projectArg.
            sync: See JavaDoc for sync.
            refresh: See JavaDoc for refresh.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::dMSyncAndRefresh
        """
        self.call_com(lambda: self._com.dMSyncAndRefresh(project_arg._com, sync, refresh))

    def dbg_check_com_in(self, i: int) -> None:
        """For debug - check communication in

        Args:
            i: See JavaDoc for i.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::dbgCheckComIn
        """
        self.call_com(lambda: self._com.dbgCheckComIn(i))

    def dbg_check_com_out(self) -> int:
        """For debug - check communication out

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::dbgCheckComOut
        """
        return int(self.call_com(lambda: self._com.dbgCheckComOut()))

    def deferred_add_to_model(self, filename: str, with_descendants: int, orig_prj_id: str, erase_dir: int) -> None:
        """Add Rhapsody unit to current project

        Args:
            filename: See JavaDoc for filename.
            with_descendants: See JavaDoc for withDescendants.
            orig_prj_id: See JavaDoc for origPrjId.
            erase_dir: See JavaDoc for eraseDir.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::deferredAddToModel
        """
        self.call_com(lambda: self._com.deferredAddToModel(filename, with_descendants, orig_prj_id, erase_dir))

    def delete_project_from_list(self, project_name: str) -> int:
        """Delete specified project from current workspace

        Args:
            project_name: See JavaDoc for projectName.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::deleteProjectFromList
        """
        return int(self.call_com(lambda: self._com.deleteProjectFromList(project_name)))

    def delete_window_layout(self, layout_name: str) -> int:
        """Delete the layout from the Rhapsody window layout location

        Args:
            layout_name: See JavaDoc for layoutName.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::deleteWindowLayout
        """
        return int(self.call_com(lambda: self._com.deleteWindowLayout(layout_name)))

    def get_diagram_of_selected_element(self) -> object:
        """get diagram of selected element

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getDiagramOfSelectedElement
        """
        return self.call_com(lambda: self._com.getDiagramOfSelectedElement())

    def disconnect_from_target(self) -> None:
        """disconnectFromTarget

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::disconnectFromTarget
        """
        self.call_com(lambda: self._com.disconnectFromTarget())

    def download_to_target(self, filename: str) -> None:
        """downloadToTarget

        Args:
            filename: See JavaDoc for filename.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::downloadToTarget
        """
        self.call_com(lambda: self._com.downloadToTarget(filename))

    def end_undo_transaction(self) -> None:
        """end undo transaction

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::endUndoTransaction
        """
        self.call_com(lambda: self._com.endUndoTransaction())

    def enter_animation_command(self, command: str) -> None:
        """enter Animation Command

        Args:
            command: See JavaDoc for command.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::enterAnimationCommand
        """
        self.call_com(lambda: self._com.enterAnimationCommand(command))

    def error_message(self) -> str:
        """Returns error message for last method called

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::errorMessage
        """
        return str(self.call_com(lambda: self._com.errorMessage()))

    def get_error_message(self, _midl__irp_application0000_: str) -> str:
        """Returns error message for last method called

        Args:
            _midl__irp_application0000_: See JavaDoc for _MIDL__IRPApplication0000_.

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getErrorMessage
        """
        return str(self.call_com(lambda: self._com.getErrorMessage(_midl__irp_application0000_)))

    def get_executable_folder(self) -> str:
        """getExecutableFolder

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getExecutableFolder
        """
        return str(self.call_com(lambda: self._com.getExecutableFolder()))

    def execute_command(self, command_type: str, p_command_initialization: IRPCollection, p_command_result: IRPCollection) -> None:
        """method execute command

        Args:
            command_type: See JavaDoc for commandType.
            p_command_initialization: See JavaDoc for pCommandInitialization.
            p_command_result: See JavaDoc for pCommandResult.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::executeCommand
        """
        self.call_com(lambda: self._com.ExecuteCommand(command_type, p_command_initialization._com, p_command_result._com))

    def execute_command_line(self, command_line: str) -> int:
        """Execute command line

        Args:
            command_line: See JavaDoc for commandLine.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::executeCommandLine
        """
        return int(self.call_com(lambda: self._com.executeCommandLine(command_line)))

    def execute_transformation_sequence(self, transformation_sequence: str, show_transformed_model_package: int) -> None:
        """Carries out model transformations in AUTOSAR projects that use one of the AR_BMT profiles for code generation

        Args:
            transformation_sequence: See JavaDoc for transformationSequence.
            show_transformed_model_package: See JavaDoc for showTransformedModelPackage.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::executeTransformationSequence
        """
        self.call_com(lambda: self._com.executeTransformationSequence(transformation_sequence, show_transformed_model_package))

    def expand_string_keywords(self, the_string: str) -> str:
        """expand environment-variable keywords in the provided string

        Args:
            the_string: See JavaDoc for theString.

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::expandStringKeywords
        """
        return str(self.call_com(lambda: self._com.expandStringKeywords(the_string)))

    def export_window_layout(self, layout_name: str, path_to_export: str, overwrite_if_exists: int) -> int:
        """Exports the layout to the folder specified in the pathToExport

        Args:
            layout_name: See JavaDoc for layoutName.
            path_to_export: See JavaDoc for pathToExport.
            overwrite_if_exists: See JavaDoc for overwriteIfExists.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::exportWindowLayout
        """
        return int(self.call_com(lambda: self._com.exportWindowLayout(layout_name, path_to_export, overwrite_if_exists)))

    def fixpack(self) -> str:
        """Get Rhapsody fixpack

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::fixpack
        """
        return str(self.call_com(lambda: self._com.fixpack()))

    def force_output2_console(self, val: int) -> None:
        """Force output to system console

        Args:
            val: See JavaDoc for val.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::forceOutput2Console
        """
        self.call_com(lambda: self._com.forceOutput2Console(val))

    def force_roundtrip(self) -> None:
        """forceRoundtrip

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::forceRoundtrip
        """
        self.call_com(lambda: self._com.forceRoundtrip())

    def force_roundtrip_elements(self, elements: IRPCollection) -> None:
        """method forceRoundtripElements

        Args:
            elements: See JavaDoc for elements.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::forceRoundtripElements
        """
        self.call_com(lambda: self._com.forceRoundtripElements(elements._com))

    def generate_main_and_make_files(self) -> None:
        """Generate Main and Make Files

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::generateMainAndMakeFiles
        """
        self.call_com(lambda: self._com.generateMainAndMakeFiles())

    def generate_with_dependencies(self) -> None:
        """generateWithDependencies

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::generateWithDependencies
        """
        self.call_com(lambda: self._com.generateWithDependencies())

    def get_helper_status(self, helper_name: str) -> int:
        """Returns the enable/disable status for menu or toolbar button created by hep file

        Args:
            helper_name: See JavaDoc for helperName.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getHelperStatus
        """
        return int(self.call_com(lambda: self._com.getHelperStatus(helper_name)))

    def set_helper_status(self, helper_name: str, b_enable: int) -> None:
        """Set enable/disable status for menu or toolbar button created by hep file

        Args:
            helper_name: See JavaDoc for helperName.
            b_enable: See JavaDoc for bEnable.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setHelperStatus
        """
        self.call_com(lambda: self._com.setHelperStatus(helper_name, b_enable))

    def high_light_element(self, val: IRPModelElement) -> None:  # type: ignore[override]
        """highlight element

        Args:
            val: See JavaDoc for val.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::highLightElement
        """
        self.call_com(lambda: self._com.highLightElement(val._com))

    def highlight_by_handle(self, str_handle: str) -> None:
        """highlight by handle

        Args:
            str_handle: See JavaDoc for strHandle.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::highlightByHandle
        """
        self.call_com(lambda: self._com.highlightByHandle(str_handle))

    def import_classes(self) -> None:
        """import Classes

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::importClasses
        """
        self.call_com(lambda: self._com.importClasses())

    def import_design_manager_model(self, server_url: str, project_area_name: str, stream_name: str, model_name: str, saveas_directory: str, include_links: int) -> IRPProject:
        """Imports a Rhapsody Design Manager model into a new Rhapsody project

        Args:
            server_url: See JavaDoc for serverURL.
            project_area_name: See JavaDoc for projectAreaName.
            stream_name: See JavaDoc for streamName.
            model_name: See JavaDoc for modelName.
            saveas_directory: See JavaDoc for saveasDirectory.
            include_links: See JavaDoc for includeLinks.

        Returns:
            IRPProject: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::importDesignManagerModel
        """
        return IRPProject(self.call_com(lambda: self._com.importDesignManagerModel(server_url, project_area_name, stream_name, model_name, saveas_directory, include_links)))

    def import_sync_simulink_block2(self, simulink_block: IRPModelElement, matlab_exe_path: str, sim_mdl_file: str, sim_src_files: str, sample_time: str) -> None:
        """Imports a Simulink model into a Rhapsody model

        Args:
            simulink_block: See JavaDoc for simulinkBlock.
            matlab_exe_path: See JavaDoc for matlabExePath.
            sim_mdl_file: See JavaDoc for simMdlFile.
            sim_src_files: See JavaDoc for simSrcFiles.
            sample_time: See JavaDoc for sampleTime.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::importSyncSimulinkBlock2
        """
        self.call_com(lambda: self._com.importSyncSimulinkBlock2(simulink_block._com, matlab_exe_path, sim_mdl_file, sim_src_files, sample_time))

    def import_tlb(self, p_path: str) -> None:
        """import tlb

        Args:
            p_path: See JavaDoc for pPath.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::importTlb
        """
        self.call_com(lambda: self._com.importTlb(p_path))

    def import_window_layout(self, layout_file: str, overwrite_if_exists: int) -> int:
        """Imports a layout from the file specified in layoutFile to the Rhapsody window layout location, from where it can be applied

        Args:
            layout_file: See JavaDoc for layoutFile.
            overwrite_if_exists: See JavaDoc for overwriteIfExists.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::importWindowLayout
        """
        return int(self.call_com(lambda: self._com.importWindowLayout(layout_file, overwrite_if_exists)))

    def get_ini_file_parameter_value(self, section_name: str, param_name: str) -> str:
        """getIniFileParameterValue

        Args:
            section_name: See JavaDoc for sectionName.
            param_name: See JavaDoc for paramName.

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getIniFileParameterValue
        """
        return str(self.call_com(lambda: self._com.getIniFileParameterValue(section_name, param_name)))

    def insert_project(self, filename: str) -> IRPProject:
        """Insert existing project into current workspace

        Args:
            filename: See JavaDoc for filename.

        Returns:
            IRPProject: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::insertProject
        """
        return IRPProject(self.call_com(lambda: self._com.insertProject(filename)))

    def insert_project_from_design_manager(self, user_name: str, passwd: str, server_url: str, project_area_name: str, stream_name: str, model_name: str) -> IRPProject:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            user_name: See JavaDoc for userName.
            passwd: See JavaDoc for passwd.
            server_url: See JavaDoc for serverURL.
            project_area_name: See JavaDoc for projectAreaName.
            stream_name: See JavaDoc for streamName.
            model_name: See JavaDoc for modelName.

        Returns:
            IRPProject: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::insertProjectFromDesignManager
        """
        return IRPProject(self.call_com(lambda: self._com.insertProjectFromDesignManager(user_name, passwd, server_url, project_area_name, stream_name, model_name)))

    @property
    def interface_name(self) -> str:
        """get property interfaceName

        Returns:
            str: get property interfaceName.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getInterfaceName
        """
        return str(self.get_com_property(self._com, "interfaceName"))

    def invoke_plugins_method(self, method_name: str) -> None:
        """invoke Plugins Method

        Args:
            method_name: See JavaDoc for methodName.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::invokePluginsMethod
        """
        self.call_com(lambda: self._com.invokePluginsMethod(method_name))

    def invoke_rpe(self) -> None:
        """Opens the Rhapsody Report Generator wizard

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::invokeRPE
        """
        self.call_com(lambda: self._com.invokeRPE())

    @property
    def is_load_on_demand(self) -> int:
        """get property isLoadOnDemand

        Returns:
            int: get property isLoadOnDemand.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getIsLoadOnDemand
        """
        return int(self.get_com_property(self._com, "isLoadOnDemand"))

    @is_load_on_demand.setter
    def is_load_on_demand(self, is_load_on_demand: int) -> None:
        """set property isLoadOnDemand

        Args:
            is_load_on_demand: Value to set.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setIsLoadOnDemand
        """
        self.set_com_property(self._com, "isLoadOnDemand", is_load_on_demand)

    def is_rhapsody_cl(self) -> int:
        """Is RhapsodyCL

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::isRhapsodyCL
        """
        return int(self.call_com(lambda: self._com.isRhapsodyCL()))

    def is_rhapsody_file_type(self, extension: str) -> int:
        """Check if specified extension corresponds to any Rhapsody unit type

        Args:
            extension: See JavaDoc for extension.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::isRhapsodyFileType
        """
        return int(self.call_com(lambda: self._com.isRhapsodyFileType(extension)))

    def is_valid_web_view(self, n_handle: object) -> int:
        """Checks weather provided Handle of WebView Window is valid or not

        Args:
            n_handle: See JavaDoc for nHandle.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::isValidWebView
        """
        return int(self.call_com(lambda: self._com.isValidWebView(n_handle)))

    @property
    def language(self) -> str:
        """get property Language

        Returns:
            str: get property Language.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getLanguage
        """
        return str(self.get_com_property(self._com, "Language"))

    @language.setter
    def language(self, language: str) -> None:
        """set property Language

        Args:
            language: Value to set.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setLanguage
        """
        self.set_com_property(self._com, "Language", language)

    def get_list_of_factory_properties(self) -> IRPCollection:
        """get list of factory properties

        Returns:
            IRPCollection: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getListOfFactoryProperties
        """
        return IRPCollection(self.call_com(lambda: self._com.getListOfFactoryProperties()))

    def get_list_of_selected_elements(self) -> IRPCollection:
        """get list of selected elements

        Returns:
            IRPCollection: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getListOfSelectedElements
        """
        return IRPCollection(self.call_com(lambda: self._com.getListOfSelectedElements()))

    def get_list_of_site_properties(self) -> IRPCollection:
        """get list of site properties

        Returns:
            IRPCollection: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getListOfSiteProperties
        """
        return IRPCollection(self.call_com(lambda: self._com.getListOfSiteProperties()))

    def get_locale_name(self) -> str:
        """Returns the locale for the version of Rhapsody running

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getLocaleName
        """
        return str(self.call_com(lambda: self._com.getLocaleName()))

    @property
    def log_root(self) -> str:
        """Gets the full path of the folder used for the Rhapsody log files

        Returns:
            str: Gets the full path of the folder used for the Rhapsody log files.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getLogRoot
        """
        return str(self.get_com_property(self._com, "LogRoot"))

    def login_to_design_manager_with_alias(self, server_url: str, alias: str) -> int:
        """Used to log in to a Design Manager server

        Args:
            server_url: See JavaDoc for serverURL.
            alias: See JavaDoc for alias.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::loginToDesignManagerWithAlias
        """
        return int(self.call_com(lambda: self._com.loginToDesignManagerWithAlias(server_url, alias)))

    def login_to_design_manager_with_certificate(self, server_url: str, certificate_location: str, password: str) -> int:
        """Used to log in to a Design Manager server

        Args:
            server_url: See JavaDoc for serverURL.
            certificate_location: See JavaDoc for certificateLocation.
            password: See JavaDoc for password.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::loginToDesignManagerWithCertificate
        """
        return int(self.call_com(lambda: self._com.loginToDesignManagerWithCertificate(server_url, certificate_location, password)))

    def login_to_design_manager_with_username(self, server_url: str, user_name: str, password: str) -> int:
        """Used to log in to a Design Manager server

        Args:
            server_url: See JavaDoc for serverURL.
            user_name: See JavaDoc for userName.
            password: See JavaDoc for password.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::loginToDesignManagerWithUsername
        """
        return int(self.call_com(lambda: self._com.loginToDesignManagerWithUsername(server_url, user_name, password)))

    def make(self) -> None:
        """make

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::make
        """
        self.call_com(lambda: self._com.make())

    def merge_elements(self, left: IRPModelElement, right: IRPModelElement) -> None:
        """mergeElements

        Args:
            left: See JavaDoc for left.
            right: See JavaDoc for right.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::mergeElements
        """
        self.call_com(lambda: self._com.mergeElements(left._com, right._com))

    def get_model_element_from_source(self, source_data: str, is_source_data_isfile_name: int, line_number: int) -> IRPModelElement:
        """Find model element from source code

        Args:
            source_data: See JavaDoc for sourceData.
            is_source_data_isfile_name: See JavaDoc for isSourceDataIsfileName.
            line_number: See JavaDoc for lineNumber.

        Returns:
            IRPModelElement: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getModelElementFromSource
        """
        return IRPModelElement(self.call_com(lambda: self._com.getModelElementFromSource(source_data, is_source_data_isfile_name, line_number)))

    def new_project_on_design_manager(self, user_name: str, password: str, server_url: str, project_area_name: str, stream_name: str, model_name: str) -> IRPProject:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            user_name: See JavaDoc for userName.
            password: See JavaDoc for password.
            server_url: See JavaDoc for serverURL.
            project_area_name: See JavaDoc for projectAreaName.
            stream_name: See JavaDoc for streamName.
            model_name: See JavaDoc for modelName.

        Returns:
            IRPProject: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::newProjectOnDesignManager
        """
        return IRPProject(self.call_com(lambda: self._com.newProjectOnDesignManager(user_name, password, server_url, project_area_name, stream_name, model_name)))

    def notify_file_changed(self, filename: str, content_changed: int) -> None:
        """File change notification

        Args:
            filename: See JavaDoc for filename.
            content_changed: See JavaDoc for contentChanged.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::notifyFileChanged
        """
        self.call_com(lambda: self._com.notifyFileChanged(filename, content_changed))

    def open_active_x_view(self, view_type: str, p_view_initialization: IRPCollection, p_extra: IRPCollection) -> object:
        """Open ActivexView

        Args:
            view_type: See JavaDoc for viewType.
            p_view_initialization: See JavaDoc for pViewInitialization.
            p_extra: See JavaDoc for pExtra.

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openActiveXView
        """
        return self.call_com(lambda: self._com.OpenActiveXView(view_type, p_view_initialization._com, p_extra._com))

    def open_advanced_search_and_replace_dialog(self) -> None:
        """Open Advanced Search and Replace dialog

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openAdvancedSearchAndReplaceDialog
        """
        self.call_com(lambda: self._com.openAdvancedSearchAndReplaceDialog())

    def open_diagram_view(self, diagram: IRPModelElement) -> object:
        """method OpenDiagramView

        Args:
            diagram: See JavaDoc for diagram.

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openDiagramView
        """
        return self.call_com(lambda: self._com.OpenDiagramView(diagram._com))

    def open_file_list(self, filename: str) -> None:
        """method openFileList

        Args:
            filename: See JavaDoc for filename.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openFileList
        """
        self.call_com(lambda: self._com.openFileList(filename))

    def open_project_from_design_manager(self, user_name: str, password: str, server_url: str, project_area_name: str, stream_name: str, model_name: str) -> IRPProject:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            user_name: See JavaDoc for userName.
            password: See JavaDoc for password.
            server_url: See JavaDoc for serverURL.
            project_area_name: See JavaDoc for projectAreaName.
            stream_name: See JavaDoc for streamName.
            model_name: See JavaDoc for modelName.

        Returns:
            IRPProject: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openProjectFromDesignManager
        """
        return IRPProject(self.call_com(lambda: self._com.openProjectFromDesignManager(user_name, password, server_url, project_area_name, stream_name, model_name)))

    def open_project_from_design_manager_after_login(self, server_url: str, project_area_name: str, stream_name: str, model_name: str) -> IRPProject:
        """Deprecated. Support for Design Manager was removed from Rhapsody in release 8.4

        Args:
            server_url: See JavaDoc for serverURL.
            project_area_name: See JavaDoc for projectAreaName.
            stream_name: See JavaDoc for streamName.
            model_name: See JavaDoc for modelName.

        Returns:
            IRPProject: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openProjectFromDesignManagerAfterLogin
        """
        return IRPProject(self.call_com(lambda: self._com.openProjectFromDesignManagerAfterLogin(server_url, project_area_name, stream_name, model_name)))

    def open_project_from_url(self, purl: str) -> None:
        """open Project From URL

        Args:
            purl: See JavaDoc for purl.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openProjectFromURL
        """
        self.call_com(lambda: self._com.openProjectFromURL(purl))

    def open_project_with_last_session(self, filename: str) -> IRPProject:
        """open project with last session

        Args:
            filename: See JavaDoc for filename.

        Returns:
            IRPProject: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openProjectWithLastSession
        """
        return IRPProject(self.call_com(lambda: self._com.openProjectWithLastSession(filename)))

    def open_project_without_sub_units(self, filename: str) -> IRPProject:
        """open project without subunits

        Args:
            filename: See JavaDoc for filename.

        Returns:
            IRPProject: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::openProjectWithoutSubUnits
        """
        return IRPProject(self.call_com(lambda: self._com.openProjectWithoutSubUnits(filename)))

    def get_output_window_text(self) -> str:
        """Returns the text displayed in the output window

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getOutputWindowText
        """
        return str(self.call_com(lambda: self._com.getOutputWindowText()))

    def get_progress_bar(self, s_id: str) -> object:
        """Retrieves a progress bar by its unique identifier

        Args:
            s_id: See JavaDoc for sID.

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getProgressBar
        """
        return self.call_com(lambda: self._com.getProgressBar(s_id))

    def rebuild(self) -> None:
        """rebuild

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::rebuild
        """
        self.call_com(lambda: self._com.rebuild())

    def rebuild_entire_project(self) -> None:
        """rebuildEntireProject

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::rebuildEntireProject
        """
        self.call_com(lambda: self._com.rebuildEntireProject())

    def rebuild_with_dependencies(self) -> None:
        """rebuildWithDependencies

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::rebuildWithDependencies
        """
        self.call_com(lambda: self._com.rebuildWithDependencies())

    def redo(self) -> int:
        """Perform Redo

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::redo
        """
        return int(self.call_com(lambda: self._com.redo()))

    def refactor_selected_operation(self, new_name: str) -> None:
        """Changes the name of the currently-selected operation and updates any references to the operation accordingly

        Args:
            new_name: See JavaDoc for newName.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::refactorSelectedOperation
        """
        self.call_com(lambda: self._com.refactorSelectedOperation(new_name))

    def refresh_all_views(self) -> None:
        """refresh all views

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::refreshAllViews
        """
        self.call_com(lambda: self._com.refreshAllViews())

    def regenerate_elements(self, elements: IRPCollection) -> None:
        """method regenerateElements

        Args:
            elements: See JavaDoc for elements.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::regenerateElements
        """
        self.call_com(lambda: self._com.regenerateElements(elements._com))

    def regenerate_entire_project(self) -> None:
        """regenerateEntireProject

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::regenerateEntireProject
        """
        self.call_com(lambda: self._com.regenerateEntireProject())

    def regenerate_with_dependencies(self) -> None:
        """regenerateWithDependencies

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::regenerateWithDependencies
        """
        self.call_com(lambda: self._com.regenerateWithDependencies())

    def register_com_client(self, process_id: int, client_filename: str, magic_number: int) -> None:
        """register COM client

        Args:
            process_id: See JavaDoc for processID.
            client_filename: See JavaDoc for clientFilename.
            magic_number: See JavaDoc for magicNumber.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::registerCOMClient
        """
        self.call_com(lambda: self._com.registerCOMClient(process_id, client_filename, magic_number))

    def remove_progress_bar(self, progress: IRPModelElement) -> int:
        """Removes a progress bar

        Args:
            progress: See JavaDoc for progress.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::removeProgressBar
        """
        return int(self.call_com(lambda: self._com.removeProgressBar(progress._com)))

    def rename_window_layout(self, old_layout_name: str, new_layout_name: str) -> int:
        """Renames the given layout with new layout name

        Args:
            old_layout_name: See JavaDoc for oldLayoutName.
            new_layout_name: See JavaDoc for newLayoutName.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::renameWindowLayout
        """
        return int(self.call_com(lambda: self._com.renameWindowLayout(old_layout_name, new_layout_name)))

    def report(self, format: str, output_file_name: str) -> None:
        """report

        Args:
            format: See JavaDoc for format.
            output_file_name: See JavaDoc for outputFileName.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::report
        """
        self.call_com(lambda: self._com.report(format, output_file_name))

    def reset_window_layout(self) -> int:
        """Resets the window layout and make it the default

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::resetWindowLayout
        """
        return int(self.call_com(lambda: self._com.resetWindowLayout()))

    def get_rhapsody_handle_error_function(self) -> int:
        """getRhapsodyHandleErrorFunction

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getRhapsodyHandleErrorFunction
        """
        return int(self.call_com(lambda: self._com.getRhapsodyHandleErrorFunction()))

    def get_rhapsody_handle_error_function_long(self) -> int:
        """getRhapsodyHandleErrorFunctionLong

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getRhapsodyHandleErrorFunctionLong
        """
        return int(self.call_com(lambda: self._com.getRhapsodyHandleErrorFunctionLong()))

    def rhp_checkin_license(self, feature: str) -> None:
        """checkin license

        Args:
            feature: See JavaDoc for feature.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::rhpCheckinLicense
        """
        self.call_com(lambda: self._com.RhpCheckinLicense(feature))

    def rhp_checkout_license(self, feature: str) -> str:
        """checkout license

        Args:
            feature: See JavaDoc for feature.

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::rhpCheckoutLicense
        """
        return str(self.call_com(lambda: self._com.RhpCheckoutLicense(feature)))

    def roundtrip(self) -> None:
        """roundtrip

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::roundtrip
        """
        self.call_com(lambda: self._com.roundtrip())

    def roundtrip_elements(self, elements: IRPCollection) -> None:
        """method roundtripElements

        Args:
            elements: See JavaDoc for elements.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::roundtripElements
        """
        self.call_com(lambda: self._com.roundtripElements(elements._com))

    def run_application(self) -> None:
        """Runs the application that was built for the project

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::runApplication
        """
        self.call_com(lambda: self._com.runApplication())

    def run_helper(self, helper_name: str) -> None:
        """runHelper

        Args:
            helper_name: See JavaDoc for helperName.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::runHelper
        """
        self.call_com(lambda: self._com.runHelper(helper_name))

    def run_helper_with_parameters(self, helper_name: str, params: str) -> None:
        """runHelperWithParameters

        Args:
            helper_name: See JavaDoc for helperName.
            params: See JavaDoc for params.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::runHelperWithParameters
        """
        self.call_com(lambda: self._com.runHelperWithParameters(helper_name, params))

    def save_check_model_result(self, csv_file_name: str, is_header: int, severity_type: int) -> None:
        """Saves the results of check model operation to CSV file, overwrites the file if exists

        Args:
            csv_file_name: See JavaDoc for csvFileName.
            is_header: See JavaDoc for isHeader.
            severity_type: See JavaDoc for severityType.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::saveCheckModelResult
        """
        self.call_com(lambda: self._com.saveCheckModelResult(csv_file_name, is_header, severity_type))

    def save_window_layout(self, layout_name: str, overwrite_if_exists: int) -> int:
        """Saves the current layout with given name to the Rhapsody window layout location

        Args:
            layout_name: See JavaDoc for layoutName.
            overwrite_if_exists: See JavaDoc for overwriteIfExists.

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::saveWindowLayout
        """
        return int(self.call_com(lambda: self._com.saveWindowLayout(layout_name, overwrite_if_exists)))

    def select_graph_elements(self, graph_elements: IRPCollection) -> None:
        """Selects multiple elements in the most recently opened diagram

        Args:
            graph_elements: See JavaDoc for graphElements.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::selectGraphElements
        """
        self.call_com(lambda: self._com.selectGraphElements(graph_elements._com))

    def select_model_elements(self, model_elements: IRPCollection) -> None:
        """Selects multiple items in the model browser

        Args:
            model_elements: See JavaDoc for modelElements.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::selectModelElements
        """
        self.call_com(lambda: self._com.selectModelElements(model_elements._com))

    def get_selected_element(self) -> IRPModelElement:
        """get selected element

        Returns:
            IRPModelElement: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getSelectedElement
        """
        return IRPModelElement(self.call_com(lambda: self._com.getSelectedElement()))

    def get_selected_graph_elements(self) -> IRPCollection:
        """get selected graph elements

        Returns:
            IRPCollection: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getSelectedGraphElements
        """
        return IRPCollection(self.call_com(lambda: self._com.getSelectedGraphElements()))

    @property
    def serial_no(self) -> str:
        """get property SerialNo

        Returns:
            str: get property SerialNo.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getSerialNo
        """
        return str(self.get_com_property(self._com, "SerialNo"))

    def start_undo_transaction(self) -> None:
        """start undo transaction

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::startUndoTransaction
        """
        self.call_com(lambda: self._com.startUndoTransaction())

    def sync_build(self) -> None:
        """syncBuild

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::syncBuild
        """
        self.call_com(lambda: self._com.syncBuild())

    def terminate_application(self) -> None:
        """Terminate the Application

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::terminateApplication
        """
        self.call_com(lambda: self._com.terminateApplication())

    def get_the_code_generator_interface(self) -> object:
        """get codegeneration interface

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getTheCodeGeneratorInterface
        """
        return self.call_com(lambda: self._com.getTheCodeGeneratorInterface())

    def get_the_external_code_generator_invoker(self) -> object:
        """get external code generator invoker

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getTheExternalCodeGeneratorInvoker
        """
        return self.call_com(lambda: self._com.getTheExternalCodeGeneratorInvoker())

    def get_the_integrator_interface(self) -> object:
        """get integrator interface

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getTheIntegratorInterface
        """
        return self.call_com(lambda: self._com.getTheIntegratorInterface())

    def get_the_java_plugins_interface(self) -> object:
        """getTheJavaPluginsInterface

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getTheJavaPluginsInterface
        """
        return self.call_com(lambda: self._com.getTheJavaPluginsInterface())

    def get_the_roundtrip_interface(self) -> object:
        """get roundtrip interface

        Returns:
            object: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getTheRoundtripInterface
        """
        return self.call_com(lambda: self._com.getTheRoundtripInterface())

    @property
    def tool_set(self) -> str:
        """get property ToolSet

        Returns:
            str: get property ToolSet.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getToolSet
        """
        return str(self.get_com_property(self._com, "ToolSet"))

    @tool_set.setter
    def tool_set(self, tool_set: str) -> None:
        """set property ToolSet

        Args:
            tool_set: Value to set.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setToolSet
        """
        self.set_com_property(self._com, "ToolSet", tool_set)

    def undo(self) -> int:
        """Perform Undo

        Returns:
            int: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::undo
        """
        return int(self.call_com(lambda: self._com.undo()))

    def unload_from_target(self) -> None:
        """unloadFromTarget

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::unloadFromTarget
        """
        self.call_com(lambda: self._com.unloadFromTarget())

    def unregister_com_client(self, process_id: int, client_filename: str, magic_number: int) -> None:
        """unregister COM client

        Args:
            process_id: See JavaDoc for processID.
            client_filename: See JavaDoc for clientFilename.
            magic_number: See JavaDoc for magicNumber.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::unregisterCOMClient
        """
        self.call_com(lambda: self._com.unregisterCOMClient(process_id, client_filename, magic_number))

    def set_update_recent_file_list(self, should_update: int) -> None:
        """setUpdateRecentFileList

        Args:
            should_update: See JavaDoc for shouldUpdate.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setUpdateRecentFileList
        """
        self.call_com(lambda: self._com.setUpdateRecentFileList(should_update))

    def update_rmm_data_to_new_version(self) -> None:
        """Updates the Rhapsody Model Manager data contained in the model to reflect all the information stored by the latest version of Rhapsody

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::updateRmmDataToNewVersion
        """
        self.call_com(lambda: self._com.updateRmmDataToNewVersion())

    @property
    def user_data_root(self) -> str:
        """Gets the full path of the folder where the Rhapsody data files were installed

        Returns:
            str: Gets the full path of the folder where the Rhapsody data files were installed.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getUserDataRoot
        """
        return str(self.get_com_property(self._com, "UserDataRoot"))

    @property
    def user_omroot(self) -> str:
        """Gets the full path of the UserShare folder of the Rhapsody installation

        Returns:
            str: Gets the full path of the UserShare folder of the Rhapsody installation.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getUserOMROOT
        """
        return str(self.get_com_property(self._com, "UserOMROOT"))

    def version_number_long(self) -> str:
        """Get Rhapsody versionNumberLong

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::versionNumberLong
        """
        return str(self.call_com(lambda: self._com.versionNumberLong()))

    def get_web_view_url(self, n_handle: object) -> str:
        """Returns the current URL loaded in WebView Note : This method will run asynchronously in Rhapsody application

        Args:
            n_handle: See JavaDoc for nHandle.

        Returns:
            str: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getWebViewURL
        """
        return str(self.call_com(lambda: self._com.getWebViewURL(n_handle)))

    def set_web_view_url(self, n_handle: object, s_url: str) -> None:
        """Set the URL to a webview, Load the html file or URL of webpage

        Args:
            n_handle: See JavaDoc for nHandle.
            s_url: See JavaDoc for sUrl.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::setWebViewURL
        """
        self.call_com(lambda: self._com.setWebViewURL(n_handle, s_url))

    def get_window_layout_list(self) -> IRPCollection:
        """Returns a collection of all the window layouts saved in the Rhapsody window layout location

        Returns:
            IRPCollection: See JavaDoc.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getWindowLayoutList
        """
        return IRPCollection(self.call_com(lambda: self._com.getWindowLayoutList()))

    def write_to_output_window(self, title: str, output_str: str) -> None:
        """Writes text to Rhapsody's Output window

        Args:
            title: See JavaDoc for title.
            output_str: See JavaDoc for outputStr.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::writeToOutputWindow
        """
        self.call_com(lambda: self._com.writeToOutputWindow(title, output_str))

    def get_plug_in_window(self, n_plug_in_id: int, n_window_id: int, n_create_new: int) -> object:
        """PlugIn window factory

        Args:
            n_plug_in_id: See JavaDoc for nPlugInID.
            n_window_id: See JavaDoc for nWindowID.
            n_create_new: See JavaDoc for nCreateNew.

        Returns:
            object: The plug-in window COM object.

        Raises:
            RhapsodyRuntimeException: If the underlying COM call fails.

        Reference:
            com.telelogic.rhapsody.core.IRPApplication::getPlugInWindow(int nPlugInID, int nWindowID, boolean nCreateNew)
        """
        return self.call_com(lambda: self._com.GetPlugInWindow(n_plug_in_id, n_window_id, n_create_new))


IRPModelElement.register_wrapper("Application", IRPApplication)
