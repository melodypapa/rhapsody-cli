# Rhapsody API Validation: IRPCollection

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPCollection` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_collection.py`)
- Members: Python `11`, Java `11`, pywin32 `10`
- Deviation items: `3` (actionable `0`, expected binding differences `3`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (8) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_item() -> addItem | addItem (method) | addItem (method) | MATCH | — |
| count (property) -> Count | getCount (method) | Count (property) | MATCH | — |
| empty() -> empty | empty (method) | empty (method) | MATCH | — |
| set_integer() -> setInteger | setInteger (method) | setInteger (method) | MATCH | — |
| set_model_element() -> setModelElement | setModelElement (method) | setModelElement (method) | MATCH | — |
| remove() -> remove | remove (method) | remove (method) | MATCH | — |
| set_size() -> setSize | setSize (method) | setSize (method) | MATCH | — |
| set_string() -> setString | setString (method) | setString (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
