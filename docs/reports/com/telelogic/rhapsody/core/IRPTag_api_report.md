# Rhapsody API Validation: IRPTag

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPTag` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_variables.py`)
- Members: Python `8`, Java `9`, pywin32 `6`
- Deviation items: `6` (actionable `6`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_base() -> base | getBase (method) | base (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_from_profile() -> fromProfile | getFromProfile (method) | fromProfile (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_multiplicity() -> multiplicity; set_multiplicity() -> multiplicity | getMultiplicity (method); setMultiplicity (method) | multiplicity (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| — | setTagContextValue (method) | setTagContextValue (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| get_tag_meta_class() -> tagMetaClass; set_tag_meta_class() -> tagMetaClass | getTagMetaClass (method); setTagMetaClass (method) | tagMetaClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_value() -> value; set_value() -> value | getValue (method); setValue (method) | value (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (5 findings)
- **Target:** `IRPTag` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_variables.py`
- **Affected call(s):** get_base() -> base; get_from_profile() -> fromProfile; get_multiplicity() -> multiplicity; set_multiplicity() -> multiplicity; get_tag_meta_class() -> tagMetaClass; set_tag_meta_class() -> tagMetaClass; get_value() -> value; set_value() -> value
- **Java signature(s):** `IRPTag.setValue(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### MISSING_PYTHON_WRAPPER (1 finding)
- **Target:** `IRPTag` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_variables.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPTag.setTagContextValue(com.telelogic.rhapsody.core.IRPCollection, com.telelogic.rhapsody.core.IRPCollection)`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
