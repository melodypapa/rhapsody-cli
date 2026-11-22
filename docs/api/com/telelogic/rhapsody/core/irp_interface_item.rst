.. _rhapsody-java-interface-IRPInterfaceItem:

IRPInterfaceItem
================

The IRPInterfaceItem interface is the base for operation-like elements carrying arguments.

- **Java interface:** IRPInterfaceItem
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPInterfaceItem interface represents an item with a signature and argument list.
- **Python wrapper:** IRPInterfaceItem
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPInterfaceItem``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_interface_item`` (the
  package also re-exports ``IRPInterfaceItem`` lazily).

.. list-table:: Verified IRPInterfaceItem deviations and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - —
     - —
     - —
     - No deviations. ``getArguments``/``getSignature`` map to the ``arguments``/
       ``signature`` pywin32 properties; ``getSignatureNoArgNames``/
       ``getSignatureNoArgTypes`` are pywin32 methods called via ``call_com``.
