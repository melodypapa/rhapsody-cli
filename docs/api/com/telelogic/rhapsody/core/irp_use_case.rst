.. _rhapsody-java-interface-IRPUseCase:

IRPUseCase
==========

The IRPUseCase interface represents a use case in the model.

- **Java interface:** IRPUseCase
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPUseCase interface represents a use case.
- **Python wrapper:** IRPUseCase
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPUseCase``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_use_case`` (the
  package also re-exports ``IRPUseCase`` lazily).

.. list-table:: Verified IRPUseCase binding differences and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - addEventReceptionWithEvent (method); updateContainedDiagramsOnServer (method)
     - absent from the committed catalog
     - add_event_reception_with_event(), update_contained_diagrams_on_server()
     - PYWIN32_MEMBER_MISSING. The Java-shaped members are absent from the pywin32
       catalog; sites are documented blockers pending Windows typelib evidence.
   * - getExtensionPoints (method); getEntryPoints (method); getDescribingDiagrams (method);
     getIsBehaviorOverriden (method)
     - extensionPoints (property); entryPoints (property); describingDiagrams (property);
     isBehaviorOverriden (property)
     - get_extension_points()/get_entry_points()/get_describing_diagrams()/
     get_is_behavior_overriden() via get_com_property
     - METHOD_PROPERTY_MISMATCH; Python get_* names retained by repo convention.
       ``get_is_behavior_overriden`` returns an int; the setter is a documented-unavailable
       NotImplementedError stub because ``setIsBehaviorOverriden`` is not exposed.
