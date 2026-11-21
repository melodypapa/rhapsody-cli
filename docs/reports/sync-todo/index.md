# Sync todo index — `docs/reports` interface sync (pywin32-direct bindings)

Execution ledger for the 16 committed interface reports in `docs/reports/` (`*_api_report.md`)
and their wrappers. One row = one report = one rhapsody-sync run; every row's steps enumerate
the rules and steps of [`.agents/skills/rhapsody-sync/SKILL.md`](../../.agents/skills/rhapsody-sync/SKILL.md)
(§1–§8). Runs tick a step the moment it passes; rows archive to `Group-finished.md` only when
all eight steps pass and the run's commit exists.

## Layout (2026-11-21)

All 16 open rows live in [Group-unfinished-1.md](Group-unfinished-1.md); completed rows
archive to [Group-finished.md](Group-finished.md) (a batch file is deleted when its last row
archives). Queue order: core.py base classes first (their migration removes the inherited
dual-binding fallback for every subclass), then leaves.

| Batch file | Rows | Legacy sites | Interface span | Status |
| --- | --- | --- | --- | --- |
| [Group-unfinished-1.md](Group-unfinished-1.md) | 16 | ~249 | IRPClass → IRPUseCase | ⬜ 0/16 archived (pilot 5/6 steps) |
| [Group-finished.md](Group-finished.md) | 0 | 0 | archive | ✅ 0 |

Progress: **0/16 rows fully done**; pilot IRPClass migrated and committed (`7163149`,
`b27a8bb`) with Step 6's Windows closeout still open. Refreshed 2026-11-21 (site counts from
the 2026-11-21 survey — re-survey with `grep -c "_method_or_property" <wrapper>` at run start).

## Resume rule

Take the first row still `[ ]` in queue order from
[Group-unfinished-1.md](Group-unfinished-1.md). Execute one rhapsody-sync run for that
interface following SKILL.md §1–§8 exactly as enumerated in the row's steps; tick a step when
its evidence lands (never batch-tick at the end); move the row to
[Group-finished.md](Group-finished.md) only after its commit exists and no step is open. Do
not re-derive scope or decisions already recorded in the row's Notes.

## Standing decisions

- **Binding rule (SKILL §3):** every wrapper member calls exactly one pywin32-exposed COM
  member from `pywin32_authority.json` — method-shaped via
  `call_com(lambda: self._com.Name(...))`, property-shaped via `get_com_property` /
  `set_com_property`. No runtime name probing or Java-name fallback; COM names are string
  arguments only. A call site whose member is absent from the catalog for that interface is a
  blocker: leave the site unchanged, record it, never migrate blind.
- **Machine split (2026-11-21):** `docs/java_api/` is gitignored and absent on macOS. There,
  Steps 1–7 are executable (Steps 3/8 use the committed report + catalog as COM evidence, with
  an offline proof substituting for regeneration checks); Step 8's Windows closeout —
  `validate_interface.py <IFACE> --source authority`, `verify_sync.py <IFACE>`, live
  integration run — stays open with the blocker recorded on the row.
- **Canonical package (SKILL §4):** only `IRPClass` lives in
  `src/rhapsody_cli/models/com/telelogic/rhapsody/core/` so far; every other row starts with
  the package move (wrapper, imports/exports/registration, unit + integration tests to the
  mirrored `tests/{unit,integration}/models/com/telelogic/rhapsody/core/` paths, snake_case
  test module names, `__init__.py` at every level, no compatibility shim).
- **Per-class documents (SKILL §6/§7):** requirement and RST artifacts live at the class's
  package path — `docs/requirements/<java.package.path>/<snake_case>.md` and
  `docs/api/<java.package.path>/<snake_case>.rst` — not in the legacy monoliths
  (`swr_elem_requirements.md`, `elements.rst`). Each run moves its class's entries out of the
  monoliths into the per-class files (no duplicates); `elements.rst` lists per-class pages in
  its toctree. `verify_sync.py` checks the per-class paths strictly (no legacy fallback).
- **core.py split:** `models/core.py` holds `AbstractRPModelElement` (2 forwarder
  definitions), `RPModelElement`, `RPCollection`, `RPUnit` — 92 legacy sites total. Survey and
  split per class at each row's start. IRPModelElement's 22 unit-family names (`CMHeader`,
  `filename`, `isReadOnly`, ...) exist only in other interfaces' catalogs: resolve against
  IRPUnit's catalog entry during the IRPUnit row, or record a blocker in the IRPModelElement
  row.
- **Uncovered interfaces have no rows yet:** ~380 further legacy sites (Interactions, Graphics,
  Codegen support, StateVertex/State, Relation, Configuration, Activity, Component, RPVariable,
  RPTag, Files, Annotation/Requirement, Statechart, Templates, IDE support, Instance,
  Generalization, AssociationRole, Stereotype, ClassifierRole, SysMLPort, Values, HyperLink,
  Dependency, Diagram, Node, EnumerationLiteral/Comment/Constraint, Actor, Collaboration).
  Add rows only after the catalog and their reports are regenerated on Windows
  (`python scripts/pywin32_authority.py --source typelib`). Never migrate blind.
- **Termination:** after the last row archives, delete `_get_method_or_property` /
  `_set_method_or_property` from `com_utils.py` / `core.py`, drop the legacy notes from
  `AGENTS.md`, `docs/CODE_GUIDELINES.md`, and the sync skill, and confirm
  `grep -r "_method_or_property" src/` is empty.
