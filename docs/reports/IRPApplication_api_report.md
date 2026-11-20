# Rhapsody API Validation: IRPApplication

## Summary
- Target wrapper: `RhapsodyApplication` (`src/rhapsody_cli/application.py`)
- Members: Python `33`, Java `176`, pywin32 `193`
- Deviations: `168`
- Deviations by status:
  - `ACCESSOR_ALIAS_MISMATCH`: 18
  - `COM_MEMBER_NOT_EXPOSED`: 2
  - `JAVA_ONLY_MEMBER`: 1
  - `METHOD_PROPERTY_MISMATCH`: 13
  - `MISSING_PYTHON_WRAPPER`: 139
  - `PYTHON_METHOD_NAME_MISMATCH`: 1
  - `PYTHON_ONLY_MEMBER`: 4
  - `PYWIN32_ONLY_MEMBER`: 19

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | addProfileToModel (method) | addProfileToModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addSelectedToFavorites (method) | addSelectedToFavorites (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addToModelByReference (method) | addToModelByReference (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addToModelFromURL (method) | addToModelFromURL (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | addUnitsToModel (method) | addUnitsToModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | allowBrowserRefresh (method) | allowBrowserRefresh (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | allowGERefresh (method) | allowGERefresh (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | allowRmmRemoteOslcLinksLoad (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | getApplicationConnectionString (method) | getApplicationConnectionString (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getApplicationName (method) | getApplicationName (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getApplicationRoot (method) | ApplicationRoot (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getApplicationStatus (method); setApplicationStatus (method) | getApplicationStatus (method); setApplicationStatus (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | applyNewTermsProfile (method) | applyNewTermsProfile (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | applyWindowLayout (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | arcCheckOut (method) | arcCheckOut (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | build (method) | build (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | buildEntireProject (method) | buildEntireProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_build_no() -> getBuildNo | getBuildNo (method) | BuildNo (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the BuildNo property or a getter/setter fallback instead of calling getBuildNo directly. |
| — | buildWithDependencies (method) | buildWithDependencies (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | canRedo (method) | canRedo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | canUndo (method) | canUndo (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | checkIn (method) | checkIn (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | checkOut (method) | checkOut (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | clean (method) | clean (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | clearOutputWindow (method) | clearOutputWindow (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | closeAllAnimatedSequenceDiagrams (method) | closeAllAnimatedSequenceDiagrams (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| close_all_projects() -> closeAllProjects | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| — | compareSequenceDiagram (method) | compareSequenceDiagram (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setComponent (method) | setComponent (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | setConfiguration (method) | setConfiguration (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | connectToArchive (method) | connectToArchive (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | connectToImportedModel (method) | connectToImportedModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | connectToTarget (method) | connectToTarget (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | createAndInsertProject (method) | createAndInsertProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | createDomainFromProfile (method) | createDomainFromProfile (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | createEmbeddedWebViewWindow (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | createProgressBar (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | getDMBoolProperty (method); setDMBoolProperty (method) | getDMBoolProperty (method); setDMBoolProperty (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDMModelWorkspaceFolder (method) | getDMModelWorkspaceFolder (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getDMProperty (method); setDMProperty (method) | getDMProperty (method); setDMProperty (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | dMRefreshRecursive (method) | dMRefreshRecursive (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | dMSyncAndRefresh (method) | dMSyncAndRefresh (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | dbgCheckComIn (method) | dbgCheckComIn (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | dbgCheckComOut (method) | dbgCheckComOut (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deferredAddToModel (method) | deferredAddToModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | deleteProjectFromList (method) | deleteProjectFromList (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | deleteWindowLayout (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
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
| — | — | exportWindowLayout (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | fixpack (method) | fixpack (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | forceOutput2Console (method) | forceOutput2Console (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | forceRoundtrip (method) | forceRoundtrip (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | forceRoundtripElements (method) | forceRoundtripElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | generateMainAndMakeFiles (method) | generateMainAndMakeFiles (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | generateWithDependencies (method) | generateWithDependencies (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | GetPlugInWindow (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | getHelperStatus (method); setHelperStatus (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | highLightElement (method) | highLightElement (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | highlightByHandle (method) | highlightByHandle (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | importClasses (method) | importClasses (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | importDesignManagerModel (method) | importDesignManagerModel (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | importSyncSimulinkBlock (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | importSyncSimulinkBlock2 (method) | importSyncSimulinkBlock2 (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | importTlb (method) | importTlb (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | importWindowLayout (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | getIniFileParameterValue (method) | getIniFileParameterValue (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | insertProject (method) | insertProject (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | insertProjectFromDesignManager (method) | insertProjectFromDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | invokePluginsMethod (method) | invokePluginsMethod (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | invokeRPE (method) | invokeRPE (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_is_hidden_ui() -> getIsHiddenUI; get_is_hidden_ui() -> isHiddenUI; set_hidden_ui() -> isHiddenUI | getIsHiddenUI (method) | isHiddenUI (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | getIsLoadOnDemand (method); setIsLoadOnDemand (method) | isLoadOnDemand (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isRhapsodyCL (method) | isRhapsodyCL (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | isRhapsodyFileType (method) | isRhapsodyFileType (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | isValidWebView (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
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
| get_omroot() -> getOMROOT | getOMROOT (method) | OMROOT (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the OMROOT property or a getter/setter fallback instead of calling getOMROOT directly. |
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
| — | getPlugInWindow (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |
| — | — | getProgressBar (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| get_projects() -> getProjects; get_projects() -> projects | getProjects (method) | projects (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| connect() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| disconnect() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
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
| — | — | removeProgressBar (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | renameWindowLayout (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | report (method) | report (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | resetWindowLayout (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| get_rhapsody_dir() -> getRhapsodyDir | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| — | getRhapsodyHandleErrorFunction (method) | getRhapsodyHandleErrorFunction (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getRhapsodyHandleErrorFunctionLong (method) | getRhapsodyHandleErrorFunctionLong (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | rhpCheckinLicense (method) | RhpCheckinLicense (method) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | rhpCheckoutLicense (method) | RhpCheckoutLicense (method) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | roundtrip (method) | roundtrip (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | roundtripElements (method) | roundtripElements (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | runApplication (method) | runApplication (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | runHelper (method) | runHelper (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | runHelperWithParameters (method) | runHelperWithParameters (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | saveCheckModelResult (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | saveWindowLayout (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
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
| get_version() -> version | version (method) | version (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| — | versionNumberLong (method) | versionNumberLong (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | getWebViewURL (method); setWebViewURL (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | getWindowLayoutList (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | writeToOutputWindow (method) | writeToOutputWindow (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |

## AI Fix Guidance

### Finding 1: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `add_profile_to_model`
- **Java signature(s):** `IRPApplication.addProfileToModel(java.lang.String)`
- **pywin32 member(s):** addProfileToModel (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `add_selected_to_favorites`
- **Java signature(s):** `IRPApplication.addSelectedToFavorites()`
- **pywin32 member(s):** addSelectedToFavorites (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 3: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `add_to_model_by_reference`
- **Java signature(s):** `IRPApplication.addToModelByReference(java.lang.String)`
- **pywin32 member(s):** addToModelByReference (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 4: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `add_to_model_from_url`
- **Java signature(s):** `IRPApplication.addToModelFromURL(java.lang.String)`
- **pywin32 member(s):** addToModelFromURL (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 5: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `add_units_to_model`
- **Java signature(s):** `IRPApplication.addUnitsToModel(com.telelogic.rhapsody.core.IRPCollection, int, int, int)`
- **pywin32 member(s):** addUnitsToModel (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 6: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `allow_browser_refresh`
- **Java signature(s):** `IRPApplication.allowBrowserRefresh(int)`
- **pywin32 member(s):** allowBrowserRefresh (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 7: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `allow_ge_refresh`
- **Java signature(s):** `IRPApplication.allowGERefresh(int)`
- **pywin32 member(s):** allowGERefresh (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 8: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** allowRmmRemoteOslcLinksLoad (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 9: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_application_connection_string`
- **Java signature(s):** `IRPApplication.getApplicationConnectionString()`
- **pywin32 member(s):** getApplicationConnectionString (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 10: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_application_name`
- **Java signature(s):** `IRPApplication.getApplicationName(java.lang.String, java.lang.String)`
- **pywin32 member(s):** getApplicationName (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 11: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_application_root`
- **Java signature(s):** `IRPApplication.getApplicationRoot()`
- **pywin32 member(s):** ApplicationRoot (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 12: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_application_status`, `set_application_status`
- **Java signature(s):** `IRPApplication.getApplicationStatus()`, `IRPApplication.setApplicationStatus(int)`
- **pywin32 member(s):** getApplicationStatus (method); setApplicationStatus (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 13: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `apply_new_terms_profile`
- **Java signature(s):** `IRPApplication.applyNewTermsProfile(java.lang.String)`
- **pywin32 member(s):** applyNewTermsProfile (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 14: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** applyWindowLayout (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 15: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `arc_check_out`
- **Java signature(s):** `IRPApplication.arcCheckOut(java.lang.String, java.lang.String, int, int)`
- **pywin32 member(s):** arcCheckOut (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 16: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `build`
- **Java signature(s):** `IRPApplication.build()`
- **pywin32 member(s):** build (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 17: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `build_entire_project`
- **Java signature(s):** `IRPApplication.buildEntireProject()`
- **pywin32 member(s):** buildEntireProject (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 18: COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_build_no() -> getBuildNo
- **Expected Python method(s):** `get_build_no`
- **Java signature(s):** `IRPApplication.getBuildNo()`
- **pywin32 member(s):** BuildNo (property)
- **Recommended change:** Use the BuildNo property or a getter/setter fallback instead of calling getBuildNo directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 19: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `build_with_dependencies`
- **Java signature(s):** `IRPApplication.buildWithDependencies()`
- **pywin32 member(s):** buildWithDependencies (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 20: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `can_redo`
- **Java signature(s):** `IRPApplication.canRedo()`
- **pywin32 member(s):** canRedo (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 21: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `can_undo`
- **Java signature(s):** `IRPApplication.canUndo()`
- **pywin32 member(s):** canUndo (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 22: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `check_in`
- **Java signature(s):** `IRPApplication.checkIn(java.lang.String, java.lang.String, int, int, java.lang.String)`
- **pywin32 member(s):** checkIn (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 23: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `check_out`
- **Java signature(s):** `IRPApplication.checkOut(java.lang.String, java.lang.String, int, int)`
- **pywin32 member(s):** checkOut (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 24: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `clean`
- **Java signature(s):** `IRPApplication.clean()`
- **pywin32 member(s):** clean (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 25: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `clear_output_window`
- **Java signature(s):** `IRPApplication.clearOutputWindow(java.lang.String)`
- **pywin32 member(s):** clearOutputWindow (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 26: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `close_all_animated_sequence_diagrams`
- **Java signature(s):** `IRPApplication.closeAllAnimatedSequenceDiagrams(int)`
- **pywin32 member(s):** closeAllAnimatedSequenceDiagrams (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 27: PYTHON_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** close_all_projects() -> closeAllProjects
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 28: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `compare_sequence_diagram`
- **Java signature(s):** `IRPApplication.compareSequenceDiagram(com.telelogic.rhapsody.core.IRPSequenceDiagram, com.telelogic.rhapsody.core.IRPSequenceDiagram)`
- **pywin32 member(s):** compareSequenceDiagram (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 29: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `set_component`
- **Java signature(s):** `IRPApplication.setComponent(java.lang.String)`
- **pywin32 member(s):** setComponent (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 30: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `set_configuration`
- **Java signature(s):** `IRPApplication.setConfiguration(java.lang.String)`
- **pywin32 member(s):** setConfiguration (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 31: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `connect_to_archive`
- **Java signature(s):** `IRPApplication.connectToArchive(java.lang.String)`
- **pywin32 member(s):** connectToArchive (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 32: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `connect_to_imported_model`
- **Java signature(s):** `IRPApplication.connectToImportedModel(java.lang.String, java.lang.String, java.lang.String)`
- **pywin32 member(s):** connectToImportedModel (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 33: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `connect_to_target`
- **Java signature(s):** `IRPApplication.connectToTarget(java.lang.String)`
- **pywin32 member(s):** connectToTarget (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 34: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `create_and_insert_project`
- **Java signature(s):** `IRPApplication.createAndInsertProject(java.lang.String, java.lang.String)`
- **pywin32 member(s):** createAndInsertProject (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 35: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `create_domain_from_profile`
- **Java signature(s):** `IRPApplication.createDomainFromProfile(com.telelogic.rhapsody.core.IRPProfile, java.lang.String)`
- **pywin32 member(s):** createDomainFromProfile (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 36: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** createEmbeddedWebViewWindow (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 37: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** createProgressBar (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 38: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_dm_bool_property`, `set_dm_bool_property`
- **Java signature(s):** `IRPApplication.getDMBoolProperty(java.lang.String)`, `IRPApplication.setDMBoolProperty(java.lang.String, int)`
- **pywin32 member(s):** getDMBoolProperty (method); setDMBoolProperty (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 39: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_dm_model_workspace_folder`
- **Java signature(s):** `IRPApplication.getDMModelWorkspaceFolder()`
- **pywin32 member(s):** getDMModelWorkspaceFolder (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 40: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_dm_property`, `set_dm_property`
- **Java signature(s):** `IRPApplication.getDMProperty(java.lang.String)`, `IRPApplication.setDMProperty(java.lang.String, java.lang.String)`
- **pywin32 member(s):** getDMProperty (method); setDMProperty (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 41: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `d_m_refresh_recursive`
- **Java signature(s):** `IRPApplication.dMRefreshRecursive(com.telelogic.rhapsody.core.IRPUnit)`
- **pywin32 member(s):** dMRefreshRecursive (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 42: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `d_m_sync_and_refresh`
- **Java signature(s):** `IRPApplication.dMSyncAndRefresh(com.telelogic.rhapsody.core.IRPProject, int, int)`
- **pywin32 member(s):** dMSyncAndRefresh (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 43: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `dbg_check_com_in`
- **Java signature(s):** `IRPApplication.dbgCheckComIn(short)`
- **pywin32 member(s):** dbgCheckComIn (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 44: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `dbg_check_com_out`
- **Java signature(s):** `IRPApplication.dbgCheckComOut()`
- **pywin32 member(s):** dbgCheckComOut (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 45: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `deferred_add_to_model`
- **Java signature(s):** `IRPApplication.deferredAddToModel(java.lang.String, int, java.lang.String, int)`
- **pywin32 member(s):** deferredAddToModel (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 46: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `delete_project_from_list`
- **Java signature(s):** `IRPApplication.deleteProjectFromList(java.lang.String)`
- **pywin32 member(s):** deleteProjectFromList (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 47: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** deleteWindowLayout (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 48: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_diagram_of_selected_element`
- **Java signature(s):** `IRPApplication.getDiagramOfSelectedElement()`
- **pywin32 member(s):** getDiagramOfSelectedElement (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 49: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `disconnect_from_target`
- **Java signature(s):** `IRPApplication.disconnectFromTarget()`
- **pywin32 member(s):** disconnectFromTarget (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 50: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `download_to_target`
- **Java signature(s):** `IRPApplication.downloadToTarget(java.lang.String)`
- **pywin32 member(s):** downloadToTarget (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 51: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `end_undo_transaction`
- **Java signature(s):** `IRPApplication.endUndoTransaction()`
- **pywin32 member(s):** endUndoTransaction (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 52: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `enter_animation_command`
- **Java signature(s):** `IRPApplication.enterAnimationCommand(java.lang.String)`
- **pywin32 member(s):** enterAnimationCommand (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 53: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `error_message`, `get_error_message`
- **Java signature(s):** `IRPApplication.errorMessage()`, `IRPApplication.getErrorMessage()`
- **pywin32 member(s):** errorMessage (method); getErrorMessage (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 54: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_executable_folder`
- **Java signature(s):** `IRPApplication.getExecutableFolder()`
- **pywin32 member(s):** getExecutableFolder (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 55: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `execute_command`
- **Java signature(s):** `IRPApplication.executeCommand(java.lang.String, com.telelogic.rhapsody.core.IRPCollection, com.telelogic.rhapsody.core.IRPCollection)`
- **pywin32 member(s):** ExecuteCommand (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 56: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `execute_command_line`
- **Java signature(s):** `IRPApplication.executeCommandLine(java.lang.String)`
- **pywin32 member(s):** executeCommandLine (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 57: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `execute_transformation_sequence`
- **Java signature(s):** `IRPApplication.executeTransformationSequence(java.lang.String, int)`
- **pywin32 member(s):** executeTransformationSequence (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 58: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `expand_string_keywords`
- **Java signature(s):** `IRPApplication.expandStringKeywords(java.lang.String)`
- **pywin32 member(s):** expandStringKeywords (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 59: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** exportWindowLayout (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 60: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `fixpack`
- **Java signature(s):** `IRPApplication.fixpack()`
- **pywin32 member(s):** fixpack (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 61: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `force_output2_console`
- **Java signature(s):** `IRPApplication.forceOutput2Console(int)`
- **pywin32 member(s):** forceOutput2Console (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 62: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `force_roundtrip`
- **Java signature(s):** `IRPApplication.forceRoundtrip()`
- **pywin32 member(s):** forceRoundtrip (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 63: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `force_roundtrip_elements`
- **Java signature(s):** `IRPApplication.forceRoundtripElements(com.telelogic.rhapsody.core.IRPCollection)`
- **pywin32 member(s):** forceRoundtripElements (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 64: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `generate_main_and_make_files`
- **Java signature(s):** `IRPApplication.generateMainAndMakeFiles()`
- **pywin32 member(s):** generateMainAndMakeFiles (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 65: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `generate_with_dependencies`
- **Java signature(s):** `IRPApplication.generateWithDependencies()`
- **pywin32 member(s):** generateWithDependencies (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 66: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** GetPlugInWindow (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 67: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** getHelperStatus (method); setHelperStatus (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 68: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `high_light_element`
- **Java signature(s):** `IRPApplication.highLightElement(com.telelogic.rhapsody.core.IRPModelElement)`
- **pywin32 member(s):** highLightElement (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 69: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `highlight_by_handle`
- **Java signature(s):** `IRPApplication.highlightByHandle(java.lang.String)`
- **pywin32 member(s):** highlightByHandle (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 70: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `import_classes`
- **Java signature(s):** `IRPApplication.importClasses()`
- **pywin32 member(s):** importClasses (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 71: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `import_design_manager_model`
- **Java signature(s):** `IRPApplication.importDesignManagerModel(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, int)`
- **pywin32 member(s):** importDesignManagerModel (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 72: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** importSyncSimulinkBlock (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 73: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `import_sync_simulink_block2`
- **Java signature(s):** `IRPApplication.importSyncSimulinkBlock2(com.telelogic.rhapsody.core.IRPModelElement, java.lang.String, java.lang.String, java.lang.String, java.lang.String)`
- **pywin32 member(s):** importSyncSimulinkBlock2 (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 74: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `import_tlb`
- **Java signature(s):** `IRPApplication.importTlb(java.lang.String)`
- **pywin32 member(s):** importTlb (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 75: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** importWindowLayout (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 76: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_ini_file_parameter_value`
- **Java signature(s):** `IRPApplication.getIniFileParameterValue(java.lang.String, java.lang.String)`
- **pywin32 member(s):** getIniFileParameterValue (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 77: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `insert_project`
- **Java signature(s):** `IRPApplication.insertProject(java.lang.String)`
- **pywin32 member(s):** insertProject (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 78: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `insert_project_from_design_manager`
- **Java signature(s):** `IRPApplication.insertProjectFromDesignManager(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)`
- **pywin32 member(s):** insertProjectFromDesignManager (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 79: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_interface_name`
- **Java signature(s):** `IRPApplication.getInterfaceName()`
- **pywin32 member(s):** interfaceName (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 80: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `invoke_plugins_method`
- **Java signature(s):** `IRPApplication.invokePluginsMethod(java.lang.String)`
- **pywin32 member(s):** invokePluginsMethod (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 81: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `invoke_rpe`
- **Java signature(s):** `IRPApplication.invokeRPE()`
- **pywin32 member(s):** invokeRPE (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 82: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_is_hidden_ui() -> getIsHiddenUI; get_is_hidden_ui() -> isHiddenUI; set_hidden_ui() -> isHiddenUI
- **Expected Python method(s):** `get_is_hidden_ui`
- **Java signature(s):** `IRPApplication.getIsHiddenUI()`
- **pywin32 member(s):** isHiddenUI (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 83: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_is_load_on_demand`, `set_is_load_on_demand`
- **Java signature(s):** `IRPApplication.getIsLoadOnDemand()`, `IRPApplication.setIsLoadOnDemand(int)`
- **pywin32 member(s):** isLoadOnDemand (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 84: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `is_rhapsody_cl`
- **Java signature(s):** `IRPApplication.isRhapsodyCL()`
- **pywin32 member(s):** isRhapsodyCL (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 85: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `is_rhapsody_file_type`
- **Java signature(s):** `IRPApplication.isRhapsodyFileType(java.lang.String)`
- **pywin32 member(s):** isRhapsodyFileType (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 86: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** isValidWebView (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 87: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_language`, `set_language`
- **Java signature(s):** `IRPApplication.getLanguage()`, `IRPApplication.setLanguage(java.lang.String)`
- **pywin32 member(s):** Language (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 88: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_list_of_factory_properties`
- **Java signature(s):** `IRPApplication.getListOfFactoryProperties()`
- **pywin32 member(s):** getListOfFactoryProperties (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 89: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_list_of_selected_elements`
- **Java signature(s):** `IRPApplication.getListOfSelectedElements()`
- **pywin32 member(s):** getListOfSelectedElements (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 90: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_list_of_site_properties`
- **Java signature(s):** `IRPApplication.getListOfSiteProperties()`
- **pywin32 member(s):** getListOfSiteProperties (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 91: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_locale_name`
- **Java signature(s):** `IRPApplication.getLocaleName()`
- **pywin32 member(s):** getLocaleName (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 92: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_log_root`
- **Java signature(s):** `IRPApplication.getLogRoot()`
- **pywin32 member(s):** LogRoot (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 93: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `login_to_design_manager_with_alias`
- **Java signature(s):** `IRPApplication.loginToDesignManagerWithAlias(java.lang.String, java.lang.String)`
- **pywin32 member(s):** loginToDesignManagerWithAlias (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 94: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `login_to_design_manager_with_certificate`
- **Java signature(s):** `IRPApplication.loginToDesignManagerWithCertificate(java.lang.String, java.lang.String, java.lang.String)`
- **pywin32 member(s):** loginToDesignManagerWithCertificate (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 95: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `login_to_design_manager_with_username`
- **Java signature(s):** `IRPApplication.loginToDesignManagerWithUsername(java.lang.String, java.lang.String, java.lang.String)`
- **pywin32 member(s):** loginToDesignManagerWithUsername (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 96: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `make`
- **Java signature(s):** `IRPApplication.make()`
- **pywin32 member(s):** make (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 97: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `merge_elements`
- **Java signature(s):** `IRPApplication.mergeElements(com.telelogic.rhapsody.core.IRPModelElement, com.telelogic.rhapsody.core.IRPModelElement)`
- **pywin32 member(s):** mergeElements (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 98: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_model_element_from_source`
- **Java signature(s):** `IRPApplication.getModelElementFromSource(java.lang.String, int, int)`
- **pywin32 member(s):** getModelElementFromSource (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 99: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `new_project_on_design_manager`
- **Java signature(s):** `IRPApplication.newProjectOnDesignManager(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)`
- **pywin32 member(s):** newProjectOnDesignManager (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 100: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `notify_file_changed`
- **Java signature(s):** `IRPApplication.notifyFileChanged(java.lang.String, int)`
- **pywin32 member(s):** notifyFileChanged (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 101: COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_omroot() -> getOMROOT
- **Expected Python method(s):** `get_omroot`
- **Java signature(s):** `IRPApplication.getOMROOT()`
- **pywin32 member(s):** OMROOT (property)
- **Recommended change:** Use the OMROOT property or a getter/setter fallback instead of calling getOMROOT directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 102: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `open_active_x_view`
- **Java signature(s):** `IRPApplication.openActiveXView(java.lang.String, com.telelogic.rhapsody.core.IRPCollection, com.telelogic.rhapsody.core.IRPCollection)`
- **pywin32 member(s):** OpenActiveXView (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 103: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `open_advanced_search_and_replace_dialog`
- **Java signature(s):** `IRPApplication.openAdvancedSearchAndReplaceDialog()`
- **pywin32 member(s):** openAdvancedSearchAndReplaceDialog (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 104: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `open_diagram_view`
- **Java signature(s):** `IRPApplication.openDiagramView(com.telelogic.rhapsody.core.IRPDiagram)`
- **pywin32 member(s):** OpenDiagramView (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 105: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `open_file_list`
- **Java signature(s):** `IRPApplication.openFileList(java.lang.String)`
- **pywin32 member(s):** openFileList (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 106: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `open_project_from_design_manager`
- **Java signature(s):** `IRPApplication.openProjectFromDesignManager(java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String, java.lang.String)`
- **pywin32 member(s):** openProjectFromDesignManager (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 107: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `open_project_from_design_manager_after_login`
- **Java signature(s):** `IRPApplication.openProjectFromDesignManagerAfterLogin(java.lang.String, java.lang.String, java.lang.String, java.lang.String)`
- **pywin32 member(s):** openProjectFromDesignManagerAfterLogin (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 108: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `open_project_from_url`
- **Java signature(s):** `IRPApplication.openProjectFromURL(java.lang.String)`
- **pywin32 member(s):** openProjectFromURL (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 109: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `open_project_with_last_session`
- **Java signature(s):** `IRPApplication.openProjectWithLastSession(java.lang.String)`
- **pywin32 member(s):** openProjectWithLastSession (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 110: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `open_project_without_sub_units`
- **Java signature(s):** `IRPApplication.openProjectWithoutSubUnits(java.lang.String)`
- **pywin32 member(s):** openProjectWithoutSubUnits (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 111: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_output_window_text`
- **Java signature(s):** `IRPApplication.getOutputWindowText()`
- **pywin32 member(s):** getOutputWindowText (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 112: JAVA_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_plug_in_window`
- **Java signature(s):** `IRPApplication.getPlugInWindow(int, int, int)`
- **pywin32 member(s):** —
- **Recommended change:** Verify the Java documentation against the installed COM type library.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 113: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** getProgressBar (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 114: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_projects() -> getProjects; get_projects() -> projects
- **Expected Python method(s):** `get_projects`
- **Java signature(s):** `IRPApplication.getProjects()`
- **pywin32 member(s):** projects (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 115: PYTHON_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** connect() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 116: PYTHON_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** disconnect() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 117: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `rebuild`
- **Java signature(s):** `IRPApplication.rebuild()`
- **pywin32 member(s):** rebuild (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 118: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `rebuild_entire_project`
- **Java signature(s):** `IRPApplication.rebuildEntireProject()`
- **pywin32 member(s):** rebuildEntireProject (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 119: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `rebuild_with_dependencies`
- **Java signature(s):** `IRPApplication.rebuildWithDependencies()`
- **pywin32 member(s):** rebuildWithDependencies (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 120: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `redo`
- **Java signature(s):** `IRPApplication.redo()`
- **pywin32 member(s):** redo (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 121: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `refactor_selected_operation`
- **Java signature(s):** `IRPApplication.refactorSelectedOperation(java.lang.String)`
- **pywin32 member(s):** refactorSelectedOperation (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 122: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `refresh_all_views`
- **Java signature(s):** `IRPApplication.refreshAllViews()`
- **pywin32 member(s):** refreshAllViews (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 123: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `regenerate_elements`
- **Java signature(s):** `IRPApplication.regenerateElements(com.telelogic.rhapsody.core.IRPCollection)`
- **pywin32 member(s):** regenerateElements (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 124: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `regenerate_entire_project`
- **Java signature(s):** `IRPApplication.regenerateEntireProject()`
- **pywin32 member(s):** regenerateEntireProject (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 125: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `regenerate_with_dependencies`
- **Java signature(s):** `IRPApplication.regenerateWithDependencies()`
- **pywin32 member(s):** regenerateWithDependencies (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 126: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `register_com_client`
- **Java signature(s):** `IRPApplication.registerCOMClient(int, java.lang.String, int)`
- **pywin32 member(s):** registerCOMClient (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 127: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** removeProgressBar (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 128: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** renameWindowLayout (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 129: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `report`
- **Java signature(s):** `IRPApplication.report(java.lang.String, java.lang.String)`
- **pywin32 member(s):** report (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 130: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** resetWindowLayout (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 131: PYTHON_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_rhapsody_dir() -> getRhapsodyDir
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 132: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_rhapsody_handle_error_function`
- **Java signature(s):** `IRPApplication.getRhapsodyHandleErrorFunction()`
- **pywin32 member(s):** getRhapsodyHandleErrorFunction (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 133: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_rhapsody_handle_error_function_long`
- **Java signature(s):** `IRPApplication.getRhapsodyHandleErrorFunctionLong()`
- **pywin32 member(s):** getRhapsodyHandleErrorFunctionLong (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 134: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `rhp_checkin_license`
- **Java signature(s):** `IRPApplication.rhpCheckinLicense(java.lang.String)`
- **pywin32 member(s):** RhpCheckinLicense (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 135: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `rhp_checkout_license`
- **Java signature(s):** `IRPApplication.rhpCheckoutLicense(java.lang.String)`
- **pywin32 member(s):** RhpCheckoutLicense (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 136: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `roundtrip`
- **Java signature(s):** `IRPApplication.roundtrip()`
- **pywin32 member(s):** roundtrip (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 137: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `roundtrip_elements`
- **Java signature(s):** `IRPApplication.roundtripElements(com.telelogic.rhapsody.core.IRPCollection)`
- **pywin32 member(s):** roundtripElements (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 138: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `run_application`
- **Java signature(s):** `IRPApplication.runApplication()`
- **pywin32 member(s):** runApplication (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 139: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `run_helper`
- **Java signature(s):** `IRPApplication.runHelper(java.lang.String)`
- **pywin32 member(s):** runHelper (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 140: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `run_helper_with_parameters`
- **Java signature(s):** `IRPApplication.runHelperWithParameters(java.lang.String, java.lang.String)`
- **pywin32 member(s):** runHelperWithParameters (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 141: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** saveCheckModelResult (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 142: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** saveWindowLayout (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 143: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `select_graph_elements`
- **Java signature(s):** `IRPApplication.selectGraphElements(com.telelogic.rhapsody.core.IRPCollection)`
- **pywin32 member(s):** selectGraphElements (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 144: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `select_model_elements`
- **Java signature(s):** `IRPApplication.selectModelElements(com.telelogic.rhapsody.core.IRPCollection)`
- **pywin32 member(s):** selectModelElements (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 145: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_selected_element`
- **Java signature(s):** `IRPApplication.getSelectedElement()`
- **pywin32 member(s):** getSelectedElement (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 146: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_selected_graph_elements`
- **Java signature(s):** `IRPApplication.getSelectedGraphElements()`
- **pywin32 member(s):** getSelectedGraphElements (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 147: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_serial_no`
- **Java signature(s):** `IRPApplication.getSerialNo()`
- **pywin32 member(s):** SerialNo (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 148: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `start_undo_transaction`
- **Java signature(s):** `IRPApplication.startUndoTransaction()`
- **pywin32 member(s):** startUndoTransaction (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 149: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `sync_build`
- **Java signature(s):** `IRPApplication.syncBuild()`
- **pywin32 member(s):** syncBuild (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 150: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `terminate_application`
- **Java signature(s):** `IRPApplication.terminateApplication()`
- **pywin32 member(s):** terminateApplication (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 151: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_the_code_generator_interface`
- **Java signature(s):** `IRPApplication.getTheCodeGeneratorInterface()`
- **pywin32 member(s):** getTheCodeGeneratorInterface (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 152: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_the_external_code_generator_invoker`
- **Java signature(s):** `IRPApplication.getTheExternalCodeGeneratorInvoker()`
- **pywin32 member(s):** getTheExternalCodeGeneratorInvoker (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 153: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_the_integrator_interface`
- **Java signature(s):** `IRPApplication.getTheIntegratorInterface()`
- **pywin32 member(s):** getTheIntegratorInterface (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 154: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_the_java_plugins_interface`
- **Java signature(s):** `IRPApplication.getTheJavaPluginsInterface()`
- **pywin32 member(s):** getTheJavaPluginsInterface (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 155: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_the_roundtrip_interface`
- **Java signature(s):** `IRPApplication.getTheRoundtripInterface()`
- **pywin32 member(s):** getTheRoundtripInterface (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 156: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_tool_set`, `set_tool_set`
- **Java signature(s):** `IRPApplication.getToolSet()`, `IRPApplication.setToolSet(java.lang.String)`
- **pywin32 member(s):** ToolSet (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 157: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `undo`
- **Java signature(s):** `IRPApplication.undo()`
- **pywin32 member(s):** undo (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 158: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `unload_from_target`
- **Java signature(s):** `IRPApplication.unloadFromTarget()`
- **pywin32 member(s):** unloadFromTarget (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 159: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `unregister_com_client`
- **Java signature(s):** `IRPApplication.unregisterCOMClient(int, java.lang.String, int)`
- **pywin32 member(s):** unregisterCOMClient (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 160: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `set_update_recent_file_list`
- **Java signature(s):** `IRPApplication.setUpdateRecentFileList(int)`
- **pywin32 member(s):** setUpdateRecentFileList (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 161: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `update_rmm_data_to_new_version`
- **Java signature(s):** `IRPApplication.updateRmmDataToNewVersion()`
- **pywin32 member(s):** updateRmmDataToNewVersion (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 162: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_user_data_root`
- **Java signature(s):** `IRPApplication.getUserDataRoot()`
- **pywin32 member(s):** UserDataRoot (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 163: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_user_omroot`
- **Java signature(s):** `IRPApplication.getUserOMROOT()`
- **pywin32 member(s):** UserOMROOT (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 164: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** get_version() -> version
- **Expected Python method(s):** `version`
- **Java signature(s):** `IRPApplication.version()`
- **pywin32 member(s):** version (method)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 165: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `version_number_long`
- **Java signature(s):** `IRPApplication.versionNumberLong()`
- **pywin32 member(s):** versionNumberLong (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 166: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** getWebViewURL (method); setWebViewURL (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 167: PYWIN32_ONLY_MEMBER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** getWindowLayoutList (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 168: MISSING_PYTHON_WRAPPER
- **Target:** `RhapsodyApplication` in `src/rhapsody_cli/application.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `write_to_output_window`
- **Java signature(s):** `IRPApplication.writeToOutputWindow(java.lang.String, java.lang.String)`
- **pywin32 member(s):** writeToOutputWindow (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
