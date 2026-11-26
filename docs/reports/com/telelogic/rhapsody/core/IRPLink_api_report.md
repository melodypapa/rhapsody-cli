# Rhapsody API Validation: IRPLink

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPLink` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`)
- Members: Python `19`, Java `19`, pywin32 `15`
- Deviation items: `15` (actionable `15`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_end1_multiplicity() -> end1Multiplicity; set_end1_multiplicity() -> end1Multiplicity | getEnd1Multiplicity (method); setEnd1Multiplicity (method) | end1Multiplicity (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_end1_name() -> end1Name; set_end1_name() -> end1Name | getEnd1Name (method); setEnd1Name (method) | end1Name (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_end2_multiplicity() -> end2Multiplicity; set_end2_multiplicity() -> end2Multiplicity | getEnd2Multiplicity (method); setEnd2Multiplicity (method) | end2Multiplicity (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_end2_name() -> end2Name; set_end2_name() -> end2Name | getEnd2Name (method); setEnd2Name (method) | end2Name (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_from() -> getFrom | getFrom (method) | From (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the From property or a getter/setter fallback instead of calling getFrom directly. |
| get_from_element() -> getFromElement | getFromElement (method) | fromElement (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the fromElement property or a getter/setter fallback instead of calling getFromElement directly. |
| get_from_port() -> getFromPort | getFromPort (method) | fromPort (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the fromPort property or a getter/setter fallback instead of calling getFromPort directly. |
| get_from_sys_ml_port() -> getFromSysMLPort | getFromSysMLPort (method) | fromSysMLPort (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the fromSysMLPort property or a getter/setter fallback instead of calling getFromSysMLPort directly. |
| get_instantiates() -> getInstantiates; set_instantiates() -> setInstantiates | getInstantiates (method); setInstantiates (method) | instantiates (property); setInstantiates (method) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_other() -> getOther | getOther (method) | other (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the other property or a getter/setter fallback instead of calling getOther directly. |
| get_to() -> getTo | getTo (method) | to (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the to property or a getter/setter fallback instead of calling getTo directly. |
| get_to_element() -> getToElement | getToElement (method) | toElement (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the toElement property or a getter/setter fallback instead of calling getToElement directly. |
| get_to_port() -> getToPort | getToPort (method) | toPort (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the toPort property or a getter/setter fallback instead of calling getToPort directly. |
| get_to_sys_ml_port() -> getToSysMLPort | getToSysMLPort (method) | toSysMLPort (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the toSysMLPort property or a getter/setter fallback instead of calling getToSysMLPort directly. |
| set_instantiates() -> setInstantiates | — | setInstantiates (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (5 findings)
- **Target:** `IRPLink` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_end1_multiplicity() -> end1Multiplicity; set_end1_multiplicity() -> end1Multiplicity; get_end1_name() -> end1Name; set_end1_name() -> end1Name; get_end2_multiplicity() -> end2Multiplicity; set_end2_multiplicity() -> end2Multiplicity; get_end2_name() -> end2Name; set_end2_name() -> end2Name; get_instantiates() -> getInstantiates; set_instantiates() -> setInstantiates
- **Java signature(s):** `IRPLink.getEnd1Multiplicity()`, `IRPLink.setInstantiates(com.telelogic.rhapsody.core.IRPRelation)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (9 findings)
- **Target:** `IRPLink` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** get_from() -> getFrom; get_from_element() -> getFromElement; get_from_port() -> getFromPort; get_from_sys_ml_port() -> getFromSysMLPort; get_other() -> getOther; get_to() -> getTo; get_to_element() -> getToElement; get_to_port() -> getToPort; get_to_sys_ml_port() -> getToSysMLPort
- **Recommended change:** Use the From property or a getter/setter fallback instead of calling getFrom directly.
- **Recommended change:** Use the fromElement property or a getter/setter fallback instead of calling getFromElement directly.
- **Recommended change:** Use the fromPort property or a getter/setter fallback instead of calling getFromPort directly.
- **Recommended change:** Use the fromSysMLPort property or a getter/setter fallback instead of calling getFromSysMLPort directly.
- **Recommended change:** Use the other property or a getter/setter fallback instead of calling getOther directly.
- **Recommended change:** Use the to property or a getter/setter fallback instead of calling getTo directly.
- **Recommended change:** Use the toElement property or a getter/setter fallback instead of calling getToElement directly.
- **Recommended change:** Use the toPort property or a getter/setter fallback instead of calling getToPort directly.
- **Recommended change:** Use the toSysMLPort property or a getter/setter fallback instead of calling getToSysMLPort directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPLink` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_graphics.py`
- **Affected call(s):** set_instantiates() -> setInstantiates
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
