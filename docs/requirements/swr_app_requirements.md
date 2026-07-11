# Software Requirements - APP (Application Connection Layer)

**Category:** APP
**Prefix:** SWR
**Source:** Extracted from code
**Last Validated:** 2026-07-07

---

## SWR_APP_00001: Attach to Running Rhapsody Instance (Internal Helper)

**ID:** SWR_APP_00001
**Title:** Attach to an already-running Rhapsody instance via COM (internal helper)
**Status:** Implemented
**Priority:** High
**Description:**
The private `RhapsodyApplication._attach()` class method shall attach to an
already-running IBM Rhapsody instance by calling
`win32com.client.GetActiveObject("Rhapsody2.Application.1")`. If no running
instance is found, a `RhapsodyConnectionError` shall be raised. This method is
an internal helper called by `connect()` and should not be called directly by
consumers.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication._attach
**Last Changed:** 2026-07-11

---

## SWR_APP_00002: Launch New Rhapsody Instance (Internal Helper)

**ID:** SWR_APP_00002
**Title:** Launch a new Rhapsody instance via COM Dispatch (internal helper)
**Status:** Implemented
**Priority:** High
**Description:**
The private `RhapsodyApplication._launch()` class method shall start a new
Rhapsody instance by calling
`win32com.client.Dispatch("Rhapsody2.Application.1")`. If launch fails, a
`RhapsodyConnectionError` shall be raised. This method is an internal helper
called by `connect()` and should not be called directly by consumers.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication._launch
**Last Changed:** 2026-07-11

---

## SWR_APP_00003: Connect with Smart Fallback

**ID:** SWR_APP_00003
**Title:** Connect to Rhapsody with attach-first fallback to launch
**Status:** Implemented
**Priority:** High
**Description:**
The `RhapsodyApplication.connect(attach_only: bool = False, show_gui: bool = True)`
class method shall be the primary entry point for connecting to Rhapsody. It shall
first attempt `_attach()` to connect to a running instance. If `_attach()` raises
`RhapsodyConnectionError` and `attach_only` is True, the error shall propagate.
If `attach_only` is False (default), it shall fall back to `_launch()` to start a
new instance. When a new instance is launched and `show_gui` is True (default), it
shall call `setHiddenUI(False)` to make the GUI window visible.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.connect
**Last Changed:** 2026-07-11

---

## SWR_APP_00004: Open Project File

**ID:** SWR_APP_00004
**Title:** Open a Rhapsody project file from a path
**Status:** Implemented
**Priority:** High
**Description:**
The `openProject(filename: str)` method shall open the Rhapsody project at the given
file path and return a wrapped `RPProject` instance. COM errors during the call shall
be translated to `RhapsodyRuntimeException`.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.openProject
**Last Changed:** 2026-07-07

---

## SWR_APP_00005: Get Active Project

**ID:** SWR_APP_00005
**Title:** Retrieve the currently active project
**Status:** Implemented
**Priority:** Medium
**Description:**
The `activeProject()` method shall return the currently active Rhapsody project as a
wrapped `RPProject` instance.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.activeProject
**Last Changed:** 2026-07-07

---

## SWR_APP_00006: Get All Open Projects

**ID:** SWR_APP_00006
**Title:** Retrieve all currently open projects
**Status:** Implemented
**Priority:** Medium
**Description:**
The `getProjects()` method shall return an `RPCollection` containing all currently open
Rhapsody projects.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.getProjects
**Last Changed:** 2026-07-07

---

## SWR_APP_00007: Quit Application

**ID:** SWR_APP_00007
**Title:** Terminate the wrapped Rhapsody instance
**Status:** Implemented
**Priority:** Medium
**Description:**
The `quit()` method shall terminate the Rhapsody instance by calling `quit()` on the
underlying COM object.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.quit
**Last Changed:** 2026-07-07

---

## SWR_APP_00008: No Global Singleton

**ID:** SWR_APP_00008
**Title:** Each RhapsodyApplication instance wraps one COM object independently
**Status:** Implemented
**Priority:** Medium
**Description:**
`RhapsodyApplication` shall not be a global singleton. Each instance shall wrap exactly
one COM object, allowing multiple simultaneous Rhapsody instances/models to be managed
side by side in the same process.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.__init__
**Last Changed:** 2026-07-07

---

## SWR_APP_00009: Prog ID Constant

**ID:** SWR_APP_00009
**Title:** Use canonical Rhapsody COM Prog ID
**Status:** Implemented
**Priority:** Low
**Description:**
The COM Prog ID used for attach/launch shall be `"Rhapsody2.Application.1"` (the
canonical Rhapsody automation Prog ID for the "new" COM API version, as documented
in IBM Rhapsody's automation samples; the legacy `"Rhapsody.Application"` Prog ID
is not registered by all Rhapsody installations, e.g. Rhapsody 9.0.2).
**Implementation:** src/rhapsody_cli/application.py:_PROG_ID
**Last Changed:** 2026-07-07

---

## SWR_APP_00010: Close All Projects

**ID:** SWR_APP_00010
**Title:** Close all open projects without quitting Rhapsody
**Status:** Implemented
**Priority:** Medium
**Description:**
The `closeAllProjects()` method shall close all open Rhapsody projects without
terminating the Rhapsody instance itself.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.closeAllProjects
**Last Changed:** 2026-07-11

---

## SWR_APP_00011: Save All Projects

**ID:** SWR_APP_00011
**Title:** Save all open projects
**Status:** Implemented
**Priority:** Medium
**Description:**
The `saveAll()` method shall save all currently open Rhapsody projects.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.saveAll
**Last Changed:** 2026-07-11

---

## SWR_APP_00012: Get Version String

**ID:** SWR_APP_00012
**Title:** Retrieve the Rhapsody version string
**Status:** Implemented
**Priority:** Low
**Description:**
The `getVersion()` method shall return the installed Rhapsody version as a string.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.getVersion
**Last Changed:** 2026-07-11

---

## SWR_APP_00013: Get Build Number

**ID:** SWR_APP_00013
**Title:** Retrieve the Rhapsody build number
**Status:** Implemented
**Priority:** Low
**Description:**
The `getBuildNo()` method shall return the Rhapsody build number as a string.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.getBuildNo
**Last Changed:** 2026-07-11

---

## SWR_APP_00014: Get Installation Directory

**ID:** SWR_APP_00014
**Title:** Retrieve the Rhapsody installation directory
**Status:** Implemented
**Priority:** Low
**Description:**
The `getRhapsodyDir()` method shall return the Rhapsody installation directory path.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.getRhapsodyDir
**Last Changed:** 2026-07-11

---

## SWR_APP_00015: Get OMROOT Directory

**ID:** SWR_APP_00015
**Title:** Retrieve the OMROOT directory path
**Status:** Implemented
**Priority:** Low
**Description:**
The `getOMROOT()` method shall return the OMROOT directory path.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.getOMROOT
**Last Changed:** 2026-07-11

---

## SWR_APP_00016: Generate Code

**ID:** SWR_APP_00016
**Title:** Generate code for the active configuration
**Status:** Implemented
**Priority:** Medium
**Description:**
The `generate()` method shall generate code for the active configuration of the
currently active Rhapsody project.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.generate
**Last Changed:** 2026-07-11

---

## SWR_APP_00017: Generate Code for Specific Elements

**ID:** SWR_APP_00017
**Title:** Generate code for specific elements
**Status:** Implemented
**Priority:** Medium
**Description:**
The `generateElements(elements: RPCollection)` method shall generate code for the
specified model elements.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.generateElements
**Last Changed:** 2026-07-11

---

## SWR_APP_00018: Generate Entire Project

**ID:** SWR_APP_00018
**Title:** Generate code for the entire active project
**Status:** Implemented
**Priority:** Medium
**Description:**
The `generateEntireProject()` method shall generate code for the entire currently
active Rhapsody project.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.generateEntireProject
**Last Changed:** 2026-07-11

---

## SWR_APP_00019: Regenerate Code

**ID:** SWR_APP_00019
**Title:** Regenerate code (full regeneration)
**Status:** Implemented
**Priority:** Medium
**Description:**
The `regenerate()` method shall perform a full code regeneration for the active
project.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.regenerate
**Last Changed:** 2026-07-11

---

## SWR_APP_00020: Add to Model

**ID:** SWR_APP_00020
**Title:** Add a model element from a file
**Status:** Implemented
**Priority:** Medium
**Description:**
The `addToModel(filename: str, withDescendant: int)` method shall add a model
element from the specified file, optionally adding descendants.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.addToModel
**Last Changed:** 2026-07-11

---

## SWR_APP_00021: Add to Model (Extended)

**ID:** SWR_APP_00021
**Title:** Add a model element from a file with extended options
**Status:** Implemented
**Priority:** Medium
**Description:**
The `addToModelEx(filename: str, mode: int, addSubUnits: int, addDependents: int)`
method shall add a model element from a file with extended options including mode,
sub-units, and dependents.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.addToModelEx
**Last Changed:** 2026-07-11

---

## SWR_APP_00022: Set Log File

**ID:** SWR_APP_00022
**Title:** Set the Rhapsody log file path
**Status:** Implemented
**Priority:** Low
**Description:**
The `setLog(fullPathname: str)` method shall set the log file path used by
Rhapsody for diagnostic output.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.setLog
**Last Changed:** 2026-07-11

---

## SWR_APP_00023: Check Model

**ID:** SWR_APP_00023
**Title:** Run model checking on the active project
**Status:** Implemented
**Priority:** Medium
**Description:**
The `checkModel()` method shall run model validation checks on the currently
active Rhapsody project.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.checkModel
**Last Changed:** 2026-07-11

---

## SWR_APP_00024: Disconnect

**ID:** SWR_APP_00024
**Title:** Disconnect from Rhapsody (lifecycle pair with connect)
**Status:** Implemented
**Priority:** High
**Description:**
The `disconnect()` method shall be the lifecycle pair of `connect()`. It shall
call `quit()` to gracefully terminate the Rhapsody instance and provide a cleanup
hook for consumers.
**Implementation:** src/rhapsody_cli/application.py:RhapsodyApplication.disconnect
**Last Changed:** 2026-07-11
