# Rhapsody API Validation: IRPFlowchart

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPFlowchart` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`)
- Members: Python `14`, Java `14`, pywin32 `12`
- Deviation items: `9` (actionable `9`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_analysis_only() -> isAnalysisOnly; set_is_analysis_only() -> isAnalysisOnly | getIsAnalysisOnly (method); setIsAnalysisOnly (method) | isAnalysisOnly (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_its_owner() -> getItsOwner; set_its_owner() -> setItsOwner | getItsOwner (method); setItsOwner (method) | itsOwner (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the itsOwner property or a getter/setter fallback instead of calling getItsOwner and setItsOwner directly. |
| get_swimlanes() -> getSwimlanes | getSwimlanes (method) | swimlanes (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the swimlanes property or a getter/setter fallback instead of calling getSwimlanes directly. |
| add_accept_event_action() -> addAcceptEventAction | — | addAcceptEventAction (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str', 'object'] but pywin32 declares ['str', 'com']. Match the documented COM parameter types. |
| add_accept_time_event() -> addAcceptTimeEvent | — | addAcceptTimeEvent (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str', 'object'] but pywin32 declares ['str', 'com']. Match the documented COM parameter types. |
| add_call_behavior() -> addCallBehavior | — | addCallBehavior (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| add_call_operation() -> addCallOperation | — | addCallOperation (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str', 'object'] but pywin32 declares ['str', 'com']. Match the documented COM parameter types. |
| add_object_node() -> addObjectNode | — | addObjectNode (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['str', 'object'] but pywin32 declares ['str', 'com']. Match the documented COM parameter types. |
| add_reference_activity() -> addReferenceActivity | — | addReferenceActivity (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (9) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_accept_event_action() -> addAcceptEventAction | addAcceptEventAction (method) | addAcceptEventAction (method) | MATCH | — |
| add_accept_time_event() -> addAcceptTimeEvent | addAcceptTimeEvent (method) | addAcceptTimeEvent (method) | MATCH | — |
| add_activity_parameter() -> addActivityParameter | addActivityParameter (method) | addActivityParameter (method) | MATCH | — |
| add_call_behavior() -> addCallBehavior | addCallBehavior (method) | addCallBehavior (method) | MATCH | — |
| add_call_operation() -> addCallOperation | addCallOperation (method) | addCallOperation (method) | MATCH | — |
| add_object_node() -> addObjectNode | addObjectNode (method) | addObjectNode (method) | MATCH | — |
| add_reference_activity() -> addReferenceActivity | addReferenceActivity (method) | addReferenceActivity (method) | MATCH | — |
| add_swimlane() -> addSwimlane | addSwimlane (method) | addSwimlane (method) | MATCH | — |
| get_flowchart_diagram() -> getFlowchartDiagram | getFlowchartDiagram (method) | getFlowchartDiagram (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPFlowchart` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** get_is_analysis_only() -> isAnalysisOnly; set_is_analysis_only() -> isAnalysisOnly
- **Java signature(s):** `IRPFlowchart.getIsAnalysisOnly()`, `IRPFlowchart.setIsAnalysisOnly(int)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPFlowchart` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** get_its_owner() -> getItsOwner; set_its_owner() -> setItsOwner; get_swimlanes() -> getSwimlanes
- **Java signature(s):** `IRPFlowchart.getItsOwner()`
- **Recommended change:** Use the itsOwner property or a getter/setter fallback instead of calling getItsOwner and setItsOwner directly.
- **Recommended change:** Use the swimlanes property or a getter/setter fallback instead of calling getSwimlanes directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (6 findings)
- **Target:** `IRPFlowchart` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** add_accept_event_action() -> addAcceptEventAction; add_accept_time_event() -> addAcceptTimeEvent; add_call_behavior() -> addCallBehavior; add_call_operation() -> addCallOperation; add_object_node() -> addObjectNode; add_reference_activity() -> addReferenceActivity
- **Recommended change:** Wrapper passes types ['str', 'object'] but pywin32 declares ['str', 'com']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
