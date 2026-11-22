.. _rhapsody-java-interface-IRPAttribute:

IRPAttribute
============

The IRPAttribute interface represents an attribute of a classifier.

- **Java interface:** IRPAttribute
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPAttribute interface represents an attribute or variable of a classifier.
- **Python wrapper:** IRPAttribute
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPAttribute``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_attribute`` (the
  package also re-exports ``IRPAttribute`` lazily).

No deviations require code changes. Each member calls exactly one pywin32-exposed
COM member: ``isConstant``, ``isOrdered``, ``isReference``, ``isStatic``,
``multiplicity``, and ``visibility`` are properties read/written via
``get_com_property``/``set_com_property``; the Python ``get_*``/``set_*`` names are
retained by repo convention.

.. list-table:: Verified IRPAttribute deviations and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - —
     - —
     - —
     - No deviations. Every JavaDoc member is backed by the matching pywin32 property
       and the wrapper reads/writes that member directly.
