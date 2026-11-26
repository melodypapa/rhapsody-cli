# Rhapsody API Validation: IRPComponentInstance

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPComponentInstance` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component_instance.py`)
- Members: Python `3`, Java `3`, pywin32 `2`
- Deviation items: `2` (actionable `2`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_component_type() -> getComponentType; set_component_type() -> setComponentType | getComponentType (method); setComponentType (method) | componentType (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the componentType property or a getter/setter fallback instead of calling getComponentType and setComponentType directly. |
| get_node() -> getNode | getNode (method) | node (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the node property or a getter/setter fallback instead of calling getNode directly. |

<details>
<summary>Correct items (0) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

</details>

## AI Fix Guidance

### COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (2 findings)
- **Target:** `IRPComponentInstance` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_component_instance.py`
- **Affected call(s):** get_component_type() -> getComponentType; set_component_type() -> setComponentType; get_node() -> getNode
- **Java signature(s):** `IRPComponentInstance.getComponentType()`
- **Recommended change:** Use the componentType property or a getter/setter fallback instead of calling getComponentType and setComponentType directly.
- **Recommended change:** Use the node property or a getter/setter fallback instead of calling getNode directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
