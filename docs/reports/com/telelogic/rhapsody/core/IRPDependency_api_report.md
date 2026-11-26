# Rhapsody API Validation: IRPDependency

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPDependency` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_dependency.py`)
- Members: Python `7`, Java `7`, pywin32 `3`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_dependent() -> dependent; set_dependent() -> setDependent | getDependent (method); setDependent (method) | dependent (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_depends_on() -> dependsOn; set_depends_on() -> setDependsOn | getDependsOn (method); setDependsOn (method) | dependsOn (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| is_need_to_migrate() -> isNeedToMigrate | isNeedToMigrate (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| set_link_type() -> setLinkType | setLinkType (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| set_owner_without_changing_dependent() -> setOwnerWithoutChangingDependent | setOwnerWithoutChangingDependent (method) | setOwnerWithoutChangingDependent (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPDependency` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_dependency.py`
- **Affected call(s):** get_dependent() -> dependent; set_dependent() -> setDependent; get_depends_on() -> dependsOn; set_depends_on() -> setDependsOn
- **Java signature(s):** `IRPDependency.getDependent()`, `IRPDependency.setDependsOn(com.telelogic.rhapsody.core.IRPModelElement)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### PYWIN32_MEMBER_MISSING (2 findings)
- **Target:** `IRPDependency` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_dependency.py`
- **Affected call(s):** is_need_to_migrate() -> isNeedToMigrate; set_link_type() -> setLinkType
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
