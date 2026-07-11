# Unit Test Specifications - Application Connection Layer

**Category:** APP
**Prefix:** UTS
**Test Type:** Unit
**Last Validated:** 2026-07-07

---

## UTS_APP_00001: _attach Internal Helper Happy Path

**ID:** UTS_APP_00001
**Traces-To:** SWR_APP_00001
**Title:** _attach() returns a RhapsodyApplication wrapping the active COM object
**Type:** Unit
**Priority:** High
**Description:**
Verifies that `RhapsodyApplication._attach()` calls `win32com.client.GetActiveObject("Rhapsody2.Application.1")` and returns a `RhapsodyApplication` instance whose `_com` is the object returned by the COM call.
**Pre-conditions:**
- `tests.fakes.make_fake_element("Application")` produces a fake COM application object.
- `win32com.client.GetActiveObject` is patched to return that fake object.
**Test Steps:**
1. Patch `rhapsody_cli.application.win32com.client.GetActiveObject` to return the fake COM object.
2. Call `RhapsodyApplication._attach()`.
3. Inspect the returned instance's `_com` attribute.
**Expected Result:**
A `RhapsodyApplication` instance is returned and its `_com` attribute is the fake COM object returned by `GetActiveObject`. `GetActiveObject` is called exactly once with `"Rhapsody2.Application.1"`.
**Verification Criteria:**
Pass if the returned object is a `RhapsodyApplication`, `result._com is fake_app`, and `GetActiveObject` was called once with `"Rhapsody2.Application.1"`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00002: _attach Raises RhapsodyConnectionError When No Instance Running

**ID:** UTS_APP_00002
**Traces-To:** SWR_APP_00001
**Title:** _attach() raises RhapsodyConnectionError when GetActiveObject fails
**Type:** Unit
**Priority:** High
**Description:**
Verifies that when `GetActiveObject` raises a `pywintypes.com_error`, `_attach()` translates it into a `RhapsodyConnectionError` whose message starts with `"No running Rhapsody instance found:"` and chains the original exception as `__cause__`.
**Pre-conditions:**
- `tests.fakes.make_com_error("no active object")` produces a `pywintypes.com_error`.
- `win32com.client.GetActiveObject` is patched to raise that error.
**Test Steps:**
1. Patch `GetActiveObject` to raise the `com_error`.
2. Call `RhapsodyApplication._attach()` inside an `assertRaises(RhapsodyConnectionError)` block.
3. Inspect the raised exception's `args[0]` and `__cause__`.
**Expected Result:**
A `RhapsodyConnectionError` is raised; its message begins with `"No running Rhapsody instance found:"` and includes the original error text; `__cause__` is the original `pywintypes.com_error`.
**Verification Criteria:**
Pass if `RhapsodyConnectionError` is raised, the message contains the original COM error text, and `__cause__` is the `com_error`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00003: _launch Internal Helper Happy Path

**ID:** UTS_APP_00003
**Traces-To:** SWR_APP_00002
**Title:** _launch() returns a RhapsodyApplication wrapping a freshly dispatched COM object
**Type:** Unit
**Priority:** High
**Description:**
Verifies that `RhapsodyApplication._launch()` calls `win32com.client.Dispatch("Rhapsody2.Application.1")` and returns a `RhapsodyApplication` wrapping the dispatched object.
**Pre-conditions:**
- A fake COM application object built via `tests.fakes.make_fake_element("Application")`.
- `win32com.client.Dispatch` is patched to return that fake object.
**Test Steps:**
1. Patch `rhapsody_cli.application.win32com.client.Dispatch` to return the fake COM object.
2. Call `RhapsodyApplication._launch()`.
3. Inspect the returned instance's `_com` attribute.
**Expected Result:**
A `RhapsodyApplication` is returned whose `_com` is the dispatched fake object. `Dispatch` is called exactly once with `"Rhapsody2.Application.1"`.
**Verification Criteria:**
Pass if `isinstance(result, RhapsodyApplication)`, `result._com is fake_app`, and `Dispatch` call args are `("Rhapsody2.Application.1",)`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00004: _launch Raises RhapsodyConnectionError on Dispatch Failure

**ID:** UTS_APP_00004
**Traces-To:** SWR_APP_00002
**Title:** _launch() raises RhapsodyConnectionError when Dispatch fails
**Type:** Unit
**Priority:** High
**Description:**
Verifies that when `Dispatch` raises a `pywintypes.com_error`, `_launch()` raises `RhapsodyConnectionError` with a message beginning `"Failed to launch Rhapsody instance:"` and chains the original error.
**Pre-conditions:**
- `tests.fakes.make_com_error("dispatch failed")` produces a `pywintypes.com_error`.
- `win32com.client.Dispatch` is patched to raise it.
**Test Steps:**
1. Patch `Dispatch` to raise the `com_error`.
2. Call `RhapsodyApplication._launch()` inside `assertRaises(RhapsodyConnectionError)`.
3. Inspect the raised exception message and `__cause__`.
**Expected Result:**
`RhapsodyConnectionError` is raised; message starts with `"Failed to launch Rhapsody instance:"` and includes `"dispatch failed"`; `__cause__` is the original `com_error`.
**Verification Criteria:**
Pass if the raised exception is a `RhapsodyConnectionError`, message contains the original text, and `__cause__` is the `com_error`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00005: Connect Falls Back to Launch When Attach Fails

**ID:** UTS_APP_00005
**Traces-To:** SWR_APP_00003
**Title:** connect() falls back to _launch() when _attach() fails
**Type:** Unit
**Priority:** High
**Description:**
Verifies that `connect()` (default `attach_only=False`) attempts `_attach()` first, and if `_attach()` raises `RhapsodyConnectionError`, falls back to `_launch()` and returns the launched instance.
**Pre-conditions:**
- `RhapsodyApplication._attach` is patched to raise `RhapsodyConnectionError`.
- `RhapsodyApplication._launch` is patched to return a sentinel `RhapsodyApplication` instance.
**Test Steps:**
1. Patch `_attach` to raise `RhapsodyConnectionError`; patch `_launch` to return the sentinel.
2. Call `RhapsodyApplication.connect()`.
3. Inspect the returned object.
**Expected Result:**
The returned object is the sentinel returned by `_launch()`. `_attach` was called once; `_launch` was called once.
**Verification Criteria:**
Pass if `result is sentinel`, `_attach.call_count == 1`, and `_launch.call_count == 1`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00006: Connect Uses Attach When It Succeeds

**ID:** UTS_APP_00006
**Traces-To:** SWR_APP_00003
**Title:** connect() returns _attach result and does not call _launch
**Type:** Unit
**Priority:** High
**Description:**
Verifies that when `_attach()` succeeds, `connect()` returns the attached instance and never calls `_launch()`.
**Pre-conditions:**
- `RhapsodyApplication._attach` is patched to return a sentinel instance.
- `RhapsodyApplication._launch` is patched (should not be invoked).
**Test Steps:**
1. Patch `_attach` to return the sentinel; patch `_launch` as a `MagicMock`.
2. Call `RhapsodyApplication.connect()`.
3. Inspect the returned object and `_launch.call_count`.
**Expected Result:**
The returned object is the sentinel from `_attach()`. `_launch` is never called.
**Verification Criteria:**
Pass if `result is sentinel`, `_attach.call_count == 1`, and `_launch.call_count == 0`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00007: Connect with attach_only=True Raises When Not Running

**ID:** UTS_APP_00007
**Traces-To:** SWR_APP_00003
**Title:** connect(attach_only=True) propagates RhapsodyConnectionError without fallback
**Type:** Unit
**Priority:** High
**Description:**
Verifies that when `attach_only=True`, `connect()` calls `_attach()` and if it raises `RhapsodyConnectionError`, propagates the error without attempting `_launch()`.
**Pre-conditions:**
- `RhapsodyApplication._attach` is patched to raise `RhapsodyConnectionError`.
- `RhapsodyApplication._launch` is patched (should not be invoked).
**Test Steps:**
1. Patch `_attach` to raise `RhapsodyConnectionError`; patch `_launch` as a `MagicMock`.
2. Call `RhapsodyApplication.connect(attach_only=True)` inside an `assertRaises(RhapsodyConnectionError)` block.
3. Inspect the raised exception and call counts.
**Expected Result:**
`RhapsodyConnectionError` is raised. `_attach` was called once; `_launch` was never called.
**Verification Criteria:**
Pass if `RhapsodyConnectionError` is raised, `_attach.call_count == 1`, and `_launch.call_count == 0`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00008: Open Project File Returns Wrapped RPProject

**ID:** UTS_APP_00008
**Traces-To:** SWR_APP_00004
**Title:** openProject(filename) delegates to COM and returns a wrapped RPProject
**Type:** Unit
**Priority:** High
**Description:**
Verifies that `openProject(filename)` calls `self._com.openProject(filename)` and returns an `RPProject` wrapping the returned COM project object.
**Pre-conditions:**
- A fake COM application object whose `openProject` method returns a fake project COM object (built via `tests.fakes.make_fake_element("Project")`).
- A `RhapsodyApplication` constructed directly with that fake COM object.
**Test Steps:**
1. Build a `RhapsodyApplication(fake_app)`.
2. Call `app.openProject("C:/models/sample.rpy")`.
3. Inspect the type and `_com` of the result.
4. Inspect `fake_app.openProject` call args.
**Expected Result:**
The result is an `RPProject` instance whose `_com` is the fake project COM object. `fake_app.openProject` was called once with `"C:/models/sample.rpy"`.
**Verification Criteria:**
Pass if `isinstance(result, RPProject)`, `result._com is fake_project`, and `fake_app.openProject.call_args == call("C:/models/sample.rpy")`.
**Last Changed:** 2026-07-07

---

## UTS_APP_00009: Open Project Translates COM Error to RhapsodyRuntimeException

**ID:** UTS_APP_00009
**Traces-To:** SWR_APP_00004
**Title:** openProject translates a com_error from the COM call into RhapsodyRuntimeException
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that when the underlying `self._com.openProject(...)` raises a `pywintypes.com_error`, `openProject` re-raises it as `RhapsodyRuntimeException` (via `call_com`) and never returns a partial result.
**Pre-conditions:**
- A fake COM application object whose `openProject` side effect is `tests.fakes.make_com_error("file not found")`.
- A `RhapsodyApplication` constructed with that fake object.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)` with `openProject` raising the `com_error`.
2. Call `app.openProject("missing.rpy")` inside `assertRaises(RhapsodyRuntimeException)`.
3. Inspect the exception message.
**Expected Result:**
`RhapsodyRuntimeException` is raised; its message contains the original COM error text. No `RPProject` is returned.
**Verification Criteria:**
Pass if `RhapsodyRuntimeException` is raised and its `str()` contains `"file not found"`.
**Last Changed:** 2026-07-07

---

## UTS_APP_00010: Get Active Project Returns Wrapped RPProject

**ID:** UTS_APP_00010
**Traces-To:** SWR_APP_00005
**Title:** activeProject() delegates to COM and returns a wrapped RPProject
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `activeProject()` calls `self._com.activeProject()` and returns an `RPProject` wrapping the returned COM object.
**Pre-conditions:**
- A fake COM application whose `activeProject` returns a fake project COM object (built via `tests.fakes.make_fake_element("Project")`).
- A `RhapsodyApplication` constructed with that fake object.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.activeProject()`.
3. Inspect the type and `_com` of the result.
4. Verify `fake_app.activeProject` was called once with no arguments.
**Expected Result:**
The result is an `RPProject` whose `_com` is the fake project COM object. `fake_app.activeProject` was called once.
**Verification Criteria:**
Pass if `isinstance(result, RPProject)`, `result._com is fake_project`, and `fake_app.activeProject.call_count == 1`.
**Last Changed:** 2026-07-07

---

## UTS_APP_00011: Get All Open Projects Returns RPCollection

**ID:** UTS_APP_00011
**Traces-To:** SWR_APP_00006
**Title:** getProjects() delegates to COM and returns an RPCollection
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `getProjects()` calls `self._com.getProjects()` and returns an `RPCollection` wrapping the returned COM collection object.
**Pre-conditions:**
- A fake COM collection built via `tests.fakes.make_fake_collection([])` (empty is fine for this test).
- A fake COM application whose `getProjects` returns that fake collection.
- A `RhapsodyApplication` constructed with that fake object.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.getProjects()`.
3. Inspect the type and `_com` of the result.
4. Verify `fake_app.getProjects` was called once with no arguments.
**Expected Result:**
The result is an `RPCollection` whose `_com` is the fake collection. `fake_app.getProjects` was called once.
**Verification Criteria:**
Pass if `isinstance(result, RPCollection)`, `result._com is fake_collection`, and `fake_app.getProjects.call_count == 1`.
**Last Changed:** 2026-07-07

---

## UTS_APP_00012: Quit Application Calls COM quit

**ID:** UTS_APP_00012
**Traces-To:** SWR_APP_00007
**Title:** quit() calls quit() on the underlying COM object
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `quit()` calls `self._com.quit()` exactly once and returns `None`.
**Pre-conditions:**
- A fake COM application object (a `MagicMock`) whose `quit` is a mock method.
- A `RhapsodyApplication` constructed with that fake object.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.quit()`.
3. Inspect the return value and `fake_app.quit.call_count`.
**Expected Result:**
`quit()` returns `None` and `fake_app.quit` was called exactly once with no arguments.
**Verification Criteria:**
Pass if `result is None` and `fake_app.quit.call_count == 1`.
**Last Changed:** 2026-07-07

---

## UTS_APP_00013: Quit Translates COM Error to RhapsodyRuntimeException

**ID:** UTS_APP_00013
**Traces-To:** SWR_APP_00007
**Title:** quit() translates a com_error from COM quit into RhapsodyRuntimeException
**Type:** Unit
**Priority:** Low
**Description:**
Verifies that when the underlying `self._com.quit()` raises a `pywintypes.com_error`, `quit()` re-raises it as `RhapsodyRuntimeException` (via `call_com`).
**Pre-conditions:**
- A fake COM application whose `quit` side effect is `tests.fakes.make_com_error("already closed")`.
- A `RhapsodyApplication` constructed with that fake object.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)` with `quit` raising the `com_error`.
2. Call `app.quit()` inside `assertRaises(RhapsodyRuntimeException)`.
3. Inspect the exception message.
**Expected Result:**
`RhapsodyRuntimeException` is raised and its message contains `"already closed"`.
**Verification Criteria:**
Pass if `RhapsodyRuntimeException` is raised and `"already closed"` is in `str(exc)`.
**Last Changed:** 2026-07-07

---

## UTS_APP_00014: Each RhapsodyApplication Instance Wraps Its Own COM Object

**ID:** UTS_APP_00014
**Traces-To:** SWR_APP_00008
**Title:** Two RhapsodyApplication instances wrap two distinct COM objects independently
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `RhapsodyApplication` is not a singleton: two instances constructed with two distinct fake COM objects each hold their own `_com` and operate independently.
**Pre-conditions:**
- Two distinct fake COM application objects, `fake_app_a` and `fake_app_b`.
**Test Steps:**
1. Construct `app_a = RhapsodyApplication(fake_app_a)`.
2. Construct `app_b = RhapsodyApplication(fake_app_b)`.
3. Assert `app_a._com is fake_app_a` and `app_b._com is fake_app_b`.
4. Assert `app_a is not app_b`.
5. Call `app_a.quit()` and verify `fake_app_b.quit` was NOT called.
**Expected Result:**
Each instance holds its own COM object. Calling `quit()` on one does not affect the other.
**Verification Criteria:**
Pass if `app_a._com is fake_app_a`, `app_b._com is fake_app_b`, `app_a is not app_b`, and after `app_a.quit()`, `fake_app_a.quit.call_count == 1` while `fake_app_b.quit.call_count == 0`.
**Last Changed:** 2026-07-07

---

## UTS_APP_00015: Prog ID Constant Equals Rhapsody2.Application.1

**ID:** UTS_APP_00015
**Traces-To:** SWR_APP_00009
**Title:** _PROG_ID module constant is the canonical Rhapsody2.Application.1 Prog ID
**Type:** Unit
**Priority:** Low
**Description:**
Verifies that the `_PROG_ID` module-level constant in `rhapsody_cli.application` equals `"Rhapsody2.Application.1"` and that `_attach()`/`_launch()` pass that exact string to `GetActiveObject`/`Dispatch`.
**Pre-conditions:**
- Import access to `rhapsody_cli.application._PROG_ID`.
- `GetActiveObject` and `Dispatch` patched to capture call args.
**Test Steps:**
1. Import `_PROG_ID` from `rhapsody_cli.application`.
2. Assert `_PROG_ID == "Rhapsody2.Application.1"`.
3. Patch `GetActiveObject` to return a fake; call `_attach()`; capture the call argument.
4. Patch `Dispatch` to return a fake; call `_launch()`; capture the call argument.
**Expected Result:**
`_PROG_ID` is `"Rhapsody2.Application.1"`. Both `GetActiveObject` and `Dispatch` are called with exactly that string.
**Verification Criteria:**
Pass if `_PROG_ID == "Rhapsody2.Application.1"`, and the captured call args for both `GetActiveObject` and `Dispatch` equal `("Rhapsody2.Application.1",)`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00016: connect(show_gui=True) Shows GUI on Launch

**ID:** UTS_APP_00016
**Traces-To:** SWR_APP_00003
**Title:** connect() shows GUI by default when a new instance is launched
**Type:** Unit
**Priority:** High
**Description:**
Verifies that when `connect()` launches a new instance (attach fails), it calls `setHiddenUI(False)` to show the GUI window by default.
**Pre-conditions:**
- `RhapsodyApplication._attach` is patched to raise `RhapsodyConnectionError`.
- `RhapsodyApplication._launch` is patched to return a mock with a `setHiddenUI` method.
**Test Steps:**
1. Patch `_attach` to raise; patch `_launch` to return a mock with `setHiddenUI`.
2. Call `RhapsodyApplication.connect()` (default `show_gui=True`).
3. Verify `setHiddenUI(False)` was called on the mock.
**Expected Result:**
`setHiddenUI(False)` is called once on the launched instance.
**Verification Criteria:**
Pass if `setHiddenUI.assert_called_once_with(False)`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00017: connect(show_gui=False) Hides GUI on Launch

**ID:** UTS_APP_00017
**Traces-To:** SWR_APP_00003
**Title:** connect(show_gui=False) does not show GUI on launched instance
**Type:** Unit
**Priority:** High
**Description:**
Verifies that when `connect(show_gui=False)` launches a new instance, it does not call `setHiddenUI`, leaving the GUI hidden.
**Pre-conditions:**
- `RhapsodyApplication._attach` is patched to raise `RhapsodyConnectionError`.
- `RhapsodyApplication._launch` is patched to return a mock with a `setHiddenUI` method.
**Test Steps:**
1. Patch `_attach` to raise; patch `_launch` to return a mock.
2. Call `RhapsodyApplication.connect(show_gui=False)`.
3. Verify `setHiddenUI` was NOT called.
**Expected Result:**
`setHiddenUI` is not called.
**Verification Criteria:**
Pass if `setHiddenUI.assert_not_called()`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00018: connect Fails When Both Attach and Launch Fail

**ID:** UTS_APP_00018
**Traces-To:** SWR_APP_00003
**Title:** connect() raises RhapsodyConnectionError when both _attach and _launch fail
**Type:** Unit
**Priority:** High
**Description:**
Verifies that when both `_attach()` and `_launch()` raise `RhapsodyConnectionError`, `connect()` propagates the launch error.
**Pre-conditions:**
- `RhapsodyApplication._attach` is patched to raise `RhapsodyConnectionError`.
- `RhapsodyApplication._launch` is patched to raise `RhapsodyConnectionError`.
**Test Steps:**
1. Patch both `_attach` and `_launch` to raise.
2. Call `RhapsodyApplication.connect()` inside `assertRaises(RhapsodyConnectionError)`.
**Expected Result:**
`RhapsodyConnectionError` is raised.
**Verification Criteria:**
Pass if `RhapsodyConnectionError` is raised.
**Last Changed:** 2026-07-11

---

## UTS_APP_00019: Disconnect Calls Quit

**ID:** UTS_APP_00019
**Traces-To:** SWR_APP_00024
**Title:** disconnect() calls quit() on the underlying COM object
**Type:** Unit
**Priority:** High
**Description:**
Verifies that `disconnect()` calls `self._com.quit()` exactly once.
**Pre-conditions:**
- A fake COM application object with a mock `quit` method.
- A `RhapsodyApplication` constructed with that fake object.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.disconnect()`.
3. Verify `fake_app.quit` was called once.
**Expected Result:**
`fake_app.quit` is called exactly once with no arguments.
**Verification Criteria:**
Pass if `fake_app.quit.call_count == 1`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00020: closeAllProjects Delegates to COM

**ID:** UTS_APP_00020
**Traces-To:** SWR_APP_00010
**Title:** closeAllProjects() calls COM closeAllProjects
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `closeAllProjects()` calls `self._com.closeAllProjects()`.
**Pre-conditions:**
- A fake COM application with a mock `closeAllProjects` method.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.closeAllProjects()`.
**Expected Result:**
`fake_app.closeAllProjects` is called once.
**Verification Criteria:**
Pass if `fake_app.closeAllProjects.call_count == 1`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00021: saveAll Delegates to COM

**ID:** UTS_APP_00021
**Traces-To:** SWR_APP_00011
**Title:** saveAll() calls COM saveAll
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `saveAll()` calls `self._com.saveAll()`.
**Pre-conditions:**
- A fake COM application with a mock `saveAll` method.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.saveAll()`.
**Expected Result:**
`fake_app.saveAll` is called once.
**Verification Criteria:**
Pass if `fake_app.saveAll.call_count == 1`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00022: getVersion Returns String

**ID:** UTS_APP_00022
**Traces-To:** SWR_APP_00012
**Title:** getVersion() returns the version string from COM
**Type:** Unit
**Priority:** Low
**Description:**
Verifies that `getVersion()` calls `self._com.getVersion()` and returns its result as a string.
**Pre-conditions:**
- A fake COM application with `getVersion` set to return `"8.3.1"`.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.getVersion()`.
**Expected Result:**
Returns `"8.3.1"`.
**Verification Criteria:**
Pass if `app.getVersion() == "8.3.1"`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00023: getBuildNo Returns String

**ID:** UTS_APP_00023
**Traces-To:** SWR_APP_00013
**Title:** getBuildNo() returns the build number string from COM
**Type:** Unit
**Priority:** Low
**Description:**
Verifies that `getBuildNo()` calls `self._com.getBuildNo()` and returns its result as a string.
**Pre-conditions:**
- A fake COM application with `getBuildNo` set to return `"12345"`.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.getBuildNo()`.
**Expected Result:**
Returns `"12345"`.
**Verification Criteria:**
Pass if `app.getBuildNo() == "12345"`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00024: getRhapsodyDir Returns String

**ID:** UTS_APP_00024
**Traces-To:** SWR_APP_00014
**Title:** getRhapsodyDir() returns the installation directory from COM
**Type:** Unit
**Priority:** Low
**Description:**
Verifies that `getRhapsodyDir()` calls `self._com.getRhapsodyDir()` and returns its result as a string.
**Pre-conditions:**
- A fake COM application with `getRhapsodyDir` set to return `"C:/Program Files/Rhapsody"`.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.getRhapsodyDir()`.
**Expected Result:**
Returns `"C:/Program Files/Rhapsody"`.
**Verification Criteria:**
Pass if `app.getRhapsodyDir() == "C:/Program Files/Rhapsody"`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00025: getOMROOT Returns String

**ID:** UTS_APP_00025
**Traces-To:** SWR_APP_00015
**Title:** getOMROOT() returns the OMROOT directory from COM
**Type:** Unit
**Priority:** Low
**Description:**
Verifies that `getOMROOT()` calls `self._com.getOMROOT()` and returns its result as a string.
**Pre-conditions:**
- A fake COM application with `getOMROOT` set to return `"C:/Rhapsody/OMROOT"`.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.getOMROOT()`.
**Expected Result:**
Returns `"C:/Rhapsody/OMROOT"`.
**Verification Criteria:**
Pass if `app.getOMROOT() == "C:/Rhapsody/OMROOT"`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00026: generate Delegates to COM

**ID:** UTS_APP_00026
**Traces-To:** SWR_APP_00016
**Title:** generate() calls COM generate
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `generate()` calls `self._com.generate()`.
**Pre-conditions:**
- A fake COM application with a mock `generate` method.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.generate()`.
**Expected Result:**
`fake_app.generate` is called once.
**Verification Criteria:**
Pass if `fake_app.generate.call_count == 1`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00027: generateElements Passes Collection to COM

**ID:** UTS_APP_00027
**Traces-To:** SWR_APP_00017
**Title:** generateElements() passes the collection's COM object to COM
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `generateElements()` passes `elements._com` to `self._com.generateElements()`.
**Pre-conditions:**
- A fake COM application with a mock `generateElements` method.
- A fake COM collection built via `make_fake_collection([])`.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.generateElements(RPCollection(fake_collection))`.
**Expected Result:**
`fake_app.generateElements` is called once with `fake_collection`.
**Verification Criteria:**
Pass if `fake_app.generateElements.call_args == call(fake_collection)`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00028: generateEntireProject Delegates to COM

**ID:** UTS_APP_00028
**Traces-To:** SWR_APP_00018
**Title:** generateEntireProject() calls COM generateEntireProject
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `generateEntireProject()` calls `self._com.generateEntireProject()`.
**Pre-conditions:**
- A fake COM application with a mock `generateEntireProject` method.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.generateEntireProject()`.
**Expected Result:**
`fake_app.generateEntireProject` is called once.
**Verification Criteria:**
Pass if `fake_app.generateEntireProject.call_count == 1`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00029: regenerate Delegates to COM

**ID:** UTS_APP_00029
**Traces-To:** SWR_APP_00019
**Title:** regenerate() calls COM regenerate
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `regenerate()` calls `self._com.regenerate()`.
**Pre-conditions:**
- A fake COM application with a mock `regenerate` method.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.regenerate()`.
**Expected Result:**
`fake_app.regenerate` is called once.
**Verification Criteria:**
Pass if `fake_app.regenerate.call_count == 1`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00030: addToModel Delegates to COM

**ID:** UTS_APP_00030
**Traces-To:** SWR_APP_00020
**Title:** addToModel() passes filename and flag to COM
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `addToModel()` passes its arguments to `self._com.addToModel()`.
**Pre-conditions:**
- A fake COM application with a mock `addToModel` method.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.addToModel("myfile.rpy", 1)`.
**Expected Result:**
`fake_app.addToModel` is called once with `("myfile.rpy", 1)`.
**Verification Criteria:**
Pass if `fake_app.addToModel.call_args == call("myfile.rpy", 1)`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00031: addToModelEx Delegates to COM

**ID:** UTS_APP_00031
**Traces-To:** SWR_APP_00021
**Title:** addToModelEx() passes all four arguments to COM
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `addToModelEx()` passes its arguments to `self._com.addToModelEx()`.
**Pre-conditions:**
- A fake COM application with a mock `addToModelEx` method.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.addToModelEx("myfile.rpy", 1, 1, 1)`.
**Expected Result:**
`fake_app.addToModelEx` is called once with `("myfile.rpy", 1, 1, 1)`.
**Verification Criteria:**
Pass if `fake_app.addToModelEx.call_args == call("myfile.rpy", 1, 1, 1)`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00032: setLog Delegates to COM

**ID:** UTS_APP_00032
**Traces-To:** SWR_APP_00022
**Title:** setLog() passes the log path to COM
**Type:** Unit
**Priority:** Low
**Description:**
Verifies that `setLog()` passes its argument to `self._com.setLog()`.
**Pre-conditions:**
- A fake COM application with a mock `setLog` method.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.setLog("C:/log.txt")`.
**Expected Result:**
`fake_app.setLog` is called once with `"C:/log.txt"`.
**Verification Criteria:**
Pass if `fake_app.setLog.call_args == call("C:/log.txt")`.
**Last Changed:** 2026-07-11

---

## UTS_APP_00033: checkModel Delegates to COM

**ID:** UTS_APP_00033
**Traces-To:** SWR_APP_00023
**Title:** checkModel() calls COM checkModel
**Type:** Unit
**Priority:** Medium
**Description:**
Verifies that `checkModel()` calls `self._com.checkModel()`.
**Pre-conditions:**
- A fake COM application with a mock `checkModel` method.
**Test Steps:**
1. Build `RhapsodyApplication(fake_app)`.
2. Call `app.checkModel()`.
**Expected Result:**
`fake_app.checkModel` is called once.
**Verification Criteria:**
Pass if `fake_app.checkModel.call_count == 1`.
**Last Changed:** 2026-07-11
