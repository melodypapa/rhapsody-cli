# Rhapsody API Validation: IRPPackage

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPPackage` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py`)
- Members: Python `101`, Java `100`, pywin32 `94`
- Deviations: `5`
- Deviations by status:
  - `JAVA_DOC_MISSING`: 1
  - `PYTHON_METHOD_NAME_MISMATCH`: 4

- Informational binding differences (expected): `6`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `6`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_association() -> addAssociation | — | addAssociation (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |
| add_statechart_diagram() -> addStatechart | addStatechart (method) | addStatechart (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_nested_packages() -> packages | getPackages (method) | packages (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| recalculate_events_base_id() -> reCalculateEventsBaseId | reCalculateEventsBaseId (method) | reCalculateEventsBaseId (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> savedInSeperateDirectory | getSavedInSeperateDirectory (method); setSavedInSeperateDirectory (method) | savedInSeperateDirectory (property) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_instance_specification() (no static COM member) | addInstanceSpecification (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| login_to_remote_artifact_server() (no static COM member) | loginToRemoteArtifactServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| get_root_instance_specifications() (no static COM member) | getRootInstanceSpecifications (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| update_contained_diagrams_on_server() (no static COM member) | updateContainedDiagramsOnServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| update_contained_matrices_on_server() (no static COM member) | updateContainedMatricesOnServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| update_contained_tables_on_server() (no static COM member) | updateContainedTablesOnServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_activity_diagram() -> addActivityDiagram | addActivityDiagram (method) | addActivityDiagram (method) | MATCH | — |
| add_actor() -> addActor | addActor (method) | addActor (method) | MATCH | — |
| add_class() -> addClass | addClass (method) | addClass (method) | MATCH | — |
| add_collaboration_diagram() -> addCollaborationDiagram | addCollaborationDiagram (method) | addCollaborationDiagram (method) | MATCH | — |
| add_component_diagram() -> addComponentDiagram | addComponentDiagram (method) | addComponentDiagram (method) | MATCH | — |
| add_deployment_diagram() -> addDeploymentDiagram | addDeploymentDiagram (method) | addDeploymentDiagram (method) | MATCH | — |
| add_event() -> addEvent | addEvent (method) | addEvent (method) | MATCH | — |
| add_flow_items() -> addFlowItems | addFlowItems (method) | addFlowItems (method) | MATCH | — |
| add_flows() -> addFlows | addFlows (method) | addFlows (method) | MATCH | — |
| add_global_function() -> addGlobalFunction | addGlobalFunction (method) | addGlobalFunction (method) | MATCH | — |
| add_global_object() -> addGlobalObject | addGlobalObject (method) | addGlobalObject (method) | MATCH | — |
| add_global_variable() -> addGlobalVariable | addGlobalVariable (method) | addGlobalVariable (method) | MATCH | — |
| add_implicit_object() -> addImplicitObject | addImplicitObject (method) | addImplicitObject (method) | MATCH | — |
| add_link() -> addLink | addLink (method) | addLink (method) | MATCH | — |
| add_link_between_sysml_ports() -> addLinkBetweenSYSMLPorts | addLinkBetweenSYSMLPorts (method) | addLinkBetweenSYSMLPorts (method) | MATCH | — |
| add_module() -> addModule | addModule (method) | addModule (method) | MATCH | — |
| add_nested_package() -> addNestedPackage | addNestedPackage (method) | addNestedPackage (method) | MATCH | — |
| add_node() -> addNode | addNode (method) | addNode (method) | MATCH | — |
| add_object_model_diagram() -> addObjectModelDiagram | addObjectModelDiagram (method) | addObjectModelDiagram (method) | MATCH | — |
| add_panel_diagram() -> addPanelDiagram | addPanelDiagram (method) | addPanelDiagram (method) | MATCH | — |
| add_sequence_diagram() -> addSequenceDiagram | addSequenceDiagram (method) | addSequenceDiagram (method) | MATCH | — |
| add_timing_diagram() -> addTimingDiagram | addTimingDiagram (method) | addTimingDiagram (method) | MATCH | — |
| add_type() -> addType | addType (method) | addType (method) | MATCH | — |
| add_use_case() -> addUseCase | addUseCase (method) | addUseCase (method) | MATCH | — |
| add_use_case_diagram() -> addUseCaseDiagram | addUseCaseDiagram (method) | addUseCaseDiagram (method) | MATCH | — |
| delete_actor() -> deleteActor | deleteActor (method) | deleteActor (method) | MATCH | — |
| delete_class() -> deleteClass | deleteClass (method) | deleteClass (method) | MATCH | — |
| delete_collaboration_diagram() -> deleteCollaborationDiagram | deleteCollaborationDiagram (method) | deleteCollaborationDiagram (method) | MATCH | — |
| delete_component_diagram() -> deleteComponentDiagram | deleteComponentDiagram (method) | deleteComponentDiagram (method) | MATCH | — |
| delete_deployment_diagram() -> deleteDeploymentDiagram | deleteDeploymentDiagram (method) | deleteDeploymentDiagram (method) | MATCH | — |
| delete_event() -> deleteEvent | deleteEvent (method) | deleteEvent (method) | MATCH | — |
| delete_flow_items() -> deleteFlowItems | deleteFlowItems (method) | deleteFlowItems (method) | MATCH | — |
| delete_flows() -> deleteFlows | deleteFlows (method) | deleteFlows (method) | MATCH | — |
| delete_global_function() -> deleteGlobalFunction | deleteGlobalFunction (method) | deleteGlobalFunction (method) | MATCH | — |
| delete_global_object() -> deleteGlobalObject | deleteGlobalObject (method) | deleteGlobalObject (method) | MATCH | — |
| delete_global_variable() -> deleteGlobalVariable | deleteGlobalVariable (method) | deleteGlobalVariable (method) | MATCH | — |
| delete_node() -> deleteNode | deleteNode (method) | deleteNode (method) | MATCH | — |
| delete_object_model_diagram() -> deleteObjectModelDiagram | deleteObjectModelDiagram (method) | deleteObjectModelDiagram (method) | MATCH | — |
| delete_package() -> deletePackage | deletePackage (method) | deletePackage (method) | MATCH | — |
| delete_panel_diagram() -> deletePanelDiagram | deletePanelDiagram (method) | deletePanelDiagram (method) | MATCH | — |
| delete_sequence_diagram() -> deleteSequenceDiagram | deleteSequenceDiagram (method) | deleteSequenceDiagram (method) | MATCH | — |
| delete_timing_diagram() -> deleteTimingDiagram | deleteTimingDiagram (method) | deleteTimingDiagram (method) | MATCH | — |
| delete_type() -> deleteType | deleteType (method) | deleteType (method) | MATCH | — |
| delete_use_case() -> deleteUseCase | deleteUseCase (method) | deleteUseCase (method) | MATCH | — |
| delete_use_case_diagram() -> deleteUseCaseDiagram | deleteUseCaseDiagram (method) | deleteUseCaseDiagram (method) | MATCH | — |
| find_actor() -> findActor | findActor (method) | findActor (method) | MATCH | — |
| find_all_by_name() -> findAllByName | findAllByName (method) | findAllByName (method) | MATCH | — |
| find_class() -> findClass | findClass (method) | findClass (method) | MATCH | — |
| find_event() -> findEvent | findEvent (method) | findEvent (method) | MATCH | — |
| find_global_function() -> findGlobalFunction | findGlobalFunction (method) | findGlobalFunction (method) | MATCH | — |
| find_global_object() -> findGlobalObject | findGlobalObject (method) | findGlobalObject (method) | MATCH | — |
| find_global_variable() -> findGlobalVariable | findGlobalVariable (method) | findGlobalVariable (method) | MATCH | — |
| find_node() -> findNode | findNode (method) | findNode (method) | MATCH | — |
| find_type() -> findType | findType (method) | findType (method) | MATCH | — |
| find_usage() -> findUsage | findUsage (method) | findUsage (method) | MATCH | — |
| find_use_case() -> findUseCase | findUseCase (method) | findUseCase (method) | MATCH | — |
| get_actors() -> actors | getActors (method) | actors (property) | MATCH | — |
| get_all_nested_elements() -> getAllNestedElements | getAllNestedElements (method) | getAllNestedElements (method) | MATCH | — |
| get_behavioral_diagrams() -> behavioralDiagrams | getBehavioralDiagrams (method) | behavioralDiagrams (property) | MATCH | — |
| get_classes() -> classes | getClasses (method) | classes (property) | MATCH | — |
| get_collaboration_diagrams() -> collaborationDiagrams | getCollaborationDiagrams (method) | collaborationDiagrams (property) | MATCH | — |
| get_component_diagrams() -> componentDiagrams | getComponentDiagrams (method) | componentDiagrams (property) | MATCH | — |
| get_deployment_diagrams() -> deploymentDiagrams | getDeploymentDiagrams (method) | deploymentDiagrams (property) | MATCH | — |
| get_events() -> events | getEvents (method) | events (property) | MATCH | — |
| get_events_base_id() -> eventsBaseId | getEventsBaseId (method) | eventsBaseId (property) | MATCH | — |
| get_flow_items() -> flowItems | getFlowItems (method) | flowItems (property) | MATCH | — |
| get_flows() -> flows | getFlows (method) | flows (property) | MATCH | — |
| get_global_functions() -> globalFunctions | getGlobalFunctions (method) | globalFunctions (property) | MATCH | — |
| get_global_objects() -> globalObjects | getGlobalObjects (method) | globalObjects (property) | MATCH | — |
| get_global_variables() -> globalVariables | getGlobalVariables (method) | globalVariables (property) | MATCH | — |
| get_instance_specifications() -> instanceSpecifications | getInstanceSpecifications (method) | instanceSpecifications (property) | MATCH | — |
| get_links() -> links | getLinks (method) | links (property) | MATCH | — |
| get_modules() -> modules | getModules (method) | modules (property) | MATCH | — |
| get_namespace() -> getNamespace | getNamespace (method) | getNamespace (method) | MATCH | — |
| get_nested_classifiers() -> nestedClassifiers | getNestedClassifiers (method) | nestedClassifiers (property) | MATCH | — |
| get_nested_components() -> nestedComponents | getNestedComponents (method) | nestedComponents (property) | MATCH | — |
| get_nodes() -> nodes | getNodes (method) | nodes (property) | MATCH | — |
| get_object_model_diagrams() -> objectModelDiagrams | getObjectModelDiagrams (method) | objectModelDiagrams (property) | MATCH | — |
| get_panel_diagrams() -> panelDiagrams | getPanelDiagrams (method) | panelDiagrams (property) | MATCH | — |
| get_remote_requirements_populate_mode() -> getRemoteRequirementsPopulateMode; set_remote_requirements_populate_mode() -> setRemoteRequirementsPopulateMode | getRemoteRequirementsPopulateMode (method); setRemoteRequirementsPopulateMode (method) | getRemoteRequirementsPopulateMode (method); setRemoteRequirementsPopulateMode (method) | MATCH | — |
| get_sequence_diagrams() -> sequenceDiagrams | getSequenceDiagrams (method) | sequenceDiagrams (property) | MATCH | — |
| get_source_artifacts() -> sourceArtifacts | getSourceArtifacts (method) | sourceArtifacts (property) | MATCH | — |
| get_timing_diagrams() -> timingDiagrams | getTimingDiagrams (method) | timingDiagrams (property) | MATCH | — |
| get_types() -> types | getTypes (method) | types (property) | MATCH | — |
| get_use_case_diagrams() -> useCaseDiagrams | getUseCaseDiagrams (method) | useCaseDiagrams (property) | MATCH | — |
| get_use_cases() -> useCases | getUseCases (method) | useCases (property) | MATCH | — |
| get_user_defined_stereotypes() -> userDefinedStereotypes | getUserDefinedStereotypes (method) | userDefinedStereotypes (property) | MATCH | — |
| populate_remote_requirements() -> populateRemoteRequirements | populateRemoteRequirements (method) | populateRemoteRequirements (method) | MATCH | — |

## AI Fix Guidance

### Finding 1: JAVA_DOC_MISSING
- **Target:** `IRPPackage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py`
- **Current Python wrapper/COM call:** add_association() -> addAssociation
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** addAssociation (method)
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `IRPPackage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py`
- **Current Python wrapper/COM call:** add_statechart_diagram() -> addStatechart
- **Expected Python method(s):** `add_statechart`
- **Java signature(s):** `IRPPackage.addStatechart()`
- **pywin32 member(s):** addStatechart (method)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 3: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `IRPPackage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py`
- **Current Python wrapper/COM call:** get_nested_packages() -> packages
- **Expected Python method(s):** `get_packages`
- **Java signature(s):** `IRPPackage.getPackages()`
- **pywin32 member(s):** packages (property)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 4: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `IRPPackage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py`
- **Current Python wrapper/COM call:** recalculate_events_base_id() -> reCalculateEventsBaseId
- **Expected Python method(s):** `re_calculate_events_base_id`
- **Java signature(s):** `IRPPackage.reCalculateEventsBaseId()`
- **pywin32 member(s):** reCalculateEventsBaseId (method)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 5: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `IRPPackage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py`
- **Current Python wrapper/COM call:** get_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> savedInSeperateDirectory
- **Expected Python method(s):** `get_saved_in_seperate_directory`, `set_saved_in_seperate_directory`
- **Java signature(s):** `IRPPackage.getSavedInSeperateDirectory()`, `IRPPackage.setSavedInSeperateDirectory(int)`
- **pywin32 member(s):** savedInSeperateDirectory (property)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
