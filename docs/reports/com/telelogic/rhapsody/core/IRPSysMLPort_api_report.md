# Rhapsody API Validation: IRPSysMLPort

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPSysMLPort` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_other_model.py`)
- Members: Python `7`, Java `7`, pywin32 `4`
- Deviation items: `4` (actionable `4`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_reversed() -> getIsReversed; set_is_reversed() -> isReversed | getIsReversed (method); setIsReversed (method) | isReversed (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_port_direction() -> portDirection; set_port_direction() -> portDirection | getPortDirection (method); setPortDirection (method) | portDirection (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_type() -> getType; set_type() -> setType | getType (method); setType (method) | type (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the type property or a getter/setter fallback instead of calling getType and setType directly. |
| add_link() -> addLink | — | addLink (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'object', 'object', 'object', 'object'] but pywin32 declares ['com', 'com', 'com', 'com', 'com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (1) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_link() -> addLink | addLink (method) | addLink (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPSysMLPort` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_other_model.py`
- **Affected call(s):** get_is_reversed() -> getIsReversed; set_is_reversed() -> isReversed; get_port_direction() -> portDirection; set_port_direction() -> portDirection
- **Java signature(s):** `IRPSysMLPort.getIsReversed()`, `IRPSysMLPort.setPortDirection(java.lang.String)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (1 finding)
- **Target:** `IRPSysMLPort` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_other_model.py`
- **Affected call(s):** get_type() -> getType; set_type() -> setType
- **Java signature(s):** `IRPSysMLPort.getType()`, `IRPSysMLPort.setType(com.telelogic.rhapsody.core.IRPClassifier)`
- **Recommended change:** Use the type property or a getter/setter fallback instead of calling getType and setType directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (1 finding)
- **Target:** `IRPSysMLPort` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_other_model.py`
- **Affected call(s):** add_link() -> addLink
- **Recommended change:** Wrapper passes types ['object', 'object', 'object', 'object', 'object'] but pywin32 declares ['com', 'com', 'com', 'com', 'com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
