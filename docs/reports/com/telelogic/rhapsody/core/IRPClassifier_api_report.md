# Rhapsody API Validation: IRPClassifier

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPClassifier` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_classifier.py`)
- Members: Python `47`, Java `46`, pywin32 `47`
- Deviations: `1`
- Deviations by status:
  - `JAVA_DOC_MISSING`: 1

- Informational binding differences (expected): `0`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_port() -> addNewAggr | — | addNewAggr (method) | JAVA_DOC_MISSING | Confirm this COM member is a supported extension and document its status. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_activity_diagram() -> addActivityDiagram | addActivityDiagram (method) | addActivityDiagram (method) | MATCH | — |
| add_attribute() -> addAttribute | addAttribute (method) | addAttribute (method) | MATCH | — |
| add_flow_items() -> addFlowItems | addFlowItems (method) | addFlowItems (method) | MATCH | — |
| add_flows() -> addFlows | addFlows (method) | addFlows (method) | MATCH | — |
| add_generalization() -> addGeneralization | addGeneralization (method) | addGeneralization (method) | MATCH | — |
| add_operation() -> addOperation | addOperation (method) | addOperation (method) | MATCH | — |
| add_relation() -> addRelation | addRelation (method) | addRelation (method) | MATCH | — |
| add_relation_to() -> addRelationTo | addRelationTo (method) | addRelationTo (method) | MATCH | — |
| add_statechart() -> addStatechart | addStatechart (method) | addStatechart (method) | MATCH | — |
| add_unidirectional_relation() -> addUnidirectionalRelation | addUnidirectionalRelation (method) | addUnidirectionalRelation (method) | MATCH | — |
| add_unidirectional_relation_to() -> addUnidirectionalRelationTo | addUnidirectionalRelationTo (method) | addUnidirectionalRelationTo (method) | MATCH | — |
| delete_attribute() -> deleteAttribute | deleteAttribute (method) | deleteAttribute (method) | MATCH | — |
| delete_flow_items() -> deleteFlowItems | deleteFlowItems (method) | deleteFlowItems (method) | MATCH | — |
| delete_flows() -> deleteFlows | deleteFlows (method) | deleteFlows (method) | MATCH | — |
| delete_generalization() -> deleteGeneralization | deleteGeneralization (method) | deleteGeneralization (method) | MATCH | — |
| delete_operation() -> deleteOperation | deleteOperation (method) | deleteOperation (method) | MATCH | — |
| delete_relation() -> deleteRelation | deleteRelation (method) | deleteRelation (method) | MATCH | — |
| find_attribute() -> findAttribute | findAttribute (method) | findAttribute (method) | MATCH | — |
| find_base_classifier() -> findBaseClassifier | findBaseClassifier (method) | findBaseClassifier (method) | MATCH | — |
| find_derived_classifier() -> findDerivedClassifier | findDerivedClassifier (method) | findDerivedClassifier (method) | MATCH | — |
| find_generalization() -> findGeneralization | findGeneralization (method) | findGeneralization (method) | MATCH | — |
| find_interface_item() -> findInterfaceItem | findInterfaceItem (method) | findInterfaceItem (method) | MATCH | — |
| find_nested_classifier() -> findNestedClassifier | findNestedClassifier (method) | findNestedClassifier (method) | MATCH | — |
| find_nested_classifier_recursive() -> findNestedClassifierRecursive | findNestedClassifierRecursive (method) | findNestedClassifierRecursive (method) | MATCH | — |
| find_relation() -> findRelation | findRelation (method) | findRelation (method) | MATCH | — |
| find_trigger() -> findTrigger | findTrigger (method) | findTrigger (method) | MATCH | — |
| get_activity_diagram() -> activityDiagram | getActivityDiagram (method) | activityDiagram (property) | MATCH | — |
| get_attributes() -> attributes | getAttributes (method) | attributes (property) | MATCH | — |
| get_attributes_including_bases() -> getAttributesIncludingBases | getAttributesIncludingBases (method) | getAttributesIncludingBases (method) | MATCH | — |
| get_base_classifiers() -> baseClassifiers | getBaseClassifiers (method) | baseClassifiers (property) | MATCH | — |
| get_behavioral_diagrams() -> behavioralDiagrams | getBehavioralDiagrams (method) | behavioralDiagrams (property) | MATCH | — |
| get_derived_classifiers() -> derivedClassifiers | getDerivedClassifiers (method) | derivedClassifiers (property) | MATCH | — |
| get_flow_items() -> flowItems | getFlowItems (method) | flowItems (property) | MATCH | — |
| get_flows() -> flows | getFlows (method) | flows (property) | MATCH | — |
| get_generalizations() -> generalizations | getGeneralizations (method) | generalizations (property) | MATCH | — |
| get_interface_items() -> interfaceItems | getInterfaceItems (method) | interfaceItems (property) | MATCH | — |
| get_interface_items_including_bases() -> getInterfaceItemsIncludingBases | getInterfaceItemsIncludingBases (method) | getInterfaceItemsIncludingBases (method) | MATCH | — |
| get_links() -> links | getLinks (method) | links (property) | MATCH | — |
| get_nested_classifiers() -> nestedClassifiers | getNestedClassifiers (method) | nestedClassifiers (property) | MATCH | — |
| get_operations() -> operations | getOperations (method) | operations (property) | MATCH | — |
| get_ports() -> ports | getPorts (method) | ports (property) | MATCH | — |
| get_relations() -> relations | getRelations (method) | relations (property) | MATCH | — |
| get_relations_including_bases() -> getRelationsIncludingBases | getRelationsIncludingBases (method) | getRelationsIncludingBases (method) | MATCH | — |
| get_sequence_diagrams() -> sequenceDiagrams | getSequenceDiagrams (method) | sequenceDiagrams (property) | MATCH | — |
| get_source_artifacts() -> sourceArtifacts | getSourceArtifacts (method) | sourceArtifacts (property) | MATCH | — |
| get_statechart() -> statechart | getStatechart (method) | statechart (property) | MATCH | — |

## AI Fix Guidance

### Finding 1: JAVA_DOC_MISSING
- **Target:** `IRPClassifier` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_classifier.py`
- **Current Python wrapper/COM call:** add_port() -> addNewAggr
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** addNewAggr (method)
- **Recommended change:** Confirm this COM member is a supported extension and document its status.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
