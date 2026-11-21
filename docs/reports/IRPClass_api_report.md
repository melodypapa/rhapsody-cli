# Rhapsody API Validation: IRPClass

## Summary
- Target wrapper: `IRPClass` (`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_class.py`)
- Members: Python `214`, Java `222`, pywin32 `201`
- Deviations: `0`
- Deviations by status:
  - None

- Informational binding differences (expected): `78`
- Wrapper backlog (supported members without wrappers): `5`
- Documented aliases: `7`, documented unavailable: `9`

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |

## Expected Binding Differences

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| is_a_template() -> aTemplate | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_activity_diagram() -> activityDiagram; get_activity_diagram() -> getActivityDiagram | getActivityDiagram (method) | activityDiagram (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | addEventReceptionWithEvent (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| get_all_tags() -> allTags; get_all_tags() -> getAllTags | getAllTags (method) | allTags (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_annotations() -> annotations; get_annotations() -> getAnnotations | getAnnotations (method) | annotations (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_association_classes() -> associationClasses; get_association_classes() -> getAssociationClasses | getAssociationClasses (method) | associationClasses (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_attributes() -> attributes; get_attributes() -> getAttributes | getAttributes (method) | attributes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_base_classifiers() -> baseClassifiers; get_base_classifiers() -> getBaseClassifiers | getBaseClassifiers (method) | baseClassifiers (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_behavioral_diagrams() -> behavioralDiagrams; get_behavioral_diagrams() -> getBehavioralDiagrams | getBehavioralDiagrams (method) | behavioralDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_binary_id() -> BinaryID; get_binary_id() -> getBinaryID | getBinaryID (method) | BinaryID (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_cm_header() -> CMHeader; get_cm_header() -> getCMHeader; set_cm_header() -> CMHeader; set_cm_header() -> setCMHeader | getCMHeader (method); setCMHeader (method) | CMHeader (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_constraints() -> constraints; get_constraints() -> getConstraints | getConstraints (method) | constraints (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_constraints_by_him() -> constraintsByHim; get_constraints_by_him() -> getConstraintsByHim | getConstraintsByHim (method) | constraintsByHim (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_controlled_files() -> controlledFiles; get_controlled_files() -> getControlledFiles | getControlledFiles (method) | controlledFiles (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | createOSLCLink (method) | createOSLCLink (method) | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| get_current_directory() -> currentDirectory; get_current_directory() -> getCurrentDirectory | getCurrentDirectory (method) | currentDirectory (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | deleteOSLCLink (method) | deleteOSLCLink (method) | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| get_dependencies() -> dependencies; get_dependencies() -> getDependencies | getDependencies (method) | dependencies (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_derived_classifiers() -> derivedClassifiers; get_derived_classifiers() -> getDerivedClassifiers | getDerivedClassifiers (method) | derivedClassifiers (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description() -> description; get_description() -> getDescription; set_description() -> description; set_description() -> setDescription | getDescription (method); setDescription (method) | description (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML | getDescriptionHTML (method); setDescriptionHTML (method) | descriptionHTML (property) | ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Documented decision: keep the current binding; no change. |
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
| is_abstract() -> getIsAbstract; is_abstract() -> isAbstract | getIsAbstract (method); setIsAbstract (method) | isAbstract (property) | ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Documented decision: keep the current binding; no change. |
| is_active() -> getIsActive; is_active() -> isActive | getIsActive (method); setIsActive (method) | isActive (property) | ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Documented decision: keep the current binding; no change. |
| is_behavior_overriden() -> getIsBehaviorOverriden; is_behavior_overriden() -> isBehaviorOverriden | getIsBehaviorOverriden (method); setIsBehaviorOverriden (method) | isBehaviorOverriden (property) | ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Documented decision: keep the current binding; no change. |
| is_composite() -> getIsComposite; is_composite() -> isComposite | getIsComposite (method) | isComposite (property) | ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Documented decision: keep the current binding; no change. |
| get_is_external() -> getIsExternal; get_is_external() -> isExternal | getIsExternal (method) | isExternal (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_final() -> getIsFinal | getIsFinal (method); setIsFinal (method) | getIsFinal (method); setIsFinal (method) | ALIAS_DOCUMENTED | Documented decision: keep the current binding; no change. |
| get_is_of_meta_class() -> isOfMetaClass | getIsOfMetaClass (method) | isOfMetaClass (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |
| is_reactive() -> getIsReactive; is_reactive() -> isReactive | getIsReactive (method) | isReactive (property) | ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Documented decision: keep the current binding; no change. |
| get_is_show_display_name() -> getIsShowDisplayName; get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> setIsShowDisplayName | getIsShowDisplayName (method); setIsShowDisplayName (method) | isShowDisplayName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_stub() -> getIsStub; get_is_stub() -> isStub | getIsStub (method) | isStub (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_unresolved() -> getIsUnresolved; get_is_unresolved() -> isUnresolved | getIsUnresolved (method) | isUnresolved (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_links() -> getLinks; get_links() -> links | getLinks (method) | links (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_local_tags() -> getLocalTags; get_local_tags() -> localTags | getLocalTags (method) | localTags (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_main_diagram() -> getMainDiagram; get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram; set_main_diagram() -> setMainDiagram | getMainDiagram (method); setMainDiagram (method) | mainDiagram (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_meta_class() -> getMetaClass; get_meta_class() -> metaClass | getMetaClass (method) | metaClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_modified() -> modified | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_name() -> getName; get_name() -> name; set_name() -> name; set_name() -> setName | getName (method); setName (method) | name (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nested_classifiers() -> getNestedClassifiers; get_nested_classifiers() -> nestedClassifiers | getNestedClassifiers (method) | nestedClassifiers (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | getOSLCLinks (method) | getOSLCLinks (method) | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| get_of_template() -> getOfTemplate; get_of_template() -> ofTemplate; set_of_template() -> ofTemplate; set_of_template() -> setOfTemplate | getOfTemplate (method); setOfTemplate (method) | ofTemplate (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_operations() -> getOperations; get_operations() -> operations | getOperations (method) | operations (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_owner() -> getOwner; get_owner() -> owner; set_owner() -> owner; set_owner() -> setOwner | getOwner (method); setOwner (method) | owner (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_ports() -> getPorts; get_ports() -> ports | getPorts (method) | ports (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_project() -> getProject; get_project() -> project | getProject (method) | project (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| add_event_reception_with_event() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| create_oslc_link() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| delete_oslc_link() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_oslc_links() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| set_description_html() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| is_reference_unit() -> referenceUnit | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_references() -> getReferences; get_references() -> references | getReferences (method) | references (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_relations() -> getRelations; get_relations() -> relations | getRelations (method) | relations (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_remote() -> remote | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_requirement_traceability_handle() -> getRequirementTraceabilityHandle; get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> setRequirementTraceabilityHandle | getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method) | requirementTraceabilityHandle (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl | getRmmUrl (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| get_sequence_diagrams() -> getSequenceDiagrams; get_sequence_diagrams() -> sequenceDiagrams | getSequenceDiagrams (method) | sequenceDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_source_artifacts() -> getSourceArtifacts; get_source_artifacts() -> sourceArtifacts | getSourceArtifacts (method) | sourceArtifacts (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_statechart() -> getStatechart; get_statechart() -> statechart | getStatechart (method) | statechart (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_stereotypes() -> getStereotypes; get_stereotypes() -> stereotypes | getStereotypes (method) | stereotypes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_structure_diagrams() -> getStructureDiagrams; get_structure_diagrams() -> structureDiagrams | getStructureDiagrams (method) | structureDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_template_parameters() -> getTemplateParameters; get_template_parameters() -> templateParameters | getTemplateParameters (method) | templateParameters (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_ti() -> getTi; get_ti() -> ti; set_ti() -> setTi; set_ti() -> ti | getTi (method); setTi (method) | ti (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_unit_path() -> getUnitPath; set_unit_path() -> setUnitPath; set_unit_path() -> unitPath | getUnitPath (method); setUnitPath (method) | setUnitPath (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |
| — | updateContainedDiagramsOnServer (method) | — | UNAVAILABLE_DOCUMENTED | Documented decision: intentionally unsupported; no change. |
| get_user_defined_meta_class() -> getUserDefinedMetaClass; get_user_defined_meta_class() -> userDefinedMetaClass | getUserDefinedMetaClass (method) | userDefinedMetaClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |

## Wrapper Backlog

| Python model wrapper | Java API | pywin32 | Status | Recommended change |
| --- | --- | --- | --- | --- |
| — | — | deleteActivityDiagram (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | — | deleteStatechart (method) | PYWIN32_ONLY_MEMBER | Confirm this version-specific member should be wrapped; otherwise classify it as unsupported. |
| — | lockOnDesignManager (method) | lockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | getStereotype (method); setStereotype (method) | stereotype (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| — | unlockOnDesignManager (method) | unlockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |

## AI Fix Guidance
No deviations require changes.
