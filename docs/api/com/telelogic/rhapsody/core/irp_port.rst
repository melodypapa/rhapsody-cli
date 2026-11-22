.. _rhapsody-java-interface-IRPPort:

IRPPort
=======

The IRPPort interface represents a port on a classifier.

- **Java interface:** IRPPort
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPPort interface represents a port on a classifier in the model.
- **Python wrapper:** IRPPort
- **Python import:** ``from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPPort``
- **Canonical module:** ``rhapsody_cli.models.com.telelogic.rhapsody.core.irp_port`` (the
  package also re-exports ``IRPPort`` lazily).

.. list-table:: Verified IRPPort binding differences and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - getContract (method); setContract (method)
     - getContract/setContract/contract absent from the committed catalog
     - get_contract()/set_contract() legacy dual-binding sites unchanged
     - PYWIN32_MEMBER_MISSING. The members are absent from every catalog; no blind
       migration was attempted. The sites are documented blockers pending Windows
       typelib evidence; use ``get_port_contract``/``set_port_contract`` instead.
   * - getIsBehavioral (method); setIsBehavioral (method); getIsReversed (method);
     setIsReversed (method); getPortContract (method); setPortContract (method);
     getProvidedInterfaces (method); getRequiredInterfaces (method)
     - isBehavioral (property); isReversed (property); portContract (property);
     providedInterfaces (property); requiredInterfaces (property)
     - get_is_behavioral()/set_is_behavioral()/... via get_com_property/set_com_property
     - METHOD_PROPERTY_MISMATCH; Python ``get_*``/``set_*`` names retained by repo
       convention, COM property shape honoured in the binding.
