# Rhapsody API Validation: IRPApplication

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `RhapsodyApplication` (`src/rhapsody_cli/application.py`)
- Members: Python `31`, Java `176`, pywin32 `172`
- Deviation items: `143` (actionable `1`, expected binding differences `3`, wrapper backlog `139`)

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_version() -> version | version (method) | version (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | getPlugInWindow (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |
| connect() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| disconnect() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | addProfileToModel (method) | addProfileToModel (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | addSelectedToFavorites (method) | addSelectedToFavorites (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | addToModelByReference (method) | addToModelByReference (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | addToModelFromURL (method) | addToModelFromURL (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | addUnitsToModel (method) | addUnitsToModel (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | allowBrowserRefresh (method) | allowBrowserRefresh (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | allowGERefresh (method) | allowGERefresh (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getApplicationConnectionString (method) | getApplicationConnectionString (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getApplicationName (method) | getApplicationName (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getApplicationRoot (method) | ApplicationRoot (property) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getApplicationStatus (method); setApplicationStatus (method) | getApplicationStatus (method); setApplicationStatus (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | applyNewTermsProfile (method) | applyNewTermsProfile (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | arcCheckOut (method) | arcCheckOut (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | build (method) | build (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | buildEntireProject (method) | buildEntireProject (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | buildWithDependencies (method) | buildWithDependencies (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | canRedo (method) | canRedo (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | canUndo (method) | canUndo (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | checkIn (method) | checkIn (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | checkOut (method) | checkOut (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | clean (method) | clean (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | clearOutputWindow (method) | clearOutputWindow (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | closeAllAnimatedSequenceDiagrams (method) | closeAllAnimatedSequenceDiagrams (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | compareSequenceDiagram (method) | compareSequenceDiagram (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | setComponent (method) | setComponent (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | setConfiguration (method) | setConfiguration (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | connectToArchive (method) | connectToArchive (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | connectToImportedModel (method) | connectToImportedModel (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | connectToTarget (method) | connectToTarget (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | createAndInsertProject (method) | createAndInsertProject (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | createDomainFromProfile (method) | createDomainFromProfile (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getDMBoolProperty (method); setDMBoolProperty (method) | getDMBoolProperty (method); setDMBoolProperty (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getDMModelWorkspaceFolder (method) | getDMModelWorkspaceFolder (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getDMProperty (method); setDMProperty (method) | getDMProperty (method); setDMProperty (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | dMRefreshRecursive (method) | dMRefreshRecursive (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | dMSyncAndRefresh (method) | dMSyncAndRefresh (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | dbgCheckComIn (method) | dbgCheckComIn (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | dbgCheckComOut (method) | dbgCheckComOut (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | deferredAddToModel (method) | deferredAddToModel (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | deleteProjectFromList (method) | deleteProjectFromList (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getDiagramOfSelectedElement (method) | getDiagramOfSelectedElement (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | disconnectFromTarget (method) | disconnectFromTarget (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | downloadToTarget (method) | downloadToTarget (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | endUndoTransaction (method) | endUndoTransaction (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | enterAnimationCommand (method) | enterAnimationCommand (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | errorMessage (method); getErrorMessage (method) | errorMessage (method); getErrorMessage (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getExecutableFolder (method) | getExecutableFolder (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | executeCommand (method) | ExecuteCommand (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | executeCommandLine (method) | executeCommandLine (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | executeTransformationSequence (method) | executeTransformationSequence (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | expandStringKeywords (method) | expandStringKeywords (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | fixpack (method) | fixpack (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | forceOutput2Console (method) | forceOutput2Console (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | forceRoundtrip (method) | forceRoundtrip (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | forceRoundtripElements (method) | forceRoundtripElements (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | generateMainAndMakeFiles (method) | generateMainAndMakeFiles (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | generateWithDependencies (method) | generateWithDependencies (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | highLightElement (method) | highLightElement (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | highlightByHandle (method) | highlightByHandle (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | importClasses (method) | importClasses (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | importDesignManagerModel (method) | importDesignManagerModel (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | importSyncSimulinkBlock2 (method) | importSyncSimulinkBlock2 (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | importTlb (method) | importTlb (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getIniFileParameterValue (method) | getIniFileParameterValue (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | insertProject (method) | insertProject (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | insertProjectFromDesignManager (method) | insertProjectFromDesignManager (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getInterfaceName (method) | interfaceName (property) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | invokePluginsMethod (method) | invokePluginsMethod (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | invokeRPE (method) | invokeRPE (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getIsLoadOnDemand (method); setIsLoadOnDemand (method) | isLoadOnDemand (property) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | isRhapsodyCL (method) | isRhapsodyCL (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | isRhapsodyFileType (method) | isRhapsodyFileType (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getLanguage (method); setLanguage (method) | Language (property) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getListOfFactoryProperties (method) | getListOfFactoryProperties (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getListOfSelectedElements (method) | getListOfSelectedElements (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getListOfSiteProperties (method) | getListOfSiteProperties (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getLocaleName (method) | getLocaleName (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getLogRoot (method) | LogRoot (property) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | loginToDesignManagerWithAlias (method) | loginToDesignManagerWithAlias (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | loginToDesignManagerWithCertificate (method) | loginToDesignManagerWithCertificate (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | loginToDesignManagerWithUsername (method) | loginToDesignManagerWithUsername (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | make (method) | make (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | mergeElements (method) | mergeElements (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getModelElementFromSource (method) | getModelElementFromSource (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | newProjectOnDesignManager (method) | newProjectOnDesignManager (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | notifyFileChanged (method) | notifyFileChanged (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | openActiveXView (method) | OpenActiveXView (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | openAdvancedSearchAndReplaceDialog (method) | openAdvancedSearchAndReplaceDialog (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | openDiagramView (method) | OpenDiagramView (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | openFileList (method) | openFileList (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | openProjectFromDesignManager (method) | openProjectFromDesignManager (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | openProjectFromDesignManagerAfterLogin (method) | openProjectFromDesignManagerAfterLogin (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | openProjectFromURL (method) | openProjectFromURL (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | openProjectWithLastSession (method) | openProjectWithLastSession (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | openProjectWithoutSubUnits (method) | openProjectWithoutSubUnits (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getOutputWindowText (method) | getOutputWindowText (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | rebuild (method) | rebuild (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | rebuildEntireProject (method) | rebuildEntireProject (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | rebuildWithDependencies (method) | rebuildWithDependencies (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | redo (method) | redo (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | refactorSelectedOperation (method) | refactorSelectedOperation (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | refreshAllViews (method) | refreshAllViews (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | regenerateElements (method) | regenerateElements (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | regenerateEntireProject (method) | regenerateEntireProject (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | regenerateWithDependencies (method) | regenerateWithDependencies (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | registerCOMClient (method) | registerCOMClient (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | report (method) | report (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getRhapsodyHandleErrorFunction (method) | getRhapsodyHandleErrorFunction (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getRhapsodyHandleErrorFunctionLong (method) | getRhapsodyHandleErrorFunctionLong (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | rhpCheckinLicense (method) | RhpCheckinLicense (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | rhpCheckoutLicense (method) | RhpCheckoutLicense (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | roundtrip (method) | roundtrip (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | roundtripElements (method) | roundtripElements (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | runApplication (method) | runApplication (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | runHelper (method) | runHelper (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | runHelperWithParameters (method) | runHelperWithParameters (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | selectGraphElements (method) | selectGraphElements (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | selectModelElements (method) | selectModelElements (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getSelectedElement (method) | getSelectedElement (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getSelectedGraphElements (method) | getSelectedGraphElements (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getSerialNo (method) | SerialNo (property) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | startUndoTransaction (method) | startUndoTransaction (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | syncBuild (method) | syncBuild (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | terminateApplication (method) | terminateApplication (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getTheCodeGeneratorInterface (method) | getTheCodeGeneratorInterface (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getTheExternalCodeGeneratorInvoker (method) | getTheExternalCodeGeneratorInvoker (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getTheIntegratorInterface (method) | getTheIntegratorInterface (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getTheJavaPluginsInterface (method) | getTheJavaPluginsInterface (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getTheRoundtripInterface (method) | getTheRoundtripInterface (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getToolSet (method); setToolSet (method) | ToolSet (property) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | undo (method) | undo (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | unloadFromTarget (method) | unloadFromTarget (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | unregisterCOMClient (method) | unregisterCOMClient (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | setUpdateRecentFileList (method) | setUpdateRecentFileList (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | updateRmmDataToNewVersion (method) | updateRmmDataToNewVersion (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getUserDataRoot (method) | UserDataRoot (property) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | getUserOMROOT (method) | UserOMROOT (property) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | versionNumberLong (method) | versionNumberLong (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | writeToOutputWindow (method) | writeToOutputWindow (method) | INTENTIONALLY_UNSUPPORTED_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| active_project() -> activeProject | activeProject (method) | activeProject (method) | MATCH | — |
| add_to_model() -> addToModel | addToModel (method) | addToModel (method) | MATCH | — |
| add_to_model_ex() -> addToModelEx | addToModelEx (method) | addToModelEx (method) | MATCH | — |
| bring_window_to_top() -> bringWindowToTop | bringWindowToTop (method) | bringWindowToTop (method) | MATCH | — |
| check_model() -> checkModel | checkModel (method) | checkModel (method) | MATCH | — |
| create_new_collection() -> createNewCollection | createNewCollection (method) | createNewCollection (method) | MATCH | — |
| create_new_project() -> createNewProject | createNewProject (method) | createNewProject (method) | MATCH | — |
| generate() -> generate | generate (method) | generate (method) | MATCH | — |
| generate_elements() -> generateElements | generateElements (method) | generateElements (method) | MATCH | — |
| generate_entire_project() -> generateEntireProject | generateEntireProject (method) | generateEntireProject (method) | MATCH | — |
| get_build_no() -> BuildNo | getBuildNo (method) | BuildNo (property) | MATCH | — |
| get_code_gen_simplifiers_registry() -> getCodeGenSimplifiersRegistry | getCodeGenSimplifiersRegistry (method) | getCodeGenSimplifiersRegistry (method) | MATCH | — |
| get_diag_synth_api() -> getDiagSynthAPI | getDiagSynthAPI (method) | getDiagSynthAPI (method) | MATCH | — |
| get_external_checker_registry() -> getExternalCheckerRegistry | getExternalCheckerRegistry (method) | getExternalCheckerRegistry (method) | MATCH | — |
| get_external_ide_registry() -> getExternalIDERegistry | getExternalIDERegistry (method) | getExternalIDERegistry (method) | MATCH | — |
| get_external_roundtrip_invoker() -> getExternalRoundtripInvoker | getExternalRoundtripInvoker (method) | getExternalRoundtripInvoker (method) | MATCH | — |
| get_is_hidden_ui() -> isHiddenUI | getIsHiddenUI (method) | isHiddenUI (property) | MATCH | — |
| get_omroot() -> OMROOT | getOMROOT (method) | OMROOT (property) | MATCH | — |
| get_ow_pane_mgr() -> getOWPaneMgr | getOWPaneMgr (method) | getOWPaneMgr (method) | MATCH | — |
| get_projects() -> projects | getProjects (method) | projects (property) | MATCH | — |
| get_search_manager() -> getSearchManager | getSearchManager (method) | getSearchManager (method) | MATCH | — |
| get_selection() -> getSelection | getSelection (method) | getSelection (method) | MATCH | — |
| open_project() -> openProject | openProject (method) | openProject (method) | MATCH | — |
| quit() -> quit | quit (method) | quit (method) | MATCH | — |
| regenerate() -> regenerate | regenerate (method) | regenerate (method) | MATCH | — |
| save_all() -> saveAll | saveAll (method) | saveAll (method) | MATCH | — |
| set_hidden_ui() -> setHiddenUI | setHiddenUI (method) | setHiddenUI (method) | MATCH | — |
| set_log() -> setLog | setLog (method) | setLog (method) | MATCH | — |

## AI Fix Guidance

### Finding 1: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_version() -> version
- **Expected Python method(s):** `version`
- **Java signature(s):** `IRPApplication.version()`
- **pywin32 member(s):** version (method)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
