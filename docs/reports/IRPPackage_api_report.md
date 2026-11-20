# Rhapsody API Validation: IRPPackage

## Summary
- Target wrapper: `RPPackage` (`src/rhapsody_cli/models/elements/containment/model_package.py`)
- Members: Python `243`, Java `247`, pywin32 `222`
- Deviations: `93`
- Deviations by status:
  - `ACCESSOR_ALIAS_MISMATCH`: 71
  - `COM_MEMBER_NOT_EXPOSED`: 3
  - `METHOD_PROPERTY_MISMATCH`: 69
  - `MISSING_PYTHON_WRAPPER`: 6
  - `PYTHON_METHOD_NAME_MISMATCH`: 5
  - `PYTHON_ONLY_MEMBER`: 8
  - `PYWIN32_MEMBER_MISSING`: 7

## Comparison details

| Python model wrapper | Java API | pywin32 | Comparison status | Recommended change |
| --- | --- | --- | --- | --- |
| is_a_template() -> aTemplate | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_actors() -> actors; get_actors() -> getActors | getActors (method) | actors (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| add_instance_specification() -> addInstanceSpecification | addInstanceSpecification (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| add_statechart_diagram() -> addStatechart | addStatechart (method) | addStatechart (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_all_tags() -> allTags; get_all_tags() -> getAllTags | getAllTags (method) | allTags (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_annotations() -> annotations; get_annotations() -> getAnnotations | getAnnotations (method) | annotations (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_association_classes() -> associationClasses; get_association_classes() -> getAssociationClasses | getAssociationClasses (method) | associationClasses (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_behavioral_diagrams() -> behavioralDiagrams; get_behavioral_diagrams() -> getBehavioralDiagrams | getBehavioralDiagrams (method) | behavioralDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_binary_id() -> binaryID; get_binary_id() -> getBinaryID | getBinaryID (method) | BinaryID (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the BinaryID property or a getter/setter fallback instead of calling binaryID and getBinaryID directly. |
| get_cm_header() -> cMHeader; get_cm_header() -> getCMHeader; set_cm_header() -> cMHeader; set_cm_header() -> setCMHeader | getCMHeader (method); setCMHeader (method) | CMHeader (property) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use the CMHeader property or a getter/setter fallback instead of calling cMHeader and getCMHeader and setCMHeader directly. |
| get_classes() -> classes; get_classes() -> getClasses | getClasses (method) | classes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_collaboration_diagrams() -> collaborationDiagrams; get_collaboration_diagrams() -> getCollaborationDiagrams | getCollaborationDiagrams (method) | collaborationDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_component_diagrams() -> componentDiagrams; get_component_diagrams() -> getComponentDiagrams | getComponentDiagrams (method) | componentDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_constraints() -> constraints; get_constraints() -> getConstraints | getConstraints (method) | constraints (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_constraints_by_him() -> constraintsByHim; get_constraints_by_him() -> getConstraintsByHim | getConstraintsByHim (method) | constraintsByHim (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_controlled_files() -> controlledFiles; get_controlled_files() -> getControlledFiles | getControlledFiles (method) | controlledFiles (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | createOSLCLink (method) | createOSLCLink (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_current_directory() -> currentDirectory; get_current_directory() -> getCurrentDirectory | getCurrentDirectory (method) | currentDirectory (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | deleteOSLCLink (method) | deleteOSLCLink (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_dependencies() -> dependencies; get_dependencies() -> getDependencies | getDependencies (method) | dependencies (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_deployment_diagrams() -> deploymentDiagrams; get_deployment_diagrams() -> getDeploymentDiagrams | getDeploymentDiagrams (method) | deploymentDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description() -> description; get_description() -> getDescription; set_description() -> description; set_description() -> setDescription | getDescription (method); setDescription (method) | description (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML | getDescriptionHTML (method); setDescriptionHTML (method) | descriptionHTML (property) | PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_description_plain_text() -> descriptionPlainText; get_description_plain_text() -> getDescriptionPlainText | getDescriptionPlainText (method) | descriptionPlainText (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_description_rtf() -> descriptionRTF; get_description_rtf() -> getDescriptionRTF; is_description_rtf() -> descriptionRTF; set_description_rtf() -> descriptionRTF; set_description_rtf() -> setDescriptionRTF | getDescriptionRTF (method); setDescriptionRTF (method) | descriptionRTF (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_display_name() -> displayName; get_display_name() -> getDisplayName; set_display_name() -> displayName; set_display_name() -> setDisplayName | getDisplayName (method); setDisplayName (method) | displayName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_events() -> events; get_events() -> getEvents | getEvents (method) | events (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_events_base_id() -> eventsBaseId; get_events_base_id() -> getEventsBaseId | getEventsBaseId (method) | eventsBaseId (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_filename() -> filename; get_filename() -> getFilename; set_filename() -> filename; set_filename() -> setFilename | getFilename (method); setFilename (method) | filename (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_flow_items() -> flowItems; get_flow_items() -> getFlowItems | getFlowItems (method) | flowItems (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_flows() -> flows; get_flows() -> getFlows | getFlows (method) | flows (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_guid() -> GUID; get_guid() -> getGUID; set_guid() -> GUID; set_guid() -> setGUID | getGUID (method); setGUID (method) | GUID (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_global_functions() -> getGlobalFunctions; get_global_functions() -> globalFunctions | getGlobalFunctions (method) | globalFunctions (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_global_objects() -> getGlobalObjects; get_global_objects() -> globalObjects | getGlobalObjects (method) | globalObjects (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_global_variables() -> getGlobalVariables; get_global_variables() -> globalVariables | getGlobalVariables (method) | globalVariables (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_hyper_links() -> getHyperLinks; get_hyper_links() -> hyperLinks | getHyperLinks (method) | hyperLinks (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_include_in_next_load() -> getIncludeInNextLoad; get_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> setIncludeInNextLoad | getIncludeInNextLoad (method); setIncludeInNextLoad (method) | includeInNextLoad (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_instance_specifications() -> getInstanceSpecifications; get_instance_specifications() -> instanceSpecifications | getInstanceSpecifications (method) | instanceSpecifications (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_interface_name() -> getInterfaceName; get_interface_name() -> interfaceName | getInterfaceName (method) | interfaceName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_external() -> getIsExternal; get_is_external() -> isExternal | getIsExternal (method) | isExternal (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_of_meta_class() -> getIsOfMetaClass | getIsOfMetaClass (method) | isOfMetaClass (method) | COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH | Change the COM call to a member exposed by the registered pywin32 interface. |
| get_is_show_display_name() -> getIsShowDisplayName; get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> setIsShowDisplayName | getIsShowDisplayName (method); setIsShowDisplayName (method) | isShowDisplayName (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_stub() -> getIsStub; get_is_stub() -> isStub | getIsStub (method) | isStub (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_is_unresolved() -> getIsUnresolved; get_is_unresolved() -> isUnresolved | getIsUnresolved (method) | isUnresolved (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_links() -> getLinks; get_links() -> links | getLinks (method) | links (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_local_tags() -> getLocalTags; get_local_tags() -> localTags | getLocalTags (method) | localTags (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | lockOnDesignManager (method) | lockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| login_to_remote_artifact_server() -> loginToRemoteArtifactServer | loginToRemoteArtifactServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_main_diagram() -> getMainDiagram; get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram; set_main_diagram() -> setMainDiagram | getMainDiagram (method); setMainDiagram (method) | mainDiagram (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_meta_class() -> getMetaClass; get_meta_class() -> metaClass | getMetaClass (method) | metaClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_modified() -> modified | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_modules() -> getModules; get_modules() -> modules | getModules (method) | modules (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_name() -> getName; get_name() -> name; set_name() -> name; set_name() -> setName | getName (method); setName (method) | name (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nested_classifiers() -> getNestedClassifiers; get_nested_classifiers() -> nestedClassifiers | getNestedClassifiers (method) | nestedClassifiers (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nested_components() -> getNestedComponents; get_nested_components() -> nestedComponents | getNestedComponents (method) | nestedComponents (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nodes() -> getNodes; get_nodes() -> nodes | getNodes (method) | nodes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | getOSLCLinks (method) | getOSLCLinks (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_object_model_diagrams() -> getObjectModelDiagrams; get_object_model_diagrams() -> objectModelDiagrams | getObjectModelDiagrams (method) | objectModelDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_of_template() -> getOfTemplate; get_of_template() -> ofTemplate; set_of_template() -> ofTemplate; set_of_template() -> setOfTemplate | getOfTemplate (method); setOfTemplate (method) | ofTemplate (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_owner() -> getOwner; get_owner() -> owner; set_owner() -> owner; set_owner() -> setOwner | getOwner (method); setOwner (method) | owner (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_nested_packages() -> getPackages; get_nested_packages() -> packages | getPackages (method) | packages (property) | PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_panel_diagrams() -> getPanelDiagrams; get_panel_diagrams() -> panelDiagrams | getPanelDiagrams (method) | panelDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_project() -> getProject; get_project() -> project | getProject (method) | project (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| create_oslc_link() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| delete_oslc_link() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_oslc_links() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| set_description_html() (no static COM member) | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| recalculate_events_base_id() -> reCalculateEventsBaseId | reCalculateEventsBaseId (method) | reCalculateEventsBaseId (method) | PYTHON_METHOD_NAME_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| is_reference_unit() -> referenceUnit | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_references() -> getReferences; get_references() -> references | getReferences (method) | references (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| is_remote() -> remote | — | — | PYTHON_ONLY_MEMBER | Keep this as a local facade helper or map it to a documented API member. |
| get_requirement_traceability_handle() -> getRequirementTraceabilityHandle; get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> setRequirementTraceabilityHandle | getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method) | requirementTraceabilityHandle (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl | getRmmUrl (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_root_instance_specifications() -> getRootInstanceSpecifications; get_root_instance_specifications() -> rootInstanceSpecifications | getRootInstanceSpecifications (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_saved_in_separate_directory() -> getSavedInSeperateDirectory; get_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> setSavedInSeperateDirectory | getSavedInSeperateDirectory (method); setSavedInSeperateDirectory (method) | savedInSeperateDirectory (property) | PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Rename the Python method to the snake_case Java API name or document the alias. |
| get_sequence_diagrams() -> getSequenceDiagrams; get_sequence_diagrams() -> sequenceDiagrams | getSequenceDiagrams (method) | sequenceDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_source_artifacts() -> getSourceArtifacts; get_source_artifacts() -> sourceArtifacts | getSourceArtifacts (method) | sourceArtifacts (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| — | getStereotype (method); setStereotype (method) | stereotype (property) | MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Implement the Python wrapper or mark this API member intentionally unsupported. |
| get_stereotypes() -> getStereotypes; get_stereotypes() -> stereotypes | getStereotypes (method) | stereotypes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_structure_diagrams() -> getStructureDiagrams; get_structure_diagrams() -> structureDiagrams | getStructureDiagrams (method) | structureDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_template_parameters() -> getTemplateParameters; get_template_parameters() -> templateParameters | getTemplateParameters (method) | templateParameters (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_ti() -> getTi; get_ti() -> ti; set_ti() -> setTi; set_ti() -> ti | getTi (method); setTi (method) | ti (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_timing_diagrams() -> getTimingDiagrams; get_timing_diagrams() -> timingDiagrams | getTimingDiagrams (method) | timingDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_types() -> getTypes; get_types() -> types | getTypes (method) | types (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_unit_path() -> getUnitPath; set_unit_path() -> setUnitPath; set_unit_path() -> unitPath | getUnitPath (method); setUnitPath (method) | setUnitPath (method) | ACCESSOR_ALIAS_MISMATCH | Review the related API spellings and document the intended mapping. |
| — | unlockOnDesignManager (method) | unlockOnDesignManager (method) | MISSING_PYTHON_WRAPPER | Implement the Python wrapper or mark this API member intentionally unsupported. |
| update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer | updateContainedDiagramsOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| update_contained_matrices_on_server() -> updateContainedMatricesOnServer | updateContainedMatricesOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| update_contained_tables_on_server() -> updateContainedTablesOnServer | updateContainedTablesOnServer (method) | — | PYWIN32_MEMBER_MISSING | Use a member exposed by the registered type library or verify the Rhapsody version. |
| get_use_case_diagrams() -> getUseCaseDiagrams; get_use_case_diagrams() -> useCaseDiagrams | getUseCaseDiagrams (method) | useCaseDiagrams (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_use_cases() -> getUseCases; get_use_cases() -> useCases | getUseCases (method) | useCases (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_user_defined_meta_class() -> getUserDefinedMetaClass; get_user_defined_meta_class() -> userDefinedMetaClass | getUserDefinedMetaClass (method) | userDefinedMetaClass (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |
| get_user_defined_stereotypes() -> getUserDefinedStereotypes; get_user_defined_stereotypes() -> userDefinedStereotypes | getUserDefinedStereotypes (method) | userDefinedStereotypes (property) | ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH | Use a property-aware getter/setter fallback or document the binding mismatch. |

## AI Fix Guidance

### Finding 1: PYTHON_ONLY_MEMBER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** is_a_template() -> aTemplate
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 2: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_actors() -> actors; get_actors() -> getActors
- **Expected Python method(s):** `get_actors`
- **Java signature(s):** `IRPPackage.getActors()`
- **pywin32 member(s):** actors (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 3: PYWIN32_MEMBER_MISSING
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** add_instance_specification() -> addInstanceSpecification
- **Expected Python method(s):** `add_instance_specification`
- **Java signature(s):** `IRPPackage.addInstanceSpecification(java.lang.String, com.telelogic.rhapsody.core.IRPClassifier)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 4: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** add_statechart_diagram() -> addStatechart
- **Expected Python method(s):** `add_statechart`
- **Java signature(s):** `IRPPackage.addStatechart()`
- **pywin32 member(s):** addStatechart (method)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 5: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_all_tags() -> allTags; get_all_tags() -> getAllTags
- **Expected Python method(s):** `get_all_tags`
- **Java signature(s):** `IRPModelElement.getAllTags()`
- **pywin32 member(s):** allTags (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 6: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_annotations() -> annotations; get_annotations() -> getAnnotations
- **Expected Python method(s):** `get_annotations`
- **Java signature(s):** `IRPModelElement.getAnnotations()`
- **pywin32 member(s):** annotations (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 7: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_association_classes() -> associationClasses; get_association_classes() -> getAssociationClasses
- **Expected Python method(s):** `get_association_classes`
- **Java signature(s):** `IRPModelElement.getAssociationClasses()`
- **pywin32 member(s):** associationClasses (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 8: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_behavioral_diagrams() -> behavioralDiagrams; get_behavioral_diagrams() -> getBehavioralDiagrams
- **Expected Python method(s):** `get_behavioral_diagrams`
- **Java signature(s):** `IRPPackage.getBehavioralDiagrams()`
- **pywin32 member(s):** behavioralDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 9: COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_binary_id() -> binaryID; get_binary_id() -> getBinaryID
- **Expected Python method(s):** `get_binary_id`
- **Java signature(s):** `IRPModelElement.getBinaryID()`
- **pywin32 member(s):** BinaryID (property)
- **Recommended change:** Use the BinaryID property or a getter/setter fallback instead of calling binaryID and getBinaryID directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 10: COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_cm_header() -> cMHeader; get_cm_header() -> getCMHeader; set_cm_header() -> cMHeader; set_cm_header() -> setCMHeader
- **Expected Python method(s):** `get_cm_header`, `set_cm_header`
- **Java signature(s):** `IRPUnit.getCMHeader()`, `IRPUnit.setCMHeader(java.lang.String)`
- **pywin32 member(s):** CMHeader (property)
- **Recommended change:** Use the CMHeader property or a getter/setter fallback instead of calling cMHeader and getCMHeader and setCMHeader directly.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 11: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_classes() -> classes; get_classes() -> getClasses
- **Expected Python method(s):** `get_classes`
- **Java signature(s):** `IRPPackage.getClasses()`
- **pywin32 member(s):** classes (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 12: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_collaboration_diagrams() -> collaborationDiagrams; get_collaboration_diagrams() -> getCollaborationDiagrams
- **Expected Python method(s):** `get_collaboration_diagrams`
- **Java signature(s):** `IRPPackage.getCollaborationDiagrams()`
- **pywin32 member(s):** collaborationDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 13: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_component_diagrams() -> componentDiagrams; get_component_diagrams() -> getComponentDiagrams
- **Expected Python method(s):** `get_component_diagrams`
- **Java signature(s):** `IRPPackage.getComponentDiagrams()`
- **pywin32 member(s):** componentDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 14: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_constraints() -> constraints; get_constraints() -> getConstraints
- **Expected Python method(s):** `get_constraints`
- **Java signature(s):** `IRPModelElement.getConstraints()`
- **pywin32 member(s):** constraints (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 15: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_constraints_by_him() -> constraintsByHim; get_constraints_by_him() -> getConstraintsByHim
- **Expected Python method(s):** `get_constraints_by_him`
- **Java signature(s):** `IRPModelElement.getConstraintsByHim()`
- **pywin32 member(s):** constraintsByHim (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 16: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_controlled_files() -> controlledFiles; get_controlled_files() -> getControlledFiles
- **Expected Python method(s):** `get_controlled_files`
- **Java signature(s):** `IRPModelElement.getControlledFiles()`
- **pywin32 member(s):** controlledFiles (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 17: MISSING_PYTHON_WRAPPER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `create_oslc_link`
- **Java signature(s):** `IRPModelElement.createOSLCLink(java.lang.String, java.lang.String)`
- **pywin32 member(s):** createOSLCLink (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 18: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_current_directory() -> currentDirectory; get_current_directory() -> getCurrentDirectory
- **Expected Python method(s):** `get_current_directory`
- **Java signature(s):** `IRPUnit.getCurrentDirectory()`
- **pywin32 member(s):** currentDirectory (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 19: MISSING_PYTHON_WRAPPER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `delete_oslc_link`
- **Java signature(s):** `IRPModelElement.deleteOSLCLink(java.lang.String, java.lang.String)`
- **pywin32 member(s):** deleteOSLCLink (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 20: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_dependencies() -> dependencies; get_dependencies() -> getDependencies
- **Expected Python method(s):** `get_dependencies`
- **Java signature(s):** `IRPModelElement.getDependencies()`
- **pywin32 member(s):** dependencies (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 21: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_deployment_diagrams() -> deploymentDiagrams; get_deployment_diagrams() -> getDeploymentDiagrams
- **Expected Python method(s):** `get_deployment_diagrams`
- **Java signature(s):** `IRPPackage.getDeploymentDiagrams()`
- **pywin32 member(s):** deploymentDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 22: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_description() -> description; get_description() -> getDescription; set_description() -> description; set_description() -> setDescription
- **Expected Python method(s):** `get_description`, `set_description`
- **Java signature(s):** `IRPModelElement.getDescription()`, `IRPModelElement.setDescription(java.lang.String)`
- **pywin32 member(s):** description (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 23: PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML
- **Expected Python method(s):** `get_description_html`, `set_description_html`
- **Java signature(s):** `IRPModelElement.getDescriptionHTML()`, `IRPModelElement.setDescriptionHTML(java.lang.String)`
- **pywin32 member(s):** descriptionHTML (property)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 24: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_description_plain_text() -> descriptionPlainText; get_description_plain_text() -> getDescriptionPlainText
- **Expected Python method(s):** `get_description_plain_text`
- **Java signature(s):** `IRPModelElement.getDescriptionPlainText()`
- **pywin32 member(s):** descriptionPlainText (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 25: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_description_rtf() -> descriptionRTF; get_description_rtf() -> getDescriptionRTF; is_description_rtf() -> descriptionRTF; set_description_rtf() -> descriptionRTF; set_description_rtf() -> setDescriptionRTF
- **Expected Python method(s):** `get_description_rtf`, `set_description_rtf`
- **Java signature(s):** `IRPModelElement.getDescriptionRTF()`, `IRPModelElement.setDescriptionRTF(java.lang.String)`
- **pywin32 member(s):** descriptionRTF (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 26: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_display_name() -> displayName; get_display_name() -> getDisplayName; set_display_name() -> displayName; set_display_name() -> setDisplayName
- **Expected Python method(s):** `get_display_name`, `set_display_name`
- **Java signature(s):** `IRPModelElement.getDisplayName()`, `IRPModelElement.setDisplayName(java.lang.String)`
- **pywin32 member(s):** displayName (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 27: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_events() -> events; get_events() -> getEvents
- **Expected Python method(s):** `get_events`
- **Java signature(s):** `IRPPackage.getEvents()`
- **pywin32 member(s):** events (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 28: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_events_base_id() -> eventsBaseId; get_events_base_id() -> getEventsBaseId
- **Expected Python method(s):** `get_events_base_id`
- **Java signature(s):** `IRPPackage.getEventsBaseId()`
- **pywin32 member(s):** eventsBaseId (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 29: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_filename() -> filename; get_filename() -> getFilename; set_filename() -> filename; set_filename() -> setFilename
- **Expected Python method(s):** `get_filename`, `set_filename`
- **Java signature(s):** `IRPUnit.getFilename()`, `IRPUnit.setFilename(java.lang.String)`
- **pywin32 member(s):** filename (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 30: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_flow_items() -> flowItems; get_flow_items() -> getFlowItems
- **Expected Python method(s):** `get_flow_items`
- **Java signature(s):** `IRPPackage.getFlowItems()`
- **pywin32 member(s):** flowItems (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 31: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_flows() -> flows; get_flows() -> getFlows
- **Expected Python method(s):** `get_flows`
- **Java signature(s):** `IRPPackage.getFlows()`
- **pywin32 member(s):** flows (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 32: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_guid() -> GUID; get_guid() -> getGUID; set_guid() -> GUID; set_guid() -> setGUID
- **Expected Python method(s):** `get_guid`, `set_guid`
- **Java signature(s):** `IRPModelElement.getGUID()`, `IRPModelElement.setGUID(java.lang.String)`
- **pywin32 member(s):** GUID (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 33: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_global_functions() -> getGlobalFunctions; get_global_functions() -> globalFunctions
- **Expected Python method(s):** `get_global_functions`
- **Java signature(s):** `IRPPackage.getGlobalFunctions()`
- **pywin32 member(s):** globalFunctions (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 34: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_global_objects() -> getGlobalObjects; get_global_objects() -> globalObjects
- **Expected Python method(s):** `get_global_objects`
- **Java signature(s):** `IRPPackage.getGlobalObjects()`
- **pywin32 member(s):** globalObjects (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 35: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_global_variables() -> getGlobalVariables; get_global_variables() -> globalVariables
- **Expected Python method(s):** `get_global_variables`
- **Java signature(s):** `IRPPackage.getGlobalVariables()`
- **pywin32 member(s):** globalVariables (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 36: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_hyper_links() -> getHyperLinks; get_hyper_links() -> hyperLinks
- **Expected Python method(s):** `get_hyper_links`
- **Java signature(s):** `IRPModelElement.getHyperLinks()`
- **pywin32 member(s):** hyperLinks (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 37: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_include_in_next_load() -> getIncludeInNextLoad; get_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> setIncludeInNextLoad
- **Expected Python method(s):** `get_include_in_next_load`, `set_include_in_next_load`
- **Java signature(s):** `IRPUnit.getIncludeInNextLoad()`, `IRPUnit.setIncludeInNextLoad(int)`
- **pywin32 member(s):** includeInNextLoad (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 38: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_instance_specifications() -> getInstanceSpecifications; get_instance_specifications() -> instanceSpecifications
- **Expected Python method(s):** `get_instance_specifications`
- **Java signature(s):** `IRPPackage.getInstanceSpecifications()`
- **pywin32 member(s):** instanceSpecifications (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 39: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_interface_name() -> getInterfaceName; get_interface_name() -> interfaceName
- **Expected Python method(s):** `get_interface_name`
- **Java signature(s):** `IRPModelElement.getInterfaceName()`
- **pywin32 member(s):** interfaceName (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 40: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_is_external() -> getIsExternal; get_is_external() -> isExternal
- **Expected Python method(s):** `get_is_external`
- **Java signature(s):** `IRPModelElement.getIsExternal()`
- **pywin32 member(s):** isExternal (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 41: COM_MEMBER_NOT_EXPOSED; ACCESSOR_ALIAS_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_is_of_meta_class() -> getIsOfMetaClass
- **Expected Python method(s):** `get_is_of_meta_class`
- **Java signature(s):** `IRPModelElement.getIsOfMetaClass(java.lang.String)`
- **pywin32 member(s):** isOfMetaClass (method)
- **Recommended change:** Change the COM call to a member exposed by the registered pywin32 interface.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 42: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_is_show_display_name() -> getIsShowDisplayName; get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> setIsShowDisplayName
- **Expected Python method(s):** `get_is_show_display_name`, `set_is_show_display_name`
- **Java signature(s):** `IRPModelElement.getIsShowDisplayName()`, `IRPModelElement.setIsShowDisplayName(int)`
- **pywin32 member(s):** isShowDisplayName (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 43: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_is_stub() -> getIsStub; get_is_stub() -> isStub
- **Expected Python method(s):** `get_is_stub`
- **Java signature(s):** `IRPUnit.getIsStub()`
- **pywin32 member(s):** isStub (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 44: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_is_unresolved() -> getIsUnresolved; get_is_unresolved() -> isUnresolved
- **Expected Python method(s):** `get_is_unresolved`
- **Java signature(s):** `IRPModelElement.getIsUnresolved()`
- **pywin32 member(s):** isUnresolved (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 45: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_links() -> getLinks; get_links() -> links
- **Expected Python method(s):** `get_links`
- **Java signature(s):** `IRPPackage.getLinks()`
- **pywin32 member(s):** links (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 46: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_local_tags() -> getLocalTags; get_local_tags() -> localTags
- **Expected Python method(s):** `get_local_tags`
- **Java signature(s):** `IRPModelElement.getLocalTags()`
- **pywin32 member(s):** localTags (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 47: MISSING_PYTHON_WRAPPER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `lock_on_design_manager`
- **Java signature(s):** `IRPModelElement.lockOnDesignManager()`
- **pywin32 member(s):** lockOnDesignManager (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 48: PYWIN32_MEMBER_MISSING
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** login_to_remote_artifact_server() -> loginToRemoteArtifactServer
- **Expected Python method(s):** `login_to_remote_artifact_server`
- **Java signature(s):** `IRPPackage.loginToRemoteArtifactServer()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 49: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_main_diagram() -> getMainDiagram; get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram; set_main_diagram() -> setMainDiagram
- **Expected Python method(s):** `get_main_diagram`, `set_main_diagram`
- **Java signature(s):** `IRPModelElement.getMainDiagram()`, `IRPModelElement.setMainDiagram(com.telelogic.rhapsody.core.IRPDiagram)`
- **pywin32 member(s):** mainDiagram (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 50: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_meta_class() -> getMetaClass; get_meta_class() -> metaClass
- **Expected Python method(s):** `get_meta_class`
- **Java signature(s):** `IRPModelElement.getMetaClass()`
- **pywin32 member(s):** metaClass (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 51: PYTHON_ONLY_MEMBER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** is_modified() -> modified
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 52: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_modules() -> getModules; get_modules() -> modules
- **Expected Python method(s):** `get_modules`
- **Java signature(s):** `IRPPackage.getModules()`
- **pywin32 member(s):** modules (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 53: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_name() -> getName; get_name() -> name; set_name() -> name; set_name() -> setName
- **Expected Python method(s):** `get_name`, `set_name`
- **Java signature(s):** `IRPModelElement.getName()`, `IRPModelElement.setName(java.lang.String)`
- **pywin32 member(s):** name (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 54: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_nested_classifiers() -> getNestedClassifiers; get_nested_classifiers() -> nestedClassifiers
- **Expected Python method(s):** `get_nested_classifiers`
- **Java signature(s):** `IRPPackage.getNestedClassifiers()`
- **pywin32 member(s):** nestedClassifiers (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 55: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_nested_components() -> getNestedComponents; get_nested_components() -> nestedComponents
- **Expected Python method(s):** `get_nested_components`
- **Java signature(s):** `IRPPackage.getNestedComponents()`
- **pywin32 member(s):** nestedComponents (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 56: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_nodes() -> getNodes; get_nodes() -> nodes
- **Expected Python method(s):** `get_nodes`
- **Java signature(s):** `IRPPackage.getNodes()`
- **pywin32 member(s):** nodes (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 57: MISSING_PYTHON_WRAPPER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_oslc_links`
- **Java signature(s):** `IRPModelElement.getOSLCLinks()`
- **pywin32 member(s):** getOSLCLinks (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 58: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_object_model_diagrams() -> getObjectModelDiagrams; get_object_model_diagrams() -> objectModelDiagrams
- **Expected Python method(s):** `get_object_model_diagrams`
- **Java signature(s):** `IRPPackage.getObjectModelDiagrams()`
- **pywin32 member(s):** objectModelDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 59: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_of_template() -> getOfTemplate; get_of_template() -> ofTemplate; set_of_template() -> ofTemplate; set_of_template() -> setOfTemplate
- **Expected Python method(s):** `get_of_template`, `set_of_template`
- **Java signature(s):** `IRPModelElement.getOfTemplate()`, `IRPModelElement.setOfTemplate(com.telelogic.rhapsody.core.IRPModelElement)`
- **pywin32 member(s):** ofTemplate (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 60: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_owner() -> getOwner; get_owner() -> owner; set_owner() -> owner; set_owner() -> setOwner
- **Expected Python method(s):** `get_owner`, `set_owner`
- **Java signature(s):** `IRPModelElement.getOwner()`, `IRPModelElement.setOwner(com.telelogic.rhapsody.core.IRPModelElement)`
- **pywin32 member(s):** owner (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 61: PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_nested_packages() -> getPackages; get_nested_packages() -> packages
- **Expected Python method(s):** `get_packages`
- **Java signature(s):** `IRPPackage.getPackages()`
- **pywin32 member(s):** packages (property)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 62: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_panel_diagrams() -> getPanelDiagrams; get_panel_diagrams() -> panelDiagrams
- **Expected Python method(s):** `get_panel_diagrams`
- **Java signature(s):** `IRPPackage.getPanelDiagrams()`
- **pywin32 member(s):** panelDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 63: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_project() -> getProject; get_project() -> project
- **Expected Python method(s):** `get_project`
- **Java signature(s):** `IRPModelElement.getProject()`
- **pywin32 member(s):** project (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 64: PYTHON_ONLY_MEMBER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** create_oslc_link() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 65: PYTHON_ONLY_MEMBER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** delete_oslc_link() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 66: PYTHON_ONLY_MEMBER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_oslc_links() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 67: PYTHON_ONLY_MEMBER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** set_description_html() (no static COM member)
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 68: PYTHON_METHOD_NAME_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** recalculate_events_base_id() -> reCalculateEventsBaseId
- **Expected Python method(s):** `re_calculate_events_base_id`
- **Java signature(s):** `IRPPackage.reCalculateEventsBaseId()`
- **pywin32 member(s):** reCalculateEventsBaseId (method)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 69: PYTHON_ONLY_MEMBER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** is_reference_unit() -> referenceUnit
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 70: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_references() -> getReferences; get_references() -> references
- **Expected Python method(s):** `get_references`
- **Java signature(s):** `IRPModelElement.getReferences()`
- **pywin32 member(s):** references (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 71: PYTHON_ONLY_MEMBER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** is_remote() -> remote
- **Expected Python method(s):** —
- **Java signature(s):** —
- **pywin32 member(s):** —
- **Recommended change:** Keep this as a local facade helper or map it to a documented API member.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 72: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_requirement_traceability_handle() -> getRequirementTraceabilityHandle; get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> setRequirementTraceabilityHandle
- **Expected Python method(s):** `get_requirement_traceability_handle`, `set_requirement_traceability_handle`
- **Java signature(s):** `IRPModelElement.getRequirementTraceabilityHandle()`, `IRPModelElement.setRequirementTraceabilityHandle(int)`
- **pywin32 member(s):** requirementTraceabilityHandle (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 73: PYWIN32_MEMBER_MISSING
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl
- **Expected Python method(s):** `get_rmm_url`
- **Java signature(s):** `IRPModelElement.getRmmUrl()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 74: PYWIN32_MEMBER_MISSING
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_root_instance_specifications() -> getRootInstanceSpecifications; get_root_instance_specifications() -> rootInstanceSpecifications
- **Expected Python method(s):** `get_root_instance_specifications`
- **Java signature(s):** `IRPPackage.getRootInstanceSpecifications()`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 75: PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_saved_in_separate_directory() -> getSavedInSeperateDirectory; get_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> savedInSeperateDirectory; set_saved_in_separate_directory() -> setSavedInSeperateDirectory
- **Expected Python method(s):** `get_saved_in_seperate_directory`, `set_saved_in_seperate_directory`
- **Java signature(s):** `IRPPackage.getSavedInSeperateDirectory()`, `IRPPackage.setSavedInSeperateDirectory(int)`
- **pywin32 member(s):** savedInSeperateDirectory (property)
- **Recommended change:** Rename the Python method to the snake_case Java API name or document the alias.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 76: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_sequence_diagrams() -> getSequenceDiagrams; get_sequence_diagrams() -> sequenceDiagrams
- **Expected Python method(s):** `get_sequence_diagrams`
- **Java signature(s):** `IRPPackage.getSequenceDiagrams()`
- **pywin32 member(s):** sequenceDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 77: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_source_artifacts() -> getSourceArtifacts; get_source_artifacts() -> sourceArtifacts
- **Expected Python method(s):** `get_source_artifacts`
- **Java signature(s):** `IRPPackage.getSourceArtifacts()`
- **pywin32 member(s):** sourceArtifacts (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 78: MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `get_stereotype`, `set_stereotype`
- **Java signature(s):** `IRPModelElement.getStereotype()`, `IRPModelElement.setStereotype(com.telelogic.rhapsody.core.IRPStereotype)`
- **pywin32 member(s):** stereotype (property)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 79: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_stereotypes() -> getStereotypes; get_stereotypes() -> stereotypes
- **Expected Python method(s):** `get_stereotypes`
- **Java signature(s):** `IRPModelElement.getStereotypes()`
- **pywin32 member(s):** stereotypes (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 80: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_structure_diagrams() -> getStructureDiagrams; get_structure_diagrams() -> structureDiagrams
- **Expected Python method(s):** `get_structure_diagrams`
- **Java signature(s):** `IRPUnit.getStructureDiagrams()`
- **pywin32 member(s):** structureDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 81: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_template_parameters() -> getTemplateParameters; get_template_parameters() -> templateParameters
- **Expected Python method(s):** `get_template_parameters`
- **Java signature(s):** `IRPModelElement.getTemplateParameters()`
- **pywin32 member(s):** templateParameters (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 82: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_ti() -> getTi; get_ti() -> ti; set_ti() -> setTi; set_ti() -> ti
- **Expected Python method(s):** `get_ti`, `set_ti`
- **Java signature(s):** `IRPModelElement.getTi()`, `IRPModelElement.setTi(com.telelogic.rhapsody.core.IRPTemplateInstantiation)`
- **pywin32 member(s):** ti (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 83: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_timing_diagrams() -> getTimingDiagrams; get_timing_diagrams() -> timingDiagrams
- **Expected Python method(s):** `get_timing_diagrams`
- **Java signature(s):** `IRPPackage.getTimingDiagrams()`
- **pywin32 member(s):** timingDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 84: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_types() -> getTypes; get_types() -> types
- **Expected Python method(s):** `get_types`
- **Java signature(s):** `IRPPackage.getTypes()`
- **pywin32 member(s):** types (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 85: ACCESSOR_ALIAS_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_unit_path() -> getUnitPath; set_unit_path() -> setUnitPath; set_unit_path() -> unitPath
- **Expected Python method(s):** `get_unit_path`, `set_unit_path`
- **Java signature(s):** `IRPUnit.getUnitPath(int)`, `IRPUnit.setUnitPath(java.lang.String)`
- **pywin32 member(s):** setUnitPath (method)
- **Recommended change:** Review the related API spellings and document the intended mapping.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 86: MISSING_PYTHON_WRAPPER
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** —
- **Expected Python method(s):** `unlock_on_design_manager`
- **Java signature(s):** `IRPModelElement.unlockOnDesignManager()`
- **pywin32 member(s):** unlockOnDesignManager (method)
- **Recommended change:** Implement the Python wrapper or mark this API member intentionally unsupported.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 87: PYWIN32_MEMBER_MISSING
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer
- **Expected Python method(s):** `update_contained_diagrams_on_server`
- **Java signature(s):** `IRPPackage.updateContainedDiagramsOnServer(int)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 88: PYWIN32_MEMBER_MISSING
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** update_contained_matrices_on_server() -> updateContainedMatricesOnServer
- **Expected Python method(s):** `update_contained_matrices_on_server`
- **Java signature(s):** `IRPPackage.updateContainedMatricesOnServer(int)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 89: PYWIN32_MEMBER_MISSING
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** update_contained_tables_on_server() -> updateContainedTablesOnServer
- **Expected Python method(s):** `update_contained_tables_on_server`
- **Java signature(s):** `IRPPackage.updateContainedTablesOnServer(int)`
- **pywin32 member(s):** —
- **Recommended change:** Use a member exposed by the registered type library or verify the Rhapsody version.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 90: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_use_case_diagrams() -> getUseCaseDiagrams; get_use_case_diagrams() -> useCaseDiagrams
- **Expected Python method(s):** `get_use_case_diagrams`
- **Java signature(s):** `IRPPackage.getUseCaseDiagrams()`
- **pywin32 member(s):** useCaseDiagrams (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 91: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_use_cases() -> getUseCases; get_use_cases() -> useCases
- **Expected Python method(s):** `get_use_cases`
- **Java signature(s):** `IRPPackage.getUseCases()`
- **pywin32 member(s):** useCases (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 92: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_user_defined_meta_class() -> getUserDefinedMetaClass; get_user_defined_meta_class() -> userDefinedMetaClass
- **Expected Python method(s):** `get_user_defined_meta_class`
- **Java signature(s):** `IRPModelElement.getUserDefinedMetaClass()`
- **pywin32 member(s):** userDefinedMetaClass (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.

### Finding 93: ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH
- **Target:** `RPPackage` in `src/rhapsody_cli/models/elements/containment/model_package.py`
- **Current Python wrapper/COM call:** get_user_defined_stereotypes() -> getUserDefinedStereotypes; get_user_defined_stereotypes() -> userDefinedStereotypes
- **Expected Python method(s):** `get_user_defined_stereotypes`
- **Java signature(s):** `IRPPackage.getUserDefinedStereotypes()`
- **pywin32 member(s):** userDefinedStereotypes (property)
- **Recommended change:** Use a property-aware getter/setter fallback or document the binding mismatch.
- **Test action:** Add or update a unit test with a fake COM object that verifies the selected member/property and returned value.
