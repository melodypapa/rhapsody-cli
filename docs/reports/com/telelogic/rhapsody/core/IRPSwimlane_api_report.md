# Rhapsody API Validation: IRPSwimlane

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPSwimlane` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`)
- Members: Python `5`, Java `5`, pywin32 `4`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_contents() -> getContents | getContents (method) | contents (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the contents property or a getter/setter fallback instead of calling getContents directly. |
| get_represents() -> getRepresents; set_represents() -> represents | getRepresents (method); setRepresents (method) | represents (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_swimlanes() -> getSwimlanes | getSwimlanes (method) | swimlanes (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the swimlanes property or a getter/setter fallback instead of calling getSwimlanes directly. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_swimlane() -> addSwimlane | addSwimlane (method) | addSwimlane (method) | MATCH | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPSwimlane` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** get_contents() -> getContents; get_swimlanes() -> getSwimlanes
- **Recommended change:** Use the contents property or a getter/setter fallback instead of calling getContents directly.
- **Recommended change:** Use the swimlanes property or a getter/setter fallback instead of calling getSwimlanes directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPSwimlane` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** get_represents() -> getRepresents; set_represents() -> represents
- **Java signature(s):** `IRPSwimlane.getRepresents()`, `IRPSwimlane.setRepresents(com.telelogic.rhapsody.core.IRPModelElement)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
