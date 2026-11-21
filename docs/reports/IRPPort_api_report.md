# Rhapsody API Validation: IRPPort

## Summary
- Target wrapper: `RPPort` (`src/rhapsody_cli/models/elements/relations/model_port.py`)
- Members: Python `14`, Java `14`, pywin32 `9`
- Deviations: `1`
- Deviations by status:
  - `PYWIN32_MEMBER_MISSING`: 1

- Informational binding differences (expected): `0`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_contract() -> contract; get_contract() -> getContract; set_contract() -> contract; set_contract() -> setContract | getContract (method); setContract (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_provided_interface() -> addProvidedInterface | addProvidedInterface (method) | addProvidedInterface (method) | MATCH | — |
| add_required_interface() -> addRequiredInterface | addRequiredInterface (method) | addRequiredInterface (method) | MATCH | — |
| get_is_behavioral() -> isBehavioral; set_is_behavioral() -> isBehavioral | getIsBehavioral (method); setIsBehavioral (method) | isBehavioral (property) | MATCH | — |
| get_is_reversed() -> isReversed; set_is_reversed() -> isReversed | getIsReversed (method); setIsReversed (method) | isReversed (property) | MATCH | — |
| get_port_contract() -> portContract; set_port_contract() -> portContract | getPortContract (method); setPortContract (method) | portContract (property) | MATCH | — |
| get_provided_interfaces() -> providedInterfaces | getProvidedInterfaces (method) | providedInterfaces (property) | MATCH | — |
| get_required_interfaces() -> requiredInterfaces | getRequiredInterfaces (method) | requiredInterfaces (property) | MATCH | — |
| remove_provided_interface() -> removeProvidedInterface | removeProvidedInterface (method) | removeProvidedInterface (method) | MATCH | — |
| remove_required_interface() -> removeRequiredInterface | removeRequiredInterface (method) | removeRequiredInterface (method) | MATCH | — |

## AI Fix Guidance

### Finding 1: PYWIN32_MEMBER_MISSING
- **Target:** `RPPort` in `src/rhapsody_cli/models/elements/relations/model_port.py`
- **Current Python wrapper/COM call:** get_contract() -> contract; get_contract() -> getContract; set_contract() -> contract; set_contract() -> setContract
- **Expected Python method(s):** `get_contract`, `set_contract`
- **Java signature(s):** `IRPPort.getContract()`, `IRPPort.setContract(com.telelogic.rhapsody.core.IRPClass)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
