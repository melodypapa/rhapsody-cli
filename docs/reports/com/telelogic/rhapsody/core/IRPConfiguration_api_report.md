# Rhapsody API Validation: IRPConfiguration

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPConfiguration` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_configuration.py`)
- Members: Python `33`, Java `46`, pywin32 `31`
- Deviation items: `1` (actionable `0`, expected binding differences `1`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_path() (no static COM member); set_path() (no static COM member) | getPath (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (29) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_initial_instance() -> addInitialInstance | addInitialInstance (method) | addInitialInstance (method) | MATCH | — |
| add_package_to_instrumentation_scope() -> addPackageToInstrumentationScope | addPackageToInstrumentationScope (method) | addPackageToInstrumentationScope (method) | MATCH | — |
| add_to_instrumentation_scope() -> addToInstrumentationScope | addToInstrumentationScope (method) | addToInstrumentationScope (method) | MATCH | — |
| additional_sources (property) -> additionalSources | getAdditionalSources (method); setAdditionalSources (method) | additionalSources (property) | MATCH | — |
| all_elements_in_instrumentation_scope (property) -> allElementsInInstrumentationScope | getAllElementsInInstrumentationScope (method); setAllElementsInInstrumentationScope (method) | allElementsInInstrumentationScope (property) | MATCH | — |
| build_set (property) -> buildSet | getBuildSet (method); setBuildSet (method) | buildSet (property) | MATCH | — |
| compiler_switches (property) -> compilerSwitches | getCompilerSwitches (method); setCompilerSwitches (method) | compilerSwitches (property) | MATCH | — |
| delete_initial_instance() -> deleteInitialInstance | deleteInitialInstance (method) | deleteInitialInstance (method) | MATCH | — |
| generate_code_for_actors (property) -> generateCodeForActors | getGenerateCodeForActors (method); setGenerateCodeForActors (method) | generateCodeForActors (property) | MATCH | — |
| get_directory() -> getDirectory; set_directory() -> setDirectory | getDirectory (method); setDirectory (method) | getDirectory (method); setDirectory (method) | MATCH | — |
| get_executable_name() -> getExecutableName | getExecutableName (method) | getExecutableName (method) | MATCH | — |
| get_its_component() -> getItsComponent; set_its_component() -> setItsComponent | getItsComponent (method); setItsComponent (method) | getItsComponent (method); setItsComponent (method) | MATCH | — |
| get_main_name() -> getMainName | getMainName (method) | getMainName (method) | MATCH | — |
| get_makefile_name() -> getMakefileName | getMakefileName (method) | getMakefileName (method) | MATCH | — |
| get_target_name() -> getTargetName | getTargetName (method) | getTargetName (method) | MATCH | — |
| include_path (property) -> includePath | getIncludePath (method); setIncludePath (method) | includePath (property) | MATCH | — |
| initial_instances (property) -> initialInstances | getInitialInstances (method) | initialInstances (property) | MATCH | — |
| initialization_code (property) -> initializationCode | getInitializationCode (method); setInitializationCode (method) | initializationCode (property) | MATCH | — |
| instrumentation_scope (property) -> instrumentationScope | getInstrumentationScope (method) | instrumentationScope (property) | MATCH | — |
| instrumentation_type (property) -> instrumentationType | getInstrumentationType (method); setInstrumentationType (method) | instrumentationType (property) | MATCH | — |
| libraries (property) -> libraries | getLibraries (method); setLibraries (method) | libraries (property) | MATCH | — |
| link_switches (property) -> linkSwitches | getLinkSwitches (method); setLinkSwitches (method) | linkSwitches (property) | MATCH | — |
| needs_code_generation() -> needsCodeGeneration | needsCodeGeneration (method) | needsCodeGeneration (method) | MATCH | — |
| remove_from_instrumentation_scope() -> removeFromInstrumentationScope | removeFromInstrumentationScope (method) | removeFromInstrumentationScope (method) | MATCH | — |
| remove_package_from_instrumentation_scope() -> removePackageFromInstrumentationScope | removePackageFromInstrumentationScope (method) | removePackageFromInstrumentationScope (method) | MATCH | — |
| scope_type (property) -> scopeType | getScopeType (method); setScopeType (method) | scopeType (property) | MATCH | — |
| standard_headers (property) -> standardHeaders | getStandardHeaders (method); setStandardHeaders (method) | standardHeaders (property) | MATCH | — |
| statechart_implementation (property) -> statechartImplementation | getStatechartImplementation (method); setStatechartImplementation (method) | statechartImplementation (property) | MATCH | — |
| time_model (property) -> timeModel | getTimeModel (method); setTimeModel (method) | timeModel (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
