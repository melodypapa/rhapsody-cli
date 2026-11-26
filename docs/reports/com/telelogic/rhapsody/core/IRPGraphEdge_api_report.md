# Rhapsody API Validation: IRPGraphEdge

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPGraphEdge` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `5`, Java `5`, pywin32 `5`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_source() -> getSource | getSource (method) | source (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the source property or a getter/setter fallback instead of calling getSource directly. |
| get_target() -> getTarget | getTarget (method) | target (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the target property or a getter/setter fallback instead of calling getTarget directly. |
| embed_flow() -> embedFlow | — | embedFlow (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (3) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_containing_arrow() -> getContainingArrow | getContainingArrow (method) | getContainingArrow (method) | MATCH | — |
| embed_flow() -> embedFlow | embedFlow (method) | embedFlow (method) | MATCH | — |
| embed_new_flow() -> embedNewFlow | embedNewFlow (method) | embedNewFlow (method) | MATCH | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPGraphEdge` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_source() -> getSource; get_target() -> getTarget
- **Recommended change:** Use the source property or a getter/setter fallback instead of calling getSource directly.
- **Recommended change:** Use the target property or a getter/setter fallback instead of calling getTarget directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPGraphEdge` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** embed_flow() -> embedFlow
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
