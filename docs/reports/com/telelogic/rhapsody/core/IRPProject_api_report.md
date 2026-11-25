# Rhapsody API Validation: IRPProject

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPProject` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`)
- Members: Python `72`, Java `72`, pywin32 `72`
- Deviation items: `18` (actionable `13`, expected binding differences `5`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_actor() -> addActor | — | addActor (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| add_class() -> addClass | — | addClass (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| add_node() -> addNode | — | addNode (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| find_node() -> findNode | — | findNode (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| — | moveToDesignManager (method) | moveToDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| — | moveToDesignManagerAfterLogin (method) | moveToDesignManagerAfterLogin (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| nodes (property) -> nodes | — | nodes (property) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| packages (property) -> packages | — | packages (property) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| — | save (method) | save (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| find_element_by_binary_id() -> findElementByBinaryID | — | findElementByBinaryID (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str'] but pywin32 declares ['object']. Match the documented COM parameter types. |
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
| — | — | — | — | — |

<details>
<summary>Correct items (60) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| active_component (property) -> activeComponent; set_active_component() -> setActiveComponent | getActiveComponent (method); setActiveComponent (method) | activeComponent (property); setActiveComponent (method) | MATCH | — |
| active_configuration (property) -> activeConfiguration; set_active_configuration() -> setActiveConfiguration | getActiveConfiguration (method); setActiveConfiguration (method) | activeConfiguration (property); setActiveConfiguration (method) | MATCH | — |
| add_component() -> addComponent | addComponent (method) | addComponent (method) | MATCH | — |
| add_custom_view_on_browser() -> addCustomViewOnBrowser | addCustomViewOnBrowser (method) | addCustomViewOnBrowser (method) | MATCH | — |
| add_custom_view_on_diagram() -> addCustomViewOnDiagram | addCustomViewOnDiagram (method) | addCustomViewOnDiagram (method) | MATCH | — |
| add_package() -> addPackage | addPackage (method) | addPackage (method) | MATCH | — |
| add_profile() -> addProfile | addProfile (method) | addProfile (method) | MATCH | — |
| add_spell_checker_result() -> addSpellCheckerResult | addSpellCheckerResult (method) | addSpellCheckerResult (method) | MATCH | — |
| all_stereotypes (property) -> allStereotypes | getAllStereotypes (method) | allStereotypes (property) | MATCH | — |
| allow_auto_save() -> allowAutoSave | allowAutoSave (method) | allowAutoSave (method) | MATCH | — |
| allow_non_unique_names() -> allowNonUniqueNames | allowNonUniqueNames (method) | allowNonUniqueNames (method) | MATCH | — |
| apply_browser_custom_views_on_diagrams() -> applyBrowserCustomViewsOnDiagrams | applyBrowserCustomViewsOnDiagrams (method) | applyBrowserCustomViewsOnDiagrams (method) | MATCH | — |
| apply_roundtrip_diff_merge() -> applyRoundtripDiffMerge | applyRoundtripDiffMerge (method) | applyRoundtripDiffMerge (method) | MATCH | — |
| become_active_project() -> becomeActiveProject | becomeActiveProject (method) | becomeActiveProject (method) | MATCH | — |
| cg_simplified_model_package (property) -> cgSimplifiedModelPackage | getCgSimplifiedModelPackage (method) | cgSimplifiedModelPackage (property) | MATCH | — |
| check_events_base_ids_solve_collisions() -> checkEventsBaseIdsSolveCollisions | checkEventsBaseIdsSolveCollisions (method) | checkEventsBaseIdsSolveCollisions (method) | MATCH | — |
| clean_unresolved_elements() -> cleanUnresolvedElements | cleanUnresolvedElements (method) | cleanUnresolvedElements (method) | MATCH | — |
| close() -> close | close (method) | close (method) | MATCH | — |
| close_csv_file() -> closeCSVFile | closeCSVFile (method) | closeCSVFile (method) | MATCH | — |
| components (property) -> components | getComponents (method) | components (property) | MATCH | — |
| default_directory_scheme (property) -> defaultDirectoryScheme | getDefaultDirectoryScheme (method); setDefaultDirectoryScheme (method) | defaultDirectoryScheme (property) | MATCH | — |
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
| get_active_custom_views_on_browser() -> getActiveCustomViewsOnBrowser | getActiveCustomViewsOnBrowser (method) | getActiveCustomViewsOnBrowser (method) | MATCH | — |
| get_active_custom_views_on_diagram() -> getActiveCustomViewsOnDiagram | getActiveCustomViewsOnDiagram (method) | getActiveCustomViewsOnDiagram (method) | MATCH | — |
| get_code_generated_files() -> getCodeGeneratedFiles | getCodeGeneratedFiles (method) | getCodeGeneratedFiles (method) | MATCH | — |
| get_new_collaboration() -> getNewCollaboration | getNewCollaboration (method) | getNewCollaboration (method) | MATCH | — |
| get_new_progress_bar() -> getNewProgressBar | getNewProgressBar (method) | getNewProgressBar (method) | MATCH | — |
| get_notify_plugin_on_elements_changed() -> getNotifyPluginOnElementsChanged; set_notify_plugin_on_elements_changed() -> setNotifyPluginOnElementsChanged | getNotifyPluginOnElementsChanged (method); setNotifyPluginOnElementsChanged (method) | getNotifyPluginOnElementsChanged (method); setNotifyPluginOnElementsChanged (method) | MATCH | — |
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
| profiles (property) -> profiles | getProfiles (method) | profiles (property) | MATCH | — |
| recalculate_events_base_ids() -> recalculateEventsBaseIds | recalculateEventsBaseIds (method) | recalculateEventsBaseIds (method) | MATCH | — |
| reload_csv_file() -> reloadCSVFile | reloadCSVFile (method) | reloadCSVFile (method) | MATCH | — |
| remove() -> remove | remove (method) | remove (method) | MATCH | — |
| remove_custom_view_on_browser() -> removeCustomViewOnBrowser | removeCustomViewOnBrowser (method) | removeCustomViewOnBrowser (method) | MATCH | — |
| remove_custom_view_on_diagram() -> removeCustomViewOnDiagram | removeCustomViewOnDiagram (method) | removeCustomViewOnDiagram (method) | MATCH | — |
| save_as() -> saveAs | saveAs (method) | saveAs (method) | MATCH | — |
| save_as_prev_version() -> saveAsPrevVersion | saveAsPrevVersion (method) | saveAsPrevVersion (method) | MATCH | — |
| set_object_explicit() -> setObjectExplicit | setObjectExplicit (method) | setObjectExplicit (method) | MATCH | — |
| set_object_implicit() -> setObjectImplicit | setObjectImplicit (method) | setObjectImplicit (method) | MATCH | — |
| set_wait_dialog_watchdog_value() -> setWaitDialogWatchdogValue | setWaitDialogWatchdogValue (method) | setWaitDialogWatchdogValue (method) | MATCH | — |
| start_transaction_of_no_cg_interest() -> startTransactionOfNoCGInterest | startTransactionOfNoCGInterest (method) | startTransactionOfNoCGInterest (method) | MATCH | — |
| use_unique_stereotype_and_ref_cache (property) -> UseUniqueStereotypeAndRefCache | setUseUniqueStereotypeAndRefCache (method) | UseUniqueStereotypeAndRefCache (property) | MATCH | — |

</details>

## AI Fix Guidance

### JAVA_DOC_MISSING (6 findings)
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Affected call(s):** add_actor() -> addActor; add_class() -> addClass; add_node() -> addNode; find_node() -> findNode; nodes (property) -> nodes; packages (property) -> packages
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### MISSING_PYTHON_WRAPPER (3 findings)
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Affected call(s):** —; —; —
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (4 findings)
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Affected call(s):** find_element_by_binary_id() -> findElementByBinaryID; set_active_component() -> setActiveComponent; set_active_configuration() -> setActiveConfiguration; set_wait_dialog_watchdog_value() -> setWaitDialogWatchdogValue
- **Recommended change:** Wrapper passes types ['str'] but pywin32 declares ['object']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['com'] but pywin32 declares ['str']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['int'] but pywin32 declares ['str']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
