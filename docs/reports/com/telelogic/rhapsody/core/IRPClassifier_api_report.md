# Rhapsody API Validation: IRPClassifier

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPClassifier` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_classifier.py`)
- Members: Python `46`, Java `46`, pywin32 `46`
- Deviation items: `0` (actionable `0`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (46) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| activity_diagram (property) -> activityDiagram | getActivityDiagram (method) | activityDiagram (property) | MATCH | — |
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
| attributes (property) -> attributes | getAttributes (method) | attributes (property) | MATCH | — |
| get_attributes_including_bases() -> getAttributesIncludingBases | getAttributesIncludingBases (method) | getAttributesIncludingBases (method) | MATCH | — |
| base_classifiers (property) -> baseClassifiers | getBaseClassifiers (method) | baseClassifiers (property) | MATCH | — |
| behavioral_diagrams (property) -> behavioralDiagrams | getBehavioralDiagrams (method) | behavioralDiagrams (property) | MATCH | — |
| delete_attribute() -> deleteAttribute | deleteAttribute (method) | deleteAttribute (method) | MATCH | — |
| delete_flow_items() -> deleteFlowItems | deleteFlowItems (method) | deleteFlowItems (method) | MATCH | — |
| delete_flows() -> deleteFlows | deleteFlows (method) | deleteFlows (method) | MATCH | — |
| delete_generalization() -> deleteGeneralization | deleteGeneralization (method) | deleteGeneralization (method) | MATCH | — |
| delete_operation() -> deleteOperation | deleteOperation (method) | deleteOperation (method) | MATCH | — |
| delete_relation() -> deleteRelation | deleteRelation (method) | deleteRelation (method) | MATCH | — |
| derived_classifiers (property) -> derivedClassifiers | getDerivedClassifiers (method) | derivedClassifiers (property) | MATCH | — |
| find_attribute() -> findAttribute | findAttribute (method) | findAttribute (method) | MATCH | — |
| find_base_classifier() -> findBaseClassifier | findBaseClassifier (method) | findBaseClassifier (method) | MATCH | — |
| find_derived_classifier() -> findDerivedClassifier | findDerivedClassifier (method) | findDerivedClassifier (method) | MATCH | — |
| find_generalization() -> findGeneralization | findGeneralization (method) | findGeneralization (method) | MATCH | — |
| find_interface_item() -> findInterfaceItem | findInterfaceItem (method) | findInterfaceItem (method) | MATCH | — |
| find_nested_classifier() -> findNestedClassifier | findNestedClassifier (method) | findNestedClassifier (method) | MATCH | — |
| find_nested_classifier_recursive() -> findNestedClassifierRecursive | findNestedClassifierRecursive (method) | findNestedClassifierRecursive (method) | MATCH | — |
| find_relation() -> findRelation | findRelation (method) | findRelation (method) | MATCH | — |
| find_trigger() -> findTrigger | findTrigger (method) | findTrigger (method) | MATCH | — |
| flow_items (property) -> flowItems | getFlowItems (method) | flowItems (property) | MATCH | — |
| flows (property) -> flows | getFlows (method) | flows (property) | MATCH | — |
| generalizations (property) -> generalizations | getGeneralizations (method) | generalizations (property) | MATCH | — |
| interface_items (property) -> interfaceItems | getInterfaceItems (method) | interfaceItems (property) | MATCH | — |
| get_interface_items_including_bases() -> getInterfaceItemsIncludingBases | getInterfaceItemsIncludingBases (method) | getInterfaceItemsIncludingBases (method) | MATCH | — |
| links (property) -> links | getLinks (method) | links (property) | MATCH | — |
| nested_classifiers (property) -> nestedClassifiers | getNestedClassifiers (method) | nestedClassifiers (property) | MATCH | — |
| operations (property) -> operations | getOperations (method) | operations (property) | MATCH | — |
| ports (property) -> ports | getPorts (method) | ports (property) | MATCH | — |
| relations (property) -> relations | getRelations (method) | relations (property) | MATCH | — |
| get_relations_including_bases() -> getRelationsIncludingBases | getRelationsIncludingBases (method) | getRelationsIncludingBases (method) | MATCH | — |
| sequence_diagrams (property) -> sequenceDiagrams | getSequenceDiagrams (method) | sequenceDiagrams (property) | MATCH | — |
| source_artifacts (property) -> sourceArtifacts | getSourceArtifacts (method) | sourceArtifacts (property) | MATCH | — |
| statechart (property) -> statechart | getStatechart (method) | statechart (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
