.. _rhapsody-java-interface-IRPType:

IRPType
=======

The IRPType interface represents a named type definition.

- **Java interface:** IRPType
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPType interface represents a type definition in the model.
- **Python wrapper:** IRPType
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPType``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type`` (the
  package also re-exports ``IRPType`` lazily).

.. list-table:: Verified IRPType binding differences and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - getEnumerationLiterals (method); getIsPredefined (method); getIsTypedef (method);
     getTypedefBaseType (method); setTypedefBaseType (method)
     - enumerationLiterals (property); isPredefined (property); isTypedef (property);
     typedefBaseType (property)
     - get_enumeration_literals(), get_is_predefined(), get_is_typedef(),
     get_typedef_base_type(), set_typedef_base_type() via
     get_com_property/set_com_property
     - COM_MEMBER_NOT_EXPOSED resolved. The Java-shaped members are absent from the
       pywin32 catalog; bindings migrated to the authoritative properties
       (``enumerationLiterals``, ``isPredefined``, ``isTypedef``, ``typedefBaseType``)
       as recommended in ``IRPType_api_report.md``. Python get_* names retained
       by repo convention; COM property shape honoured in the binding.
   * - getIsTypedefConstant (method); setIsTypedefConstant (method);
     getIsTypedefOrdered (method); setIsTypedefOrdered (method);
     getIsTypedefReference (method); setIsTypedefReference (method)
     - isTypedefConstant (property); isTypedefOrdered (property);
     isTypedefReference (property)
     - get_is_typedef_constant(), set_is_typedef_constant(),
     get_is_typedef_ordered(), set_is_typedef_ordered(),
     get_is_typedef_reference(), set_is_typedef_reference() via
     get_com_property/set_com_property
     - ACCESSOR_ALIAS_MISMATCH; METHOD_PROPERTY_MISMATCH. Python get_* names retained
       by repo convention; COM property shape honoured in the binding.
   * - getDeclaration (method); getKind (method); getTypedefMultiplicity (method);
     setDeclaration (method); setKind (method); setTypedefMultiplicity (method)
     - declaration (property); kind (property); typedefMultiplicity (property)
     - get_declaration()/set_declaration()/... via get_com_property/set_com_property
     - METHOD_PROPERTY_MISMATCH; resolved as above.
