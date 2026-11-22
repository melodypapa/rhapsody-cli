.. _rhapsody-java-interface-IRPPackage:

IRPPackage
==========

The IRPPackage interface represents a package that contains model elements.

- **Java interface:** IRPPackage
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPPackage interface represents a model package containing classes, actors, and other elements.
- **Python wrapper:** IRPPackage
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPPackage``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package`` (the
  package also re-exports ``IRPPackage`` lazily).

.. list-table:: Verified IRPPackage binding differences and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - addAssociation (method)
     - addAssociation (method); absent from JavaDoc
     - add_association() -> addAssociation
     - JAVA_DOC_MISSING. Catalog-backed COM extension; calls the member directly.
   * - addInstanceSpecification (method); loginToRemoteArtifactServer (method);
     updateContainedDiagramsOnServer (method); updateContainedMatricesOnServer (method);
     updateContainedTablesOnServer (method); getRootInstanceSpecifications (method)
     - absent from the committed catalog
     - add_instance_specification(), login_to_remote_artifact_server(),
     update_contained_diagrams_on_server(), update_contained_matrices_on_server(),
     update_contained_tables_on_server(), get_root_instance_specifications()
     - PYWIN32_MEMBER_MISSING. No direct COM call added for an unexposed member;
       sites are documented blockers pending Windows typelib evidence.
   * - addStatechart (method); getPackages (method); reCalculateEventsBaseId (method);
     getSavedInSeperateDirectory (method); setSavedInSeperateDirectory (method)
     - addStatechart (method); packages (property); reCalculateEventsBaseId (method);
     savedInSeperateDirectory (property)
     - add_statechart_diagram(), get_nested_packages(), recalculate_events_base_id(),
     get_saved_in_separate_directory(), set_saved_in_separate_directory()
     - PYTHON_METHOD_NAME_MISMATCH / METHOD_PROPERTY_MISMATCH. Python surface names
       retained by repo convention; property-shaped members use get_com_property/
       set_com_property.
   * - getClasses (method); getActors (method); getUseCases (method);
     getSequenceDiagrams (method); getUseCaseDiagrams (method);
     getCollaborationDiagrams (method); getComponentDiagrams (method);
     getDeploymentDiagrams (method); getObjectModelDiagrams (method);
     getTimingDiagrams (method); getPanelDiagrams (method); getEvents (method);
     getFlowItems (method); getFlows (method); getNodes (method); getModules (method);
     getTypes (method); getGlobalFunctions (method); getGlobalObjects (method);
     getGlobalVariables (method); getNestedClassifiers (method);
     getNestedComponents (method); getInstanceSpecifications (method); getLinks (method);
     getBehavioralDiagrams (method); getSourceArtifacts (method); getEventsBaseId (method);
     getUserDefinedStereotypes (method)
     - classes, actors, useCases, sequenceDiagrams, useCaseDiagrams,
     collaborationDiagrams, componentDiagrams, deploymentDiagrams, objectModelDiagrams,
     timingDiagrams, panelDiagrams, events, flowItems, flows, nodes, modules, types,
     globalFunctions, globalObjects, globalVariables, nestedClassifiers,
     nestedComponents, instanceSpecifications, links, behavioralDiagrams,
     sourceArtifacts, eventsBaseId, userDefinedStereotypes (all properties)
     - corresponding get_*() methods via get_com_property("<name>")
     - METHOD_PROPERTY_MISMATCH; Python get_* names retained by repo convention.
   * - getRemoteRequirementsPopulateMode (method); setRemoteRequirementsPopulateMode (method);
     getAllNestedElements (method); getNamespace (method)
     - getRemoteRequirementsPopulateMode (method); setRemoteRequirementsPopulateMode (method);
     getAllNestedElements (method); getNamespace (method)
     - get_remote_requirements_populate_mode()/... via call_com
     - MATCH; method-shaped in both JavaDoc and pywin32.
