# Rhapsody API Validation: IRPFileFragment

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPFileFragment` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_files.py`)
- Members: Python `5`, Java `5`, pywin32 `4`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_fragment_element() -> fragmentElement | getFragmentElement (method) | fragmentElement (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_fragment_text() -> fragmentText; set_fragment_text() -> fragmentText | getFragmentText (method); setFragmentText (method) | fragmentText (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_fragment_type() -> fragmentType | getFragmentType (method) | fragmentType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| move_fragment_in_owner() -> moveFragmentInOwner | moveFragmentInOwner (method) | moveFragmentInOwner (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (3 findings)
- **Target:** `IRPFileFragment` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_files.py`
- **Affected call(s):** get_fragment_element() -> fragmentElement; get_fragment_text() -> fragmentText; set_fragment_text() -> fragmentText; get_fragment_type() -> fragmentType
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
