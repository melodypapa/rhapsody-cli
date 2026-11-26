# Rhapsody API Validation: IRPComponent

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPComponent` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component.py`)
- Members: Python `43`, Java `43`, pywin32 `36`
- Deviation items: `15` (actionable `14`, expected binding differences `1`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_additional_sources() -> additionalSources; set_additional_sources() -> additionalSources | getAdditionalSources (method); setAdditionalSources (method) | additionalSources (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_build_type() -> buildType; set_build_type() -> buildType | getBuildType (method); setBuildType (method) | buildType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_configurations() -> getConfigurations | getConfigurations (method) | configurations (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the configurations property or a getter/setter fallback instead of calling getConfigurations directly. |
| get_files() -> getFiles | getFiles (method) | files (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the files property or a getter/setter fallback instead of calling getFiles directly. |
| get_include_path() -> includePath; set_include_path() -> includePath | getIncludePath (method); setIncludePath (method) | includePath (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_libraries() -> libraries; set_libraries() -> libraries | getLibraries (method); setLibraries (method) | libraries (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_nested_components() -> getNestedComponents | getNestedComponents (method) | nestedComponents (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the nestedComponents property or a getter/setter fallback instead of calling getNestedComponents directly. |
| get_panel_diagrams() -> getPanelDiagrams | getPanelDiagrams (method) | panelDiagrams (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the panelDiagrams property or a getter/setter fallback instead of calling getPanelDiagrams directly. |
| get_scope_by_selected_elements() -> getScopeBySelectedElements; set_scope_by_selected_elements() -> setScopeBySelectedElements | getScopeBySelectedElements (method); setScopeBySelectedElements (method) | scopeBySelectedElements (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the scopeBySelectedElements property or a getter/setter fallback instead of calling getScopeBySelectedElements and setScopeBySelectedElements directly. |
| get_scope_elements() -> getScopeElements | getScopeElements (method) | scopeElements (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the scopeElements property or a getter/setter fallback instead of calling getScopeElements directly. |
| get_standard_headers() -> standardHeaders; set_standard_headers() -> standardHeaders | getStandardHeaders (method); setStandardHeaders (method) | standardHeaders (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer | updateContainedDiagramsOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_variation_points() -> getVariationPoints | getVariationPoints (method) | variationPoints (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the variationPoints property or a getter/setter fallback instead of calling getVariationPoints directly. |
| delete_configuration() -> deleteConfiguration | — | deleteConfiguration (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (21) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_configuration() -> addConfiguration | addConfiguration (method) | addConfiguration (method) | MATCH | — |
| add_file() -> addFile | addFile (method) | addFile (method) | MATCH | — |
| add_folder() -> addFolder | addFolder (method) | addFolder (method) | MATCH | — |
| add_nested_component() -> addNestedComponent | addNestedComponent (method) | addNestedComponent (method) | MATCH | — |
| add_scope_element() -> addScopeElement | addScopeElement (method) | addScopeElement (method) | MATCH | — |
| add_scope_element_without_aggregates() -> addScopeElementWithoutAggregates | addScopeElementWithoutAggregates (method) | addScopeElementWithoutAggregates (method) | MATCH | — |
| add_to_scope() -> addToScope | addToScope (method) | addToScope (method) | MATCH | — |
| all_elements_in_scope() -> allElementsInScope | allElementsInScope (method) | allElementsInScope (method) | MATCH | — |
| get_config_by_dependency() -> getConfigByDependency | getConfigByDependency (method) | getConfigByDependency (method) | MATCH | — |
| delete_configuration() -> deleteConfiguration | deleteConfiguration (method) | deleteConfiguration (method) | MATCH | — |
| delete_file() -> deleteFile | deleteFile (method) | deleteFile (method) | MATCH | — |
| get_file() -> getFile | getFile (method) | getFile (method) | MATCH | — |
| get_file_name() -> getFileName | getFileName (method) | getFileName (method) | MATCH | — |
| find_configuration() -> findConfiguration | findConfiguration (method) | findConfiguration (method) | MATCH | — |
| is_directory_per_model_component() -> isDirectoryPerModelComponent | isDirectoryPerModelComponent (method) | isDirectoryPerModelComponent (method) | MATCH | — |
| get_model_element_file_name() -> getModelElementFileName | getModelElementFileName (method) | getModelElementFileName (method) | MATCH | — |
| get_package_file() -> getPackageFile | getPackageFile (method) | getPackageFile (method) | MATCH | — |
| get_possible_variants() -> getPossibleVariants | getPossibleVariants (method) | getPossibleVariants (method) | MATCH | — |
| remove_scope_element() -> removeScopeElement | removeScopeElement (method) | removeScopeElement (method) | MATCH | — |
| get_scope_elements_by_category() -> getScopeElementsByCategory | getScopeElementsByCategory (method) | getScopeElementsByCategory (method) | MATCH | — |
| get_variant() -> getVariant; set_variant() -> setVariant | getVariant (method); setVariant (method) | getVariant (method); setVariant (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (5 findings)
- **Target:** `IRPComponent` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component.py`
- **Affected call(s):** get_additional_sources() -> additionalSources; set_additional_sources() -> additionalSources; get_build_type() -> buildType; set_build_type() -> buildType; get_include_path() -> includePath; set_include_path() -> includePath; get_libraries() -> libraries; set_libraries() -> libraries; get_standard_headers() -> standardHeaders; set_standard_headers() -> standardHeaders
- **Java signature(s):** `IRPComponent.getAdditionalSources()`, `IRPComponent.setStandardHeaders(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (7 findings)
- **Target:** `IRPComponent` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component.py`
- **Affected call(s):** get_configurations() -> getConfigurations; get_files() -> getFiles; get_nested_components() -> getNestedComponents; get_panel_diagrams() -> getPanelDiagrams; get_scope_by_selected_elements() -> getScopeBySelectedElements; set_scope_by_selected_elements() -> setScopeBySelectedElements; get_scope_elements() -> getScopeElements; get_variation_points() -> getVariationPoints
- **Recommended change:** Use the configurations property or a getter/setter fallback instead of calling getConfigurations directly.
- **Recommended change:** Use the files property or a getter/setter fallback instead of calling getFiles directly.
- **Recommended change:** Use the nestedComponents property or a getter/setter fallback instead of calling getNestedComponents directly.
- **Recommended change:** Use the panelDiagrams property or a getter/setter fallback instead of calling getPanelDiagrams directly.
- **Recommended change:** Use the scopeBySelectedElements property or a getter/setter fallback instead of calling getScopeBySelectedElements and setScopeBySelectedElements directly.
- **Recommended change:** Use the scopeElements property or a getter/setter fallback instead of calling getScopeElements directly.
- **Recommended change:** Use the variationPoints property or a getter/setter fallback instead of calling getVariationPoints directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### PYWIN32_MEMBER_MISSING (1 finding)
- **Target:** `IRPComponent` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component.py`
- **Affected call(s):** update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer
- **Java signature(s):** `IRPComponent.updateContainedDiagramsOnServer(int)`
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPComponent` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component.py`
- **Affected call(s):** delete_configuration() -> deleteConfiguration
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
