.. _rhapsody-java-interface-IRPUnit:

IRPUnit
=======

The IRPUnit interface represents model elements that can be saved as separate files.

- **Java interface:** IRPUnit
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPUnit interface represents model elements that can be saved as separate files.
- **Python wrapper:** IRPUnit
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit import IRPUnit``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_unit`` (the
  package also re-exports ``IRPUnit`` lazily).

No deviations require code changes. Every migrated member calls exactly one pywin32-exposed
COM member: method-shaped members via ``call_com`` and property-shaped members via
``get_com_property``/``set_com_property``. The Python surface keeps the Java-shaped
``get_*``/``set_*`` method names even where COM exposes a property — the binding, not the
Python name, follows the COM shape recorded in ``IRPUnit_api_report.md``.

.. list-table:: Verified IRPUnit binding differences and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - getUnitPath (method); setUnitPath (method)
     - setUnitPath (method); getUnitPath absent from the committed catalog
     - get_unit_path() is a `NotImplementedError` stub; set_unit_path() -> setUnitPath
     - UNAVAILABLE_DOCUMENTED; expected informational difference. getUnitPath is absent from
       pywin32, so get_unit_path() is a documented Java-only stub that raises
       `NotImplementedError` before dispatch; set_unit_path() uses the catalogued setUnitPath
       method via call_com.
   * - getCMHeader (method); setCMHeader (method)
     - CMHeader (property)
     - get_cm_header()/set_cm_header() via get_com_property/set_com_property("CMHeader")
     - METHOD_PROPERTY_MISMATCH; Python get/set names retained by repo convention, COM
       property shape honoured in the binding.
   * - getCurrentDirectory (method)
     - currentDirectory (property)
     - get_current_directory() via get_com_property("currentDirectory")
     - METHOD_PROPERTY_MISMATCH; resolved as above.
   * - getFilename (method); setFilename (method)
     - filename (property)
     - get_filename()/set_filename() via get_com_property/set_com_property("filename")
     - METHOD_PROPERTY_MISMATCH; resolved as above.
   * - getIncludeInNextLoad (method); setIncludeInNextLoad (method)
     - includeInNextLoad (property)
     - get_include_in_next_load()/set_include_in_next_load() via get_com_property/
       set_com_property("includeInNextLoad")
     - METHOD_PROPERTY_MISMATCH; resolved as above.
   * - getIsStub (method)
     - isStub (property)
     - get_is_stub() via get_com_property("isStub")
     - METHOD_PROPERTY_MISMATCH; resolved as above.
   * - getStructureDiagrams (method)
     - structureDiagrams (property)
     - get_structure_diagrams() via get_com_property("structureDiagrams")
     - METHOD_PROPERTY_MISMATCH; resolved as above.
