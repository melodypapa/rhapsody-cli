# Rhapsody API Validation: IRPProject

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPProject` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`)
- Members: Python `74`, Java `70`, pywin32 `73`
- Deviations: `11`
- Deviations by status:
  - `COM_MEMBER_NOT_EXPOSED`: 4
  - `JAVA_DOC_MISSING`: 7

- Informational binding differences (expected): `3`
- Wrapper backlog (supported members without wrappers): `3`
- Documented aliases: `0`, documented unavailable: `3`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_actor() -> addActor | — | addActor (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| add_class() -> addClass | — | addClass (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| add_node() -> addNode | — | addNode (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| delete_node() -> deleteNode | — | deleteNode (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| find_node() -> findNode | — | findNode (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| gateway_export_to_xml() -> gatewayExportToXML | gatewayExportToXML (method) | GatewayExportToXML (method) | COM_MEMBER_NOT_EXPOSED | Change the COM call to a member exposed by the registered pywin32 interface. |
| gateway_export_to_xml2() -> gatewayExportToXML2 | gatewayExportToXML2 (method) | GatewayExportToXML2 (method) | COM_MEMBER_NOT_EXPOSED | Change the COM call to a member exposed by the registered pywin32 interface. |
| generate_report() -> generateReport | generateReport (method) | GenerateReport (method) | COM_MEMBER_NOT_EXPOSED | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_nodes() -> nodes | — | nodes (property) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| get_packages() -> packages | — | packages (property) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| set_use_unique_stereotype_and_ref_cache() -> setUseUniqueStereotypeAndRefCache; set_use_unique_stereotype_and_ref_cache() -> useUniqueStereotypeAndRefCache | setUseUniqueStereotypeAndRefCache (method) | UseUniqueStereotypeAndRefCache (property) | COM_MEMBER_NOT_EXPOSED | Use the UseUniqueStereotypeAndRefCache property or a getter/setter fallback instead of calling setUseUniqueStereotypeAndRefCache and useUniqueStereotypeAndRefCache directly. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| enable_rhapsody_model_manager() (no static COM member) | enableRhapsodyModelManager (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| set_global_configuration() (no static COM member) | setGlobalConfiguration (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| migrate_design_manager_links() (no static COM member) | migrateDesignManagerLinks (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | moveToDesignManager (method) | moveToDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | moveToDesignManagerAfterLogin (method) | moveToDesignManagerAfterLogin (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | save (method) | save (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |

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
| set_wait_dialog_watchdog_value() -> setWaitDialogWatchdogValue | setWaitDialogWatchdogValue (method) | setWaitDialogWatchdogValue (method) | MATCH | — |
| start_transaction_of_no_cg_interest() -> startTransactionOfNoCGInterest | startTransactionOfNoCGInterest (method) | startTransactionOfNoCGInterest (method) | MATCH | — |

## AI Fix Guidance

### Finding 1: JAVA_DOC_MISSING
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** add_actor() -> addActor
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** addActor (method)
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: JAVA_DOC_MISSING
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** add_class() -> addClass
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** addClass (method)
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 3: JAVA_DOC_MISSING
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** add_node() -> addNode
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** addNode (method)
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 4: JAVA_DOC_MISSING
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** delete_node() -> deleteNode
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** deleteNode (method)
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 5: JAVA_DOC_MISSING
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** find_node() -> findNode
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** findNode (method)
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 6: COM_MEMBER_NOT_EXPOSED
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** gateway_export_to_xml() -> gatewayExportToXML
- **Expected Python method(s):** `gateway_export_to_xml`
- **Java signature(s):** `IRPProject.gatewayExportToXML(java.lang.String, java.lang.String)`
- **pywin32 member(s):** GatewayExportToXML (method)
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 7: COM_MEMBER_NOT_EXPOSED
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** gateway_export_to_xml2() -> gatewayExportToXML2
- **Expected Python method(s):** `gateway_export_to_xml2`
- **Java signature(s):** `IRPProject.gatewayExportToXML2(java.lang.String, java.lang.String, com.telelogic.rhapsody.core.IRPProject)`
- **pywin32 member(s):** GatewayExportToXML2 (method)
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 8: COM_MEMBER_NOT_EXPOSED
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** generate_report() -> generateReport
- **Expected Python method(s):** `generate_report`
- **Java signature(s):** `IRPProject.generateReport(java.lang.String, java.lang.String, java.lang.String, java.lang.String, int, int)`
- **pywin32 member(s):** GenerateReport (method)
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 9: JAVA_DOC_MISSING
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** get_nodes() -> nodes
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** nodes (property)
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 10: JAVA_DOC_MISSING
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** get_packages() -> packages
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** packages (property)
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 11: COM_MEMBER_NOT_EXPOSED
- **Target:** `IRPProject` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_project.py`
- **Current Python wrapper/COM call:** set_use_unique_stereotype_and_ref_cache() -> setUseUniqueStereotypeAndRefCache; set_use_unique_stereotype_and_ref_cache() -> useUniqueStereotypeAndRefCache
- **Expected Python method(s):** `set_use_unique_stereotype_and_ref_cache`
- **Java signature(s):** `IRPProject.setUseUniqueStereotypeAndRefCache(int)`
- **pywin32 member(s):** UseUniqueStereotypeAndRefCache (property)
- **Recommended change:** Use the UseUniqueStereotypeAndRefCache property or a getter/setter fallback instead of calling setUseUniqueStereotypeAndRefCache and useUniqueStereotypeAndRefCache directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
