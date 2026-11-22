.. _rhapsody-java-interface-IRPArgument:

IRPArgument
===========

The IRPArgument interface represents an argument of an operation.

- **Java interface:** IRPArgument
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPArgument interface represents an operation argument or parameter.
- **Python wrapper:** IRPArgument
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPArgument``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_argument`` (the
  package also re-exports ``IRPArgument`` lazily).

No deviations require code changes. ``argumentDirection`` is a pywin32 property read
and written via ``get_com_property``/``set_com_property``; the Python
``get_argument_direction``/``set_argument_direction`` names are retained by repo
convention.

.. list-table:: Verified IRPArgument deviations and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - —
     - —
     - —
     - No deviations. ``getArgumentDirection``/``setArgumentDirection`` map to the
       catalogued ``argumentDirection`` property.
