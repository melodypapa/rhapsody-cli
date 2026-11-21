# Rhapsody API Validation: IRPCollection

## Summary
- Target wrapper: `RPCollection` (`src/rhapsody_cli/models/core.py`)
- Members: Python `11`, Java `11`, pywin32 `13`
- Deviations: `1`
- Deviations by status:
  - `PYWIN32_MEMBER_MISSING`: 1

- Informational binding differences (expected): `4`
- Wrapper backlog (supported members without wrappers): `4`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_graphical_item() -> addGraphicalItem | addGraphicalItem (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_count() -> Count; get_count() -> getCount | getCount (method) | Count (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_item() -> Item; get_item() -> getItem | getItem (method) | Item (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |
| to_list() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| — | toList (method) | — | JAVA_ONLY_MEMBER | Verify the Java documentation against the installed COM type library. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | addGraphicalElementItem (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | setGraphElement (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | interfaceName (property) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | Items (property) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |

## AI Fix Guidance

### Finding 1: PYWIN32_MEMBER_MISSING
- **Target:** `RPCollection` in `src/rhapsody_cli/models/core.py`
- **Current Python wrapper/COM call:** add_graphical_item() -> addGraphicalItem
- **Expected Python method(s):** `add_graphical_item`
- **Java signature(s):** `IRPCollection.addGraphicalItem(com.telelogic.rhapsody.core.IRPGraphElement)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
