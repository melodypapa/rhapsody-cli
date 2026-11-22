.. _rhapsody-java-interface-IRPApplication:

IRPApplication
==============

The IRPApplication interface represents the Rhapsody application and its menu-bar commands.

- **Java interface:** IRPApplication
- **Java package:** com.telelogic.rhapsody.core
- **JavaDoc description:** The IRPApplication interface represents the Rhapsody application.
- **Python wrapper:** RhapsodyApplication
- **Python import:** ``from rhapsody_cli.application import RhapsodyApplication``
- **Canonical module:** ``rhapsody_cli.application`` (application layer; §2 package move N/A).

.. list-table:: Verified IRPApplication binding differences and dispositions
   :header-rows: 1
   :widths: 34 24 24 18

   * - JavaDoc member/signature
     - COM/pywin32 exposure
     - Python implementation
     - Deviation and treatment
   * - getBuildNo (method); getOMROOT (method)
     - BuildNo (property); OMROOT (property)
     - get_build_no() -> getBuildNo; get_omroot() -> getOMROOT
     - COM_MEMBER_NOT_EXPOSED. Java-shaped calls left unchanged and documented as
       informational binding differences in ``IRPApplication_api_report.md``.
   * - version (method)
     - version (method)
     - get_version() -> version
     - PYTHON_METHOD_NAME_MISMATCH. Python alias retained by repo convention.
   * - closeAllProjects (method); connect; disconnect; getRhapsodyDir (method)
     - no static COM member (facade helpers)
     - close_all_projects(), connect(), disconnect(), get_rhapsody_dir()
     - PYTHON_ONLY_MEMBER. These helpers have live callers across the codebase;
       removal is a recorded blocker rather than performed. ``getPlugInWindow``
       is Java-only and intentionally unsupported.
   * - getProjects (method); getIsHiddenUI (method); setHiddenUI (method)
     - projects (property); isHiddenUI (property); setHiddenUI (method)
     - get_projects()/get_is_hidden_ui() via get_com_property; set_hidden_ui() via call_com
     - METHOD_PROPERTY_MISMATCH; Python get_* names retained by repo convention.
