# Rhapsody API Validation: IRPEvent

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPEvent` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`)
- Members: Python `4`, Java `4`, pywin32 `2`
- Deviation items: `2` (actionable `2`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_base_event() -> baseEvent; set_base_event() -> baseEvent | getBaseEvent (method); setBaseEvent (method) | baseEvent (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_super_event() -> superEvent; set_super_event() -> superEvent | getSuperEvent (method); setSuperEvent (method) | superEvent (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPEvent` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interactions.py`
- **Affected call(s):** get_base_event() -> baseEvent; set_base_event() -> baseEvent; get_super_event() -> superEvent; set_super_event() -> superEvent
- **Java signature(s):** `IRPEvent.getBaseEvent()`, `IRPEvent.setSuperEvent(com.telelogic.rhapsody.core.IRPEvent)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
