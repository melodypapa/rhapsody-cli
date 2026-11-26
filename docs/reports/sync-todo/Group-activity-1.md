# Sync todo — `activity` (group 1 of 2)

**10 classes** · ✅ 10 archived · ⬜ 0 open

One row per sync run. A step is ticked only when its evidence lands; a row is archived only after all eight steps pass. Binding rule: one pywin32-exposed COM member per call — `call_com(lambda: self._com.Name(...))` for methods, `get_com_property` / `set_com_property` for properties; catalog-absent sites are blockers, never blind migrations. Canonical package: `src/rhapsody_cli/models/com/telelogic/rhapsody/core/`, mirrored tests under `tests/{unit,integration}/models/com/telelogic/rhapsody/core/`.

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
| 1 | `irp_flow_api_report` | IRPFlow | `elements/activity/model_activity.py` | 4 | — | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 2 | `irp_flowchart_api_report` | IRPFlowchart | `rhapsody_cli/models/elements/activity/model_activity.py` | 2 | 14 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 3 | `irp_swimlane_api_report` | IRPSwimlane | `rhapsody_cli/models/elements/activity/model_activity.py` | 1 | 5 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 4 | `irp_action_api_report` | IRPAction | `rhapsody_cli/models/elements/activity/model_actions.py` | 2 | 2 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 5 | `irp_send_action_api_report` | IRPSendAction | `rhapsody_cli/models/elements/activity/model_actions.py` | 7 | 8 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 6 | `irp_flow_item_api_report` | IRPFlowItem | `rhapsody_cli/models/elements/activity/model_activity.py` | 0 | 3 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 7 | `irp_object_node_api_report` | IRPObjectNode | `rhapsody_cli/models/elements/activity/model_activity.py` | 3 | 7 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 8 | `irp_call_operation_api_report` | IRPCallOperation | `rhapsody_cli/models/elements/activity/model_actions.py` | 4 | 4 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 9 | `irp_context_specification_api_report` | IRPContextSpecification | `rhapsody_cli/models/elements/activity/model_actions.py` | 2 | 4 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |
| 10 | `irp_accept_time_event_api_report` | IRPAcceptTimeEvent | `rhapsody_cli/models/elements/activity/model_actions.py` | 2 | 2 | 8/8 (①②③④⑤⑥⑦⑧) | ✅ archived |

## Row details

<details>
<summary><code>irp_flow_api_report</code> · IRPFlow · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** activity-flow element (107 src / 59 test) shared by operations, diagrams and statecharts. Split `IRPFlow` into `irp_flow.py`; siblings stay in `irp_activity.py` for their own rows. Eight JavaDoc accessors map to pywin32 properties and are exposed as `@property`; six members use `call_com`.
- [x] ① §1
- [x] ② §2 — canonical module `irp_flow.py`; exports and direct imports updated; sibling classes untouched
- [x] ③ §3 — 0 actionable deviations after binding migration; authority catalog refreshed from committed reports
- [x] ④ §4 — 18 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 14 integration tests; getter matrix all OK; macOS = collection-only (live run is Windows CI-only)
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_flow.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_flow.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; skill tests 90 passed; full unit suite 2200 passed; ruff/black clean; mypy skipped on py3.14 (CI runs it on <3.10)

</details>

<details>
<summary><code>irp_flowchart_api_report</code> · IRPFlowchart · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** usage 41 src / 21 test refs, 14 owned members. Split `IRPFlowchart` into `irp_flowchart.py`; siblings stay in `irp_activity.py` for their own rows. Three JavaDoc accessors map to pywin32 properties; the other eleven use `call_com`.
- [x] ① §1
- [x] ② §2 — canonical module `irp_flowchart.py`; exports and direct imports updated; sibling classes untouched
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 15 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 12 integration tests; getter matrix all OK; macOS = collection-only (live run is Windows CI-only)
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_flowchart.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_flowchart.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2199 passed; ruff/black clean; mypy skipped on py3.14 (CI runs it on <3.10)

</details>

<details>
<summary><code>irp_swimlane_api_report</code> · IRPSwimlane · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived. `contents` getter recorded as a P0 live blocker (no documented API populates a lane's contents).
- **Note:** usage 29 src / 12 test refs, 5 owned members. Split `IRPSwimlane` into `irp_swimlane.py`; siblings stay in `irp_activity.py` for their own rows. Three accessors are COM properties; `add_swimlane` uses `call_com`.
- [x] ① §1
- [x] ② §2 — canonical module `irp_swimlane.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 6 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 4 integration tests; `contents` blocked, other getters populated; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_swimlane.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_swimlane.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2198 passed; ruff/black clean

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
<summary><code>irp_send_action_api_report</code> · IRPSendAction · 8/8 steps · ✅ archived</summary>

- **Status (2026-11-26):** verify_sync passes; all steps archived.
- **Note:** usage 18 src / 12 test refs, 8 owned members. Split `IRPSendAction` into `irp_send_action.py`; siblings stay in `irp_actions.py`. Four accessors map to pywin32 properties; `add_argument_value` uses `call_com`.
- [x] ① §1
- [x] ② §2 — canonical module `irp_send_action.py`; exports and direct imports updated
- [x] ③ §3 — 0 actionable deviations after binding migration
- [x] ④ §4 — 9 fake-COM unit tests, 100% statements/branches
- [x] ⑤ §5 — 5 integration tests built from a real state's send action; macOS = collection-only
- [x] ⑥ §6 — `docs/requirements/com/telelogic/rhapsody/core/irp_send_action.md`
- [x] ⑦ §7 — `docs/api/com/telelogic/rhapsody/core/irp_send_action.rst` + toctree entry
- [x] ⑧ §8 — validator 0 deviations; verify_sync + --strict-getters green; full unit suite 2196 passed; ruff/black clean

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
- [x] ⑤ §5 — 5 integration tests with real activity nodes and states; macOS = collection-only
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
