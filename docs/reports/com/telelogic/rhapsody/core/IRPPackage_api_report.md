# Rhapsody API Validation: IRPPackage

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPPackage` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py`)
- Members: Python `100`, Java `100`, pywin32 `94`
- Deviation items: `7` (actionable `1`, expected binding differences `6`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_association() -> addAssociation | — | addAssociation (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |

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

<details>
<summary>Correct items (92) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| actors (property) -> actors | getActors (method) | actors (property) | MATCH | — |
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
| add_statechart() -> addStatechart | addStatechart (method) | addStatechart (method) | MATCH | — |
| add_timing_diagram() -> addTimingDiagram | addTimingDiagram (method) | addTimingDiagram (method) | MATCH | — |
| add_type() -> addType | addType (method) | addType (method) | MATCH | — |
| add_use_case() -> addUseCase | addUseCase (method) | addUseCase (method) | MATCH | — |
| add_use_case_diagram() -> addUseCaseDiagram | addUseCaseDiagram (method) | addUseCaseDiagram (method) | MATCH | — |
| behavioral_diagrams (property) -> behavioralDiagrams | getBehavioralDiagrams (method) | behavioralDiagrams (property) | MATCH | — |
| classes (property) -> classes | getClasses (method) | classes (property) | MATCH | — |
| collaboration_diagrams (property) -> collaborationDiagrams | getCollaborationDiagrams (method) | collaborationDiagrams (property) | MATCH | — |
| component_diagrams (property) -> componentDiagrams | getComponentDiagrams (method) | componentDiagrams (property) | MATCH | — |
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
| deployment_diagrams (property) -> deploymentDiagrams | getDeploymentDiagrams (method) | deploymentDiagrams (property) | MATCH | — |
| events (property) -> events | getEvents (method) | events (property) | MATCH | — |
| events_base_id (property) -> eventsBaseId | getEventsBaseId (method) | eventsBaseId (property) | MATCH | — |
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
| flow_items (property) -> flowItems | getFlowItems (method) | flowItems (property) | MATCH | — |
| flows (property) -> flows | getFlows (method) | flows (property) | MATCH | — |
| get_all_nested_elements() -> getAllNestedElements | getAllNestedElements (method) | getAllNestedElements (method) | MATCH | — |
| get_namespace() -> getNamespace | getNamespace (method) | getNamespace (method) | MATCH | — |
| get_remote_requirements_populate_mode() -> getRemoteRequirementsPopulateMode; set_remote_requirements_populate_mode() -> setRemoteRequirementsPopulateMode | getRemoteRequirementsPopulateMode (method); setRemoteRequirementsPopulateMode (method) | getRemoteRequirementsPopulateMode (method); setRemoteRequirementsPopulateMode (method) | MATCH | — |
| global_functions (property) -> globalFunctions | getGlobalFunctions (method) | globalFunctions (property) | MATCH | — |
| global_objects (property) -> globalObjects | getGlobalObjects (method) | globalObjects (property) | MATCH | — |
| global_variables (property) -> globalVariables | getGlobalVariables (method) | globalVariables (property) | MATCH | — |
| instance_specifications (property) -> instanceSpecifications | getInstanceSpecifications (method) | instanceSpecifications (property) | MATCH | — |
| links (property) -> links | getLinks (method) | links (property) | MATCH | — |
| modules (property) -> modules | getModules (method) | modules (property) | MATCH | — |
| nested_classifiers (property) -> nestedClassifiers | getNestedClassifiers (method) | nestedClassifiers (property) | MATCH | — |
| nested_components (property) -> nestedComponents | getNestedComponents (method) | nestedComponents (property) | MATCH | — |
| nodes (property) -> nodes | getNodes (method) | nodes (property) | MATCH | — |
| object_model_diagrams (property) -> objectModelDiagrams | getObjectModelDiagrams (method) | objectModelDiagrams (property) | MATCH | — |
| packages (property) -> packages | getPackages (method) | packages (property) | MATCH | — |
| panel_diagrams (property) -> panelDiagrams | getPanelDiagrams (method) | panelDiagrams (property) | MATCH | — |
| populate_remote_requirements() -> populateRemoteRequirements | populateRemoteRequirements (method) | populateRemoteRequirements (method) | MATCH | — |
| re_calculate_events_base_id() -> reCalculateEventsBaseId | reCalculateEventsBaseId (method) | reCalculateEventsBaseId (method) | MATCH | — |
| saved_in_seperate_directory (property) -> savedInSeperateDirectory | getSavedInSeperateDirectory (method); setSavedInSeperateDirectory (method) | savedInSeperateDirectory (property) | MATCH | — |
| sequence_diagrams (property) -> sequenceDiagrams | getSequenceDiagrams (method) | sequenceDiagrams (property) | MATCH | — |
| source_artifacts (property) -> sourceArtifacts | getSourceArtifacts (method) | sourceArtifacts (property) | MATCH | — |
| timing_diagrams (property) -> timingDiagrams | getTimingDiagrams (method) | timingDiagrams (property) | MATCH | — |
| types (property) -> types | getTypes (method) | types (property) | MATCH | — |
| use_case_diagrams (property) -> useCaseDiagrams | getUseCaseDiagrams (method) | useCaseDiagrams (property) | MATCH | — |
| use_cases (property) -> useCases | getUseCases (method) | useCases (property) | MATCH | — |
| user_defined_stereotypes (property) -> userDefinedStereotypes | getUserDefinedStereotypes (method) | userDefinedStereotypes (property) | MATCH | — |

</details>

## AI Fix Guidance

### JAVA_DOC_MISSING (1 finding)
- **Target:** `IRPPackage` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_package.py`
- **Affected call(s):** add_association() -> addAssociation
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
