# Rhapsody API Validation: IRPOperation

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPOperation` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_operation.py`)
- Members: Python `32`, Java `32`, pywin32 `21`
- Deviation items: `1` (actionable `0`, expected binding differences `1`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| update_contained_diagrams_on_server() (no static COM member) | updateContainedDiagramsOnServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

<details>
<summary>Correct items (20) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| create_auto_flow_chart() -> createAutoFlowChart | createAutoFlowChart (method) | createAutoFlowChart (method) | MATCH | — |
| delete_argument() -> deleteArgument | deleteArgument (method) | deleteArgument (method) | MATCH | — |
| delete_flowchart() -> deleteFlowchart | deleteFlowchart (method) | deleteFlowchart (method) | MATCH | — |
| get_body() -> body; set_body() -> body | getBody (method); setBody (method) | body (property) | MATCH | — |
| get_flowchart() -> flowchart; set_flowchart() -> flowchart | getFlowchart (method); setFlowchart (method) | flowchart (property) | MATCH | — |
| get_implementation_signature() -> getImplementationSignature | getImplementationSignature (method) | getImplementationSignature (method) | MATCH | — |
| get_initializer() -> initializer; set_initializer() -> initializer | getInitializer (method); setInitializer (method) | initializer (property) | MATCH | — |
| get_is_abstract() -> isAbstract; set_is_abstract() -> isAbstract | getIsAbstract (method); setIsAbstract (method) | isAbstract (property) | MATCH | — |
| get_is_cg_derived() -> isCgDerived | getIsCgDerived (method) | isCgDerived (property) | MATCH | — |
| get_is_const() -> isConst; set_is_const() -> isConst | getIsConst (method); setIsConst (method) | isConst (property) | MATCH | — |
| get_is_ctor() -> isCtor | getIsCtor (method) | isCtor (property) | MATCH | — |
| get_is_dtor() -> isDtor | getIsDtor (method) | isDtor (property) | MATCH | — |
| get_is_final() -> isFinal; set_is_final() -> isFinal | getIsFinal (method); setIsFinal (method) | isFinal (property) | MATCH | — |
| get_is_inline() -> isInline | getIsInline (method) | isInline (property) | MATCH | — |
| get_is_static() -> isStatic; set_is_static() -> isStatic | getIsStatic (method); setIsStatic (method) | isStatic (property) | MATCH | — |
| get_is_trigger() -> isTrigger | getIsTrigger (method) | isTrigger (property) | MATCH | — |
| get_is_virtual() -> isVirtual; set_is_virtual() -> isVirtual | getIsVirtual (method); setIsVirtual (method) | isVirtual (property) | MATCH | — |
| get_return_type_declaration() -> getReturnTypeDeclaration; set_return_type_declaration() -> setReturnTypeDeclaration | getReturnTypeDeclaration (method); setReturnTypeDeclaration (method) | getReturnTypeDeclaration (method); setReturnTypeDeclaration (method) | MATCH | — |
| get_returns() -> returns; set_returns() -> returns | getReturns (method); setReturns (method) | returns (property) | MATCH | — |
| get_visibility() -> visibility; set_visibility() -> visibility | getVisibility (method); setVisibility (method) | visibility (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
