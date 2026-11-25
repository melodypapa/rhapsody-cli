# Rhapsody API Validation: IRPCollection

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPCollection` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py`)
- Members: Python `11`, Java `11`, pywin32 `10`
- Deviation items: `1` (actionable `0`, expected binding differences `1`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| to_list() (no static COM member) | toList (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (10) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_graphical_item() -> addGraphicalElementItem | addGraphicalItem (method) | addGraphicalElementItem (method) | MATCH | — |
| add_item() -> addItem | addItem (method) | addItem (method) | MATCH | — |
| count (property) -> Count | getCount (method) | Count (property) | MATCH | — |
| empty() -> empty | empty (method) | empty (method) | MATCH | — |
| get_item() -> Item | getItem (method) | Item (method) | MATCH | — |
| remove() -> remove | remove (method) | remove (method) | MATCH | — |
| set_integer() -> setInteger | setInteger (method) | setInteger (method) | MATCH | — |
| set_model_element() -> setModelElement | setModelElement (method) | setModelElement (method) | MATCH | — |
| set_size() -> setSize | setSize (method) | setSize (method) | MATCH | — |
| set_string() -> setString | setString (method) | setString (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
