# Rhapsody API Validation: IRPPin

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPPin` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `6`, Java `6`, pywin32 `3`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_parameter() -> isParameter; set_is_parameter() -> isParameter | getIsParameter (method); setIsParameter (method) | isParameter (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_pin_direction() -> pinDirection; set_pin_direction() -> pinDirection | getPinDirection (method); setPinDirection (method) | pinDirection (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_pin_type() -> getPinType; set_pin_type() -> setPinType | getPinType (method); setPinType (method) | pinType (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the pinType property or a getter/setter fallback instead of calling getPinType and setPinType directly. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPPin` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_is_parameter() -> isParameter; set_is_parameter() -> isParameter; get_pin_direction() -> pinDirection; set_pin_direction() -> pinDirection
- **Java signature(s):** `IRPPin.getIsParameter()`, `IRPPin.setPinDirection(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPPin` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_pin_type() -> getPinType; set_pin_type() -> setPinType
- **Java signature(s):** `IRPPin.getPinType()`, `IRPPin.setPinType(com.telelogic.rhapsody.core.IRPClassifier)`
- **Recommended change:** Use the pinType property or a getter/setter fallback instead of calling getPinType and setPinType directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
