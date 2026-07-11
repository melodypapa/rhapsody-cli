# RhapsodyApplication Redesign — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Refactor `RhapsodyApplication` to remove its dependency on `AbstractRPModelElement` by extracting COM utility functions into a standalone module, simplify the lifecycle API (`connect`/`disconnect`), and add ~15 missing IRPApplication methods.

**Architecture:** Extract `call_com`, `get_method_or_property`, `set_method_or_property` into `com_utils.py`. `AbstractRPModelElement` forwards to these via one-liner classmethods (0 diff in 100+ call sites). `RhapsodyApplication` uses `com_utils` directly with no imports from the element hierarchy. `connect()` gains `attach_only` and `show_gui` params; `attach()`/`launch()` become private; `disconnect()` wraps `quit()`.

**Tech Stack:** Python 3.8+, pywin32 (COM), MagicMock (tests)

## Global Constraints

- No changes to element wrapper call sites (100+ references to `AbstractRPModelElement.call_com(...)` stay unchanged)
- Method names must mirror the Rhapsody Java API exactly (`getName`, `activeProject`, `quit`, etc.)
- All COM calls must go through `call_com(lambda: ...)` or the helper accessors
- No use of `from __future__ import annotations`
- Tests must use MagicMock-based fakes from `tests/unit/models/fakes.py`
- The `pywintypes` import guard (`try/except ImportError`) must stay for cross-platform compatibility (Sphinx on Linux)

---
