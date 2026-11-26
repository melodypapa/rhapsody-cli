# Rhapsody API Validation: IRPRequirement

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPRequirement` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_requirements.py`)
- Members: Python `2`, Java `2`, pywin32 `1`
- Deviation items: `1` (actionable `1`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_requirement_id() -> requirementID; set_requirement_id() -> requirementID | getRequirementID (method); setRequirementID (method) | requirementID (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPRequirement` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_requirements.py`
- **Affected call(s):** get_requirement_id() -> requirementID; set_requirement_id() -> requirementID
- **Java signature(s):** `IRPRequirement.getRequirementID()`, `IRPRequirement.setRequirementID(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
