# Rhapsody API Validation: IRPOperation

## Summary
- Target wrapper: `RPOperation` (`src/rhapsody_cli/models/elements/classifiers/model_operation.py`)
- Members: Python `32`, Java `32`, pywin32 `21`
- Deviations: `1`
- Deviations by status:
  - `PYWIN32_MEMBER_MISSING`: 1

- Informational binding differences (expected): `3`
- Wrapper backlog (supported members without wrappers): `0`
- Documented aliases: `0`, documented unavailable: `0`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer | updateContainedDiagramsOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_is_const() -> isConst; set_is_const() -> setIsConst | getIsConst (method); setIsConst (method) | isConst (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_final() -> isFinal; set_is_final() -> setIsFinal | getIsFinal (method); setIsFinal (method) | isFinal (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_visibility() -> visibility; set_visibility() -> setVisibility | getVisibility (method); setVisibility (method) | visibility (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | — | — |

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
| get_is_ctor() -> isCtor | getIsCtor (method) | isCtor (property) | MATCH | — |
| get_is_dtor() -> isDtor | getIsDtor (method) | isDtor (property) | MATCH | — |
| get_is_inline() -> isInline | getIsInline (method) | isInline (property) | MATCH | — |
| get_is_static() -> isStatic; set_is_static() -> isStatic | getIsStatic (method); setIsStatic (method) | isStatic (property) | MATCH | — |
| get_is_trigger() -> isTrigger | getIsTrigger (method) | isTrigger (property) | MATCH | — |
| get_is_virtual() -> isVirtual; set_is_virtual() -> isVirtual | getIsVirtual (method); setIsVirtual (method) | isVirtual (property) | MATCH | — |
| get_return_type_declaration() -> getReturnTypeDeclaration; set_return_type_declaration() -> setReturnTypeDeclaration | getReturnTypeDeclaration (method); setReturnTypeDeclaration (method) | getReturnTypeDeclaration (method); setReturnTypeDeclaration (method) | MATCH | — |
| get_returns() -> returns; set_returns() -> returns | getReturns (method); setReturns (method) | returns (property) | MATCH | — |

## AI Fix Guidance

### Finding 1: PYWIN32_MEMBER_MISSING
- **Target:** `RPOperation` in `src/rhapsody_cli/models/elements/classifiers/model_operation.py`
- **Current Python wrapper/COM call:** update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer
- **Expected Python method(s):** `update_contained_diagrams_on_server`
- **Java signature(s):** `IRPOperation.updateContainedDiagramsOnServer(int)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
