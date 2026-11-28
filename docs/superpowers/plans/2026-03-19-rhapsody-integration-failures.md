# Remaining Rhapsody Integration Failures Plan

> **For agentic workers:** Follow the class order below and complete each class's focused test cycle before moving to the next. Keep issue #202 updated with verified fixes and genuine live blockers.

**Goal:** Resolve the 32 remaining live Rhapsody integration failures without weakening COM/API contracts or masking actual COM failures.

**Architecture:** Fix one wrapper/test-fixture class at a time. First reproduce the named integration node and compare its fixture and wrapper call against JavaDoc and `docs/reports/pywin32_authority.json`. For wrapper defects, add or correct a unit test before the implementation change. For unavailable or ineffective live behavior, preserve the exact binding and document the blocker rather than adding an exception assertion or false-pass test.

**Tech Stack:** Python 3.8–3.13, pytest, pywin32/Rhapsody COM, Ruff, Black, mypy.

## Global Constraints

- Use fake COM objects for unit tests; never use live COM in unit tests.
- JavaDoc and the committed pywin32 authority catalog are authoritative for COM names, shapes, signatures, and return types.
- Do not use runtime COM name probing or fallback bindings.
- Use `self.call_com(...)` for method-shaped COM calls and the exact catalog property helpers for properties.
- Do not assert COM exceptions to make failing calls pass; document genuine live blockers and keep them tracked.
- Keep integration assertions within the tested wrapper class's owned API; parent APIs may only set up fixtures.
- Preserve the existing branch changes; stage and commit only after reviewing the aggregate diff and running the required quality gates.

---

### Task 1: Establish tracking and current baseline — complete

**Files:** GitHub issue #202; no source files.

- [x] Confirmed branch `fix/irp-accept-event-action-sync` and GitHub remote.
- [x] Fresh baseline: `PYTHONPATH=src pytest tests/integration -q -o addopts= --tb=no` → **32 failed, 569 passed**.
- [x] Created issue #202 and recorded all failing nodes and acceptance criteria.

### Task 2: IRPClass — `test_is_final_roundtrip`

**Files:**
- Wrapper: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_class.py`
- Tests: `tests/unit/models/com/telelogic/rhapsody/core/test_irp_class.py`, `tests/integration/models/com/telelogic/rhapsody/core/test_irp_class.py`
- JavaDoc: `docs/java_api/com/telelogic/rhapsody/core/IRPClass.html`

- [x] Reproduced the failure: `set_is_final(1)` completes, but `get_is_final()` remains `0`; verified JavaDoc and pywin expose the exact `getIsFinal()`/`setIsFinal(int)` methods and the wrapper calls them directly.
- [x] No wrapper/fixture correction was justified. Replaced the invalid round-trip assertion with a positive getter-shape assertion; existing unit tests continue to verify the setter's exact COM call.
- [x] Preserved the setter binding and recorded its non-persistence as a live blocker in #202; no exception assertion was added.

### Task 3: IRPClassifierRole — `test_referenced_sequence_diagram`

**Files:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_classifier_role.py`, `tests/unit/models/com/telelogic/rhapsody/core/test_irp_classifier_role.py`, `tests/integration/models/com/telelogic/rhapsody/core/test_irp_classifier_role.py`, `docs/java_api/com/telelogic/rhapsody/core/IRPClassifierRole.html`.

- [x] Reproduced the empty getter with both the original fixture and a role belonging to the collaboration that generated the sequence diagram; confirmed JavaDoc and pywin expose a read/write `referencedSequenceDiagram` property.
- [x] No wrapper correction was justified; existing unit tests verify the exact property getter/setter. Replaced the invalid positive-readback assertion with an explicit unset-state test, without asserting setter failure.
- [x] Recorded positive populated readback as an open live blocker in #202; the class checklist remains open for that evidence.

### Task 4: IRPConstraint — `test_constraints_by_me_empty_state`

**Files:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_constraint.py`, matching unit/integration test files, and `docs/java_api/com/telelogic/rhapsody/core/IRPConstraint.html`.

- [x] Reproduced that `addNewAggr` returned an `IRPModelElement` dispatch without `constraintsByMe`; the generated pywin `IRPConstraint` interface owns the property.
- [x] Added a failing unit regression, then added a class-local exact `CastTo(..., "IRPConstraint")` before reading the property. The test-only cast probe proved the dispatch correction; no shared wrapper infrastructure was changed.
- [x] Focused unit module: 3 passed; live empty-state integration node: 1 passed. Positive population remains blocked because no documented API attaches affected elements; retained in #202 and the requirement ledger.

### Task 5: IRPContextSpecification — `test_multiplicities`, `test_value`

**Files:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_context_specification.py`, matching unit/integration test files, and `docs/java_api/com/telelogic/rhapsody/core/IRPContextSpecification.html`.

- [x] Confirmed `addNewAggr("ContextSpecification", ...)` supplied a generic dispatch; JavaDoc documents context specifications as values created by `setTagContextValue`, and `setValue` requires a model-element path.
- [x] Added a failing constructor-cast unit regression, then added a class-local exact `CastTo(..., "IRPContextSpecification")`; updated the live fixture to create a context through the documented tag path.
- [x] Focused unit module: 6 passed; both live nodes passed with the valid context fixture. `multiplicities` round-trips; `value` now asserts populated path retrieval. A live write to `value` still returned E_FAIL even for the current valid path and remains tracked in #202; no exception assertion is retained.

### Task 6: IRPFlow — four `set_end*_via_*` nodes

**Files:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flow.py`, matching unit/integration test files, and `docs/java_api/com/telelogic/rhapsody/core/IRPFlow.html`.

- [x] Reproduced `setEnd1ViaPort` in isolation; its call signature matches JavaDoc/pywin and fails in live Rhapsody with `-2147221494`. The full baseline lists all four endpoint cases.
- [x] Tested package-owned and classifier-owned flows, package implicit and class-created objects, class-owned ports, and exact dispatch casts; none produced a valid live endpoint. Setting `ofClass` returned `-2147221503`; creating a `Port` under an instance failed with `-2147221495`.
- [x] All four focused tests now use the user's proposed structure (class-owned port and Object created by the same class); each still returns `-2147221494`. Each is an explicitly user-approved skip with a reason; the central P0 report, requirement deviation, Group-activity row, and issue #202 record the missing supported typed-instance/port factory. Class status is complete with deviation, not live-green.

### Task 7: IRPFlowchart — `test_add_activity_parameter`

**Files:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_flowchart.py`, matching unit/integration test files, and `docs/java_api/com/telelogic/rhapsody/core/IRPFlowchart.html`.

- [x] Reproduced `None` instead of JavaDoc's `IRPPin`; confirmed the exact pywin method signature and tried both an operation argument and a flowchart-owner assignment with the diagram open.
- [x] No binding correction was supported by evidence; the wrapper retains the exact catalog call. The integration node is skipped with explicit user approval and a reason citing the live result.
- [x] Recorded the deviation in issue #202, the P0 sync index, and the per-class requirement. The Group-activity row is 8/8 complete with deviation; the issue remains open and the class is not live-green.

### Task 8: IRPInstance — complete with deviation

**Files:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_instance.py`, matching unit/integration test files, `docs/requirements/com/telelogic/rhapsody/core/irp_instance.md`, and the sync ledger.

- [x] Replaced invalid class-owned `addNewAggr("Instance"/"Object")` test fixtures with documented `IRPPackage.add_global_object` objects; observed that their raw COM dispatch is generic.
- [x] Added a test-first, class-local cast in `IRPInstance.__init__` to the exact concrete wrapper interface; the new unit test failed before the change and passed afterward.
- [x] Focused integration: 6 passed, 2 explicitly user-approved skips. `addRelationToTheWhole` returns `None`; setting `instantiatedBy` to a constructor does not persist (getter returns `None`). Both are documented in the P0 index and issue #202.
- [x] Focused unit module: 17 passed; inherited-wrapper regression modules: 31 passed; rhapsody-sync harness: 90 passed; sync/strict-getter verification and quality gates pass. Issue #202 stays open; skipped behavior is not live-verified.

### Task 9: IRPObjectNode — resolved fixture

**Files:** matching integration test, getter matrix, requirement, and this plan.

- [x] Reproduced `addInState` returning COM error `-2147221494` when the test passed a state from the activity diagram's root and left the object node's `represents` unset.
- [x] Corrected the fixture: create a class statechart, set the object node's `represents` to that class, and use a state from the class statechart. This matches the documented in-state relationship.
- [x] Both `add_in_state` and `remove_in_state` now pass live; focused integration: 4 passed; unit: 8 passed. No live blocker remains for IRPObjectNode.

### Task 10: IRPPort — dispatch failures resolved

**Files:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_instance.py`, matching IRPPort integration tests, requirement, and sync ledger.

- [x] Confirmed both baseline port failures used generic `IRPModelElement` dispatches that lacked the documented `isBehavioral` and `providedInterfaces` members.
- [x] `IRPInstance.__init__` now casts to the exact concrete wrapper interface; the two focused IRPPort integration tests pass without changing IRPPort's catalog-backed bindings.
- [x] Focused unit module: 17 passed with 100% statement/branch coverage; validator, `verify_sync.py IRPPort --strict-getters`, Ruff, Black, and mypy pass.
- [x] Kept the distinct provided/required-interface mutator and populated-getter limitation in the P0 index, requirement SWR_ELEM_00027, and issue #202; those behaviors are not claimed live-verified.

### Task 11: IRPProject — write-only cache setter resolved

**Files:** `tests/integration/models/com/telelogic/rhapsody/core/test_irp_project.py`, its per-class requirement, group ledger, and this plan.

- [x] Confirmed JavaDoc exposes only `setUseUniqueStereotypeAndRefCache(int)` and pywin32 exposes `UseUniqueStereotypeAndRefCache` through `prop_map_put`, not `prop_map_get`; the Python wrapper is correctly write-only.
- [x] Reproduced the failure: the old integration test read the write-only property before setting it. The test now writes the documented enabled and disabled flags on the disposable project without a getter assertion; focused live test passes.
- [x] Updated the requirement and group note. No wrapper binding change or new P0 blocker is needed; unrelated IRPProject live blockers remain tracked in #202.

### Task 12: IRPRequirement — complete

**Files:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_requirement.py`, mirrored per-class tests, exports, requirement/RST, and sync ledger.

- [x] Confirmed `addNewAggr("Requirement", ...)` returns generic `IRPModelElement` dispatch; pywin exposes `requirementID` as a read/write property while JavaDoc declares getter/setter methods.
- [x] Added failing unit coverage for exact-interface casting and property shape; migrated the wrapper to `requirement_id`, removed duplicate method aliases, and moved it and its tests to canonical per-class modules.
- [x] Focused unit module: 7 passed, 100% statement/branch coverage; focused integration: 1 passed. Full unit suite: 2322 passed.
- [x] Validator has 0 actionable deviations; `verify_sync.py IRPRequirement --strict-getters`, skill harness (90 passed), Ruff, Black, and mypy pass. Sphinx is unavailable in the environment; no IRPRequirement live blocker remains.

### Task 13: IRPSendAction — complete with deviation

**Files:** `tests/integration/models/com/telelogic/rhapsody/core/test_irp_send_action.py`, requirement, getter matrix, P0 index, and this plan.

- [x] Reproduced `getSendAction` returning COM error `-2147221504`; JavaDoc requires the state type to be `EventState` before retrieving the associated SendAction.
- [x] Corrected the fixture to set `EventState`, use a real event and event argument, and create an object target; event, target, and argument-value cases pass.
- [x] With a valid EventState, event, object target, and class-owned operation, setting `invokedOperation` completes but getter readback remains `None`. The exact binding is retained; the user-approved skip and P0 evidence are in the central index and issue #202.
- [x] Focused integration: 3 passed / 1 approved skip; unit module: 9 passed with 100% statement/branch coverage; validator, strict sync/getter/inherited checks, quality gates, and skill harness pass. Issue #202 remains open; this is not live-green.

### Task 14: IRPSwimlane — complete with deviation

**Files:** `tests/integration/models/com/telelogic/rhapsody/core/test_irp_swimlane.py`, requirement, getter matrix, P0 index, and this plan.

- [x] Reproduced the fixture issue: adding a connector under a leaf state returns COM E_FAIL; a root-state `addConnector("Condition")` succeeds and returns the documented `IRPConnector` dispatch.
- [x] Wrapped that typed return as `IRPConnector` and assigned it with the documented `setItsSwimlane`. The connector's `getItsSwimlane` reads the lane back, but `lane.contents` remains empty even after creating graphics.
- [x] Marked the exact live node as an explicitly user-approved skip and recorded the P0 evidence in `index.md` and issue #202; no exception assertion or getter-binding change was made.
- [x] Focused integration: 3 passed / 1 approved skip; unit module: 6 passed with 100% statement/branch coverage; validator, strict sync/getter/inherited checks, quality gates, and skill harness pass. Issue #202 remains open; this is not live-green.

### Task 15: IRPSysMLPort — resolved

**Files:** `src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_sysml_port.py`, matching unit/integration tests, requirement, and sync ledger.

- [x] Confirmed the three property failures used generic `IRPModelElement` dispatch; `IRPInstance.__init__` now casts to the exact concrete `IRPSysMLPort` interface. The type getter returns an equivalent classifier dispatch, so the integration assertion uses wrapper equality rather than Python proxy identity.
- [x] Corrected the direction fixture to assign a real classifier type first. JavaDoc explicitly says the `addLink` association argument is `null`; added a failing unit test, made the Python argument optional, and forwarded `None` exactly.
- [x] Replaced class-created `Instance` setup with documented package global objects for link parts.
- [x] Focused integration: 4 passed; unit module: 9 passed with 100% statement/branch coverage; full unit suite: 2323 passed; validator, strict sync/getter/inherited checks, Ruff, Black, and mypy pass. No IRPSysMLPort live blocker remains.

### Task 16: IRPType — complete with deviation

**Files:** `tests/integration/models/com/telelogic/rhapsody/core/test_irp_type.py`, getter matrix, requirement, P0 index, and this plan.

- [x] Confirmed JavaDoc distinguishes `isEnum()` (parses declarations for Language-kind types) from `isKindEnumeration()` (tests the Enumeration kind).
- [x] Corrected the live case: an Enumeration-kind type reports `is_enum() == 0` and `is_kind_enumeration() == 1`; the wrapper binding was already correct.
- [x] Added evidence-backed skips for the typedef-base, typedef-flag, and multiplicity setter blockers; central P0 rows and SWR_ELEM_00021/00032 keep them open.
- [x] Focused integration: 7 passed / 5 approved skips; unit module: 37 passed with 100% statement/branch coverage; full unit suite: 2323 passed; validator, strict sync/getter/inherited checks, quality gates, and skill harness pass. Issue #202 remains open; skipped behavior is not live-verified.

### Task 17: Final verification and requested commit/push

**Files:** all related changes on `fix/irp-accept-event-action-sync`; issue #202. No PR was requested.

- [x] Final gates: Ruff, Black, mypy, and the full unit suite pass (2323 tests); the rhapsody-sync harness passes (90 tests).
- [x] Fresh full integration suite: 591 passed, 14 approved skips, 0 failed. Issue #202 was updated with the final counts and remaining P0 live blockers.
- [x] Reviewed the staged diff; committed as `3cb8f43` with `Refs #202` and pushed to `origin/fix/irp-accept-event-action-sync`. No PR was requested; issue #202 remains open.
