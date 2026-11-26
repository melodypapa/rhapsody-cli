# Rhapsody API Validation: IRPConfiguration

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPConfiguration` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_configuration.py`)
- Members: Python `46`, Java `46`, pywin32 `32`
- Deviation items: `20` (actionable `19`, expected binding differences `1`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_additional_sources() -> additionalSources; set_additional_sources() -> additionalSources | getAdditionalSources (method); setAdditionalSources (method) | additionalSources (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_all_elements_in_instrumentation_scope() -> getAllElementsInInstrumentationScope; set_all_elements_in_instrumentation_scope() -> setAllElementsInInstrumentationScope | getAllElementsInInstrumentationScope (method); setAllElementsInInstrumentationScope (method) | allElementsInInstrumentationScope (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the allElementsInInstrumentationScope property or a getter/setter fallback instead of calling getAllElementsInInstrumentationScope and setAllElementsInInstrumentationScope directly. |
| get_build_set() -> buildSet; set_build_set() -> buildSet | getBuildSet (method); setBuildSet (method) | buildSet (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_compiler_switches() -> compilerSwitches; set_compiler_switches() -> compilerSwitches | getCompilerSwitches (method); setCompilerSwitches (method) | compilerSwitches (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_generate_code_for_actors() -> getGenerateCodeForActors; set_generate_code_for_actors() -> setGenerateCodeForActors | getGenerateCodeForActors (method); setGenerateCodeForActors (method) | generateCodeForActors (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the generateCodeForActors property or a getter/setter fallback instead of calling getGenerateCodeForActors and setGenerateCodeForActors directly. |
| get_include_path() -> includePath; set_include_path() -> includePath | getIncludePath (method); setIncludePath (method) | includePath (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_initial_instances() -> getInitialInstances | getInitialInstances (method) | initialInstances (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the initialInstances property or a getter/setter fallback instead of calling getInitialInstances directly. |
| get_initialization_code() -> initializationCode; set_initialization_code() -> initializationCode | getInitializationCode (method); setInitializationCode (method) | initializationCode (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_instrumentation_scope() -> getInstrumentationScope | getInstrumentationScope (method) | instrumentationScope (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the instrumentationScope property or a getter/setter fallback instead of calling getInstrumentationScope directly. |
| get_instrumentation_type() -> getInstrumentationType; set_instrumentation_type() -> setInstrumentationType | getInstrumentationType (method); setInstrumentationType (method) | instrumentationType (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the instrumentationType property or a getter/setter fallback instead of calling getInstrumentationType and setInstrumentationType directly. |
| get_libraries() -> libraries; set_libraries() -> libraries | getLibraries (method); setLibraries (method) | libraries (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_link_switches() -> linkSwitches; set_link_switches() -> linkSwitches | getLinkSwitches (method); setLinkSwitches (method) | linkSwitches (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_scope_type() -> getScopeType; set_scope_type() -> setScopeType | getScopeType (method); setScopeType (method) | scopeType (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the scopeType property or a getter/setter fallback instead of calling getScopeType and setScopeType directly. |
| get_standard_headers() -> standardHeaders; set_standard_headers() -> standardHeaders | getStandardHeaders (method); setStandardHeaders (method) | standardHeaders (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_statechart_implementation() -> getStatechartImplementation; set_statechart_implementation() -> setStatechartImplementation | getStatechartImplementation (method); setStatechartImplementation (method) | statechartImplementation (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the statechartImplementation property or a getter/setter fallback instead of calling getStatechartImplementation and setStatechartImplementation directly. |
| get_time_model() -> getTimeModel; set_time_model() -> setTimeModel | getTimeModel (method); setTimeModel (method) | timeModel (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the timeModel property or a getter/setter fallback instead of calling getTimeModel and setTimeModel directly. |
| add_initial_instance() -> addInitialInstance | — | addInitialInstance (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| delete_initial_instance() -> deleteInitialInstance | — | deleteInitialInstance (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| set_its_component() -> setItsComponent | — | setItsComponent (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (13) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_initial_instance() -> addInitialInstance | addInitialInstance (method) | addInitialInstance (method) | MATCH | — |
| add_package_to_instrumentation_scope() -> addPackageToInstrumentationScope | addPackageToInstrumentationScope (method) | addPackageToInstrumentationScope (method) | MATCH | — |
| add_to_instrumentation_scope() -> addToInstrumentationScope | addToInstrumentationScope (method) | addToInstrumentationScope (method) | MATCH | — |
| delete_initial_instance() -> deleteInitialInstance | deleteInitialInstance (method) | deleteInitialInstance (method) | MATCH | — |
| get_directory() -> getDirectory; set_directory() -> setDirectory | getDirectory (method); setDirectory (method) | getDirectory (method); setDirectory (method) | MATCH | — |
| get_executable_name() -> getExecutableName | getExecutableName (method) | getExecutableName (method) | MATCH | — |
| get_its_component() -> getItsComponent; set_its_component() -> setItsComponent | getItsComponent (method); setItsComponent (method) | getItsComponent (method); setItsComponent (method) | MATCH | — |
| get_main_name() -> getMainName | getMainName (method) | getMainName (method) | MATCH | — |
| get_makefile_name() -> getMakefileName | getMakefileName (method) | getMakefileName (method) | MATCH | — |
| needs_code_generation() -> needsCodeGeneration | needsCodeGeneration (method) | needsCodeGeneration (method) | MATCH | — |
| remove_from_instrumentation_scope() -> removeFromInstrumentationScope | removeFromInstrumentationScope (method) | removeFromInstrumentationScope (method) | MATCH | — |
| remove_package_from_instrumentation_scope() -> removePackageFromInstrumentationScope | removePackageFromInstrumentationScope (method) | removePackageFromInstrumentationScope (method) | MATCH | — |
| get_target_name() -> getTargetName | getTargetName (method) | getTargetName (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (8 findings)
- **Target:** `IRPConfiguration` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_configuration.py`
- **Affected call(s):** get_additional_sources() -> additionalSources; set_additional_sources() -> additionalSources; get_build_set() -> buildSet; set_build_set() -> buildSet; get_compiler_switches() -> compilerSwitches; set_compiler_switches() -> compilerSwitches; get_include_path() -> includePath; set_include_path() -> includePath; get_initialization_code() -> initializationCode; set_initialization_code() -> initializationCode; get_libraries() -> libraries; set_libraries() -> libraries; get_link_switches() -> linkSwitches; set_link_switches() -> linkSwitches; get_standard_headers() -> standardHeaders; set_standard_headers() -> standardHeaders
- **Java signature(s):** `IRPConfiguration.getAdditionalSources()`, `IRPConfiguration.setStandardHeaders(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (8 findings)
- **Target:** `IRPConfiguration` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_configuration.py`
- **Affected call(s):** get_all_elements_in_instrumentation_scope() -> getAllElementsInInstrumentationScope; set_all_elements_in_instrumentation_scope() -> setAllElementsInInstrumentationScope; get_generate_code_for_actors() -> getGenerateCodeForActors; set_generate_code_for_actors() -> setGenerateCodeForActors; get_initial_instances() -> getInitialInstances; get_instrumentation_scope() -> getInstrumentationScope; get_instrumentation_type() -> getInstrumentationType; set_instrumentation_type() -> setInstrumentationType; get_scope_type() -> getScopeType; set_scope_type() -> setScopeType; get_statechart_implementation() -> getStatechartImplementation; set_statechart_implementation() -> setStatechartImplementation; get_time_model() -> getTimeModel; set_time_model() -> setTimeModel
- **Java signature(s):** `IRPConfiguration.getAllElementsInInstrumentationScope()`, `IRPConfiguration.setTimeModel(java.lang.String)`
- **Recommended change:** Use the allElementsInInstrumentationScope property or a getter/setter fallback instead of calling getAllElementsInInstrumentationScope and setAllElementsInInstrumentationScope directly.
- **Recommended change:** Use the generateCodeForActors property or a getter/setter fallback instead of calling getGenerateCodeForActors and setGenerateCodeForActors directly.
- **Recommended change:** Use the initialInstances property or a getter/setter fallback instead of calling getInitialInstances directly.
- **Recommended change:** Use the instrumentationScope property or a getter/setter fallback instead of calling getInstrumentationScope directly.
- **Recommended change:** Use the instrumentationType property or a getter/setter fallback instead of calling getInstrumentationType and setInstrumentationType directly.
- **Recommended change:** Use the scopeType property or a getter/setter fallback instead of calling getScopeType and setScopeType directly.
- **Recommended change:** Use the statechartImplementation property or a getter/setter fallback instead of calling getStatechartImplementation and setStatechartImplementation directly.
- **Recommended change:** Use the timeModel property or a getter/setter fallback instead of calling getTimeModel and setTimeModel directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (3 findings)
- **Target:** `IRPConfiguration` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_configuration.py`
- **Affected call(s):** add_initial_instance() -> addInitialInstance; delete_initial_instance() -> deleteInitialInstance; set_its_component() -> setItsComponent
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
