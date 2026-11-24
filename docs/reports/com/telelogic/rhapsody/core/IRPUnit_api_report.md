# Rhapsody API Validation: IRPUnit

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPUnit` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_unit.py`)
- Members: Python `26`, Java `29`, pywin32 `25`
- Deviation items: `1` (actionable `0`, expected binding differences `1`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_unit_path() (no static COM member); set_unit_path() -> setUnitPath | getUnitPath (method); setUnitPath (method) | setUnitPath (method) | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (23) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| cm_header (property) -> CMHeader | getCMHeader (method); setCMHeader (method) | CMHeader (property) | MATCH | — |
| copy_to_another_project() -> copyToAnotherProject | copyToAnotherProject (method) | copyToAnotherProject (method) | MATCH | — |
| current_directory (property) -> currentDirectory | getCurrentDirectory (method) | currentDirectory (property) | MATCH | — |
| filename (property) -> filename | getFilename (method); setFilename (method) | filename (property) | MATCH | — |
| get_add_to_model_mode() -> getAddToModelMode | getAddToModelMode (method) | getAddToModelMode (method) | MATCH | — |
| get_cm_state() -> getCMState | getCMState (method) | getCMState (method) | MATCH | — |
| get_language() -> getLanguage; set_language() -> setLanguage | getLanguage (method); setLanguage (method) | getLanguage (method); setLanguage (method) | MATCH | — |
| get_last_modified_time() -> getLastModifiedTime | getLastModifiedTime (method) | getLastModifiedTime (method) | MATCH | — |
| get_nested_save_units() -> getNestedSaveUnits | getNestedSaveUnits (method) | getNestedSaveUnits (method) | MATCH | — |
| get_nested_save_units_count() -> getNestedSaveUnitsCount | getNestedSaveUnitsCount (method) | getNestedSaveUnitsCount (method) | MATCH | — |
| include_in_next_load (property) -> includeInNextLoad | getIncludeInNextLoad (method); setIncludeInNextLoad (method) | includeInNextLoad (property) | MATCH | — |
| is_read_only() -> isReadOnly | isReadOnly (method) | isReadOnly (method) | MATCH | — |
| is_reference_unit() -> isReferenceUnit | isReferenceUnit (method) | isReferenceUnit (method) | MATCH | — |
| is_separate_save_unit() -> isSeparateSaveUnit | isSeparateSaveUnit (method) | isSeparateSaveUnit (method) | MATCH | — |
| is_stub (property) -> isStub | getIsStub (method) | isStub (property) | MATCH | — |
| load() -> load | load (method) | load (method) | MATCH | — |
| move_to_another_project_leave_a_reference() -> moveToAnotherProjectLeaveAReference | moveToAnotherProjectLeaveAReference (method) | moveToAnotherProjectLeaveAReference (method) | MATCH | — |
| reference_to_another_project() -> referenceToAnotherProject | referenceToAnotherProject (method) | referenceToAnotherProject (method) | MATCH | — |
| save() -> save | save (method) | save (method) | MATCH | — |
| set_read_only() -> setReadOnly | setReadOnly (method) | setReadOnly (method) | MATCH | — |
| set_separate_save_unit() -> setSeparateSaveUnit | setSeparateSaveUnit (method) | setSeparateSaveUnit (method) | MATCH | — |
| structure_diagrams (property) -> structureDiagrams | getStructureDiagrams (method) | structureDiagrams (property) | MATCH | — |
| unload() -> unload | unload (method) | unload (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
