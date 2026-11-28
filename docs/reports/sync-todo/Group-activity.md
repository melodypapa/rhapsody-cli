# Sync todo — `activity`

**12 classes** · ✅ 8 archived · ⚠️ 4 complete with deviation · ⬜ 0 open

One row per sync run. A step is ticked only when its evidence lands; a row is archived only after all eight steps pass. Binding rule: one pywin32-exposed COM member per call — `call_com(lambda: self._com.Name(...))` for methods, `get_com_property` / `set_com_property` for properties; catalog-absent sites are blockers, never blind migrations. Canonical package: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/`, mirrored tests under `tests/{unit,integration}/models/com/telelogic/rhapsody/core/`.

Merged from `Group-activity-1.md` and `Group-activity-2.md`; row details are refreshed as each interface completes its sync.

## Step legend

| Step | Meaning |
| --- | --- |
| ① §1 | publish the per-run checklist with a subtask per target-owned JavaDoc member |
| ② §2 | resolve the wrapper, inheritance, exports, and tests; move to the canonical package |
| ③ §3 | reconcile every owned member against JavaDoc, pywin32, and the Python wrapper |
| ④ §4 | failing fake-COM unit tests first, then migrate the legacy sites |
| ⑤ §5 | integration coverage on the mirrored path; live run on Windows |
| ⑥ §6 | update the per-class requirement document |
| ⑦ §7 | update the per-class RST page and its toctree entry |
| ⑧ §8 | run the validator, `verify_sync.py`, skill tests, both suites, and the quality gate |

`[x] §2` on every row records the 2026-11-24 bulk package move; other steps show their evidence inline when it differs from the legend.

## At a glance

| # | Class | Interface | Legacy source | Sites | Owned | Steps | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `irp_flow_api_report` | IRPFlow | `elements/activity/model_activity.py` | 4 | — | 8/8 (①②③④⑤⑥⑦⑧) | ⚠️ complete with deviation |
| 2 | `irp_flowchart_api_report` | IRPFlowchart | `rhapsody_cli/models/elements/activity/model_activity.py` | 2 | 14 | 8/8 (①②③④⑤⑥⑦⑧) | ⚠️ complete with deviation |
| 3 | `irp_swimlane_api_report` | IRPSwimlane | `rhapsody_cli/models/elements/activity/model_activity.py` | 1 | 5 | 8/8 (①②③④⑤⑥⑦⑧) | ⚠️ complete with deviation |
| 4 | `irp_action_api_report` | IRPAction | `rhapsody_cli/models/elements/activity/model_actions.py` | 2 | 2 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 5 | `irp_send_action_api_report` | IRPSendAction | `rhapsody_cli/models/elements/activity/model_actions.py` | 7 | 8 | 8/8 (①②③④⑤⑥⑦⑧) | ⚠️ complete with deviation |
| 6 | `irp_flow_item_api_report` | IRPFlowItem | `rhapsody_cli/models/elements/activity/model_activity.py` | 0 | 3 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 7 | `irp_object_node_api_report` | IRPObjectNode | `rhapsody_cli/models/elements/activity/model_activity.py` | 3 | 7 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 8 | `irp_call_operation_api_report` | IRPCallOperation | `rhapsody_cli/models/elements/activity/model_actions.py` | 4 | 4 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 9 | `irp_context_specification_api_report` | IRPContextSpecification | `rhapsody_cli/models/elements/activity/model_actions.py` | 2 | 4 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 10 | `irp_accept_time_event_api_report` | IRPAcceptTimeEvent | `rhapsody_cli/models/elements/activity/model_actions.py` | 2 | 2 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 11 | `irp_accept_event_action_api_report` | IRPAcceptEventAction | `rhapsody_cli/models/elements/activity/model_actions.py` | 2 | 2 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 12 | `irp_action_block_api_report` | IRPActionBlock | `rhapsody_cli/models/elements/activity/model_actions.py` | 0 | 0 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_flow_api_report</code> · IRPFlow · 8/8 steps · ⚠️ complete with deviation</summary>

- **Status (2026-03-19):** API-sync steps are complete with an approved live deviation; issue #202 remains open for future endpoint-fixture evidence. This is not a live-green claim.
- **Note:** activity-flow element (107 src / 59 test) shared by operations, diagrams and statecharts. Split `IRPFlow` into `irp_flow.py`; siblings stay in `irp_activity.py` for their own rows. Eight JavaDoc accessors map to pywin32 properties and are exposed as `@property`; six members use `call_com`. Exact `setEnd*ViaPort` / `setEnd*ViaSysMLPort` bindings remain; live calls return `-2147221494` even with a class-owned port and a class-created object.
- [x] ① §1
- [x] ② §2 — canonical module `irp_flow.py`; exports and direct imports updated; sibling classes untouched
- [x] ③ §3 — 0 actionable deviations after binding migration; authority catalog refreshed from committed reports
- [x] ④ §4 — 18 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — Complete with deviation: 9 integration tests, 5 passed and 4 explicitly user-approved skips. Each skip records the live `-2147221494` result with class-owned ports and class-created objects; issue #202 remains open for a supported instance/port fixture. Not live-green.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_flow.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_flow.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; skill tests 90 passed; full unit suite 2200 passed; ruff/black clean; mypy skipped on py3.14 (CI runs it on <3.10)

</details>

<details>
<summary><code>irp_flowchart_api_report</code> · IRPFlowchart · 8/8 steps · ⚠️ complete with deviation</summary>

- **Status (2026-03-19):** API-sync steps are complete with an approved live deviation; issue #202 remains open for future `addActivityParameter` return evidence. This is not a live-green claim.
- **Note:** usage 41 src / 21 test refs, 14 owned members. Split `IRPFlowchart` into `irp_flowchart.py`; siblings stay in `irp_activity.py` for their own rows. Three JavaDoc accessors map to pywin32 properties; the other eleven use `call_com`.
- [x] ① §1
- [x] ② §2 — canonical module `irp_flowchart.py`; exports and direct imports updated; sibling classes untouched
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 15 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — Complete with deviation: 12 integration tests, 11 passed and 1 explicitly user-approved skip. Rhapsody returns `None` from `addActivityParameter(name)` instead of `IRPPin` despite an operation argument, flowchart owner assignment, and open diagram; issue #202 remains open. Not live-green.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_flowchart.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_flowchart.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2199 passed; ruff/black clean; mypy skipped on py3.14 (CI runs it on <3.10)

</details>

<details>
<summary><code>irp_swimlane_api_report</code> · IRPSwimlane · 8/8 steps · ⚠️ complete with deviation</summary>

- **Status (2026-03-19):** API sync is complete with an approved live deviation; `contents` remains blocked and issue #202 stays open. This is not a live-green claim.
- **Note:** usage 29 src / 12 test refs, 5 owned members. Split `IRPSwimlane` into `irp_swimlane.py`; siblings stay in `irp_activity.py` for their own rows. Three accessors are COM properties; `add_swimlane` uses `call_com`.
- [x] ① §1
- [x] ② §2 — canonical module `irp_swimlane.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 6 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — Complete with deviation: 4 integration tests, 3 passed and 1 explicitly user-approved skip. A real root-state connector accepts `setItsSwimlane` and reads the lane back, but `lane.contents` remains empty; recorded in the P0 index and issue #202. Not live-green.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_swimlane.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_swimlane.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; skill harness 90 passed; full unit suite 2322 passed; focused integration 3 passed / 1 approved skip; unit coverage 100%; Ruff, Black, and mypy clean. The skipped live behavior remains a P0 and issue #202.

</details>

<details>
<summary><code>irp_action_api_report</code> · IRPAction · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** usage 27 src / 11 test refs, 2 owned members. Split `IRPAction` into `irp_action.py`; `IRPSendAction` now inherits from the canonical module and other siblings stay in `irp_actions.py`. The JavaDoc `getBody`/`setBody` pair maps to the pywin32 `body` property.
- [x] ① §1
- [x] ② §2 — canonical module `irp_action.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 3 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 2 integration tests built from a real statechart transition; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_action.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_action.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2197 passed; ruff/black clean

</details>

<details>
<summary><code>irp_send_action_api_report</code> · IRPSendAction · 8/8 steps · ⚠️ complete with deviation</summary>

- **Status (2026-03-19):** API sync is complete with an approved live deviation; `invoked_operation` remains blocked and issue #202 stays open. This is not a live-green claim.
- **Note:** usage 18 src / 12 test refs, 8 owned members. Split `IRPSendAction` into `irp_send_action.py`; siblings stay in `irp_actions.py`. Four accessors map to pywin32 properties; `add_argument_value` uses `call_com`. The state fixture sets `EventState` before retrieving the SendAction.
- [x] ① §1
- [x] ② §2 — canonical module `irp_send_action.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 9 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — Complete with deviation: 4 integration tests; 3 pass and 1 explicitly user-approved skip. With an `EventState`, real event, target object, and class-owned operation, setting `invokedOperation` completes but getter readback remains `None`; tracked in issue #202. Not live-green.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_send_action.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_send_action.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; skill harness 90 passed; full unit suite 2322 passed; focused integration 3 passed / 1 approved skip; ruff/black/mypy clean. The skipped live behavior remains a P0 and issue #202.

</details>

<details>
<summary><code>irp_flow_item_api_report</code> · IRPFlowItem · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** usage 24 src / 12 test refs, 3 owned members. Split `IRPFlowItem` into `irp_flow_item.py`; `IRPObjectNode` remains in `irp_activity.py` for its own row. `getRepresented` maps to the pywin32 `represented` property; the other two members use `call_com`.
- [x] ① §1
- [x] ② §2 — canonical module `irp_flow_item.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 4 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 3 integration tests with a populated represented collection; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_flow_item.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_flow_item.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2195 passed; ruff/black clean

</details>

<details>
<summary><code>irp_object_node_api_report</code> · IRPObjectNode · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** usage 17 src / 12 test refs, 7 owned members. Split `IRPObjectNode` into `irp_object_node.py`; this was the last class in `irp_activity.py`, so the empty shim and its mirrored unit test were removed. Three accessors map to pywin32 properties; the other two use `call_com`.
- [x] ① §1
- [x] ② §2 — canonical module `irp_object_node.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 8 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 4 focused Windows live integration tests pass. `add_in_state` / `remove_in_state` bind the object node to a represented class and use a state from that class's statechart.
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_object_node.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_object_node.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2194 passed; ruff/black clean

</details>

<details>
<summary><code>irp_call_operation_api_report</code> · IRPCallOperation · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** usage 15 src / 8 test refs, 4 owned members. Split `IRPCallOperation` into `irp_call_operation.py`; siblings stay in `irp_actions.py`. Both JavaDoc accessor pairs map to read/write pywin32 properties.
- [x] ① §1
- [x] ② §2 — canonical module `irp_call_operation.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 5 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 2 integration tests with real operation and relation fixtures; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_call_operation.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_call_operation.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2193 passed; ruff/black clean

</details>

<details>
<summary><code>irp_context_specification_api_report</code> · IRPContextSpecification · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** usage 12 src / 8 test refs, 4 owned members. Split `IRPContextSpecification` into `irp_context_specification.py`; siblings stay in `irp_actions.py`. Both JavaDoc accessor pairs map to read/write pywin32 properties.
- [x] ① §1
- [x] ② §2 — canonical module `irp_context_specification.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 5 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 2 integration tests with real string collections; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_context_specification.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_context_specification.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2192 passed; ruff/black clean

</details>

<details>
<summary><code>irp_accept_time_event_api_report</code> · IRPAcceptTimeEvent · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** usage 13 src / 6 test refs, 2 owned members. Split `IRPAcceptTimeEvent` into `irp_accept_time_event.py`; siblings stay in `irp_actions.py`. The JavaDoc duration pair maps to the pywin32 `durationTime` property.
- [x] ① §1
- [x] ② §2 — canonical module `irp_accept_time_event.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 3 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 1 integration test with a real Accept Time Event; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_accept_time_event.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_accept_time_event.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2191 passed; ruff/black clean

</details>

<details>
<summary><code>irp_accept_event_action_api_report</code> · IRPAcceptEventAction · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** validator and `verify_sync` pass; the populated event-property integration test passes against live Rhapsody.
- **Note:** two owned JavaDoc methods (`getEvent` / `setEvent`) map to the read/write pywin32 `event` property. The class and mirrored tests were split from the shared actions files into canonical per-class paths. Full-suite COM instability is unchanged from baseline: the run went from 13 passed / 30 failed / 558 errors before this sync to 14 passed / 30 failed / 558 errors after it; the added Accept Event Action case passed, while the baseline Rhapsody process crash and subsequent RPC-server errors remain outside this wrapper.
- [x] ① §1 — recorded both JavaDoc members and the populated event getter fixture matrix row
- [x] ② §2 — canonical wrapper/test paths, exports, and direct imports updated
- [x] ③ §3 — read/write `event` property uses the exact catalog property; validator reports 0 actionable deviations
- [x] ④ §4 — TDD red/green; 3 fake-COM unit tests, 100% statement/branch coverage (13 statements, 0 branches)
- [x] ⑤ §5 — focused live integration test passed (1); getter matrix `event` identity/value row is OK
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_accept_event_action.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_accept_event_action.rst` and toctree entry
- [x] ⑧ §8 — `verify_sync` and `--strict-getters` green; harness tests 90 passed; full unit suite 2309 passed; integration collection 601; Ruff, Black, and mypy clean. Full integration cascade is the same 30-failure/558-error baseline; the new live test passed.

</details>

<details>
<summary><code>irp_action_block_api_report</code> · IRPActionBlock · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** the class now has a canonical wrapper and per-class documentation; `verify_sync` passes.
- **Note:** JavaDoc declares no members owned by `IRPActionBlock`; it extends `IRPMessage`. The shared `irp_actions.py` shim and `test_irp_actions.py` were removed after this last sibling moved. The empty pywin32 catalog entry contains no getters; the getter-diff generator reports the interface as missing rather than producing an empty section.
- [x] ① §1 — JavaDoc package, description, no-owned-member inventory, and inherited `IRPMessage` API recorded
- [x] ② §2 — canonical wrapper/unit paths and package exports updated; obsolete shared wrapper/test files removed
- [x] ③ §3 — 0 JavaDoc/Python/pywin32-owned members; all behavior is inherited; no duplicate methods added
- [x] ④ §4 — TDD red/green; 2 fake-COM unit tests, 100% statement/branch coverage (6 statements, 0 branches)
- [x] ⑤ §5 — N/A: no child-owned behavior exists to assert; the mirrored integration file records the AGENTS.md inherited-member boundary rather than adding a parent-method smoke test
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_action_block.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_action_block.rst` and toctree entry
- [x] ⑧ §8 — validator 0 deviations; `verify_sync` and `--strict-getters` green; harness tests 90 passed; full unit suite 2309 passed; integration collection 601; Ruff, Black, and mypy clean. Full live suite remains at its unrelated 14 passed / 30 failed / 558 error baseline; the focused Accept Event Action live test passed.

</details>
