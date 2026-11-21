.. _rhapsody-java-interface-IRPClass:

IRPClass
========

The IRPClass interface represents classes in Rhapsody models.

- **Java interface:** IRPClass
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPClass interface represents classes in Rhapsody models.
- **Python wrapper:** IRPClass
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class``

Zero actionable deviations require code changes. The table below records every reported
binding difference and wrapper-backlog member with its verified disposition. Method/property
mismatches are expected because the Java API exposes accessors as methods while the pywin32
binding exposes the same names as properties; the Python wrappers call the exposed member
directly (`call_com` for methods, `get_com_property`/`set_com_property` for properties).
JavaDoc-only members are intentionally unsupported when absent from
the Rhapsody2.Application.1 type library; no direct COM call is added for such members.

.. list-table:: Verified IRPClass deviations and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - —
     - —
     - is_a_template() -> aTemplate
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - getActivityDiagram (method)
     - activityDiagram (property)
     - get_activity_diagram() -> activityDiagram; get_activity_diagram() -> getActivityDiagram
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - addEventReceptionWithEvent (method)
     - —
     - —
     - JAVA_ONLY_MEMBER; Verify the Java documentation against the installed COM type library.
   * - getAllTags (method)
     - allTags (property)
     - get_all_tags() -> allTags; get_all_tags() -> getAllTags
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getAnnotations (method)
     - annotations (property)
     - get_annotations() -> annotations; get_annotations() -> getAnnotations
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getAssociationClasses (method)
     - associationClasses (property)
     - get_association_classes() -> associationClasses; get_association_classes() -> getAssociationClasses
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getAttributes (method)
     - attributes (property)
     - get_attributes() -> attributes; get_attributes() -> getAttributes
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getBaseClassifiers (method)
     - baseClassifiers (property)
     - get_base_classifiers() -> baseClassifiers; get_base_classifiers() -> getBaseClassifiers
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getBehavioralDiagrams (method)
     - behavioralDiagrams (property)
     - get_behavioral_diagrams() -> behavioralDiagrams; get_behavioral_diagrams() -> getBehavioralDiagrams
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getBinaryID (method)
     - BinaryID (property)
     - get_binary_id() -> BinaryID; get_binary_id() -> getBinaryID
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getCMHeader (method); setCMHeader (method)
     - CMHeader (property)
     - get_cm_header() -> CMHeader; get_cm_header() -> getCMHeader; set_cm_header() -> CMHeader; set_cm_header() -> setCMHeader
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getConstraints (method)
     - constraints (property)
     - get_constraints() -> constraints; get_constraints() -> getConstraints
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getConstraintsByHim (method)
     - constraintsByHim (property)
     - get_constraints_by_him() -> constraintsByHim; get_constraints_by_him() -> getConstraintsByHim
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getControlledFiles (method)
     - controlledFiles (property)
     - get_controlled_files() -> controlledFiles; get_controlled_files() -> getControlledFiles
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getCurrentDirectory (method)
     - currentDirectory (property)
     - get_current_directory() -> currentDirectory; get_current_directory() -> getCurrentDirectory
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDependencies (method)
     - dependencies (property)
     - get_dependencies() -> dependencies; get_dependencies() -> getDependencies
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDerivedClassifiers (method)
     - derivedClassifiers (property)
     - get_derived_classifiers() -> derivedClassifiers; get_derived_classifiers() -> getDerivedClassifiers
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDescription (method); setDescription (method)
     - description (property)
     - get_description() -> description; get_description() -> getDescription; set_description() -> description; set_description() -> setDescription
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDescriptionHTML (method); setDescriptionHTML (method)
     - descriptionHTML (property)
     - get_description_html() -> descriptionHTML; get_description_html() -> getDescriptionHTML
     - PYTHON_METHOD_NAME_MISMATCH; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Rename the Python method to the snake_case Java API name or document the alias.
   * - getDescriptionPlainText (method)
     - descriptionPlainText (property)
     - get_description_plain_text() -> descriptionPlainText; get_description_plain_text() -> getDescriptionPlainText
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDescriptionRTF (method); setDescriptionRTF (method)
     - descriptionRTF (property)
     - get_description_rtf() -> descriptionRTF; get_description_rtf() -> getDescriptionRTF; is_description_rtf() -> descriptionRTF; set_description_rtf() -> descriptionRTF; set_description_rtf() -> setDescriptionRTF
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getDisplayName (method); setDisplayName (method)
     - displayName (property)
     - get_display_name() -> displayName; get_display_name() -> getDisplayName; set_display_name() -> displayName; set_display_name() -> setDisplayName
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getFilename (method); setFilename (method)
     - filename (property)
     - get_filename() -> filename; get_filename() -> getFilename; set_filename() -> filename; set_filename() -> setFilename
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getFlowItems (method)
     - flowItems (property)
     - get_flow_items() -> flowItems; get_flow_items() -> getFlowItems
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getFlows (method)
     - flows (property)
     - get_flows() -> flows; get_flows() -> getFlows
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getGUID (method); setGUID (method)
     - GUID (property)
     - get_guid() -> GUID; get_guid() -> getGUID; set_guid() -> GUID; set_guid() -> setGUID
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getGeneralizations (method)
     - generalizations (property)
     - get_generalizations() -> generalizations; get_generalizations() -> getGeneralizations
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getHyperLinks (method)
     - hyperLinks (property)
     - get_hyper_links() -> getHyperLinks; get_hyper_links() -> hyperLinks
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getIncludeInNextLoad (method); setIncludeInNextLoad (method)
     - includeInNextLoad (property)
     - get_include_in_next_load() -> getIncludeInNextLoad; get_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> includeInNextLoad; set_include_in_next_load() -> setIncludeInNextLoad
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getInterfaceItems (method)
     - interfaceItems (property)
     - get_interface_items() -> getInterfaceItems; get_interface_items() -> interfaceItems
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getInterfaceName (method)
     - interfaceName (property)
     - get_interface_name() -> getInterfaceName; get_interface_name() -> interfaceName
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getIsAbstract (method); setIsAbstract (method)
     - isAbstract (property)
     - is_abstract() -> isAbstract
     - ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Documented decision: keep the current binding; no change.
   * - getIsActive (method); setIsActive (method)
     - isActive (property)
     - is_active() -> isActive
     - ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Documented decision: keep the current binding; no change.
   * - getIsBehaviorOverriden (method); setIsBehaviorOverriden (method)
     - isBehaviorOverriden (property)
     - is_behavior_overriden() -> isBehaviorOverriden
     - ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Documented decision: keep the current binding; no change.
   * - getIsFinal (method); setIsFinal (method)
     - getIsFinal (method); setIsFinal (method)
     - is_final() -> getIsFinal
     - ALIAS_DOCUMENTED; Documented decision: keep the current binding; no change.
   * - getIsComposite (method)
     - isComposite (property)
     - is_composite() -> isComposite
     - ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Documented decision: keep the current binding; no change.
   * - getIsExternal (method)
     - isExternal (property)
     - get_is_external() -> getIsExternal; get_is_external() -> isExternal
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getIsOfMetaClass (method)
     - isOfMetaClass (method)
     - get_is_of_meta_class() -> isOfMetaClass
     - ACCESSOR_ALIAS_MISMATCH; Review the related API spellings and document the intended mapping.
   * - getIsReactive (method)
     - isReactive (property)
     - is_reactive() -> isReactive
     - ALIAS_DOCUMENTED; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Documented decision: keep the current binding; no change.
   * - getIsShowDisplayName (method); setIsShowDisplayName (method)
     - isShowDisplayName (property)
     - get_is_show_display_name() -> getIsShowDisplayName; get_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> isShowDisplayName; set_is_show_display_name() -> setIsShowDisplayName
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getIsStub (method)
     - isStub (property)
     - get_is_stub() -> getIsStub; get_is_stub() -> isStub
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getIsUnresolved (method)
     - isUnresolved (property)
     - get_is_unresolved() -> getIsUnresolved; get_is_unresolved() -> isUnresolved
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getLinks (method)
     - links (property)
     - get_links() -> getLinks; get_links() -> links
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getLocalTags (method)
     - localTags (property)
     - get_local_tags() -> getLocalTags; get_local_tags() -> localTags
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getMainDiagram (method); setMainDiagram (method)
     - mainDiagram (property)
     - get_main_diagram() -> getMainDiagram; get_main_diagram() -> mainDiagram; set_main_diagram() -> mainDiagram; set_main_diagram() -> setMainDiagram
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getMetaClass (method)
     - metaClass (property)
     - get_meta_class() -> getMetaClass; get_meta_class() -> metaClass
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - —
     - —
     - is_modified() -> modified
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - getName (method); setName (method)
     - name (property)
     - get_name() -> getName; get_name() -> name; set_name() -> name; set_name() -> setName
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getNestedClassifiers (method)
     - nestedClassifiers (property)
     - get_nested_classifiers() -> getNestedClassifiers; get_nested_classifiers() -> nestedClassifiers
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getOfTemplate (method); setOfTemplate (method)
     - ofTemplate (property)
     - get_of_template() -> getOfTemplate; get_of_template() -> ofTemplate; set_of_template() -> ofTemplate; set_of_template() -> setOfTemplate
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getOperations (method)
     - operations (property)
     - get_operations() -> getOperations; get_operations() -> operations
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getOwner (method); setOwner (method)
     - owner (property)
     - get_owner() -> getOwner; get_owner() -> owner; set_owner() -> owner; set_owner() -> setOwner
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getPorts (method)
     - ports (property)
     - get_ports() -> getPorts; get_ports() -> ports
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getProject (method)
     - project (property)
     - get_project() -> getProject; get_project() -> project
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - —
     - —
     - add_event_reception_with_event() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - —
     - —
     - create_oslc_link() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - —
     - —
     - delete_oslc_link() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - —
     - —
     - get_oslc_links() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - —
     - —
     - set_description_html() (no static COM member)
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - —
     - —
     - is_reference_unit() -> referenceUnit
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - getReferences (method)
     - references (property)
     - get_references() -> getReferences; get_references() -> references
   * - getRmmUrl (method)
     - —
     - get_rmm_url() -> getRmmUrl; get_rmm_url() -> rmmUrl
     - UNAVAILABLE_DOCUMENTED; Documented decision: intentionally unsupported; no change.
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getRelations (method)
     - relations (property)
     - get_relations() -> getRelations; get_relations() -> relations
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - —
     - —
     - is_remote() -> remote
     - PYTHON_ONLY_MEMBER; Keep this as a local facade helper or map it to a documented API member.
   * - getRequirementTraceabilityHandle (method); setRequirementTraceabilityHandle (method)
     - requirementTraceabilityHandle (property)
     - get_requirement_traceability_handle() -> getRequirementTraceabilityHandle; get_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> requirementTraceabilityHandle; set_requirement_traceability_handle() -> setRequirementTraceabilityHandle
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getSequenceDiagrams (method)
     - sequenceDiagrams (property)
     - get_sequence_diagrams() -> getSequenceDiagrams; get_sequence_diagrams() -> sequenceDiagrams
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getSourceArtifacts (method)
     - sourceArtifacts (property)
     - get_source_artifacts() -> getSourceArtifacts; get_source_artifacts() -> sourceArtifacts
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getStatechart (method)
     - statechart (property)
     - get_statechart() -> getStatechart; get_statechart() -> statechart
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getStereotypes (method)
     - stereotypes (property)
     - get_stereotypes() -> getStereotypes; get_stereotypes() -> stereotypes
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getStructureDiagrams (method)
     - structureDiagrams (property)
     - get_structure_diagrams() -> getStructureDiagrams; get_structure_diagrams() -> structureDiagrams
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getTemplateParameters (method)
     - templateParameters (property)
     - get_template_parameters() -> getTemplateParameters; get_template_parameters() -> templateParameters
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getTi (method); setTi (method)
     - ti (property)
     - get_ti() -> getTi; get_ti() -> ti; set_ti() -> setTi; set_ti() -> ti
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - getUnitPath (method); setUnitPath (method)
     - setUnitPath (method)
     - get_unit_path() -> getUnitPath; set_unit_path() -> setUnitPath; set_unit_path() -> unitPath
     - ACCESSOR_ALIAS_MISMATCH; Review the related API spellings and document the intended mapping.
   * - updateContainedDiagramsOnServer (method)
     - —
     - —
     - JAVA_ONLY_MEMBER; Verify the Java documentation against the installed COM type library.
   * - getUserDefinedMetaClass (method)
     - userDefinedMetaClass (property)
     - get_user_defined_meta_class() -> getUserDefinedMetaClass; get_user_defined_meta_class() -> userDefinedMetaClass
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Use a property-aware getter/setter fallback or document the binding mismatch.
   * - createOSLCLink (method)
     - createOSLCLink (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.
   * - —
     - deleteActivityDiagram (method)
     - —
     - PYWIN32_ONLY_MEMBER; Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
   * - deleteOSLCLink (method)
     - deleteOSLCLink (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.
   * - —
     - deleteStatechart (method)
     - —
     - PYWIN32_ONLY_MEMBER; Confirm this version-specific member should be wrapped; otherwise classify it as unsupported.
   * - lockOnDesignManager (method)
     - lockOnDesignManager (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.
   * - getOSLCLinks (method)
     - getOSLCLinks (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.
   * - getStereotype (method); setStereotype (method)
     - stereotype (property)
     - —
     - MISSING_PYTHON_WRAPPER; ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH; Implement the Python wrapper or mark this API member intentionally unsupported.
   * - unlockOnDesignManager (method)
     - unlockOnDesignManager (method)
     - —
     - MISSING_PYTHON_WRAPPER; Implement the Python wrapper or mark this API member intentionally unsupported.
