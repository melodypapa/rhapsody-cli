# Rhapsody API Validation: IRPProject

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPProject` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`)
- Members: Python `74`, Java `72`, pywin32 `73`
- Deviation items: `41` (actionable `33`, expected binding differences `5`, wrapper backlog `3`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_actor() -> addActor | — | addActor (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| add_class() -> addClass | — | addClass (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| add_node() -> addNode | — | addNode (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| delete_node() -> deleteNode | — | deleteNode (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| find_node() -> findNode | — | findNode (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| get_nodes() -> nodes | — | nodes (property) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| get_packages() -> packages | — | packages (property) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| gateway_export_to_xml() -> GatewayExportToXML | — | GatewayExportToXML (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: filename, params; types: str, str). Pass the documented parameters. |
| gateway_export_to_xml2() -> GatewayExportToXML2 | — | GatewayExportToXML2 (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [2] arg(s) but pywin32 declares 3 parameter(s) (3 required; params: filename, params, proj; types: str, str, com). Pass the documented parameters. |
| generate_report() -> GenerateReport | — | GenerateReport (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [2] arg(s) but pywin32 declares 6 parameter(s) (6 required; params: modelscope, templatename, docType, filename, showDocument, silentMode; types: str, str, str, str, int, int). Pass the documented parameters. |
| add_custom_view_on_diagram() -> addCustomViewOnDiagram | — | addCustomViewOnDiagram (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: diagram, customView; types: com, com). Pass the documented parameters. |
| add_spell_checker_result() -> addSpellCheckerResult | — | addSpellCheckerResult (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [2] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: value; types: str). Pass the documented parameters. |
| apply_browser_custom_views_on_diagrams() -> applyBrowserCustomViewsOnDiagrams | — | applyBrowserCustomViewsOnDiagrams (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: newVal; types: int). Pass the documented parameters. |
| apply_roundtrip_diff_merge() -> applyRoundtripDiffMerge | — | applyRoundtripDiffMerge (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 3 parameter(s) (3 required; params: magicNumber, shadowModel, filesToUpdate; types: int, com, com). Pass the documented parameters. |
| clean_unresolved_elements() -> cleanUnresolvedElements | — | cleanUnresolvedElements (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: rootElement; types: com). Pass the documented parameters. |
| close_csv_file() -> closeCSVFile | — | closeCSVFile (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: fullCSVFileName; types: str). Pass the documented parameters. |
| delete_node() -> deleteNode | — | deleteNode (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['com'] but pywin32 declares ['str']. Match the documented COM parameter types. |
| find_element_by_binary_id() -> findElementByBinaryID | — | findElementByBinaryID (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['object']. Match the documented COM parameter types. |
| find_element_by_file_name() -> findElementByFileName | — | findElementByFileName (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: theFolderName, theFileName; types: str, str). Pass the documented parameters. |
| find_elements_with_oslc_link() -> findElementsWithOSLCLink | — | findElementsWithOSLCLink (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: type, purl; types: str, str). Pass the documented parameters. |
| get_active_custom_views_on_diagram() -> getActiveCustomViewsOnDiagram | — | getActiveCustomViewsOnDiagram (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: diagram; types: com). Pass the documented parameters. |
| get_new_progress_bar() -> getNewProgressBar | — | getNewProgressBar (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: amount, name; types: int, str). Pass the documented parameters. |
| get_requirements_by_id() -> getRequirementsByID | — | getRequirementsByID (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: requirementID, returnFirstFoundOnly; types: str, int). Pass the documented parameters. |
| get_roundtrip_shadow_model() -> getRoundtripShadowModel | — | getRoundtripShadowModel (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: magicNumber; types: int). Pass the documented parameters. |
| import_package_from_rose() -> importPackageFromRose | — | importPackageFromRose (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 3 parameter(s) (3 required; params: projectName, packageName, logFileName; types: str, str, str). Pass the documented parameters. |
| import_project_from_rose() -> importProjectFromRose | — | importProjectFromRose (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: projectName, logFileName; types: str, str). Pass the documented parameters. |
| locate_in_ide() -> locateInIDE | — | locateInIDE (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 3 parameter(s) (3 required; params: config, filename, lineNumber; types: com, str, int). Pass the documented parameters. |
| reload_csv_file() -> reloadCSVFile | — | reloadCSVFile (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: fullCSVFileName; types: str). Pass the documented parameters. |
| remove_custom_view_on_diagram() -> removeCustomViewOnDiagram | — | removeCustomViewOnDiagram (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: diagram, customView; types: com, com). Pass the documented parameters. |
| save_as_prev_version() -> saveAsPrevVersion | — | saveAsPrevVersion (method) | SIGNATURE_ARITY_MISMATCH | Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: filename, prevVersion; types: str, str). Pass the documented parameters. |
| set_active_component() -> setActiveComponent | — | setActiveComponent (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['com'] but pywin32 declares ['str']. Match the documented COM parameter types. |
| set_active_configuration() -> setActiveConfiguration | — | setActiveConfiguration (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['com'] but pywin32 declares ['str']. Match the documented COM parameter types. |
| set_wait_dialog_watchdog_value() -> setWaitDialogWatchdogValue | — | setWaitDialogWatchdogValue (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['int'] but pywin32 declares ['str']. Match the documented COM parameter types. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| enable_rhapsody_model_manager() (no static COM member) | enableRhapsodyModelManager (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| set_global_configuration() (no static COM member) | setGlobalConfiguration (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | isResolveOnDemand (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |
| migrate_design_manager_links() (no static COM member) | migrateDesignManagerLinks (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| — | setResolveOnDemand (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | moveToDesignManager (method) | moveToDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | moveToDesignManagerAfterLogin (method) | moveToDesignManagerAfterLogin (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | save (method) | save (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |

<details>
<summary>Correct items (60) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_component() -> addComponent | addComponent (method) | addComponent (method) | MATCH | — |
| add_custom_view_on_browser() -> addCustomViewOnBrowser | addCustomViewOnBrowser (method) | addCustomViewOnBrowser (method) | MATCH | — |
| add_custom_view_on_diagram() -> addCustomViewOnDiagram | addCustomViewOnDiagram (method) | addCustomViewOnDiagram (method) | MATCH | — |
| add_package() -> addPackage | addPackage (method) | addPackage (method) | MATCH | — |
| add_profile() -> addProfile | addProfile (method) | addProfile (method) | MATCH | — |
| add_spell_checker_result() -> addSpellCheckerResult | addSpellCheckerResult (method) | addSpellCheckerResult (method) | MATCH | — |
| allow_auto_save() -> allowAutoSave | allowAutoSave (method) | allowAutoSave (method) | MATCH | — |
| allow_non_unique_names() -> allowNonUniqueNames | allowNonUniqueNames (method) | allowNonUniqueNames (method) | MATCH | — |
| apply_browser_custom_views_on_diagrams() -> applyBrowserCustomViewsOnDiagrams | applyBrowserCustomViewsOnDiagrams (method) | applyBrowserCustomViewsOnDiagrams (method) | MATCH | — |
| apply_roundtrip_diff_merge() -> applyRoundtripDiffMerge | applyRoundtripDiffMerge (method) | applyRoundtripDiffMerge (method) | MATCH | — |
| become_active_project() -> becomeActiveProject | becomeActiveProject (method) | becomeActiveProject (method) | MATCH | — |
| check_events_base_ids_solve_collisions() -> checkEventsBaseIdsSolveCollisions | checkEventsBaseIdsSolveCollisions (method) | checkEventsBaseIdsSolveCollisions (method) | MATCH | — |
| clean_unresolved_elements() -> cleanUnresolvedElements | cleanUnresolvedElements (method) | cleanUnresolvedElements (method) | MATCH | — |
| close() -> close | close (method) | close (method) | MATCH | — |
| close_csv_file() -> closeCSVFile | closeCSVFile (method) | closeCSVFile (method) | MATCH | — |
| delete_component() -> deleteComponent | deleteComponent (method) | deleteComponent (method) | MATCH | — |
| end_transaction_of_no_cg_interest() -> endTransactionOfNoCGInterest | endTransactionOfNoCGInterest (method) | endTransactionOfNoCGInterest (method) | MATCH | — |
| find_component() -> findComponent | findComponent (method) | findComponent (method) | MATCH | — |
| find_element_by_binary_id() -> findElementByBinaryID | findElementByBinaryID (method) | findElementByBinaryID (method) | MATCH | — |
| find_element_by_file_name() -> findElementByFileName | findElementByFileName (method) | findElementByFileName (method) | MATCH | — |
| find_element_by_guid() -> findElementByGUID | findElementByGUID (method) | findElementByGUID (method) | MATCH | — |
| find_elements_with_oslc_link() -> findElementsWithOSLCLink | findElementsWithOSLCLink (method) | findElementsWithOSLCLink (method) | MATCH | — |
| gateway_export_to_xml() -> GatewayExportToXML | gatewayExportToXML (method) | GatewayExportToXML (method) | MATCH | — |
| gateway_export_to_xml2() -> GatewayExportToXML2 | gatewayExportToXML2 (method) | GatewayExportToXML2 (method) | MATCH | — |
| generate_report() -> GenerateReport | generateReport (method) | GenerateReport (method) | MATCH | — |
| get_active_component() -> activeComponent; set_active_component() -> setActiveComponent | getActiveComponent (method); setActiveComponent (method) | activeComponent (property); setActiveComponent (method) | MATCH | — |
| get_active_configuration() -> activeConfiguration; set_active_configuration() -> setActiveConfiguration | getActiveConfiguration (method); setActiveConfiguration (method) | activeConfiguration (property); setActiveConfiguration (method) | MATCH | — |
| get_active_custom_views_on_browser() -> getActiveCustomViewsOnBrowser | getActiveCustomViewsOnBrowser (method) | getActiveCustomViewsOnBrowser (method) | MATCH | — |
| get_active_custom_views_on_diagram() -> getActiveCustomViewsOnDiagram | getActiveCustomViewsOnDiagram (method) | getActiveCustomViewsOnDiagram (method) | MATCH | — |
| get_all_stereotypes() -> allStereotypes | getAllStereotypes (method) | allStereotypes (property) | MATCH | — |
| get_cg_simplified_model_package() -> cgSimplifiedModelPackage | getCgSimplifiedModelPackage (method) | cgSimplifiedModelPackage (property) | MATCH | — |
| get_code_generated_files() -> getCodeGeneratedFiles | getCodeGeneratedFiles (method) | getCodeGeneratedFiles (method) | MATCH | — |
| get_components() -> components | getComponents (method) | components (property) | MATCH | — |
| get_default_directory_scheme() -> defaultDirectoryScheme; set_default_directory_scheme() -> defaultDirectoryScheme | getDefaultDirectoryScheme (method); setDefaultDirectoryScheme (method) | defaultDirectoryScheme (property) | MATCH | — |
| get_new_collaboration() -> getNewCollaboration | getNewCollaboration (method) | getNewCollaboration (method) | MATCH | — |
| get_new_progress_bar() -> getNewProgressBar | getNewProgressBar (method) | getNewProgressBar (method) | MATCH | — |
| get_notify_plugin_on_elements_changed() -> getNotifyPluginOnElementsChanged; set_notify_plugin_on_elements_changed() -> setNotifyPluginOnElementsChanged | getNotifyPluginOnElementsChanged (method); setNotifyPluginOnElementsChanged (method) | getNotifyPluginOnElementsChanged (method); setNotifyPluginOnElementsChanged (method) | MATCH | — |
| get_profiles() -> profiles | getProfiles (method) | profiles (property) | MATCH | — |
| get_remote_resource_packages() -> getRemoteResourcePackages | getRemoteResourcePackages (method) | getRemoteResourcePackages (method) | MATCH | — |
| get_requirements_by_id() -> getRequirementsByID | getRequirementsByID (method) | getRequirementsByID (method) | MATCH | — |
| get_roundtrip_shadow_model() -> getRoundtripShadowModel | getRoundtripShadowModel (method) | getRoundtripShadowModel (method) | MATCH | — |
| highlight_from_code() -> highlightFromCode | highlightFromCode (method) | highlightFromCode (method) | MATCH | — |
| import_package_from_rose() -> importPackageFromRose | importPackageFromRose (method) | importPackageFromRose (method) | MATCH | — |
| import_project_from_rose() -> importProjectFromRose | importProjectFromRose (method) | importProjectFromRose (method) | MATCH | — |
| is_actively_managed() -> isActivelyManaged | isActivelyManaged (method) | isActivelyManaged (method) | MATCH | — |
| is_modified_recursive() -> isModifiedRecursive | isModifiedRecursive (method) | isModifiedRecursive (method) | MATCH | — |
| locate_in_ide() -> locateInIDE | locateInIDE (method) | locateInIDE (method) | MATCH | — |
| open_csv_file() -> openCSVFile | openCSVFile (method) | openCSVFile (method) | MATCH | — |
| recalculate_events_base_ids() -> recalculateEventsBaseIds | recalculateEventsBaseIds (method) | recalculateEventsBaseIds (method) | MATCH | — |
| reload_csv_file() -> reloadCSVFile | reloadCSVFile (method) | reloadCSVFile (method) | MATCH | — |
| remove() -> remove | remove (method) | remove (method) | MATCH | — |
| remove_custom_view_on_browser() -> removeCustomViewOnBrowser | removeCustomViewOnBrowser (method) | removeCustomViewOnBrowser (method) | MATCH | — |
| remove_custom_view_on_diagram() -> removeCustomViewOnDiagram | removeCustomViewOnDiagram (method) | removeCustomViewOnDiagram (method) | MATCH | — |
| save_as() -> saveAs | saveAs (method) | saveAs (method) | MATCH | — |
| save_as_prev_version() -> saveAsPrevVersion | saveAsPrevVersion (method) | saveAsPrevVersion (method) | MATCH | — |
| set_object_explicit() -> setObjectExplicit | setObjectExplicit (method) | setObjectExplicit (method) | MATCH | — |
| set_object_implicit() -> setObjectImplicit | setObjectImplicit (method) | setObjectImplicit (method) | MATCH | — |
| set_use_unique_stereotype_and_ref_cache() -> UseUniqueStereotypeAndRefCache | setUseUniqueStereotypeAndRefCache (method) | UseUniqueStereotypeAndRefCache (property) | MATCH | — |
| set_wait_dialog_watchdog_value() -> setWaitDialogWatchdogValue | setWaitDialogWatchdogValue (method) | setWaitDialogWatchdogValue (method) | MATCH | — |
| start_transaction_of_no_cg_interest() -> startTransactionOfNoCGInterest | startTransactionOfNoCGInterest (method) | startTransactionOfNoCGInterest (method) | MATCH | — |

</details>

## AI Fix Guidance

### JAVA_DOC_MISSING (7 findings)
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Affected call(s):** add_actor() -> addActor; add_class() -> addClass; add_node() -> addNode; delete_node() -> deleteNode; find_node() -> findNode; get_nodes() -> nodes; get_packages() -> packages
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_ARITY_MISMATCH (21 findings)
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Affected call(s):** gateway_export_to_xml() -> GatewayExportToXML; gateway_export_to_xml2() -> GatewayExportToXML2; generate_report() -> GenerateReport; add_custom_view_on_diagram() -> addCustomViewOnDiagram; add_spell_checker_result() -> addSpellCheckerResult; apply_browser_custom_views_on_diagrams() -> applyBrowserCustomViewsOnDiagrams; apply_roundtrip_diff_merge() -> applyRoundtripDiffMerge; clean_unresolved_elements() -> cleanUnresolvedElements; close_csv_file() -> closeCSVFile; find_element_by_file_name() -> findElementByFileName; find_elements_with_oslc_link() -> findElementsWithOSLCLink; get_active_custom_views_on_diagram() -> getActiveCustomViewsOnDiagram; get_new_progress_bar() -> getNewProgressBar; get_requirements_by_id() -> getRequirementsByID; get_roundtrip_shadow_model() -> getRoundtripShadowModel; import_package_from_rose() -> importPackageFromRose; import_project_from_rose() -> importProjectFromRose; locate_in_ide() -> locateInIDE; reload_csv_file() -> reloadCSVFile; remove_custom_view_on_diagram() -> removeCustomViewOnDiagram; save_as_prev_version() -> saveAsPrevVersion
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: filename, params; types: str, str). Pass the documented parameters.
- **Recommended change:** Wrapper passes [2] arg(s) but pywin32 declares 3 parameter(s) (3 required; params: filename, params, proj; types: str, str, com). Pass the documented parameters.
- **Recommended change:** Wrapper passes [2] arg(s) but pywin32 declares 6 parameter(s) (6 required; params: modelscope, templatename, docType, filename, showDocument, silentMode; types: str, str, str, str, int, int). Pass the documented parameters.
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: diagram, customView; types: com, com). Pass the documented parameters.
- **Recommended change:** Wrapper passes [2] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: value; types: str). Pass the documented parameters.
- **Recommended change:** Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: newVal; types: int). Pass the documented parameters.
- **Recommended change:** Wrapper passes [0] arg(s) but pywin32 declares 3 parameter(s) (3 required; params: magicNumber, shadowModel, filesToUpdate; types: int, com, com). Pass the documented parameters.
- **Recommended change:** Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: rootElement; types: com). Pass the documented parameters.
- **Recommended change:** Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: fullCSVFileName; types: str). Pass the documented parameters.
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: theFolderName, theFileName; types: str, str). Pass the documented parameters.
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: type, purl; types: str, str). Pass the documented parameters.
- **Recommended change:** Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: diagram; types: com). Pass the documented parameters.
- **Recommended change:** Wrapper passes [0] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: amount, name; types: int, str). Pass the documented parameters.
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: requirementID, returnFirstFoundOnly; types: str, int). Pass the documented parameters.
- **Recommended change:** Wrapper passes [0] arg(s) but pywin32 declares 1 parameter(s) (1 required; params: magicNumber; types: int). Pass the documented parameters.
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 3 parameter(s) (3 required; params: projectName, packageName, logFileName; types: str, str, str). Pass the documented parameters.
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: projectName, logFileName; types: str, str). Pass the documented parameters.
- **Recommended change:** Wrapper passes [0] arg(s) but pywin32 declares 3 parameter(s) (3 required; params: config, filename, lineNumber; types: com, str, int). Pass the documented parameters.
- **Recommended change:** Wrapper passes [1] arg(s) but pywin32 declares 2 parameter(s) (2 required; params: filename, prevVersion; types: str, str). Pass the documented parameters.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (5 findings)
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Affected call(s):** delete_node() -> deleteNode; find_element_by_binary_id() -> findElementByBinaryID; set_active_component() -> setActiveComponent; set_active_configuration() -> setActiveConfiguration; set_wait_dialog_watchdog_value() -> setWaitDialogWatchdogValue
- **Recommended change:** Wrapper passes types ['com'] but pywin32 declares ['str']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['str'] but pywin32 declares ['object']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['int'] but pywin32 declares ['str']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
