# Rhapsody API Validation: IRPUnit

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `RPUnit` (`src/rhapsody_cli/models/core.py`)
- Members: Python `29`, Java `29`, pywin32 `25`
- Deviations: `0`
- Deviations by status:
  - None

- Informational binding differences (expected): `1`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_unit_path() -> getUnitPath; set_unit_path() -> setUnitPath | getUnitPath (method); setUnitPath (method) | setUnitPath (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| copy_to_another_project() -> copyToAnotherProject | copyToAnotherProject (method) | copyToAnotherProject (method) | MATCH | — |
| get_add_to_model_mode() -> getAddToModelMode | getAddToModelMode (method) | getAddToModelMode (method) | MATCH | — |
| get_cm_header() -> CMHeader; set_cm_header() -> CMHeader | getCMHeader (method); setCMHeader (method) | CMHeader (property) | MATCH | — |
| get_cm_state() -> getCMState | getCMState (method) | getCMState (method) | MATCH | — |
| get_current_directory() -> currentDirectory | getCurrentDirectory (method) | currentDirectory (property) | MATCH | — |
| get_filename() -> filename; set_filename() -> filename | getFilename (method); setFilename (method) | filename (property) | MATCH | — |
| get_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> includeInNextLoad | getIncludeInNextLoad (method); setIncludeInNextLoad (method) | includeInNextLoad (property) | MATCH | — |
| get_is_stub() -> isStub | getIsStub (method) | isStub (property) | MATCH | — |
| get_language() -> getLanguage; set_language() -> setLanguage | getLanguage (method); setLanguage (method) | getLanguage (method); setLanguage (method) | MATCH | — |
| get_last_modified_time() -> getLastModifiedTime | getLastModifiedTime (method) | getLastModifiedTime (method) | MATCH | — |
| get_nested_save_units() -> getNestedSaveUnits | getNestedSaveUnits (method) | getNestedSaveUnits (method) | MATCH | — |
| get_nested_save_units_count() -> getNestedSaveUnitsCount | getNestedSaveUnitsCount (method) | getNestedSaveUnitsCount (method) | MATCH | — |
| get_structure_diagrams() -> structureDiagrams | getStructureDiagrams (method) | structureDiagrams (property) | MATCH | — |
| is_read_only() -> isReadOnly | isReadOnly (method) | isReadOnly (method) | MATCH | — |
| is_reference_unit() -> isReferenceUnit | isReferenceUnit (method) | isReferenceUnit (method) | MATCH | — |
| is_separate_save_unit() -> isSeparateSaveUnit | isSeparateSaveUnit (method) | isSeparateSaveUnit (method) | MATCH | — |
| load() -> load | load (method) | load (method) | MATCH | — |
| move_to_another_project_leave_a_reference() -> moveToAnotherProjectLeaveAReference | moveToAnotherProjectLeaveAReference (method) | moveToAnotherProjectLeaveAReference (method) | MATCH | — |
| reference_to_another_project() -> referenceToAnotherProject | referenceToAnotherProject (method) | referenceToAnotherProject (method) | MATCH | — |
| save() -> save | save (method) | save (method) | MATCH | — |
| set_read_only() -> setReadOnly | setReadOnly (method) | setReadOnly (method) | MATCH | — |
| set_separate_save_unit() -> setSeparateSaveUnit | setSeparateSaveUnit (method) | setSeparateSaveUnit (method) | MATCH | — |
| unload() -> unload | unload (method) | unload (method) | MATCH | — |

## AI Fix Guidance
No deviations require changes.
