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
   * - —
     - —
     - —
     - No deviations. Every JavaDoc member is backed by the matching pywin32
       property or method and the wrapper reads/writes that member directly.
       The former Java-named `get*` bindings (`getEnumerationLiterals`,
       `getIsPredefined`, `getIsTypedef`, `getTypedefBaseType` /
       `setTypedefBaseType`) were migrated to the authoritative properties
       (`enumerationLiterals`, `isPredefined`, `isTypedef`, `typedefBaseType`);
       Python get_* names are retained by repo convention while the COM
       property shape is honoured in the binding.
