.. _rhapsody-java-interface-IRPProject:

IRPProject
==========

The IRPProject interface represents the top-level Rhapsody project container.

- **Java interface:** IRPProject
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPProject interface represents the root container of a Rhapsody project.
- **Python wrapper:** IRPProject
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPProject``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project`` (the
  package also re-exports ``IRPProject`` lazily).

.. list-table:: Verified IRPProject binding differences and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - addActor (method); addClass (method); addNode (method); deleteNode (method);
     findNode (method); getNodes (method); getPackages (method)
     - pywin32 extension members absent from JavaDoc
     - add_actor(), add_class(), add_node(), delete_node(), find_node(), get_nodes(),
     get_packages()
     - JAVA_DOC_MISSING. Catalog-backed COM extensions; called directly and documented.
   * - enableRhapsodyModelManager (method); setGlobalConfiguration (method);
     migrateDesignManagerLinks (method)
     - absent from the committed catalog
     - enable_rhapsody_model_manager(), set_global_configuration(),
     migrate_design_manager_links()
     - PYWIN32_MEMBER_MISSING. No direct COM call added for an unexposed member;
       sites are documented blockers pending Windows typelib evidence.
   * - gatewayExportToXML (method); gatewayExportToXML2 (method); generateReport (method)
     - GatewayExportToXML (method); GatewayExportToXML2 (method); GenerateReport (method)
     - gateway_export_to_xml(), gateway_export_to_xml2(), generate_report()
     - COM_MEMBER_NOT_EXPOSED. Python names retain the JavaDoc casing while the COM
       members use different capitalisation; the binding follows the JavaDoc names.
   * - setUseUniqueStereotypeAndRefCache (method)
     - UseUniqueStereotypeAndRefCache (property)
     - set_use_unique_stereotype_and_ref_cache()
     - COM_MEMBER_NOT_EXPOSED. The Java-shaped setter is absent from the pywin32
       catalog; its legacy dual-binding site is left unchanged pending typelib evidence.
   * - moveToDesignManager (method); moveToDesignManagerAfterLogin (method); save (method)
     - documented informational binding differences
     - move_to_design_manager(), move_to_design_manager_after_login(), save()
     - Expected informational binding differences recorded in IRPProject_api_report.md.
   * - getPackages (method); getComponents (method); getNodes (method);
     getActiveConfiguration (method); getActiveComponent (method); getAllStereotypes (method);
     getProfiles (method); getCgSimplifiedModelPackage (method); getDefaultDirectoryScheme (method);
     setDefaultDirectoryScheme (method); getNotifyPluginOnElementsChanged (method);
     setNotifyPluginOnElementsChanged (method); setWaitDialogWatchdogValue (method);
     getNewCollaboration (method); getCodeGeneratedFiles (method);
     getActiveCustomViewsOnBrowser (method); getActiveCustomViewsOnDiagram (method);
     getRemoteResourcePackages (method); getRoundtripShadowModel (method);
     isActivelyManaged (method); checkEventsBaseIdsSolveCollisions (method);
     getNewProgressBar (method)
     - packages (property); components (property); nodes (property);
     activeConfiguration (property); activeComponent (property); allStereotypes (property);
     profiles (property); cgSimplifiedModelPackage (property); defaultDirectoryScheme (property);
     notifyPluginOnElementsChanged (method); waitDialogWatchdogValue (method);
     newCollaboration (method); codeGeneratedFiles (method); activeCustomViewsOnBrowser (method);
     activeCustomViewsOnDiagram (method); remoteResourcePackages (method);
     roundtripShadowModel (method); activelyManaged (method); eventsBaseIdsSolveCollisions (method);
     newProgressBar (method)
     - get_*()/set_*() via get_com_property/set_com_property or call_com per the catalog
     - METHOD_PROPERTY_MISMATCH; Python get_* names retained by repo convention.
