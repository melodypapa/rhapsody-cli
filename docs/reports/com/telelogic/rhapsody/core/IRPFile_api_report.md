# Rhapsody API Validation: IRPFile

## Summary
- Java package: `com.telelogic.rhapsody.core`
- Target wrapper: `IRPFile` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_files.py`)
- Members: Python `15`, Java `15`, pywin32 `14`
- Deviation items: `9` (actionable `9`, expected binding differences `0`, wrapper backlog `0`)
- Status legend: `MATCH` verified binding · `UNAVAILABLE_DOCUMENTED` pywin32 lacks the member (NotImplementedError stub) · `ALIAS_DOCUMENTED` documented alias · actionable rows are named by code in `Comparison details`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| get_elements() -> elements | getElements (method) | elements (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_file_fragments() -> fileFragments | getFileFragments (method) | fileFragments (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_file_type() -> fileType; set_file_type() -> fileType | getFileType (method); setFileType (method) | fileType (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_files() -> files | getFiles (method) | files (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members. |
| get_path() -> getPath; set_path() -> path; set_path() -> setPath | getPath (method); setPath (method) | path (method); setPath (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |
| add_element() -> addElement | — | addElement (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'str'] but pywin32 declares ['com', 'str']. Match the documented COM parameter types. |
| add_model_element() -> addModelElement | — | addModelElement (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object', 'str'] but pywin32 declares ['com', 'str']. Match the documented COM parameter types. |
| add_package_to_scope() -> addPackageToScope | — | addPackageToScope (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |
| add_to_scope() -> addToScope | — | addToScope (method) | SIGNATURE_TYPE_MISMATCH | Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types. |

<details>
<summary>Correct items (8) — bindings verified against pywin32</summary>


## Correct Items

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| add_element() -> addElement | addElement (method) | addElement (method) | MATCH | — |
| add_model_element() -> addModelElement | addModelElement (method) | addModelElement (method) | MATCH | — |
| add_package_to_scope() -> addPackageToScope | addPackageToScope (method) | addPackageToScope (method) | MATCH | — |
| add_text_element() -> addTextElement | addTextElement (method) | addTextElement (method) | MATCH | — |
| add_to_scope() -> addToScope | addToScope (method) | addToScope (method) | MATCH | — |
| get_imp_name() -> getImpName | getImpName (method) | getImpName (method) | MATCH | — |
| is_empty() -> isEmpty | isEmpty (method) | isEmpty (method) | MATCH | — |
| get_spec_name() -> getSpecName | getSpecName (method) | getSpecName (method) | MATCH | — |

</details>

## AI Fix Guidance

### ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH (4 findings)
- **Target:** `IRPFile` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_files.py`
- **Affected call(s):** get_elements() -> elements; get_file_fragments() -> fileFragments; get_file_type() -> fileType; set_file_type() -> fileType; get_files() -> files
- **Recommended change:** Expose the member with the COM shape: use @property for property-shaped COM members (setter only when writable) and a plain method for method-shaped members.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### ACCESSOR_ALIAS_MISMATCH (1 finding)
- **Target:** `IRPFile` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_files.py`
- **Affected call(s):** get_path() -> getPath; set_path() -> path; set_path() -> setPath
- **Java signature(s):** `IRPFile.getPath(int)`, `IRPFile.setPath(java.lang.String)`
- **Recommended change:** Review the related API spellings and document the intended mapping.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### SIGNATURE_TYPE_MISMATCH (4 findings)
- **Target:** `IRPFile` in `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_files.py`
- **Affected call(s):** add_element() -> addElement; add_model_element() -> addModelElement; add_package_to_scope() -> addPackageToScope; add_to_scope() -> addToScope
- **Recommended change:** Wrapper passes types ['object', 'str'] but pywin32 declares ['com', 'str']. Match the documented COM parameter types.
- **Recommended change:** Wrapper passes types ['object'] but pywin32 declares ['com']. Match the documented COM parameter types.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
