.. _rhapsody-java-interface-IRPClassifier:

IRPClassifier
=============

The IRPClassifier interface is the shared base for all classifiable model elements.

- **Java interface:** IRPClassifier
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPClassifier interface is the base interface for classifiable model elements.
- **Python wrapper:** IRPClassifier
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClassifier``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier`` (the
  package also re-exports ``IRPClassifier`` lazily).

Every migrated member calls exactly one pywin32-exposed COM member: method-shaped
members via ``call_com`` and property-shaped members via ``get_com_property``. The
Python surface keeps the Java-shaped ``get_*``/``set_*`` method names even where COM
exposes a property — the binding, not the Python name, follows the COM shape recorded
in ``IRPClassifier_api_report.md``.

.. list-table:: Verified IRPClassifier binding differences and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - addPort (method)
     - addNewAggr (method)
     - add_port() -> addNewAggr("Port", name)
     - JAVA_DOC_MISSING. ``addNewAggr`` is absent from the JavaDoc but is present in
       the committed pywin32 catalog; the site calls the catalogued member directly
       and the deviation is recorded in the API report.
   * - getAttributes (method); getOperations (method); getRelations (method);
     getGeneralizations (method); getInterfaceItems (method); getPorts (method);
     getNestedClassifiers (method); getFlows (method); getFlowItems (method);
     getLinks (method); getSourceArtifacts (method); getBehavioralDiagrams (method);
     getSequenceDiagrams (method); getActivityDiagram (method); getStatechart (method);
     getBaseClassifiers (method); getDerivedClassifiers (method)
     - attributes (property); operations (property); relations (property);
     generalizations (property); interfaceItems (property); ports (property);
     nestedClassifiers (property); flows (property); flowItems (property);
     links (property); sourceArtifacts (property); behavioralDiagrams (property);
     sequenceDiagrams (property); activityDiagram (property); statechart (property);
     baseClassifiers (property); derivedClassifiers (property)
     - get_attributes()/get_operations()/... via get_com_property("<name>")
     - METHOD_PROPERTY_MISMATCH; Python ``get_*`` names retained by repo convention,
       COM property shape honoured in the binding.
   * - getAttributesIncludingBases (method); getInterfaceItemsIncludingBases (method);
     getRelationsIncludingBases (method)
     - getAttributesIncludingBases (method); getInterfaceItemsIncludingBases (method);
     getRelationsIncludingBases (method)
     - get_attributes_including_bases()/... via call_com(lambda: self._com.<name>())
     - MATCH; method-shaped in both JavaDoc and pywin32.
