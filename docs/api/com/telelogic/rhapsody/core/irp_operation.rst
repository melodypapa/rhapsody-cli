.. _rhapsody-java-interface-IRPOperation:

IRPOperation
============

The IRPOperation interface represents an operation or method in a classifier.

- **Java interface:** IRPOperation
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPOperation interface represents an operation or method in a classifier.
- **Python wrapper:** IRPOperation
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPOperation``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation`` (the
  package also re-exports ``IRPOperation`` lazily).

Every migrated member calls exactly one pywin32-exposed COM member: method-shaped
members via ``call_com`` and property-shaped members via ``get_com_property``/
``set_com_property``. The Python surface keeps the Java-shaped ``get_*``/``set_*``
names even where COM exposes a property.

.. list-table:: Verified IRPOperation binding differences and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - updateContainedDiagramsOnServer (method)
     - updateContainedDiagramsOnServer absent from the committed catalog
     - update_contained_diagrams_on_server() -> updateContainedDiagramsOnServer
     - PYWIN32_MEMBER_MISSING. The Java-shaped member is absent from the pywin32
       catalog; the site is left unchanged and recorded as a blocker pending
       Windows typelib evidence. No direct COM call was added for an unexposed member.
   * - getIsConst (method); setIsConst (method); getIsFinal (method);
     setIsFinal (method); getVisibility (method); setVisibility (method)
     - isConst (property); isFinal (property); visibility (property)
     - get_is_const()/set_is_const(); get_is_final()/set_is_final();
     get_visibility()/set_visibility()
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH. The getters read the
       catalogued property via ``get_com_property``; the pre-existing setters call the
       Java-shaped members directly and are documented as expected informational
       differences in ``IRPOperation_api_report.md``.
   * - getReturnTypeDeclaration (method); setReturnTypeDeclaration (method);
     getImplementationSignature (method)
     - getReturnTypeDeclaration (method); setReturnTypeDeclaration (method);
     getImplementationSignature (method)
     - get_return_type_declaration()/set_return_type_declaration()/
     get_implementation_signature() via ``call_com``
     - MATCH; method-shaped in both JavaDoc and pywin32.
