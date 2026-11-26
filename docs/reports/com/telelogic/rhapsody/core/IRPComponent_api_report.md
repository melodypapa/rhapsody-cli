# Rhapsody API Validation: IRPComponent

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPComponent` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component.py`)
- Members: Python `37`, Java `43`, pywin32 `34`
- Deviation items: `2` (actionable `0`, expected binding differences `2`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_path() (no static COM member); set_path() (no static COM member) | getPath (method); setPath (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| update_contained_diagrams_on_server() (no static COM member) | updateContainedDiagramsOnServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (33) — bindings verified against pywin32</summary>


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
| additional_sources (property) -> additionalSources | getAdditionalSources (method); setAdditionalSources (method) | additionalSources (property) | MATCH | — |
| all_elements_in_scope() -> allElementsInScope | allElementsInScope (method) | allElementsInScope (method) | MATCH | — |
| build_type (property) -> buildType | getBuildType (method); setBuildType (method) | buildType (property) | MATCH | — |
| configurations (property) -> configurations | getConfigurations (method) | configurations (property) | MATCH | — |
| delete_configuration() -> deleteConfiguration | deleteConfiguration (method) | deleteConfiguration (method) | MATCH | — |
| delete_file() -> deleteFile | deleteFile (method) | deleteFile (method) | MATCH | — |
| files (property) -> files | getFiles (method) | files (property) | MATCH | — |
| find_configuration() -> findConfiguration | findConfiguration (method) | findConfiguration (method) | MATCH | — |
| get_config_by_dependency() -> getConfigByDependency | getConfigByDependency (method) | getConfigByDependency (method) | MATCH | — |
| get_file() -> getFile | getFile (method) | getFile (method) | MATCH | — |
| get_file_name() -> getFileName | getFileName (method) | getFileName (method) | MATCH | — |
| get_model_element_file_name() -> getModelElementFileName | getModelElementFileName (method) | getModelElementFileName (method) | MATCH | — |
| get_package_file() -> getPackageFile | getPackageFile (method) | getPackageFile (method) | MATCH | — |
| get_possible_variants() -> getPossibleVariants | getPossibleVariants (method) | getPossibleVariants (method) | MATCH | — |
| get_scope_elements_by_category() -> getScopeElementsByCategory | getScopeElementsByCategory (method) | getScopeElementsByCategory (method) | MATCH | — |
| get_variant() -> getVariant; set_variant() -> setVariant | getVariant (method); setVariant (method) | getVariant (method); setVariant (method) | MATCH | — |
| include_path (property) -> includePath | getIncludePath (method); setIncludePath (method) | includePath (property) | MATCH | — |
| is_directory_per_model_component() -> isDirectoryPerModelComponent | isDirectoryPerModelComponent (method) | isDirectoryPerModelComponent (method) | MATCH | — |
| libraries (property) -> libraries | getLibraries (method); setLibraries (method) | libraries (property) | MATCH | — |
| nested_components (property) -> nestedComponents | getNestedComponents (method) | nestedComponents (property) | MATCH | — |
| panel_diagrams (property) -> panelDiagrams | getPanelDiagrams (method) | panelDiagrams (property) | MATCH | — |
| remove_scope_element() -> removeScopeElement | removeScopeElement (method) | removeScopeElement (method) | MATCH | — |
| scope_by_selected_elements (property) -> scopeBySelectedElements | getScopeBySelectedElements (method); setScopeBySelectedElements (method) | scopeBySelectedElements (property) | MATCH | — |
| scope_elements (property) -> scopeElements | getScopeElements (method) | scopeElements (property) | MATCH | — |
| standard_headers (property) -> standardHeaders | getStandardHeaders (method); setStandardHeaders (method) | standardHeaders (property) | MATCH | — |
| variation_points (property) -> variationPoints | getVariationPoints (method) | variationPoints (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
