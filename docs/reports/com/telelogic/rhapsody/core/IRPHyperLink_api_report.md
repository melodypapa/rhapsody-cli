# Rhapsody API Validation: IRPHyperLink

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPHyperLink` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_hyperlink.py`)
- Members: Python `5`, Java `8`, pywin32 `4`
- Deviation items: `6` (actionable `3`, expected binding differences `3`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| set_display_option() -> setDisplayOption | getDisplayOption (method); setDisplayOption (method) | getDisplayOption (method); setDisplayOption (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_target() -> target; set_target() -> setTarget | getTarget (method); setTarget (method) | target (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_url() -> getURL; set_url() -> setURL | getURL (method); setURL (method) | URL (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the URL property or a getter/setter fallback instead of calling getURL and setURL directly. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### PYTHON_METHOD_NAME_MISMATCH (1 finding)
- **Target:** `IRPHyperLink` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_hyperlink.py`
- **Affected call(s):** set_display_option() -> setDisplayOption
- **Java signature(s):** `IRPHyperLink.getDisplayOption(char, java.lang.String)`, `IRPHyperLink.setDisplayOption(char, java.lang.String)`
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPHyperLink` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_hyperlink.py`
- **Affected call(s):** get_target() -> target; set_target() -> setTarget
- **Java signature(s):** `IRPHyperLink.getTarget()`, `IRPHyperLink.setTarget(com.telelogic.rhapsody.core.IRPModelElement)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPHyperLink` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_hyperlink.py`
- **Affected call(s):** get_url() -> getURL; set_url() -> setURL
- **Java signature(s):** `IRPHyperLink.getURL()`, `IRPHyperLink.setURL(java.lang.String)`
- **Recommended change:** Use the URL property or a getter/setter fallback instead of calling getURL and setURL directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
