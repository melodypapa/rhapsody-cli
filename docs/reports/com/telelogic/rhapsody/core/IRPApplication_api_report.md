# Rhapsody API Validation: IRPApplication

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPApplication` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_application.py`)
- Members: Python `192`, Java `195`, pywin32 `173`
- Deviation items: `23` (actionable `17`, expected binding differences `6`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| allow_rmm_remote_oslc_links_load() -> allowRmmRemoteOslcLinksLoad | allowRmmRemoteOslcLinksLoad (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| apply_window_layout() -> applyWindowLayout | applyWindowLayout (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| create_embedded_web_view_window() -> createEmbeddedWebViewWindow | createEmbeddedWebViewWindow (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| create_progress_bar() -> createProgressBar | createProgressBar (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| delete_window_layout() -> deleteWindowLayout | deleteWindowLayout (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| export_window_layout() -> exportWindowLayout | exportWindowLayout (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_helper_status() -> getHelperStatus; set_helper_status() -> setHelperStatus | getHelperStatus (method); setHelperStatus (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| import_window_layout() -> importWindowLayout | importWindowLayout (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| is_valid_web_view() -> isValidWebView | isValidWebView (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_progress_bar() -> getProgressBar | getProgressBar (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| remove_progress_bar() -> removeProgressBar | removeProgressBar (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| rename_window_layout() -> renameWindowLayout | renameWindowLayout (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| reset_window_layout() -> resetWindowLayout | resetWindowLayout (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| save_check_model_result() -> saveCheckModelResult | saveCheckModelResult (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| save_window_layout() -> saveWindowLayout | saveWindowLayout (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_web_view_url() -> getWebViewURL; set_web_view_url() -> setWebViewURL | getWebViewURL (method); setWebViewURL (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_window_layout_list() -> getWindowLayoutList | getWindowLayoutList (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |

<details>
<summary>Correct items (163) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| active_project() -> activeProject | activeProject (method) | activeProject (method) | MATCH | — |
| add_profile_to_model() -> addProfileToModel | addProfileToModel (method) | addProfileToModel (method) | MATCH | — |
| add_selected_to_favorites() -> addSelectedToFavorites | addSelectedToFavorites (method) | addSelectedToFavorites (method) | MATCH | — |
| add_to_model() -> addToModel | addToModel (method) | addToModel (method) | MATCH | — |
| add_to_model_by_reference() -> addToModelByReference | addToModelByReference (method) | addToModelByReference (method) | MATCH | — |
| add_to_model_ex() -> addToModelEx | addToModelEx (method) | addToModelEx (method) | MATCH | — |
| add_to_model_from_url() -> addToModelFromURL | addToModelFromURL (method) | addToModelFromURL (method) | MATCH | — |
| add_units_to_model() -> addUnitsToModel | addUnitsToModel (method) | addUnitsToModel (method) | MATCH | — |
| allow_browser_refresh() -> allowBrowserRefresh | allowBrowserRefresh (method) | allowBrowserRefresh (method) | MATCH | — |
| allow_ge_refresh() -> allowGERefresh | allowGERefresh (method) | allowGERefresh (method) | MATCH | — |
| get_application_connection_string() -> getApplicationConnectionString | getApplicationConnectionString (method) | getApplicationConnectionString (method) | MATCH | — |
| get_application_name() -> getApplicationName | getApplicationName (method) | getApplicationName (method) | MATCH | — |
| application_root (property) -> ApplicationRoot | getApplicationRoot (method) | ApplicationRoot (property) | MATCH | — |
| get_application_status() -> getApplicationStatus; set_application_status() -> setApplicationStatus | getApplicationStatus (method); setApplicationStatus (method) | getApplicationStatus (method); setApplicationStatus (method) | MATCH | — |
| apply_new_terms_profile() -> applyNewTermsProfile | applyNewTermsProfile (method) | applyNewTermsProfile (method) | MATCH | — |
| arc_check_out() -> arcCheckOut | arcCheckOut (method) | arcCheckOut (method) | MATCH | — |
| bring_window_to_top() -> bringWindowToTop | bringWindowToTop (method) | bringWindowToTop (method) | MATCH | — |
| build() -> build | build (method) | build (method) | MATCH | — |
| build_entire_project() -> buildEntireProject | buildEntireProject (method) | buildEntireProject (method) | MATCH | — |
| build_no (property) -> BuildNo | getBuildNo (method) | BuildNo (property) | MATCH | — |
| build_with_dependencies() -> buildWithDependencies | buildWithDependencies (method) | buildWithDependencies (method) | MATCH | — |
| can_redo() -> canRedo | canRedo (method) | canRedo (method) | MATCH | — |
| can_undo() -> canUndo | canUndo (method) | canUndo (method) | MATCH | — |
| check_in() -> checkIn | checkIn (method) | checkIn (method) | MATCH | — |
| check_model() -> checkModel | checkModel (method) | checkModel (method) | MATCH | — |
| check_out() -> checkOut | checkOut (method) | checkOut (method) | MATCH | — |
| clean() -> clean | clean (method) | clean (method) | MATCH | — |
| clear_output_window() -> clearOutputWindow | clearOutputWindow (method) | clearOutputWindow (method) | MATCH | — |
| close_all_animated_sequence_diagrams() -> closeAllAnimatedSequenceDiagrams | closeAllAnimatedSequenceDiagrams (method) | closeAllAnimatedSequenceDiagrams (method) | MATCH | — |
| get_code_gen_simplifiers_registry() -> getCodeGenSimplifiersRegistry | getCodeGenSimplifiersRegistry (method) | getCodeGenSimplifiersRegistry (method) | MATCH | — |
| compare_sequence_diagram() -> compareSequenceDiagram | compareSequenceDiagram (method) | compareSequenceDiagram (method) | MATCH | — |
| set_component() -> setComponent | setComponent (method) | setComponent (method) | MATCH | — |
| set_configuration() -> setConfiguration | setConfiguration (method) | setConfiguration (method) | MATCH | — |
| connect_to_archive() -> connectToArchive | connectToArchive (method) | connectToArchive (method) | MATCH | — |
| connect_to_imported_model() -> connectToImportedModel | connectToImportedModel (method) | connectToImportedModel (method) | MATCH | — |
| connect_to_target() -> connectToTarget | connectToTarget (method) | connectToTarget (method) | MATCH | — |
| create_and_insert_project() -> createAndInsertProject | createAndInsertProject (method) | createAndInsertProject (method) | MATCH | — |
| create_domain_from_profile() -> createDomainFromProfile | createDomainFromProfile (method) | createDomainFromProfile (method) | MATCH | — |
| create_new_collection() -> createNewCollection | createNewCollection (method) | createNewCollection (method) | MATCH | — |
| create_new_project() -> createNewProject | createNewProject (method) | createNewProject (method) | MATCH | — |
| get_dm_bool_property() -> getDMBoolProperty; set_dm_bool_property() -> setDMBoolProperty | getDMBoolProperty (method); setDMBoolProperty (method) | getDMBoolProperty (method); setDMBoolProperty (method) | MATCH | — |
| get_dm_model_workspace_folder() -> getDMModelWorkspaceFolder | getDMModelWorkspaceFolder (method) | getDMModelWorkspaceFolder (method) | MATCH | — |
| get_dm_property() -> getDMProperty; set_dm_property() -> setDMProperty | getDMProperty (method); setDMProperty (method) | getDMProperty (method); setDMProperty (method) | MATCH | — |
| d_m_refresh_recursive() -> dMRefreshRecursive | dMRefreshRecursive (method) | dMRefreshRecursive (method) | MATCH | — |
| d_m_sync_and_refresh() -> dMSyncAndRefresh | dMSyncAndRefresh (method) | dMSyncAndRefresh (method) | MATCH | — |
| dbg_check_com_in() -> dbgCheckComIn | dbgCheckComIn (method) | dbgCheckComIn (method) | MATCH | — |
| dbg_check_com_out() -> dbgCheckComOut | dbgCheckComOut (method) | dbgCheckComOut (method) | MATCH | — |
| deferred_add_to_model() -> deferredAddToModel | deferredAddToModel (method) | deferredAddToModel (method) | MATCH | — |
| delete_project_from_list() -> deleteProjectFromList | deleteProjectFromList (method) | deleteProjectFromList (method) | MATCH | — |
| get_diag_synth_api() -> getDiagSynthAPI | getDiagSynthAPI (method) | getDiagSynthAPI (method) | MATCH | — |
| get_diagram_of_selected_element() -> getDiagramOfSelectedElement | getDiagramOfSelectedElement (method) | getDiagramOfSelectedElement (method) | MATCH | — |
| disconnect_from_target() -> disconnectFromTarget | disconnectFromTarget (method) | disconnectFromTarget (method) | MATCH | — |
| download_to_target() -> downloadToTarget | downloadToTarget (method) | downloadToTarget (method) | MATCH | — |
| end_undo_transaction() -> endUndoTransaction | endUndoTransaction (method) | endUndoTransaction (method) | MATCH | — |
| enter_animation_command() -> enterAnimationCommand | enterAnimationCommand (method) | enterAnimationCommand (method) | MATCH | — |
| error_message() -> errorMessage; get_error_message() -> getErrorMessage | errorMessage (method); getErrorMessage (method) | errorMessage (method); getErrorMessage (method) | MATCH | — |
| get_executable_folder() -> getExecutableFolder | getExecutableFolder (method) | getExecutableFolder (method) | MATCH | — |
| execute_command_line() -> executeCommandLine | executeCommandLine (method) | executeCommandLine (method) | MATCH | — |
| execute_transformation_sequence() -> executeTransformationSequence | executeTransformationSequence (method) | executeTransformationSequence (method) | MATCH | — |
| expand_string_keywords() -> expandStringKeywords | expandStringKeywords (method) | expandStringKeywords (method) | MATCH | — |
| get_external_checker_registry() -> getExternalCheckerRegistry | getExternalCheckerRegistry (method) | getExternalCheckerRegistry (method) | MATCH | — |
| get_external_ide_registry() -> getExternalIDERegistry | getExternalIDERegistry (method) | getExternalIDERegistry (method) | MATCH | — |
| get_external_roundtrip_invoker() -> getExternalRoundtripInvoker | getExternalRoundtripInvoker (method) | getExternalRoundtripInvoker (method) | MATCH | — |
| fixpack() -> fixpack | fixpack (method) | fixpack (method) | MATCH | — |
| force_output2_console() -> forceOutput2Console | forceOutput2Console (method) | forceOutput2Console (method) | MATCH | — |
| force_roundtrip() -> forceRoundtrip | forceRoundtrip (method) | forceRoundtrip (method) | MATCH | — |
| force_roundtrip_elements() -> forceRoundtripElements | forceRoundtripElements (method) | forceRoundtripElements (method) | MATCH | — |
| generate() -> generate | generate (method) | generate (method) | MATCH | — |
| generate_elements() -> generateElements | generateElements (method) | generateElements (method) | MATCH | — |
| generate_entire_project() -> generateEntireProject | generateEntireProject (method) | generateEntireProject (method) | MATCH | — |
| generate_main_and_make_files() -> generateMainAndMakeFiles | generateMainAndMakeFiles (method) | generateMainAndMakeFiles (method) | MATCH | — |
| generate_with_dependencies() -> generateWithDependencies | generateWithDependencies (method) | generateWithDependencies (method) | MATCH | — |
| set_hidden_ui() -> setHiddenUI | setHiddenUI (method) | setHiddenUI (method) | MATCH | — |
| high_light_element() -> highLightElement | highLightElement (method) | highLightElement (method) | MATCH | — |
| highlight_by_handle() -> highlightByHandle | highlightByHandle (method) | highlightByHandle (method) | MATCH | — |
| import_classes() -> importClasses | importClasses (method) | importClasses (method) | MATCH | — |
| import_design_manager_model() -> importDesignManagerModel | importDesignManagerModel (method) | importDesignManagerModel (method) | MATCH | — |
| import_sync_simulink_block2() -> importSyncSimulinkBlock2 | importSyncSimulinkBlock2 (method) | importSyncSimulinkBlock2 (method) | MATCH | — |
| import_tlb() -> importTlb | importTlb (method) | importTlb (method) | MATCH | — |
| get_ini_file_parameter_value() -> getIniFileParameterValue | getIniFileParameterValue (method) | getIniFileParameterValue (method) | MATCH | — |
| insert_project() -> insertProject | insertProject (method) | insertProject (method) | MATCH | — |
| insert_project_from_design_manager() -> insertProjectFromDesignManager | insertProjectFromDesignManager (method) | insertProjectFromDesignManager (method) | MATCH | — |
| interface_name (property) -> interfaceName | getInterfaceName (method) | interfaceName (property) | MATCH | — |
| invoke_plugins_method() -> invokePluginsMethod | invokePluginsMethod (method) | invokePluginsMethod (method) | MATCH | — |
| invoke_rpe() -> invokeRPE | invokeRPE (method) | invokeRPE (method) | MATCH | — |
| is_hidden_ui (property) -> isHiddenUI | getIsHiddenUI (method) | isHiddenUI (property) | MATCH | — |
| is_load_on_demand (property) -> isLoadOnDemand | getIsLoadOnDemand (method); setIsLoadOnDemand (method) | isLoadOnDemand (property) | MATCH | — |
| is_rhapsody_cl() -> isRhapsodyCL | isRhapsodyCL (method) | isRhapsodyCL (method) | MATCH | — |
| is_rhapsody_file_type() -> isRhapsodyFileType | isRhapsodyFileType (method) | isRhapsodyFileType (method) | MATCH | — |
| language (property) -> Language | getLanguage (method); setLanguage (method) | Language (property) | MATCH | — |
| get_list_of_factory_properties() -> getListOfFactoryProperties | getListOfFactoryProperties (method) | getListOfFactoryProperties (method) | MATCH | — |
| get_list_of_selected_elements() -> getListOfSelectedElements | getListOfSelectedElements (method) | getListOfSelectedElements (method) | MATCH | — |
| get_list_of_site_properties() -> getListOfSiteProperties | getListOfSiteProperties (method) | getListOfSiteProperties (method) | MATCH | — |
| get_locale_name() -> getLocaleName | getLocaleName (method) | getLocaleName (method) | MATCH | — |
| set_log() -> setLog | setLog (method) | setLog (method) | MATCH | — |
| log_root (property) -> LogRoot | getLogRoot (method) | LogRoot (property) | MATCH | — |
| login_to_design_manager_with_alias() -> loginToDesignManagerWithAlias | loginToDesignManagerWithAlias (method) | loginToDesignManagerWithAlias (method) | MATCH | — |
| login_to_design_manager_with_certificate() -> loginToDesignManagerWithCertificate | loginToDesignManagerWithCertificate (method) | loginToDesignManagerWithCertificate (method) | MATCH | — |
| login_to_design_manager_with_username() -> loginToDesignManagerWithUsername | loginToDesignManagerWithUsername (method) | loginToDesignManagerWithUsername (method) | MATCH | — |
| make() -> make | make (method) | make (method) | MATCH | — |
| merge_elements() -> mergeElements | mergeElements (method) | mergeElements (method) | MATCH | — |
| get_model_element_from_source() -> getModelElementFromSource | getModelElementFromSource (method) | getModelElementFromSource (method) | MATCH | — |
| new_project_on_design_manager() -> newProjectOnDesignManager | newProjectOnDesignManager (method) | newProjectOnDesignManager (method) | MATCH | — |
| notify_file_changed() -> notifyFileChanged | notifyFileChanged (method) | notifyFileChanged (method) | MATCH | — |
| omroot (property) -> OMROOT | getOMROOT (method) | OMROOT (property) | MATCH | — |
| get_ow_pane_mgr() -> getOWPaneMgr | getOWPaneMgr (method) | getOWPaneMgr (method) | MATCH | — |
| open_advanced_search_and_replace_dialog() -> openAdvancedSearchAndReplaceDialog | openAdvancedSearchAndReplaceDialog (method) | openAdvancedSearchAndReplaceDialog (method) | MATCH | — |
| open_file_list() -> openFileList | openFileList (method) | openFileList (method) | MATCH | — |
| open_project() -> openProject | openProject (method) | openProject (method) | MATCH | — |
| open_project_from_design_manager() -> openProjectFromDesignManager | openProjectFromDesignManager (method) | openProjectFromDesignManager (method) | MATCH | — |
| open_project_from_design_manager_after_login() -> openProjectFromDesignManagerAfterLogin | openProjectFromDesignManagerAfterLogin (method) | openProjectFromDesignManagerAfterLogin (method) | MATCH | — |
| open_project_from_url() -> openProjectFromURL | openProjectFromURL (method) | openProjectFromURL (method) | MATCH | — |
| open_project_with_last_session() -> openProjectWithLastSession | openProjectWithLastSession (method) | openProjectWithLastSession (method) | MATCH | — |
| open_project_without_sub_units() -> openProjectWithoutSubUnits | openProjectWithoutSubUnits (method) | openProjectWithoutSubUnits (method) | MATCH | — |
| get_output_window_text() -> getOutputWindowText | getOutputWindowText (method) | getOutputWindowText (method) | MATCH | — |
| projects (property) -> projects | getProjects (method) | projects (property) | MATCH | — |
| quit() -> quit | quit (method) | quit (method) | MATCH | — |
| rebuild() -> rebuild | rebuild (method) | rebuild (method) | MATCH | — |
| rebuild_entire_project() -> rebuildEntireProject | rebuildEntireProject (method) | rebuildEntireProject (method) | MATCH | — |
| rebuild_with_dependencies() -> rebuildWithDependencies | rebuildWithDependencies (method) | rebuildWithDependencies (method) | MATCH | — |
| redo() -> redo | redo (method) | redo (method) | MATCH | — |
| refactor_selected_operation() -> refactorSelectedOperation | refactorSelectedOperation (method) | refactorSelectedOperation (method) | MATCH | — |
| refresh_all_views() -> refreshAllViews | refreshAllViews (method) | refreshAllViews (method) | MATCH | — |
| regenerate() -> regenerate | regenerate (method) | regenerate (method) | MATCH | — |
| regenerate_elements() -> regenerateElements | regenerateElements (method) | regenerateElements (method) | MATCH | — |
| regenerate_entire_project() -> regenerateEntireProject | regenerateEntireProject (method) | regenerateEntireProject (method) | MATCH | — |
| regenerate_with_dependencies() -> regenerateWithDependencies | regenerateWithDependencies (method) | regenerateWithDependencies (method) | MATCH | — |
| register_com_client() -> registerCOMClient | registerCOMClient (method) | registerCOMClient (method) | MATCH | — |
| report() -> report | report (method) | report (method) | MATCH | — |
| get_rhapsody_handle_error_function() -> getRhapsodyHandleErrorFunction | getRhapsodyHandleErrorFunction (method) | getRhapsodyHandleErrorFunction (method) | MATCH | — |
| get_rhapsody_handle_error_function_long() -> getRhapsodyHandleErrorFunctionLong | getRhapsodyHandleErrorFunctionLong (method) | getRhapsodyHandleErrorFunctionLong (method) | MATCH | — |
| roundtrip() -> roundtrip | roundtrip (method) | roundtrip (method) | MATCH | — |
| roundtrip_elements() -> roundtripElements | roundtripElements (method) | roundtripElements (method) | MATCH | — |
| run_application() -> runApplication | runApplication (method) | runApplication (method) | MATCH | — |
| run_helper() -> runHelper | runHelper (method) | runHelper (method) | MATCH | — |
| run_helper_with_parameters() -> runHelperWithParameters | runHelperWithParameters (method) | runHelperWithParameters (method) | MATCH | — |
| save_all() -> saveAll | saveAll (method) | saveAll (method) | MATCH | — |
| get_search_manager() -> getSearchManager | getSearchManager (method) | getSearchManager (method) | MATCH | — |
| select_graph_elements() -> selectGraphElements | selectGraphElements (method) | selectGraphElements (method) | MATCH | — |
| select_model_elements() -> selectModelElements | selectModelElements (method) | selectModelElements (method) | MATCH | — |
| get_selected_element() -> getSelectedElement | getSelectedElement (method) | getSelectedElement (method) | MATCH | — |
| get_selected_graph_elements() -> getSelectedGraphElements | getSelectedGraphElements (method) | getSelectedGraphElements (method) | MATCH | — |
| get_selection() -> getSelection | getSelection (method) | getSelection (method) | MATCH | — |
| serial_no (property) -> SerialNo | getSerialNo (method) | SerialNo (property) | MATCH | — |
| start_undo_transaction() -> startUndoTransaction | startUndoTransaction (method) | startUndoTransaction (method) | MATCH | — |
| sync_build() -> syncBuild | syncBuild (method) | syncBuild (method) | MATCH | — |
| terminate_application() -> terminateApplication | terminateApplication (method) | terminateApplication (method) | MATCH | — |
| get_the_code_generator_interface() -> getTheCodeGeneratorInterface | getTheCodeGeneratorInterface (method) | getTheCodeGeneratorInterface (method) | MATCH | — |
| get_the_external_code_generator_invoker() -> getTheExternalCodeGeneratorInvoker | getTheExternalCodeGeneratorInvoker (method) | getTheExternalCodeGeneratorInvoker (method) | MATCH | — |
| get_the_integrator_interface() -> getTheIntegratorInterface | getTheIntegratorInterface (method) | getTheIntegratorInterface (method) | MATCH | — |
| get_the_java_plugins_interface() -> getTheJavaPluginsInterface | getTheJavaPluginsInterface (method) | getTheJavaPluginsInterface (method) | MATCH | — |
| get_the_roundtrip_interface() -> getTheRoundtripInterface | getTheRoundtripInterface (method) | getTheRoundtripInterface (method) | MATCH | — |
| tool_set (property) -> ToolSet | getToolSet (method); setToolSet (method) | ToolSet (property) | MATCH | — |
| undo() -> undo | undo (method) | undo (method) | MATCH | — |
| unload_from_target() -> unloadFromTarget | unloadFromTarget (method) | unloadFromTarget (method) | MATCH | — |
| unregister_com_client() -> unregisterCOMClient | unregisterCOMClient (method) | unregisterCOMClient (method) | MATCH | — |
| set_update_recent_file_list() -> setUpdateRecentFileList | setUpdateRecentFileList (method) | setUpdateRecentFileList (method) | MATCH | — |
| update_rmm_data_to_new_version() -> updateRmmDataToNewVersion | updateRmmDataToNewVersion (method) | updateRmmDataToNewVersion (method) | MATCH | — |
| user_data_root (property) -> UserDataRoot | getUserDataRoot (method) | UserDataRoot (property) | MATCH | — |
| user_omroot (property) -> UserOMROOT | getUserOMROOT (method) | UserOMROOT (property) | MATCH | — |
| version() -> version | version (method) | version (method) | MATCH | — |
| version_number_long() -> versionNumberLong | versionNumberLong (method) | versionNumberLong (method) | MATCH | — |
| write_to_output_window() -> writeToOutputWindow | writeToOutputWindow (method) | writeToOutputWindow (method) | MATCH | — |

</details>

## AI Fix Guidance

### PYWIN32_MEMBER_MISSING (17 findings)
- **Target:** `IRPApplication` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_application.py`
- **Affected call(s):** allow_rmm_remote_oslc_links_load() -> allowRmmRemoteOslcLinksLoad; apply_window_layout() -> applyWindowLayout; create_embedded_web_view_window() -> createEmbeddedWebViewWindow; create_progress_bar() -> createProgressBar; delete_window_layout() -> deleteWindowLayout; export_window_layout() -> exportWindowLayout; get_helper_status() -> getHelperStatus; set_helper_status() -> setHelperStatus; import_window_layout() -> importWindowLayout; is_valid_web_view() -> isValidWebView; get_progress_bar() -> getProgressBar; remove_progress_bar() -> removeProgressBar; rename_window_layout() -> renameWindowLayout; reset_window_layout() -> resetWindowLayout; save_check_model_result() -> saveCheckModelResult; save_window_layout() -> saveWindowLayout; get_web_view_url() -> getWebViewURL; set_web_view_url() -> setWebViewURL; get_window_layout_list() -> getWindowLayoutList
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
