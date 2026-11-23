# Rhapsody API Validation: IRPCollection

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPCollection` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py`)
- Members: Python `11`, Java `11`, pywin32 `9`
- Deviation items: `3` (actionable `1`, expected binding differences `2`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| set_string() -> setString | — | setString (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['int', 'str'] but pywin32 declares ['int', 'object']. Match the documented COM parameter types. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_graphical_item() (no static COM member) | addGraphicalItem (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| to_list() (no static COM member) | toList (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (9) — bindings verified against pywin32</summary>


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

</details>

## AI Fix Guidance

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPCollection` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py`
- **Affected call(s):** set_string() -> setString
- **Recommended change:** Wrapper passes types ['int', 'str'] but pywin32 declares ['int', 'object']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
