# Rhapsody API Validation: IRPSelection

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPSelection` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`)
- Members: Python `8`, Java `9`, pywin32 `9`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |

<details>
<summary>Correct items (8) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| can_copy() -> canCopy | canCopy (method) | canCopy (method) | MATCH | — |
| can_cut() -> canCut | canCut (method) | canCut (method) | MATCH | — |
| can_delete() -> canDelete | canDelete (method) | canDelete (method) | MATCH | — |
| can_paste() -> canPaste | canPaste (method) | canPaste (method) | MATCH | — |
| copy_selected() -> copySelected | copySelected (method) | copySelected (method) | MATCH | — |
| cut_selected() -> cutSelected | cutSelected (method) | cutSelected (method) | MATCH | — |
| delete_selected() -> deleteSelected | deleteSelected (method) | deleteSelected (method) | MATCH | — |
| paste_selected() -> pasteSelected | pasteSelected (method) | pasteSelected (method) | MATCH | — |

</details>

## AI Fix Guidance

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPSelection` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_ide.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPSelection.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
