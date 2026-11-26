# Rhapsody API Validation: IRPInstanceValue

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPInstanceValue` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_values.py`)
- Members: Python `2`, Java `2`, pywin32 `1`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_value() -> getValue; set_value() -> setValue | getValue (method); setValue (method) | value (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the value property or a getter/setter fallback instead of calling getValue and setValue directly. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPInstanceValue` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_values.py`
- **Affected call(s):** get_value() -> getValue; set_value() -> setValue
- **Java signature(s):** `IRPInstanceValue.getValue()`, `IRPInstanceValue.setValue(com.telelogic.rhapsody.core.IRPModelElement)`
- **Recommended change:** Use the value property or a getter/setter fallback instead of calling getValue and setValue directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
