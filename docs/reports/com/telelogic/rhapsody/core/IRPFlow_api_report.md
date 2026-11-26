# Rhapsody API Validation: IRPFlow

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPFlow` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`)
- Members: Python `17`, Java `17`, pywin32 `14`
- Deviation items: `14` (actionable `14`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_conveyed() -> getConveyed | getConveyed (method) | conveyed (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the conveyed property or a getter/setter fallback instead of calling getConveyed directly. |
| get_direction() -> direction; set_direction() -> direction | getDirection (method); setDirection (method) | direction (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_end1() -> getEnd1; set_end1() -> end1 | getEnd1 (method); setEnd1 (method) | end1 (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_end1_port() -> getEnd1Port | getEnd1Port (method) | end1Port (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the end1Port property or a getter/setter fallback instead of calling getEnd1Port directly. |
| get_end1_sys_ml_port() -> getEnd1SysMLPort | getEnd1SysMLPort (method) | end1SysMLPort (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the end1SysMLPort property or a getter/setter fallback instead of calling getEnd1SysMLPort directly. |
| get_end2() -> getEnd2; set_end2() -> end2 | getEnd2 (method); setEnd2 (method) | end2 (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_end2_port() -> getEnd2Port | getEnd2Port (method) | end2Port (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the end2Port property or a getter/setter fallback instead of calling getEnd2Port directly. |
| get_end2_sys_ml_port() -> getEnd2SysMLPort | getEnd2SysMLPort (method) | end2SysMLPort (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the end2SysMLPort property or a getter/setter fallback instead of calling getEnd2SysMLPort directly. |
| add_conveyed() -> addConveyed | — | addConveyed (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| remove_conveyed() -> removeConveyed | — | removeConveyed (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| set_end1_via_port() -> setEnd1ViaPort | — | setEnd1ViaPort (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'object'] but pywin32 declares ['com', 'com']. Match the documented COM parameter types. |
| set_end1_via_sys_ml_port() -> setEnd1ViaSysMLPort | — | setEnd1ViaSysMLPort (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'object'] but pywin32 declares ['com', 'com']. Match the documented COM parameter types. |
| set_end2_via_port() -> setEnd2ViaPort | — | setEnd2ViaPort (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'object'] but pywin32 declares ['com', 'com']. Match the documented COM parameter types. |
| set_end2_via_sys_ml_port() -> setEnd2ViaSysMLPort | — | setEnd2ViaSysMLPort (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'object'] but pywin32 declares ['com', 'com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (6) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_conveyed() -> addConveyed | addConveyed (method) | addConveyed (method) | MATCH | — |
| set_end1_via_port() -> setEnd1ViaPort | setEnd1ViaPort (method) | setEnd1ViaPort (method) | MATCH | — |
| set_end1_via_sys_ml_port() -> setEnd1ViaSysMLPort | setEnd1ViaSysMLPort (method) | setEnd1ViaSysMLPort (method) | MATCH | — |
| set_end2_via_port() -> setEnd2ViaPort | setEnd2ViaPort (method) | setEnd2ViaPort (method) | MATCH | — |
| set_end2_via_sys_ml_port() -> setEnd2ViaSysMLPort | setEnd2ViaSysMLPort (method) | setEnd2ViaSysMLPort (method) | MATCH | — |
| remove_conveyed() -> removeConveyed | removeConveyed (method) | removeConveyed (method) | MATCH | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (5 findings)
- **Target:** `IRPFlow` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** get_conveyed() -> getConveyed; get_end1_port() -> getEnd1Port; get_end1_sys_ml_port() -> getEnd1SysMLPort; get_end2_port() -> getEnd2Port; get_end2_sys_ml_port() -> getEnd2SysMLPort
- **Recommended change:** Use the conveyed property or a getter/setter fallback instead of calling getConveyed directly.
- **Recommended change:** Use the end1Port property or a getter/setter fallback instead of calling getEnd1Port directly.
- **Recommended change:** Use the end1SysMLPort property or a getter/setter fallback instead of calling getEnd1SysMLPort directly.
- **Recommended change:** Use the end2Port property or a getter/setter fallback instead of calling getEnd2Port directly.
- **Recommended change:** Use the end2SysMLPort property or a getter/setter fallback instead of calling getEnd2SysMLPort directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (3 findings)
- **Target:** `IRPFlow` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** get_direction() -> direction; set_direction() -> direction; get_end1() -> getEnd1; set_end1() -> end1; get_end2() -> getEnd2; set_end2() -> end2
- **Java signature(s):** `IRPFlow.getDirection()`, `IRPFlow.setEnd2(com.telelogic.rhapsody.core.IRPModelElement)`
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (6 findings)
- **Target:** `IRPFlow` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_activity.py`
- **Affected call(s):** add_conveyed() -> addConveyed; remove_conveyed() -> removeConveyed; set_end1_via_port() -> setEnd1ViaPort; set_end1_via_sys_ml_port() -> setEnd1ViaSysMLPort; set_end2_via_port() -> setEnd2ViaPort; set_end2_via_sys_ml_port() -> setEnd2ViaSysMLPort
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['object', 'object'] but pywin32 declares ['com', 'com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
