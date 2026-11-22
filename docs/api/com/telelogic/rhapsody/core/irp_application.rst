.. _rhapsody-java-interface-IRPApplication:

IRPApplication
==============

The IRPApplication interface represents the Rhapsody application and its menu-bar commands.

- **Java interface:** IRPApplication
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPApplication interface represents the Rhapsody application.
- **Python wrapper:** RhapsodyApplication
- **Python import:** ``from rhapsody_cli.application import RhapsodyApplication``
- **Canonical module:** ``rhapsody_cli.application`` (application layer; §2 package move N/A).

Deviation-item totals (``IRPApplication_api_report.md``): 143 items — 1 actionable
(PYTHON_METHOD_NAME_MISMATCH on ``version``), 3 expected binding differences
(``getBuildNo``/``getOMROOT``/``getPlugInWindow``), and 139 wrapper-backlog members
enumerated below. ``close_all_projects`` and ``get_rhapsody_dir`` were python-only
conveniences that could never succeed (catalog-absent COM members) and were removed;
the integration teardown closes each project through ``IRPProject.close()``.

.. list-table:: Verified IRPApplication deviations, binding differences, and wrapper backlog
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - getBuildNo (method); getOMROOT (method)
     - BuildNo (property); OMROOT (property)
     - get_build_no(); get_omroot() via get_com_property
     - COM_MEMBER_NOT_EXPOSED (expected binding difference). Java-shaped
       getters do not exist; the wrappers read the exposed properties.
   * - version (method)
     - version (method)
     - get_version() -> version()
     - PYTHON_METHOD_NAME_MISMATCH. Python ``get_version`` alias retained by
       repo convention.
   * - —
     - no static COM member (facade helpers)
     - connect(); disconnect()
     - PYTHON_ONLY_MEMBER. Facade helpers with live callers across the
       codebase; removal is a recorded blocker rather than performed.
       ``getPlugInWindow`` is Java-only and intentionally unsupported.
   * - getProjects (method); getIsHiddenUI (method); setHiddenUI (method)
     - projects (property); isHiddenUI (property); setHiddenUI (method)
     - get_projects()/get_is_hidden_ui() via get_com_property; set_hidden_ui() via call_com
     - METHOD_PROPERTY_MISMATCH; Python get_* names retained by repo convention.
   * - addProfileToModel (method)
     - addProfileToModel (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - addSelectedToFavorites (method)
     - addSelectedToFavorites (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - addToModelByReference (method)
     - addToModelByReference (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - addToModelFromURL (method)
     - addToModelFromURL (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - addUnitsToModel (method)
     - addUnitsToModel (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - allowBrowserRefresh (method)
     - allowBrowserRefresh (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - allowGERefresh (method)
     - allowGERefresh (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getApplicationConnectionString (method)
     - getApplicationConnectionString (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getApplicationName (method)
     - getApplicationName (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getApplicationRoot (method)
     - ApplicationRoot (property)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getApplicationStatus (method); setApplicationStatus (method)
     - getApplicationStatus (method); setApplicationStatus (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - applyNewTermsProfile (method)
     - applyNewTermsProfile (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - arcCheckOut (method)
     - arcCheckOut (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - build (method)
     - build (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - buildEntireProject (method)
     - buildEntireProject (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - buildWithDependencies (method)
     - buildWithDependencies (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - canRedo (method)
     - canRedo (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - canUndo (method)
     - canUndo (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - checkIn (method)
     - checkIn (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - checkOut (method)
     - checkOut (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - clean (method)
     - clean (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - clearOutputWindow (method)
     - clearOutputWindow (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - closeAllAnimatedSequenceDiagrams (method)
     - closeAllAnimatedSequenceDiagrams (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - compareSequenceDiagram (method)
     - compareSequenceDiagram (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - setComponent (method)
     - setComponent (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - setConfiguration (method)
     - setConfiguration (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - connectToArchive (method)
     - connectToArchive (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - connectToImportedModel (method)
     - connectToImportedModel (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - connectToTarget (method)
     - connectToTarget (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - createAndInsertProject (method)
     - createAndInsertProject (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - createDomainFromProfile (method)
     - createDomainFromProfile (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getDMBoolProperty (method); setDMBoolProperty (method)
     - getDMBoolProperty (method); setDMBoolProperty (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getDMModelWorkspaceFolder (method)
     - getDMModelWorkspaceFolder (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getDMProperty (method); setDMProperty (method)
     - getDMProperty (method); setDMProperty (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - dMRefreshRecursive (method)
     - dMRefreshRecursive (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - dMSyncAndRefresh (method)
     - dMSyncAndRefresh (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - dbgCheckComIn (method)
     - dbgCheckComIn (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - dbgCheckComOut (method)
     - dbgCheckComOut (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - deferredAddToModel (method)
     - deferredAddToModel (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - deleteProjectFromList (method)
     - deleteProjectFromList (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getDiagramOfSelectedElement (method)
     - getDiagramOfSelectedElement (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - disconnectFromTarget (method)
     - disconnectFromTarget (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - downloadToTarget (method)
     - downloadToTarget (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - endUndoTransaction (method)
     - endUndoTransaction (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - enterAnimationCommand (method)
     - enterAnimationCommand (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - errorMessage (method); getErrorMessage (method)
     - errorMessage (method); getErrorMessage (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getExecutableFolder (method)
     - getExecutableFolder (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - executeCommand (method)
     - ExecuteCommand (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - executeCommandLine (method)
     - executeCommandLine (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - executeTransformationSequence (method)
     - executeTransformationSequence (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - expandStringKeywords (method)
     - expandStringKeywords (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - fixpack (method)
     - fixpack (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - forceOutput2Console (method)
     - forceOutput2Console (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - forceRoundtrip (method)
     - forceRoundtrip (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - forceRoundtripElements (method)
     - forceRoundtripElements (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - generateMainAndMakeFiles (method)
     - generateMainAndMakeFiles (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - generateWithDependencies (method)
     - generateWithDependencies (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - highLightElement (method)
     - highLightElement (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - highlightByHandle (method)
     - highlightByHandle (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - importClasses (method)
     - importClasses (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - importDesignManagerModel (method)
     - importDesignManagerModel (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - importSyncSimulinkBlock2 (method)
     - importSyncSimulinkBlock2 (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - importTlb (method)
     - importTlb (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getIniFileParameterValue (method)
     - getIniFileParameterValue (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - insertProject (method)
     - insertProject (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - insertProjectFromDesignManager (method)
     - insertProjectFromDesignManager (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getInterfaceName (method)
     - interfaceName (property)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - invokePluginsMethod (method)
     - invokePluginsMethod (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - invokeRPE (method)
     - invokeRPE (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getIsLoadOnDemand (method); setIsLoadOnDemand (method)
     - isLoadOnDemand (property)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - isRhapsodyCL (method)
     - isRhapsodyCL (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - isRhapsodyFileType (method)
     - isRhapsodyFileType (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getLanguage (method); setLanguage (method)
     - Language (property)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getListOfFactoryProperties (method)
     - getListOfFactoryProperties (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getListOfSelectedElements (method)
     - getListOfSelectedElements (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getListOfSiteProperties (method)
     - getListOfSiteProperties (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getLocaleName (method)
     - getLocaleName (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getLogRoot (method)
     - LogRoot (property)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - loginToDesignManagerWithAlias (method)
     - loginToDesignManagerWithAlias (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - loginToDesignManagerWithCertificate (method)
     - loginToDesignManagerWithCertificate (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - loginToDesignManagerWithUsername (method)
     - loginToDesignManagerWithUsername (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - make (method)
     - make (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - mergeElements (method)
     - mergeElements (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getModelElementFromSource (method)
     - getModelElementFromSource (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - newProjectOnDesignManager (method)
     - newProjectOnDesignManager (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - notifyFileChanged (method)
     - notifyFileChanged (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - openActiveXView (method)
     - OpenActiveXView (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - openAdvancedSearchAndReplaceDialog (method)
     - openAdvancedSearchAndReplaceDialog (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - openDiagramView (method)
     - OpenDiagramView (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - openFileList (method)
     - openFileList (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - openProjectFromDesignManager (method)
     - openProjectFromDesignManager (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - openProjectFromDesignManagerAfterLogin (method)
     - openProjectFromDesignManagerAfterLogin (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - openProjectFromURL (method)
     - openProjectFromURL (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - openProjectWithLastSession (method)
     - openProjectWithLastSession (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - openProjectWithoutSubUnits (method)
     - openProjectWithoutSubUnits (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getOutputWindowText (method)
     - getOutputWindowText (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - rebuild (method)
     - rebuild (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - rebuildEntireProject (method)
     - rebuildEntireProject (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - rebuildWithDependencies (method)
     - rebuildWithDependencies (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - redo (method)
     - redo (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - refactorSelectedOperation (method)
     - refactorSelectedOperation (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - refreshAllViews (method)
     - refreshAllViews (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - regenerateElements (method)
     - regenerateElements (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - regenerateEntireProject (method)
     - regenerateEntireProject (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - regenerateWithDependencies (method)
     - regenerateWithDependencies (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - registerCOMClient (method)
     - registerCOMClient (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - report (method)
     - report (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getRhapsodyHandleErrorFunction (method)
     - getRhapsodyHandleErrorFunction (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getRhapsodyHandleErrorFunctionLong (method)
     - getRhapsodyHandleErrorFunctionLong (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - rhpCheckinLicense (method)
     - RhpCheckinLicense (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - rhpCheckoutLicense (method)
     - RhpCheckoutLicense (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - roundtrip (method)
     - roundtrip (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - roundtripElements (method)
     - roundtripElements (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - runApplication (method)
     - runApplication (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - runHelper (method)
     - runHelper (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - runHelperWithParameters (method)
     - runHelperWithParameters (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - selectGraphElements (method)
     - selectGraphElements (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - selectModelElements (method)
     - selectModelElements (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getSelectedElement (method)
     - getSelectedElement (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getSelectedGraphElements (method)
     - getSelectedGraphElements (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getSerialNo (method)
     - SerialNo (property)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - startUndoTransaction (method)
     - startUndoTransaction (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - syncBuild (method)
     - syncBuild (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - terminateApplication (method)
     - terminateApplication (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getTheCodeGeneratorInterface (method)
     - getTheCodeGeneratorInterface (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getTheExternalCodeGeneratorInvoker (method)
     - getTheExternalCodeGeneratorInvoker (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getTheIntegratorInterface (method)
     - getTheIntegratorInterface (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getTheJavaPluginsInterface (method)
     - getTheJavaPluginsInterface (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getTheRoundtripInterface (method)
     - getTheRoundtripInterface (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getToolSet (method); setToolSet (method)
     - ToolSet (property)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - undo (method)
     - undo (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - unloadFromTarget (method)
     - unloadFromTarget (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - unregisterCOMClient (method)
     - unregisterCOMClient (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - setUpdateRecentFileList (method)
     - setUpdateRecentFileList (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - updateRmmDataToNewVersion (method)
     - updateRmmDataToNewVersion (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getUserDataRoot (method)
     - UserDataRoot (property)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - getUserOMROOT (method)
     - UserOMROOT (property)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - versionNumberLong (method)
     - versionNumberLong (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
   * - writeToOutputWindow (method)
     - writeToOutputWindow (method)
     - —
     - Wrapper backlog: intentionally unsupported. COM-supported but no Python wrapper; tracked in ``IRPApplication_api_report.md``.
