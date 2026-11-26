# Rhapsody API Validation: IRPInstanceSpecification

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPInstanceSpecification` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_values.py`)
- Members: Python `6`, Java `6`, pywin32 `3`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_instance_slot() -> addInstanceSlot | addInstanceSlot (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_classifier() -> getClassifier; set_classifier() -> setClassifier | getClassifier (method); setClassifier (method) | classifier (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the classifier property or a getter/setter fallback instead of calling getClassifier and setClassifier directly. |
| get_instance_slots() -> getInstanceSlots | getInstanceSlots (method) | instanceSlots (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the instanceSlots property or a getter/setter fallback instead of calling getInstanceSlots directly. |
| is_root_instance_specification() -> isRootInstanceSpecification | isRootInstanceSpecification (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| populate_slots() -> populateSlots | populateSlots (method) | populateSlots (method) | MATCH | — |

</details>

## AI Fix Guidance

### PYWIN32_MEMBER_MISSING (2 findings)
- **Target:** `IRPInstanceSpecification` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_values.py`
- **Affected call(s):** add_instance_slot() -> addInstanceSlot; is_root_instance_specification() -> isRootInstanceSpecification
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPInstanceSpecification` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_values.py`
- **Affected call(s):** get_classifier() -> getClassifier; set_classifier() -> setClassifier; get_instance_slots() -> getInstanceSlots
- **Java signature(s):** `IRPInstanceSpecification.getClassifier()`
- **Recommended change:** Use the classifier property or a getter/setter fallback instead of calling getClassifier and setClassifier directly.
- **Recommended change:** Use the instanceSlots property or a getter/setter fallback instead of calling getInstanceSlots directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
