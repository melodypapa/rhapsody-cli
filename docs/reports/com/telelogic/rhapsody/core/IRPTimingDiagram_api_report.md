# Rhapsody API Validation: IRPTimingDiagram

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPTimingDiagram` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagram_types.py`)
- Members: Python `2`, Java `2`, pywin32 `1`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_elaborated() -> getIsElaborated; set_is_elaborated() -> setIsElaborated | getIsElaborated (method); setIsElaborated (method) | isElaborated (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the isElaborated property or a getter/setter fallback instead of calling getIsElaborated and setIsElaborated directly. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPTimingDiagram` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_diagram_types.py`
- **Affected call(s):** get_is_elaborated() -> getIsElaborated; set_is_elaborated() -> setIsElaborated
- **Java signature(s):** `IRPTimingDiagram.getIsElaborated()`, `IRPTimingDiagram.setIsElaborated(int)`
- **Recommended change:** Use the isElaborated property or a getter/setter fallback instead of calling getIsElaborated and setIsElaborated directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
