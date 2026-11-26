# Rhapsody API Validation: IRPOperation

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPOperation` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_operation.py`)
- Members: Python `22`, Java `32`, pywin32 `21`
- Deviation items: `1` (actionable `0`, expected binding differences `1`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (20) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| body (property) -> body | getBody (method); setBody (method) | body (property) | MATCH | — |
| create_auto_flow_chart() -> createAutoFlowChart | createAutoFlowChart (method) | createAutoFlowChart (method) | MATCH | — |
| delete_argument() -> deleteArgument | deleteArgument (method) | deleteArgument (method) | MATCH | — |
| delete_flowchart() -> deleteFlowchart | deleteFlowchart (method) | deleteFlowchart (method) | MATCH | — |
| flowchart (property) -> flowchart | getFlowchart (method); setFlowchart (method) | flowchart (property) | MATCH | — |
| get_implementation_signature() -> getImplementationSignature | getImplementationSignature (method) | getImplementationSignature (method) | MATCH | — |
| initializer (property) -> initializer | getInitializer (method); setInitializer (method) | initializer (property) | MATCH | — |
| is_abstract (property) -> isAbstract | getIsAbstract (method); setIsAbstract (method) | isAbstract (property) | MATCH | — |
| is_cg_derived (property) -> isCgDerived | getIsCgDerived (method) | isCgDerived (property) | MATCH | — |
| is_const (property) -> isConst | getIsConst (method); setIsConst (method) | isConst (property) | MATCH | — |
| is_ctor (property) -> isCtor | getIsCtor (method) | isCtor (property) | MATCH | — |
| is_dtor (property) -> isDtor | getIsDtor (method) | isDtor (property) | MATCH | — |
| is_final (property) -> isFinal | getIsFinal (method); setIsFinal (method) | isFinal (property) | MATCH | — |
| is_inline (property) -> isInline | getIsInline (method) | isInline (property) | MATCH | — |
| is_static (property) -> isStatic | getIsStatic (method); setIsStatic (method) | isStatic (property) | MATCH | — |
| is_trigger (property) -> isTrigger | getIsTrigger (method) | isTrigger (property) | MATCH | — |
| is_virtual (property) -> isVirtual | getIsVirtual (method); setIsVirtual (method) | isVirtual (property) | MATCH | — |
| get_return_type_declaration() -> getReturnTypeDeclaration; set_return_type_declaration() -> setReturnTypeDeclaration | getReturnTypeDeclaration (method); setReturnTypeDeclaration (method) | getReturnTypeDeclaration (method); setReturnTypeDeclaration (method) | MATCH | — |
| returns (property) -> returns | getReturns (method); setReturns (method) | returns (property) | MATCH | — |
| visibility (property) -> visibility | getVisibility (method); setVisibility (method) | visibility (property) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
