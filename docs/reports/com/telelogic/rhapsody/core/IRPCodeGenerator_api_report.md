# Rhapsody API Validation: IRPCodeGenerator

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPCodeGenerator` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`)
- Members: Python `2`, Java `3`, pywin32 `3`
- Deviation items: `3` (actionable `3`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| — | getInterfaceName (method) | interfaceName (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH | Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale. |
| get_code_annotations() -> getCodeAnnotations | — | getCodeAnnotations (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'int'] but pywin32 declares ['com', 'int']. Match the documented COM parameter types. |
| get_generated_file_names() -> getGeneratedFileNames | — | getGeneratedFileNames (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (2) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| get_code_annotations() -> getCodeAnnotations | getCodeAnnotations (method) | getCodeAnnotations (method) | MATCH | — |
| get_generated_file_names() -> getGeneratedFileNames | getGeneratedFileNames (method) | getGeneratedFileNames (method) | MATCH | — |

</details>

## AI Fix Guidance

### MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPCodeGenerator` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** —
- **Java signature(s):** `IRPCodeGenerator.getInterfaceName()`
- **Recommended change:** Implement the Python wrapper, or record the Java member in documented_intentionally_unsupported with a rationale.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (2 findings)
- **Target:** `IRPCodeGenerator` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_codegen.py`
- **Affected call(s):** get_code_annotations() -> getCodeAnnotations; get_generated_file_names() -> getGeneratedFileNames
- **Recommended change:** Wrapper passes types ['object', 'int'] but pywin32 declares ['com', 'int']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
