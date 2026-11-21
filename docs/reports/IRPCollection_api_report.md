# Rhapsody API Validation: IRPCollection

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPCollection` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py`)
- Members: Python `11`, Java `11`, pywin32 `9`
- Deviations: `2`
- Deviations by status:
  - `PYWIN32_MEMBER_MISSING`: 2

- Informational binding differences (expected): `0`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| add_graphical_item() -> addGraphicalItem | addGraphicalItem (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| to_list() (no static COM member) | toList (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_item() -> addItem | addItem (method) | addItem (method) | MATCH | — |
| empty() -> empty | empty (method) | empty (method) | MATCH | — |
| get_count() -> Count | getCount (method) | Count (property) | MATCH | — |
| get_item() -> Item | getItem (method) | Item (method) | MATCH | — |
| remove() -> remove | remove (method) | remove (method) | MATCH | — |
| set_integer() -> setInteger | setInteger (method) | setInteger (method) | MATCH | — |
| set_model_element() -> setModelElement | setModelElement (method) | setModelElement (method) | MATCH | — |
| set_size() -> setSize | setSize (method) | setSize (method) | MATCH | — |
| set_string() -> setString | setString (method) | setString (method) | MATCH | — |

## AI Fix Guidance

### Finding 1: PYWIN32_MEMBER_MISSING
- **Target:** `IRPCollection` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py`
- **Current Python wrapper/COM call:** add_graphical_item() -> addGraphicalItem
- **Expected Python method(s):** `add_graphical_item`
- **Java signature(s):** `IRPCollection.addGraphicalItem(com.telelogic.rhapsody.core.IRPGraphElement)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: PYWIN32_MEMBER_MISSING
- **Target:** `IRPCollection` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py`
- **Current Python wrapper/COM call:** to_list() (no static COM member)
- **Expected Python method(s):** `to_list`
- **Java signature(s):** `IRPCollection.toList()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
