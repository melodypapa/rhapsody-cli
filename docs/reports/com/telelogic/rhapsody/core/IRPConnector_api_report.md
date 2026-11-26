# Rhapsody API Validation: IRPConnector

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPConnector` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `16`, Java `16`, pywin32 `16`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_connector_type() -> connectorType | getConnectorType (method) | connectorType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| create_default_transition() -> createDefaultTransition | — | createDefaultTransition (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| set_its_swimlane() -> setItsSwimlane | — | setItsSwimlane (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| set_of_state() -> setOfState | — | setOfState (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (13) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| create_default_transition() -> createDefaultTransition | createDefaultTransition (method) | createDefaultTransition (method) | MATCH | — |
| get_derived_in_edges() -> getDerivedInEdges | getDerivedInEdges (method) | getDerivedInEdges (method) | MATCH | — |
| get_derived_out_edge() -> getDerivedOutEdge | getDerivedOutEdge (method) | getDerivedOutEdge (method) | MATCH | — |
| is_condition_connector() -> isConditionConnector | isConditionConnector (method) | isConditionConnector (method) | MATCH | — |
| is_diagram_connector() -> isDiagramConnector | isDiagramConnector (method) | isDiagramConnector (method) | MATCH | — |
| is_fork_connector() -> isForkConnector | isForkConnector (method) | isForkConnector (method) | MATCH | — |
| is_history_connector() -> isHistoryConnector | isHistoryConnector (method) | isHistoryConnector (method) | MATCH | — |
| is_join_connector() -> isJoinConnector | isJoinConnector (method) | isJoinConnector (method) | MATCH | — |
| is_junction_connector() -> isJunctionConnector | isJunctionConnector (method) | isJunctionConnector (method) | MATCH | — |
| is_stub_connector() -> isStubConnector | isStubConnector (method) | isStubConnector (method) | MATCH | — |
| is_termination_connector() -> isTerminationConnector | isTerminationConnector (method) | isTerminationConnector (method) | MATCH | — |
| get_its_swimlane() -> getItsSwimlane; set_its_swimlane() -> setItsSwimlane | getItsSwimlane (method); setItsSwimlane (method) | getItsSwimlane (method); setItsSwimlane (method) | MATCH | — |
| get_of_state() -> getOfState; set_of_state() -> setOfState | getOfState (method); setOfState (method) | getOfState (method); setOfState (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPConnector` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_connector_type() -> connectorType
- **Java signature(s):** `IRPConnector.getConnectorType()`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (3 findings)
- **Target:** `IRPConnector` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** create_default_transition() -> createDefaultTransition; set_its_swimlane() -> setItsSwimlane; set_of_state() -> setOfState
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
