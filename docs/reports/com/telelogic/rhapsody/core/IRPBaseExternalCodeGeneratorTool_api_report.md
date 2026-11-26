# Rhapsody API Validation: IRPBaseExternalCodeGeneratorTool

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPBaseExternalCodeGeneratorTool` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`)
- Members: Python `3`, Java `3`, pywin32 `3`
- Deviation items: `0` (actionable `0`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | — | PASS | No change needed. |

<details>
<summary>Correct items (3) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| advance_code_gen_progress_bar() -> advanceCodeGenProgressBar | advanceCodeGenProgressBar (method) | advanceCodeGenProgressBar (method) | MATCH | — |
| should_abort_code_generation() -> shouldAbortCodeGeneration | shouldAbortCodeGeneration (method) | shouldAbortCodeGeneration (method) | MATCH | — |
| write_code_gen_message() -> writeCodeGenMessage | writeCodeGenMessage (method) | writeCodeGenMessage (method) | MATCH | — |

</details>

## AI Fix Guidance
No deviations require changes.
