# Rhapsody API Validation: IRPGeneralization

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPGeneralization` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_generalization.py`)
- Members: Python `10`, Java `10`, pywin32 `5`
- Deviation items: `5` (actionable `5`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_base_class() -> baseClass; set_base_class() -> setBaseClass | getBaseClass (method); setBaseClass (method) | baseClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_derived_class() -> derivedClass; set_derived_class() -> setDerivedClass | getDerivedClass (method); setDerivedClass (method) | derivedClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_extension_point() -> extensionPoint; set_extension_point() -> setExtensionPoint | getExtensionPoint (method); setExtensionPoint (method) | extensionPoint (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_is_virtual() -> isVirtual; set_is_virtual() -> setIsVirtual | getIsVirtual (method); setIsVirtual (method) | isVirtual (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_visibility() -> visibility; set_visibility() -> setVisibility | getVisibility (method); setVisibility (method) | visibility (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (5 findings)
- **Target:** `IRPGeneralization` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_generalization.py`
- **Affected call(s):** get_base_class() -> baseClass; set_base_class() -> setBaseClass; get_derived_class() -> derivedClass; set_derived_class() -> setDerivedClass; get_extension_point() -> extensionPoint; set_extension_point() -> setExtensionPoint; get_is_virtual() -> isVirtual; set_is_virtual() -> setIsVirtual; get_visibility() -> visibility; set_visibility() -> setVisibility
- **Java signature(s):** `IRPGeneralization.getBaseClass()`, `IRPGeneralization.setVisibility(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
