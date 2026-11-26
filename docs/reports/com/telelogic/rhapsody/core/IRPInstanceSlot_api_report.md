# Rhapsody API Validation: IRPInstanceSlot

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPInstanceSlot` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_values.py`)
- Members: Python `5`, Java `5`, pywin32 `4`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_slot_property() -> getSlotProperty; set_slot_property() -> setSlotProperty | getSlotProperty (method); setSlotProperty (method) | slotProperty (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the slotProperty property or a getter/setter fallback instead of calling getSlotProperty and setSlotProperty directly. |
| get_values() -> getValues | getValues (method) | values (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the values property or a getter/setter fallback instead of calling getValues directly. |
| add_element_value() -> addElementValue | — | addElementValue (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (2) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_element_value() -> addElementValue | addElementValue (method) | addElementValue (method) | MATCH | — |
| add_string_value() -> addStringValue | addStringValue (method) | addStringValue (method) | MATCH | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPInstanceSlot` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_values.py`
- **Affected call(s):** get_slot_property() -> getSlotProperty; set_slot_property() -> setSlotProperty; get_values() -> getValues
- **Java signature(s):** `IRPInstanceSlot.getSlotProperty()`
- **Recommended change:** Use the slotProperty property or a getter/setter fallback instead of calling getSlotProperty and setSlotProperty directly.
- **Recommended change:** Use the values property or a getter/setter fallback instead of calling getValues directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPInstanceSlot` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_values.py`
- **Affected call(s):** add_element_value() -> addElementValue
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
