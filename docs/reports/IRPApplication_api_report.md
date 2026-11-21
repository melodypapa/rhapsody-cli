# Rhapsody API Validation: IRPApplication

## Summary
- Target wrapper: `RhapsodyApplication` (`src/rhapsody_cli/application.py`)
- Members: Python `33`, Java `176`, pywin32 `172`
- Deviations: `3`
- Deviations by status:
  - `COM_MEMBER_NOT_EXPOSED`: 2
  - `PYTHON_METHOD_NAME_MISMATCH`: 1

- Informational binding differences (expected): `5`
- Wrapper backlog (supported members without wrappers): `139`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_build_no() -> getBuildNo | getBuildNo (method) | BuildNo (property) | COM_MEMBER_NOT_EXPOSED | Use the BuildNo property or a getter/setter fallback instead of calling getBuildNo directly. |
| get_omroot() -> getOMROOT | getOMROOT (method) | OMROOT (property) | COM_MEMBER_NOT_EXPOSED | Use the OMROOT property or a getter/setter fallback instead of calling getOMROOT directly. |
| get_version() -> version | version (method) | version (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| close_all_projects() -> closeAllProjects | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| — | getPlugInWindow (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |
| connect() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| disconnect() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_rhapsody_dir() -> getRhapsodyDir | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | addProfileToModel (method) | addProfileToModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addSelectedToFavorites (method) | addSelectedToFavorites (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addToModelByReference (method) | addToModelByReference (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addToModelFromURL (method) | addToModelFromURL (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addUnitsToModel (method) | addUnitsToModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | allowBrowserRefresh (method) | allowBrowserRefresh (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | allowGERefresh (method) | allowGERefresh (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getApplicationConnectionString (method) | getApplicationConnectionString (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getApplicationName (method) | getApplicationName (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getApplicationRoot (method) | ApplicationRoot (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getApplicationStatus (method); setApplicationStatus (method) | getApplicationStatus (method); setApplicationStatus (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | applyNewTermsProfile (method) | applyNewTermsProfile (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | arcCheckOut (method) | arcCheckOut (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | build (method) | build (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | buildEntireProject (method) | buildEntireProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | buildWithDependencies (method) | buildWithDependencies (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | canRedo (method) | canRedo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | canUndo (method) | canUndo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | checkIn (method) | checkIn (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | checkOut (method) | checkOut (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | clean (method) | clean (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | clearOutputWindow (method) | clearOutputWindow (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | closeAllAnimatedSequenceDiagrams (method) | closeAllAnimatedSequenceDiagrams (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | compareSequenceDiagram (method) | compareSequenceDiagram (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setComponent (method) | setComponent (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setConfiguration (method) | setConfiguration (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | connectToArchive (method) | connectToArchive (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | connectToImportedModel (method) | connectToImportedModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | connectToTarget (method) | connectToTarget (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | createAndInsertProject (method) | createAndInsertProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | createDomainFromProfile (method) | createDomainFromProfile (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDMBoolProperty (method); setDMBoolProperty (method) | getDMBoolProperty (method); setDMBoolProperty (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDMModelWorkspaceFolder (method) | getDMModelWorkspaceFolder (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDMProperty (method); setDMProperty (method) | getDMProperty (method); setDMProperty (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | dMRefreshRecursive (method) | dMRefreshRecursive (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | dMSyncAndRefresh (method) | dMSyncAndRefresh (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | dbgCheckComIn (method) | dbgCheckComIn (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | dbgCheckComOut (method) | dbgCheckComOut (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deferredAddToModel (method) | deferredAddToModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteProjectFromList (method) | deleteProjectFromList (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDiagramOfSelectedElement (method) | getDiagramOfSelectedElement (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | disconnectFromTarget (method) | disconnectFromTarget (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | downloadToTarget (method) | downloadToTarget (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | endUndoTransaction (method) | endUndoTransaction (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | enterAnimationCommand (method) | enterAnimationCommand (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | errorMessage (method); getErrorMessage (method) | errorMessage (method); getErrorMessage (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getExecutableFolder (method) | getExecutableFolder (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | executeCommand (method) | ExecuteCommand (method) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | executeCommandLine (method) | executeCommandLine (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | executeTransformationSequence (method) | executeTransformationSequence (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | expandStringKeywords (method) | expandStringKeywords (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | fixpack (method) | fixpack (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | forceOutput2Console (method) | forceOutput2Console (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | forceRoundtrip (method) | forceRoundtrip (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | forceRoundtripElements (method) | forceRoundtripElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | generateMainAndMakeFiles (method) | generateMainAndMakeFiles (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | generateWithDependencies (method) | generateWithDependencies (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | highLightElement (method) | highLightElement (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | highlightByHandle (method) | highlightByHandle (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | importClasses (method) | importClasses (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | importDesignManagerModel (method) | importDesignManagerModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | importSyncSimulinkBlock2 (method) | importSyncSimulinkBlock2 (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | importTlb (method) | importTlb (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIniFileParameterValue (method) | getIniFileParameterValue (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | insertProject (method) | insertProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | insertProjectFromDesignManager (method) | insertProjectFromDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | invokePluginsMethod (method) | invokePluginsMethod (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | invokeRPE (method) | invokeRPE (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getIsLoadOnDemand (method); setIsLoadOnDemand (method) | isLoadOnDemand (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isRhapsodyCL (method) | isRhapsodyCL (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isRhapsodyFileType (method) | isRhapsodyFileType (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getLanguage (method); setLanguage (method) | Language (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getListOfFactoryProperties (method) | getListOfFactoryProperties (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getListOfSelectedElements (method) | getListOfSelectedElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getListOfSiteProperties (method) | getListOfSiteProperties (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getLocaleName (method) | getLocaleName (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getLogRoot (method) | LogRoot (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | loginToDesignManagerWithAlias (method) | loginToDesignManagerWithAlias (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | loginToDesignManagerWithCertificate (method) | loginToDesignManagerWithCertificate (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | loginToDesignManagerWithUsername (method) | loginToDesignManagerWithUsername (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | make (method) | make (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | mergeElements (method) | mergeElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getModelElementFromSource (method) | getModelElementFromSource (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | newProjectOnDesignManager (method) | newProjectOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | notifyFileChanged (method) | notifyFileChanged (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openActiveXView (method) | OpenActiveXView (method) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openAdvancedSearchAndReplaceDialog (method) | openAdvancedSearchAndReplaceDialog (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openDiagramView (method) | OpenDiagramView (method) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openFileList (method) | openFileList (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openProjectFromDesignManager (method) | openProjectFromDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openProjectFromDesignManagerAfterLogin (method) | openProjectFromDesignManagerAfterLogin (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openProjectFromURL (method) | openProjectFromURL (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openProjectWithLastSession (method) | openProjectWithLastSession (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | openProjectWithoutSubUnits (method) | openProjectWithoutSubUnits (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getOutputWindowText (method) | getOutputWindowText (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | rebuild (method) | rebuild (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | rebuildEntireProject (method) | rebuildEntireProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | rebuildWithDependencies (method) | rebuildWithDependencies (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | redo (method) | redo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | refactorSelectedOperation (method) | refactorSelectedOperation (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | refreshAllViews (method) | refreshAllViews (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | regenerateElements (method) | regenerateElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | regenerateEntireProject (method) | regenerateEntireProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | regenerateWithDependencies (method) | regenerateWithDependencies (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | registerCOMClient (method) | registerCOMClient (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | report (method) | report (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getRhapsodyHandleErrorFunction (method) | getRhapsodyHandleErrorFunction (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getRhapsodyHandleErrorFunctionLong (method) | getRhapsodyHandleErrorFunctionLong (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | rhpCheckinLicense (method) | RhpCheckinLicense (method) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | rhpCheckoutLicense (method) | RhpCheckoutLicense (method) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | roundtrip (method) | roundtrip (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | roundtripElements (method) | roundtripElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | runApplication (method) | runApplication (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | runHelper (method) | runHelper (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | runHelperWithParameters (method) | runHelperWithParameters (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | selectGraphElements (method) | selectGraphElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | selectModelElements (method) | selectModelElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getSelectedElement (method) | getSelectedElement (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getSelectedGraphElements (method) | getSelectedGraphElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getSerialNo (method) | SerialNo (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | startUndoTransaction (method) | startUndoTransaction (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | syncBuild (method) | syncBuild (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | terminateApplication (method) | terminateApplication (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getTheCodeGeneratorInterface (method) | getTheCodeGeneratorInterface (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getTheExternalCodeGeneratorInvoker (method) | getTheExternalCodeGeneratorInvoker (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getTheIntegratorInterface (method) | getTheIntegratorInterface (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getTheJavaPluginsInterface (method) | getTheJavaPluginsInterface (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getTheRoundtripInterface (method) | getTheRoundtripInterface (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getToolSet (method); setToolSet (method) | ToolSet (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | undo (method) | undo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | unloadFromTarget (method) | unloadFromTarget (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | unregisterCOMClient (method) | unregisterCOMClient (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setUpdateRecentFileList (method) | setUpdateRecentFileList (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | updateRmmDataToNewVersion (method) | updateRmmDataToNewVersion (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getUserDataRoot (method) | UserDataRoot (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getUserOMROOT (method) | UserOMROOT (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | versionNumberLong (method) | versionNumberLong (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | writeToOutputWindow (method) | writeToOutputWindow (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |

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
| get_code_gen_simplifiers_registry() -> getCodeGenSimplifiersRegistry | getCodeGenSimplifiersRegistry (method) | getCodeGenSimplifiersRegistry (method) | MATCH | — |
| get_diag_synth_api() -> getDiagSynthAPI | getDiagSynthAPI (method) | getDiagSynthAPI (method) | MATCH | — |
| get_external_checker_registry() -> getExternalCheckerRegistry | getExternalCheckerRegistry (method) | getExternalCheckerRegistry (method) | MATCH | — |
| get_external_ide_registry() -> getExternalIDERegistry | getExternalIDERegistry (method) | getExternalIDERegistry (method) | MATCH | — |
| get_external_roundtrip_invoker() -> getExternalRoundtripInvoker | getExternalRoundtripInvoker (method) | getExternalRoundtripInvoker (method) | MATCH | — |
| get_is_hidden_ui() -> isHiddenUI; set_hidden_ui() -> isHiddenUI | getIsHiddenUI (method) | isHiddenUI (property) | MATCH | — |
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

### Finding 1: COM_MEMBER_NOT_EXPOSED
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_build_no() -> getBuildNo
- **Expected Python method(s):** `get_build_no`
- **Java signature(s):** `IRPApplication.getBuildNo()`
- **pywin32 member(s):** BuildNo (property)
- **Recommended change:** Use the BuildNo property or a getter/setter fallback instead of calling getBuildNo directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: COM_MEMBER_NOT_EXPOSED
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_omroot() -> getOMROOT
- **Expected Python method(s):** `get_omroot`
- **Java signature(s):** `IRPApplication.getOMROOT()`
- **pywin32 member(s):** OMROOT (property)
- **Recommended change:** Use the OMROOT property or a getter/setter fallback instead of calling getOMROOT directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 3: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_version() -> version
- **Expected Python method(s):** `version`
- **Java signature(s):** `IRPApplication.version()`
- **pywin32 member(s):** version (method)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
