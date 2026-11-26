# Rhapsody API Validation: IRPSendAction

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPSendAction` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_actions.py`)
- Members: Python `8`, Java `8`, pywin32 `5`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_arg_vals() -> argVals | getArgVals (method) | argVals (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_event() -> event; set_event() -> event | getEvent (method); setEvent (method) | event (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_invoked_operation() -> invokedOperation; set_invoked_operation() -> invokedOperation | getInvokedOperation (method); setInvokedOperation (method) | invokedOperation (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_target() -> target; set_target() -> target | getTarget (method); setTarget (method) | target (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_argument_value() -> addArgumentValue | addArgumentValue (method) | addArgumentValue (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (4 findings)
- **Target:** `IRPSendAction` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_actions.py`
- **Affected call(s):** get_arg_vals() -> argVals; get_event() -> event; set_event() -> event; get_invoked_operation() -> invokedOperation; set_invoked_operation() -> invokedOperation; get_target() -> target; set_target() -> target
- **Java signature(s):** `IRPSendAction.setTarget(com.telelogic.rhapsody.core.IRPModelElement)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
