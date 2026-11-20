# Rhapsody API Validation: IRPClassifier

## Summary
- Target wrapper: `RPClassifier` (`src/rhapsody_cli/models/elements/classifiers/model_classifier.py`)
- Members: Python `190`, Java `193`, pywin32 `177`
- Deviations: `74`
- Deviations by status:
  - `ACCESSOR_ALIAS_MISMATCH`: 58
  - `COM_MEMBER_NOT_EXPOSED`: 3
  - `METHOD_PROPERTY_MISMATCH`: 56
  - `MISSING_PYTHON_WRAPPER`: 6
  - `PYTHON_METHOD_NAME_MISMATCH`: 1
  - `PYTHON_ONLY_MEMBER`: 8
  - `PYWIN32_MEMBER_MISSING`: 1
  - `PYWIN32_ONLY_MEMBER`: 2

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| is_a_template() -> aTemplate | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_activity_diagram() -> activityDiagram; get_activity_diagram() -> getActivityDiagram | getActivityDiagram (method) | activityDiagram (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_all_tags() -> allTags; get_all_tags() -> getAllTags | getAllTags (method) | allTags (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_annotations() -> annotations; get_annotations() -> getAnnotations | getAnnotations (method) | annotations (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_association_classes() -> associationClasses; get_association_classes() -> getAssociationClasses | getAssociationClasses (method) | associationClasses (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_attributes() -> attributes; get_attributes() -> getAttributes | getAttributes (method) | attributes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_base_classifiers() -> baseClassifiers; get_base_classifiers() -> getBaseClassifiers | getBaseClassifiers (method) | baseClassifiers (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_behavioral_diagrams() -> behavioralDiagrams; get_behavioral_diagrams() -> getBehavioralDiagrams | getBehavioralDiagrams (method) | behavioralDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_binary_id() -> binaryID; get_binary_id() -> getBinaryID | getBinaryID (method) | BinaryID (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the BinaryID property or a getter/setter fallback instead of calling binaryID and getBinaryID directly. |
| get_cm_header() -> cMHeader; get_cm_header() -> getCMHeader; set_cm_header() -> cMHeader; set_cm_header() -> setCMHeader | getCMHeader (method); setCMHeader (method) | CMHeader (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the CMHeader property or a getter/setter fallback instead of calling cMHeader and getCMHeader and setCMHeader directly. |
| get_constraints() -> constraints; get_constraints() -> getConstraints | getConstraints (method) | constraints (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_constraints_by_him() -> constraintsByHim; get_constraints_by_him() -> getConstraintsByHim | getConstraintsByHim (method) | constraintsByHim (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_controlled_files() -> controlledFiles; get_controlled_files() -> getControlledFiles | getControlledFiles (method) | controlledFiles (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | createOSLCLink (method) | createOSLCLink (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_current_directory() -> currentDirectory; get_current_directory() -> getCurrentDirectory | getCurrentDirectory (method) | currentDirectory (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | — | deleteActivityDiagram (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | deleteOSLCLink (method) | deleteOSLCLink (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | — | deleteStatechart (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| get_dependencies() -> dependencies; get_dependencies() -> getDependencies | getDependencies (method) | dependencies (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_derived_classifiers() -> derivedClassifiers; get_derived_classifiers() -> getDerivedClassifiers | getDerivedClassifiers (method) | derivedClassifiers (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description() -> description; get_description() -> getDescription; set_description() -> description; set_description() -> setDescription | getDescription (method); setDescription (method) | description (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML | getDescriptionHTML (method); setDescriptionHTML (method) | descriptionHTML (property) | PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_description_plain_text() -> descriptionPlainText; get_description_plain_text() -> getDescriptionPlainText | getDescriptionPlainText (method) | descriptionPlainText (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description_rtf() -> descriptionRTF; get_description_rtf() -> getDescriptionRTF; is_description_rtf() -> descriptionRTF; set_description_rtf() -> descriptionRTF; set_description_rtf() -> setDescriptionRTF | getDescriptionRTF (method); setDescriptionRTF (method) | descriptionRTF (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_display_name() -> displayName; get_display_name() -> getDisplayName; set_display_name() -> displayName; set_display_name() -> setDisplayName | getDisplayName (method); setDisplayName (method) | displayName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_filename() -> filename; get_filename() -> getFilename; set_filename() -> filename; set_filename() -> setFilename | getFilename (method); setFilename (method) | filename (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_flow_items() -> flowItems; get_flow_items() -> getFlowItems | getFlowItems (method) | flowItems (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_flows() -> flows; get_flows() -> getFlows | getFlows (method) | flows (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_guid() -> GUID; get_guid() -> getGUID; set_guid() -> GUID; set_guid() -> setGUID | getGUID (method); setGUID (method) | GUID (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_generalizations() -> generalizations; get_generalizations() -> getGeneralizations | getGeneralizations (method) | generalizations (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_hyper_links() -> getHyperLinks; get_hyper_links() -> hyperLinks | getHyperLinks (method) | hyperLinks (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_include_in_next_load() -> getIncludeInNextLoad; get_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> setIncludeInNextLoad | getIncludeInNextLoad (method); setIncludeInNextLoad (method) | includeInNextLoad (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_interface_items() -> getInterfaceItems; get_interface_items() -> interfaceItems | getInterfaceItems (method) | interfaceItems (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_interface_name() -> getInterfaceName; get_interface_name() -> interfaceName | getInterfaceName (method) | interfaceName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_external() -> getIsExternal; get_is_external() -> isExternal | getIsExternal (method) | isExternal (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_of_meta_class() -> getIsOfMetaClass | getIsOfMetaClass (method) | isOfMetaClass (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_is_show_display_name() -> getIsShowDisplayName; get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> setIsShowDisplayName | getIsShowDisplayName (method); setIsShowDisplayName (method) | isShowDisplayName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_stub() -> getIsStub; get_is_stub() -> isStub | getIsStub (method) | isStub (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_unresolved() -> getIsUnresolved; get_is_unresolved() -> isUnresolved | getIsUnresolved (method) | isUnresolved (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_links() -> getLinks; get_links() -> links | getLinks (method) | links (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_local_tags() -> getLocalTags; get_local_tags() -> localTags | getLocalTags (method) | localTags (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | lockOnDesignManager (method) | lockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_main_diagram() -> getMainDiagram; get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram; set_main_diagram() -> setMainDiagram | getMainDiagram (method); setMainDiagram (method) | mainDiagram (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_meta_class() -> getMetaClass; get_meta_class() -> metaClass | getMetaClass (method) | metaClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_modified() -> modified | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_name() -> getName; get_name() -> name; set_name() -> name; set_name() -> setName | getName (method); setName (method) | name (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nested_classifiers() -> getNestedClassifiers; get_nested_classifiers() -> nestedClassifiers | getNestedClassifiers (method) | nestedClassifiers (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | getOSLCLinks (method) | getOSLCLinks (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_of_template() -> getOfTemplate; get_of_template() -> ofTemplate; set_of_template() -> ofTemplate; set_of_template() -> setOfTemplate | getOfTemplate (method); setOfTemplate (method) | ofTemplate (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_operations() -> getOperations; get_operations() -> operations | getOperations (method) | operations (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_owner() -> getOwner; get_owner() -> owner; set_owner() -> owner; set_owner() -> setOwner | getOwner (method); setOwner (method) | owner (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_ports() -> getPorts; get_ports() -> ports | getPorts (method) | ports (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_project() -> getProject; get_project() -> project | getProject (method) | project (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| create_oslc_link() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| delete_oslc_link() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_oslc_links() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| set_description_html() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| is_reference_unit() -> referenceUnit | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_references() -> getReferences; get_references() -> references | getReferences (method) | references (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_relations() -> getRelations; get_relations() -> relations | getRelations (method) | relations (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_remote() -> remote | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_requirement_traceability_handle() -> getRequirementTraceabilityHandle; get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> setRequirementTraceabilityHandle | getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method) | requirementTraceabilityHandle (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl | getRmmUrl (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_sequence_diagrams() -> getSequenceDiagrams; get_sequence_diagrams() -> sequenceDiagrams | getSequenceDiagrams (method) | sequenceDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_source_artifacts() -> getSourceArtifacts; get_source_artifacts() -> sourceArtifacts | getSourceArtifacts (method) | sourceArtifacts (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_statechart() -> getStatechart; get_statechart() -> statechart | getStatechart (method) | statechart (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | getStereotype (method); setStereotype (method) | stereotype (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_stereotypes() -> getStereotypes; get_stereotypes() -> stereotypes | getStereotypes (method) | stereotypes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_structure_diagrams() -> getStructureDiagrams; get_structure_diagrams() -> structureDiagrams | getStructureDiagrams (method) | structureDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_template_parameters() -> getTemplateParameters; get_template_parameters() -> templateParameters | getTemplateParameters (method) | templateParameters (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_ti() -> getTi; get_ti() -> ti; set_ti() -> setTi; set_ti() -> ti | getTi (method); setTi (method) | ti (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_unit_path() -> getUnitPath; set_unit_path() -> setUnitPath; set_unit_path() -> unitPath | getUnitPath (method); setUnitPath (method) | setUnitPath (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |
| — | unlockOnDesignManager (method) | unlockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_user_defined_meta_class() -> getUserDefinedMetaClass; get_user_defined_meta_class() -> userDefinedMetaClass | getUserDefinedMetaClass (method) | userDefinedMetaClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |

## AI Fix Guidance

### Finding 1: PYTHON_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** is_a_template() -> aTemplate
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_activity_diagram() -> activityDiagram; get_activity_diagram() -> getActivityDiagram
- **Expected Python method(s):** `get_activity_diagram`
- **Java signature(s):** `IRPClassifier.getActivityDiagram()`
- **pywin32 member(s):** activityDiagram (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 3: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_all_tags() -> allTags; get_all_tags() -> getAllTags
- **Expected Python method(s):** `get_all_tags`
- **Java signature(s):** `IRPModelElement.getAllTags()`
- **pywin32 member(s):** allTags (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 4: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_annotations() -> annotations; get_annotations() -> getAnnotations
- **Expected Python method(s):** `get_annotations`
- **Java signature(s):** `IRPModelElement.getAnnotations()`
- **pywin32 member(s):** annotations (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 5: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_association_classes() -> associationClasses; get_association_classes() -> getAssociationClasses
- **Expected Python method(s):** `get_association_classes`
- **Java signature(s):** `IRPModelElement.getAssociationClasses()`
- **pywin32 member(s):** associationClasses (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 6: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_attributes() -> attributes; get_attributes() -> getAttributes
- **Expected Python method(s):** `get_attributes`
- **Java signature(s):** `IRPClassifier.getAttributes()`
- **pywin32 member(s):** attributes (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 7: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_base_classifiers() -> baseClassifiers; get_base_classifiers() -> getBaseClassifiers
- **Expected Python method(s):** `get_base_classifiers`
- **Java signature(s):** `IRPClassifier.getBaseClassifiers()`
- **pywin32 member(s):** baseClassifiers (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 8: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_behavioral_diagrams() -> behavioralDiagrams; get_behavioral_diagrams() -> getBehavioralDiagrams
- **Expected Python method(s):** `get_behavioral_diagrams`
- **Java signature(s):** `IRPClassifier.getBehavioralDiagrams()`
- **pywin32 member(s):** behavioralDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 9: COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_binary_id() -> binaryID; get_binary_id() -> getBinaryID
- **Expected Python method(s):** `get_binary_id`
- **Java signature(s):** `IRPModelElement.getBinaryID()`
- **pywin32 member(s):** BinaryID (property)
- **Recommended change:** Use the BinaryID property or a getter/setter fallback instead of calling binaryID and getBinaryID directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 10: COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_cm_header() -> cMHeader; get_cm_header() -> getCMHeader; set_cm_header() -> cMHeader; set_cm_header() -> setCMHeader
- **Expected Python method(s):** `get_cm_header`, `set_cm_header`
- **Java signature(s):** `IRPUnit.getCMHeader()`, `IRPUnit.setCMHeader(java.lang.String)`
- **pywin32 member(s):** CMHeader (property)
- **Recommended change:** Use the CMHeader property or a getter/setter fallback instead of calling cMHeader and getCMHeader and setCMHeader directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 11: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_constraints() -> constraints; get_constraints() -> getConstraints
- **Expected Python method(s):** `get_constraints`
- **Java signature(s):** `IRPModelElement.getConstraints()`
- **pywin32 member(s):** constraints (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 12: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_constraints_by_him() -> constraintsByHim; get_constraints_by_him() -> getConstraintsByHim
- **Expected Python method(s):** `get_constraints_by_him`
- **Java signature(s):** `IRPModelElement.getConstraintsByHim()`
- **pywin32 member(s):** constraintsByHim (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 13: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_controlled_files() -> controlledFiles; get_controlled_files() -> getControlledFiles
- **Expected Python method(s):** `get_controlled_files`
- **Java signature(s):** `IRPModelElement.getControlledFiles()`
- **pywin32 member(s):** controlledFiles (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 14: MISSING_PYTHON_WRAPPER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `create_oslc_link`
- **Java signature(s):** `IRPModelElement.createOSLCLink(java.lang.String, java.lang.String)`
- **pywin32 member(s):** createOSLCLink (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 15: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_current_directory() -> currentDirectory; get_current_directory() -> getCurrentDirectory
- **Expected Python method(s):** `get_current_directory`
- **Java signature(s):** `IRPUnit.getCurrentDirectory()`
- **pywin32 member(s):** currentDirectory (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 16: PYWIN32_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** deleteActivityDiagram (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 17: MISSING_PYTHON_WRAPPER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `delete_oslc_link`
- **Java signature(s):** `IRPModelElement.deleteOSLCLink(java.lang.String, java.lang.String)`
- **pywin32 member(s):** deleteOSLCLink (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 18: PYWIN32_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** deleteStatechart (method)
- **Recommended change:** Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 19: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_dependencies() -> dependencies; get_dependencies() -> getDependencies
- **Expected Python method(s):** `get_dependencies`
- **Java signature(s):** `IRPModelElement.getDependencies()`
- **pywin32 member(s):** dependencies (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 20: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_derived_classifiers() -> derivedClassifiers; get_derived_classifiers() -> getDerivedClassifiers
- **Expected Python method(s):** `get_derived_classifiers`
- **Java signature(s):** `IRPClassifier.getDerivedClassifiers()`
- **pywin32 member(s):** derivedClassifiers (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 21: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_description() -> description; get_description() -> getDescription; set_description() -> description; set_description() -> setDescription
- **Expected Python method(s):** `get_description`, `set_description`
- **Java signature(s):** `IRPModelElement.getDescription()`, `IRPModelElement.setDescription(java.lang.String)`
- **pywin32 member(s):** description (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 22: PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML
- **Expected Python method(s):** `get_description_html`, `set_description_html`
- **Java signature(s):** `IRPModelElement.getDescriptionHTML()`, `IRPModelElement.setDescriptionHTML(java.lang.String)`
- **pywin32 member(s):** descriptionHTML (property)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 23: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_description_plain_text() -> descriptionPlainText; get_description_plain_text() -> getDescriptionPlainText
- **Expected Python method(s):** `get_description_plain_text`
- **Java signature(s):** `IRPModelElement.getDescriptionPlainText()`
- **pywin32 member(s):** descriptionPlainText (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 24: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_description_rtf() -> descriptionRTF; get_description_rtf() -> getDescriptionRTF; is_description_rtf() -> descriptionRTF; set_description_rtf() -> descriptionRTF; set_description_rtf() -> setDescriptionRTF
- **Expected Python method(s):** `get_description_rtf`, `set_description_rtf`
- **Java signature(s):** `IRPModelElement.getDescriptionRTF()`, `IRPModelElement.setDescriptionRTF(java.lang.String)`
- **pywin32 member(s):** descriptionRTF (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 25: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_display_name() -> displayName; get_display_name() -> getDisplayName; set_display_name() -> displayName; set_display_name() -> setDisplayName
- **Expected Python method(s):** `get_display_name`, `set_display_name`
- **Java signature(s):** `IRPModelElement.getDisplayName()`, `IRPModelElement.setDisplayName(java.lang.String)`
- **pywin32 member(s):** displayName (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 26: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_filename() -> filename; get_filename() -> getFilename; set_filename() -> filename; set_filename() -> setFilename
- **Expected Python method(s):** `get_filename`, `set_filename`
- **Java signature(s):** `IRPUnit.getFilename()`, `IRPUnit.setFilename(java.lang.String)`
- **pywin32 member(s):** filename (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 27: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_flow_items() -> flowItems; get_flow_items() -> getFlowItems
- **Expected Python method(s):** `get_flow_items`
- **Java signature(s):** `IRPClassifier.getFlowItems()`
- **pywin32 member(s):** flowItems (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 28: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_flows() -> flows; get_flows() -> getFlows
- **Expected Python method(s):** `get_flows`
- **Java signature(s):** `IRPClassifier.getFlows()`
- **pywin32 member(s):** flows (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 29: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_guid() -> GUID; get_guid() -> getGUID; set_guid() -> GUID; set_guid() -> setGUID
- **Expected Python method(s):** `get_guid`, `set_guid`
- **Java signature(s):** `IRPModelElement.getGUID()`, `IRPModelElement.setGUID(java.lang.String)`
- **pywin32 member(s):** GUID (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 30: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_generalizations() -> generalizations; get_generalizations() -> getGeneralizations
- **Expected Python method(s):** `get_generalizations`
- **Java signature(s):** `IRPClassifier.getGeneralizations()`
- **pywin32 member(s):** generalizations (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 31: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_hyper_links() -> getHyperLinks; get_hyper_links() -> hyperLinks
- **Expected Python method(s):** `get_hyper_links`
- **Java signature(s):** `IRPModelElement.getHyperLinks()`
- **pywin32 member(s):** hyperLinks (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 32: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_include_in_next_load() -> getIncludeInNextLoad; get_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> setIncludeInNextLoad
- **Expected Python method(s):** `get_include_in_next_load`, `set_include_in_next_load`
- **Java signature(s):** `IRPUnit.getIncludeInNextLoad()`, `IRPUnit.setIncludeInNextLoad(int)`
- **pywin32 member(s):** includeInNextLoad (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 33: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_interface_items() -> getInterfaceItems; get_interface_items() -> interfaceItems
- **Expected Python method(s):** `get_interface_items`
- **Java signature(s):** `IRPClassifier.getInterfaceItems()`
- **pywin32 member(s):** interfaceItems (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 34: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_interface_name() -> getInterfaceName; get_interface_name() -> interfaceName
- **Expected Python method(s):** `get_interface_name`
- **Java signature(s):** `IRPModelElement.getInterfaceName()`
- **pywin32 member(s):** interfaceName (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 35: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_is_external() -> getIsExternal; get_is_external() -> isExternal
- **Expected Python method(s):** `get_is_external`
- **Java signature(s):** `IRPModelElement.getIsExternal()`
- **pywin32 member(s):** isExternal (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 36: COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_is_of_meta_class() -> getIsOfMetaClass
- **Expected Python method(s):** `get_is_of_meta_class`
- **Java signature(s):** `IRPModelElement.getIsOfMetaClass(java.lang.String)`
- **pywin32 member(s):** isOfMetaClass (method)
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 37: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_is_show_display_name() -> getIsShowDisplayName; get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> setIsShowDisplayName
- **Expected Python method(s):** `get_is_show_display_name`, `set_is_show_display_name`
- **Java signature(s):** `IRPModelElement.getIsShowDisplayName()`, `IRPModelElement.setIsShowDisplayName(int)`
- **pywin32 member(s):** isShowDisplayName (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 38: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_is_stub() -> getIsStub; get_is_stub() -> isStub
- **Expected Python method(s):** `get_is_stub`
- **Java signature(s):** `IRPUnit.getIsStub()`
- **pywin32 member(s):** isStub (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 39: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_is_unresolved() -> getIsUnresolved; get_is_unresolved() -> isUnresolved
- **Expected Python method(s):** `get_is_unresolved`
- **Java signature(s):** `IRPModelElement.getIsUnresolved()`
- **pywin32 member(s):** isUnresolved (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 40: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_links() -> getLinks; get_links() -> links
- **Expected Python method(s):** `get_links`
- **Java signature(s):** `IRPClassifier.getLinks()`
- **pywin32 member(s):** links (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 41: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_local_tags() -> getLocalTags; get_local_tags() -> localTags
- **Expected Python method(s):** `get_local_tags`
- **Java signature(s):** `IRPModelElement.getLocalTags()`
- **pywin32 member(s):** localTags (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 42: MISSING_PYTHON_WRAPPER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `lock_on_design_manager`
- **Java signature(s):** `IRPModelElement.lockOnDesignManager()`
- **pywin32 member(s):** lockOnDesignManager (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 43: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_main_diagram() -> getMainDiagram; get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram; set_main_diagram() -> setMainDiagram
- **Expected Python method(s):** `get_main_diagram`, `set_main_diagram`
- **Java signature(s):** `IRPModelElement.getMainDiagram()`, `IRPModelElement.setMainDiagram(com.telelogic.rhapsody.core.IRPDiagram)`
- **pywin32 member(s):** mainDiagram (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 44: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_meta_class() -> getMetaClass; get_meta_class() -> metaClass
- **Expected Python method(s):** `get_meta_class`
- **Java signature(s):** `IRPModelElement.getMetaClass()`
- **pywin32 member(s):** metaClass (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 45: PYTHON_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** is_modified() -> modified
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 46: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_name() -> getName; get_name() -> name; set_name() -> name; set_name() -> setName
- **Expected Python method(s):** `get_name`, `set_name`
- **Java signature(s):** `IRPModelElement.getName()`, `IRPModelElement.setName(java.lang.String)`
- **pywin32 member(s):** name (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 47: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_nested_classifiers() -> getNestedClassifiers; get_nested_classifiers() -> nestedClassifiers
- **Expected Python method(s):** `get_nested_classifiers`
- **Java signature(s):** `IRPClassifier.getNestedClassifiers()`
- **pywin32 member(s):** nestedClassifiers (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 48: MISSING_PYTHON_WRAPPER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_oslc_links`
- **Java signature(s):** `IRPModelElement.getOSLCLinks()`
- **pywin32 member(s):** getOSLCLinks (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 49: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_of_template() -> getOfTemplate; get_of_template() -> ofTemplate; set_of_template() -> ofTemplate; set_of_template() -> setOfTemplate
- **Expected Python method(s):** `get_of_template`, `set_of_template`
- **Java signature(s):** `IRPModelElement.getOfTemplate()`, `IRPModelElement.setOfTemplate(com.telelogic.rhapsody.core.IRPModelElement)`
- **pywin32 member(s):** ofTemplate (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 50: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_operations() -> getOperations; get_operations() -> operations
- **Expected Python method(s):** `get_operations`
- **Java signature(s):** `IRPClassifier.getOperations()`
- **pywin32 member(s):** operations (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 51: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_owner() -> getOwner; get_owner() -> owner; set_owner() -> owner; set_owner() -> setOwner
- **Expected Python method(s):** `get_owner`, `set_owner`
- **Java signature(s):** `IRPModelElement.getOwner()`, `IRPModelElement.setOwner(com.telelogic.rhapsody.core.IRPModelElement)`
- **pywin32 member(s):** owner (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 52: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_ports() -> getPorts; get_ports() -> ports
- **Expected Python method(s):** `get_ports`
- **Java signature(s):** `IRPClassifier.getPorts()`
- **pywin32 member(s):** ports (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 53: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_project() -> getProject; get_project() -> project
- **Expected Python method(s):** `get_project`
- **Java signature(s):** `IRPModelElement.getProject()`
- **pywin32 member(s):** project (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 54: PYTHON_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** create_oslc_link() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 55: PYTHON_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** delete_oslc_link() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 56: PYTHON_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_oslc_links() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 57: PYTHON_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** set_description_html() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 58: PYTHON_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** is_reference_unit() -> referenceUnit
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 59: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_references() -> getReferences; get_references() -> references
- **Expected Python method(s):** `get_references`
- **Java signature(s):** `IRPModelElement.getReferences()`
- **pywin32 member(s):** references (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 60: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_relations() -> getRelations; get_relations() -> relations
- **Expected Python method(s):** `get_relations`
- **Java signature(s):** `IRPClassifier.getRelations()`
- **pywin32 member(s):** relations (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 61: PYTHON_ONLY_MEMBER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** is_remote() -> remote
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 62: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_requirement_traceability_handle() -> getRequirementTraceabilityHandle; get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> setRequirementTraceabilityHandle
- **Expected Python method(s):** `get_requirement_traceability_handle`, `set_requirement_traceability_handle`
- **Java signature(s):** `IRPModelElement.getRequirementTraceabilityHandle()`, `IRPModelElement.setRequirementTraceabilityHandle(int)`
- **pywin32 member(s):** requirementTraceabilityHandle (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 63: PYWIN32_MEMBER_MISSING
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl
- **Expected Python method(s):** `get_rmm_url`
- **Java signature(s):** `IRPModelElement.getRmmUrl()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 64: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_sequence_diagrams() -> getSequenceDiagrams; get_sequence_diagrams() -> sequenceDiagrams
- **Expected Python method(s):** `get_sequence_diagrams`
- **Java signature(s):** `IRPClassifier.getSequenceDiagrams()`
- **pywin32 member(s):** sequenceDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 65: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_source_artifacts() -> getSourceArtifacts; get_source_artifacts() -> sourceArtifacts
- **Expected Python method(s):** `get_source_artifacts`
- **Java signature(s):** `IRPClassifier.getSourceArtifacts()`
- **pywin32 member(s):** sourceArtifacts (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 66: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_statechart() -> getStatechart; get_statechart() -> statechart
- **Expected Python method(s):** `get_statechart`
- **Java signature(s):** `IRPClassifier.getStatechart()`
- **pywin32 member(s):** statechart (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 67: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_stereotype`, `set_stereotype`
- **Java signature(s):** `IRPModelElement.getStereotype()`, `IRPModelElement.setStereotype(com.telelogic.rhapsody.core.IRPStereotype)`
- **pywin32 member(s):** stereotype (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 68: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_stereotypes() -> getStereotypes; get_stereotypes() -> stereotypes
- **Expected Python method(s):** `get_stereotypes`
- **Java signature(s):** `IRPModelElement.getStereotypes()`
- **pywin32 member(s):** stereotypes (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 69: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_structure_diagrams() -> getStructureDiagrams; get_structure_diagrams() -> structureDiagrams
- **Expected Python method(s):** `get_structure_diagrams`
- **Java signature(s):** `IRPUnit.getStructureDiagrams()`
- **pywin32 member(s):** structureDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 70: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_template_parameters() -> getTemplateParameters; get_template_parameters() -> templateParameters
- **Expected Python method(s):** `get_template_parameters`
- **Java signature(s):** `IRPModelElement.getTemplateParameters()`
- **pywin32 member(s):** templateParameters (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 71: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_ti() -> getTi; get_ti() -> ti; set_ti() -> setTi; set_ti() -> ti
- **Expected Python method(s):** `get_ti`, `set_ti`
- **Java signature(s):** `IRPModelElement.getTi()`, `IRPModelElement.setTi(com.telelogic.rhapsody.core.IRPTemplateInstantiation)`
- **pywin32 member(s):** ti (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 72: ACCESSOR_ALIAS_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_unit_path() -> getUnitPath; set_unit_path() -> setUnitPath; set_unit_path() -> unitPath
- **Expected Python method(s):** `get_unit_path`, `set_unit_path`
- **Java signature(s):** `IRPUnit.getUnitPath(int)`, `IRPUnit.setUnitPath(java.lang.String)`
- **pywin32 member(s):** setUnitPath (method)
- **Recommended change:** Review the related API spellings and document the intended mapping.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 73: MISSING_PYTHON_WRAPPER
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `unlock_on_design_manager`
- **Java signature(s):** `IRPModelElement.unlockOnDesignManager()`
- **pywin32 member(s):** unlockOnDesignManager (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 74: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPClassifier` in `src/rhapsody_cli/models/elements/classifiers/model_classifier.py`
- **Current Python wrapper/COM call:** get_user_defined_meta_class() -> getUserDefinedMetaClass; get_user_defined_meta_class() -> userDefinedMetaClass
- **Expected Python method(s):** `get_user_defined_meta_class`
- **Java signature(s):** `IRPModelElement.getUserDefinedMetaClass()`
- **pywin32 member(s):** userDefinedMetaClass (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
