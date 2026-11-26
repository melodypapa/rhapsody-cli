# Rhapsody API Validation: IRPInterfaceItem

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPInterfaceItem` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_interface_item.py`)
- Members: Python `7`, Java `7`, pywin32 `7`
- Deviation items: `0` (actionable `0`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (7) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_argument() -> addArgument | addArgument (method) | addArgument (method) | MATCH | — |
| add_argument_before_position() -> addArgumentBeforePosition | addArgumentBeforePosition (method) | addArgumentBeforePosition (method) | MATCH | — |
| arguments (property) -> arguments | getArguments (method) | arguments (property) | MATCH | — |
| match_on_signature() -> matchOnSignature | matchOnSignature (method) | matchOnSignature (method) | MATCH | — |
| signature (property) -> signature | getSignature (method) | signature (property) | MATCH | — |
| get_signature_no_arg_names() -> getSignatureNoArgNames | getSignatureNoArgNames (method) | getSignatureNoArgNames (method) | MATCH | — |
| get_signature_no_arg_types() -> getSignatureNoArgTypes | getSignatureNoArgTypes (method) | getSignatureNoArgTypes (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
