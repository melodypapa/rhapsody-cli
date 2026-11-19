# COM Binding Switch Design: RHAPSODY_COM_BINDING (dynamic | early)

- **Date:** 2026-11-19
- **Status:** Approved design (brainstorming session, pending implementation plan)
- **Scope:** `src/rhapsody_cli/application.py` only (wrappers, `com_utils.py`, and CLI untouched)

## Problem

All COM access currently uses dynamic (late) binding: `GetActiveObject`/`Dispatch`
return `win32com.client.dynamic.CDispatch` objects whose members resolve by name
at runtime. Live probes against Rhapsody 10.0.3 (`Rhapsody2.Application.1`)
established:

- Early binding (`EnsureDispatch`) generates typed wrappers from the typelib:
  `IRPApplication` (180 methods), `IRPProject` (212 members), `IRPComponent`
  (116 members), generated lazily per interface on first return.
- Property-style basics (`name`, `metaClass`) are **not** in the generated
  class member lists but **live-read works** — pywin falls through to dynamic
  resolution for undeclared members.
- `getName()`/`getGUID()`/`getMetaClass()` fail on **both** paths (the COM
  server itself does not answer them); the property fallback is the working
  access. `_get_method_or_property` therefore behaves identically under both
  bindings (verified: `hasattr(method)` is False on both; property read works
  on both; force-dynamic rewrap of early objects works for properties).
- The gen_py cache is machine-global and auto-used by plain
  `Dispatch`/`GetActiveObject` once written: after one `EnsureDispatch`, even
  dynamic callers receive generated shells. This is a hazard only when mixed
  accidentally; a deliberate switch makes the cache a managed asset.

Early binding offers: fail-fast typed errors, typed app-level calls, and
dispid-precomputed dispatch. The full behavioral parity can only be proven by
running the real workloads against a live Rhapsody — hence a switchable
binding with a smoke gate, not a big-bang flip.

## Goal

Make the COM binding selectable via the `RHAPSODY_COM_BINDING` environment
variable (`dynamic` default, `early` opt-in), validate `early` against the
full live smoke checklist, and flip the default to `early` only if parity is
proven.

## Non-Goals

- Renaming the Python API (snake_case stays; camelCase remains only at the COM
  boundary inside wrappers).
- Any change to `com_utils.py`, wrapper classes, or CLI code.
- Supporting `EnsureDispatch` usage outside `application.py` (the codebase's
  single COM entry point).
- Design Manager features (remain unsupported).

## Design

### 1. Binding switch (`application.py`)

- Module constant `_BINDING_ENV = "RHAPSODY_COM_BINDING"`; helper
  `_get_binding()` reads it at connect time (not import time so tests can
  toggle): values `dynamic` | `early` (case-insensitive); anything else logs a
  warning and falls back to `dynamic`.
- `_launch()`: `early` -> `win32com.client.gencache.EnsureDispatch(_PROG_ID)`
  (generates/uses the gen_py cache and launches if no instance is running);
  `dynamic` -> `win32com.client.Dispatch(_PROG_ID)` (unchanged).
- `_attach()`: stays `GetActiveObject(_PROG_ID)` for both bindings — attach
  must never launch. Once the gen_py cache exists, the returned object is
  early-bound automatically (documented pywin behavior); with no cache it is
  dynamic. Early binding therefore fully activates after the first launch (or
  any cache-generating call).
- The property-style fallback in `com_utils._get_method_or_property` is
  unchanged and required under both bindings (probe evidence: `getName`
  absent/failing everywhere; `name` works everywhere).

### 2. Go/no-go spike (first implementation task)

Under `RHAPSODY_COM_BINDING=early`, live-exercise the wrapper's member
inventory on a scratch project: `get_classes`/`classes`, `get_nested_packages`,
`add_nested_package`, `add_class`, `add_generalization`,
`find_nested_element_recursive`, `get_name`, `get_meta_class`,
`add_component`, `get_components`. Any member that works under `dynamic` but
fails under `early` that cannot be fixed by the existing property fallback
stops the switch (fall back to design revision) — properties are expected to
work per the probes.

### 3. Smoke gate

Run the 26-command live checklist from
`docs/superpowers/plans/2026-11-19-cli-simplification.md` under
`RHAPSODY_COM_BINDING=early` (scratch project, cleanup afterward). All 26 must
pass. Record results in the implementation plan.

### 4. Default flip decision

- If the spike and smoke pass with no wrapper changes: flip the default to
  `early` in the same change, keeping `dynamic` as the documented escape
  hatch.
- If any divergence is found: keep `dynamic` default, document the divergent
  members, and stop.

### 5. gen_py cache management (documented behavior)

- Cache location: `%TEMP%\gen_py\3.9\<typelib-guid>x<version>` (Rhapsody 10:
  `C1E0F4B1-2B50-11E8-9927-463500000031x0x1x0`).
- After a Rhapsody upgrade, stale caches can misbind — remediation is
  `win32com.client.gencache.Rebuild()` or deleting the GUID folder. Documented
  in CLAUDE.md and the user guide.

## Risks

| Risk | Mitigation |
| --- | --- |
| Members present dynamically but absent from the typelib fail under early | Spike (§2) + full smoke (§3) before any default flip; property fallback covers the basic accessors per probes |
| Stale gen_py cache after Rhapsody upgrades | Documented `Rebuild()` remediation (§5) |
| Attach semantics change (accidental launch) | `_attach` keeps `GetActiveObject` for both bindings (§1) |
| CI breakage | CI is non-Windows; `win32com` imports stay guarded; unit tests fake the connect path |

## Testing

- **Unit (TDD)**: binding parsing (valid/invalid/default), `_launch` uses
  `EnsureDispatch` when `early` and `Dispatch` when `dynamic`,
  `_attach` always uses `GetActiveObject`; all via patching
  `win32com.client` functions — no real COM in unit tests.
- **Live (Windows)**: spike (§2) + smoke gate (§3) under early; dynamic smoke
  unchanged as control.
- **Quality gate**: `ruff check src/ tests/ && black --check src/ tests/ &&
  mypy src/ tests/ && pytest tests/unit`.

## Rollback

Set `RHAPSODY_COM_BINDING=dynamic` (or unset) — the dynamic path is unchanged.
If the default was flipped and must be reverted, flip the constant back; the
gen_py cache may remain harmlessly (or be cleared per §5).
