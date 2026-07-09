# Enhanced Element CLI with Multi-Level Paths & Bulk Operations

**Date:** 2026-07-09  
**Status:** Design Approved  
**Scope:** Enhance element CLI commands (add, view, query, delete) with multi-level path support and bulk operations  

---

## Overview

This design enhances the element CLI to support:
1. **Multi-level hierarchical paths** using `/` or `\` separators (e.g., `parent-pkg/pkg/child-pkg/class-1`)
2. **Bulk operations** for adding multiple elements and recursive querying/deletion
3. **Robust error handling** with partial success reporting and safety confirmations
4. **Comprehensive documentation** with Sphinx user guide and API reference updates

The enhancements follow **Approach 1: Minimal Path Refactor** to keep changes focused and pragmatic while maintaining the existing class-based action architecture.

---

## Current State

The element CLI currently supports four subcommands:
- `rhapsody-cli element add --type [class|actor|package] --name NAME`
- `rhapsody-cli element view --path PATH`
- `rhapsody-cli element query [PATTERN]`
- `rhapsody-cli element delete PATH`

**Limitations:**
- Hardcoded "Default" package logic; no support for arbitrary nesting
- Single-item operations only
- Limited path syntax (`::` style, confusing for Windows users)
- No recursive operations (query nested structures, delete with contents)

---

## Design: Multi-Level Path Resolution

### Path Resolver Utility

**File:** `src/rhapsody_cli/cli/path_resolver.py`

**Purpose:** Parse and navigate hierarchical element paths consistently across all actions.

**Key Functions:**
```python
class PathResolver:
    @staticmethod
    def normalize_path(path: str) -> str:
        """Normalize / or \ separators to internal representation."""
        # Example: "parent-pkg\pkg/child-pkg" → "parent-pkg/pkg/child-pkg"

    @staticmethod
    def parse_path(path: str) -> tuple[str, list[str], str]:
        """
        Parse path into (start_element, navigation_steps, target_name).
        
        Example:
            Input: "parent-pkg/pkg/class-1"
            Output: (Root, ["parent-pkg", "pkg"], "class-1")
        
        Raises:
            PathResolverError: Invalid path syntax
        """

    @staticmethod
    def navigate_to_container(root_element: RPModelElement, steps: list[str]) -> RPModelElement:
        """Navigate through nested elements following the path steps."""
        # Example: Navigate from Root → parent-pkg → pkg
```

**Error Cases:**
- Empty path: `PathResolverError: "Path cannot be empty"`
- Invalid syntax: `PathResolverError: "Invalid path syntax: 'foo///bar'"`
- Path not found: `PathResolverError: "Could not navigate to 'parent-pkg/unknown' — stopped at 'parent-pkg' (not found: 'unknown')"`

### Supported Path Formats

| Format | Example | Notes |
|--------|---------|-------|
| **Forward slash** | `parent-pkg/pkg/class` | Preferred; Windows-compatible |
| **Backslash** | `parent-pkg\pkg\class` | Windows-native format |
| **Root prefix** (optional) | `Root/parent-pkg/pkg/class` | Ignored if present |
| **Mixed separators** | `parent-pkg/pkg\class` | Normalized to forward slash |

---

## Design: Enhanced Actions

### ElementAddAction (Enhanced)

**Single-Item Mode:**
```bash
rhapsody-cli element add --type class --name MyClass --path pkg/subpkg
```

**Bulk Mode (New):**
```bash
rhapsody-cli element add --type class --bulk items.txt --path pkg/subpkg
```

**Arguments:**
- `--type` (required): Element type (class, actor, package, etc.)
- `--name` (optional if --bulk): Name of single element
- `--path` (optional): Path to target container (default: Root)
- `--bulk` (optional): Path to items file (one name per line)

**Bulk Items File Format:**

*items.txt:*
```
MyClass1
MyClass2
AnotherClass
```

**Output (Success):**
```
Added 3 items:
  ✓ MyClass1 created at pkg/subpkg/MyClass1
  ✓ MyClass2 created at pkg/subpkg/MyClass2
  ✓ AnotherClass created at pkg/subpkg/AnotherClass
```

**Output (Partial Success):**
```
Added 2/3 items. Errors:
  Line 2 (MyClass2): Name already exists in pkg/subpkg
  Line 3 (AnotherClass): Invalid character in name
```

**Implementation:**
- Use `PathResolver` to navigate to target container
- If `--bulk` present: read file, iterate items, apply same creation logic
- Continue on individual failures; report summary at end
- Log each creation with full path

### ElementViewAction (Enhanced)

**Multi-Level Path Support:**
```bash
rhapsody-cli element view --path parent-pkg/pkg/class-1
```

**Arguments:**
- `--path` (required): Multi-level path to element

**Implementation:**
- Use `PathResolver` to navigate to element
- Display element properties (no changes to output format)
- Handle missing paths gracefully with helpful error messages

### ElementQueryAction (Enhanced)

**Single Container (Updated Path Support):**
```bash
rhapsody-cli element query --path pkg/subpkg
```

**Recursive Mode (New):**
```bash
rhapsody-cli element query --path pkg --recursive
rhapsody-cli element query --recursive  # List entire hierarchy from Root
```

**Arguments:**
- `PATTERN` (optional): Search pattern (existing)
- `--path` (optional): Container to query (default: Root)
- `--recursive` (optional): Include nested elements recursively

**Output Format (Recursive):**
```
Name           Type       Path
MyClass1       Class      pkg/MyClass1
MyClass2       Class      pkg/MyClass2
subpkg         Package    pkg/subpkg
NestedClass    Class      pkg/subpkg/NestedClass
```

**Implementation:**
- Use `PathResolver` to navigate to starting container
- If `--recursive`: perform depth-first traversal, include full paths
- If `--path` only: list direct children (current behavior with better paths)
- Maintain JSON output format for structured queries

### ElementDeleteAction (Enhanced)

**Single Element (Updated Path Support):**
```bash
rhapsody-cli element delete pkg/subpkg/class-1
```

**Recursive Delete (New, with Safety):**
```bash
rhapsody-cli element delete pkg/subpkg --recursive
rhapsody-cli element delete pkg/subpkg --recursive --force  # Skip confirmation
```

**Arguments:**
- `PATH` (required): Element path
- `--recursive` (optional): Delete container and all nested elements
- `--force` (optional): Skip confirmation prompt

**Safety Flow:**
1. User runs: `rhapsody-cli element delete pkg --recursive`
2. CLI counts nested elements and prompts:
   ```
   This will delete 'pkg' and 12 nested elements. Continue? [y/N]
   ```
3. On yes: perform delete, log each step
4. Report summary: `Deleted pkg and 12 nested elements`

**Implementation:**
- Use `PathResolver` to navigate to target element
- If `--recursive`: count nested elements, show confirmation (unless `--force`)
- Delete recursively, logging each step
- Report count of elements deleted

---

## Error Handling & Validation

### Path Validation

| Scenario | Error Message | Recovery |
|----------|---------------|----------|
| Empty path | `Path cannot be empty` | Use default (Root) or provide path |
| Invalid syntax | `Invalid path syntax: 'foo///bar'` | Fix syntax (remove extra slashes) |
| Navigation fails | `Could not navigate to 'foo/unknown' — stopped at 'foo' (not found: 'unknown')` | Verify path exists |
| Invalid element type | `Unknown element type 'invalidtype'` | Use supported type (class, actor, package) |

### Bulk Operations

| Scenario | Handling | Output |
|----------|----------|--------|
| Empty items file | Create 0 items | `Added 0 items` |
| Invalid line format | Skip empty lines; error on duplicates | Line number + reason |
| Partial success | Continue on error | `Added X/Y items. Errors: [list]` |
| Destination not found | Fail immediately; do not create any items | `Error: Path not found: 'pkg/unknown'` |

### Delete Safety

| Scenario | Behavior |
|----------|----------|
| `--recursive` without `--force` | Show element count + confirmation prompt |
| `--recursive --force` | Delete without prompt; log all deletions |
| Single element delete | Delete immediately (no prompt needed) |
| Element not found | Error: `Element not found at path 'pkg/unknown'` |

---

## Implementation Strategy

### Files to Create/Modify

| File | Action | Purpose |
|------|--------|---------|
| `src/rhapsody_cli/cli/path_resolver.py` | **Create** | PathResolver utility class |
| `src/rhapsody_cli/actions/element_action.py` | **Modify** | Enhance all four action classes |
| `tests/unit/cli/test_path_resolver.py` | **Create** | Unit tests for PathResolver |
| `tests/unit/actions/test_element_action_bulk.py` | **Create** | Tests for bulk operations |
| `docs/user-guide/element-cli.rst` | **Modify** | Add usage examples & bulk op docs |
| `docs/api-reference/cli-actions.rst` | **Modify** | Document new flags |
| `docs/cli-command-reference.rst` | **Modify** | Update command signatures |

### Test Coverage

**PathResolver Tests:**
- Normalize paths: `/`, `\`, mixed separators
- Parse paths: valid, invalid, edge cases (empty, leading slash, trailing slash)
- Navigate to container: success, not found, multi-level
- Error conditions: raise `PathResolverError` with clear messages

**Action Tests (Bulk Operations):**
- **Add:** Create N items from file, partial failure, invalid names
- **Query:** Recursive listing, full path output, depth-first order
- **Delete:** Confirm prompt, `--force` flag, recursive count verification
- All tests use fake COM objects (no Rhapsody installation needed)

### Test Files to Create

1. **`tests/unit/cli/test_path_resolver.py`**
   - Test path normalization (`/` vs `\` vs mixed)
   - Test path parsing (valid, invalid, edge cases)
   - Test navigation (success, not found scenarios)
   - Test error messages

2. **`tests/unit/actions/test_element_action_bulk.py`**
   - Test bulk add: multiple items, partial failure, error reporting
   - Test recursive query: nested structure, full paths, JSON output
   - Test recursive delete: confirmation prompt, `--force`, count verification

---

## Documentation Updates

### Sphinx Files to Update

#### 1. `docs/user-guide/element-cli.rst`

**New Sections:**
- "Path Syntax" — explain `/` and `\` formats, nesting examples
- "Bulk Operations" — add, query recursive, delete recursive with examples
- "Error Messages" — common errors and solutions

**Example Additions:**

```rst
Multi-Level Paths
-----------------

Add a class in a nested structure::

    $ rhapsody-cli element add --type class --name MyClass --path pkg/subpkg
    Created class: MyClass

Query nested elements recursively::

    $ rhapsody-cli element query --path pkg --recursive
    Name           Type       Path
    MyClass        Class      pkg/MyClass
    subpkg         Package    pkg/subpkg
    NestedClass    Class      pkg/subpkg/NestedClass

Bulk Operations
---------------

Add multiple classes from a file::

    $ cat items.txt
    Class1
    Class2
    Class3

    $ rhapsody-cli element add --type class --bulk items.txt --path pkg
    Added 3 items:
      ✓ Class1 created at pkg/Class1
      ✓ Class2 created at pkg/Class2
      ✓ Class3 created at pkg/Class3
```

#### 2. `docs/api-reference/cli-actions.rst`

**Update Command Signatures:**

```rst
rhapsody-cli element add
~~~~~~~~~~~~~~~~~~~~~~~~~

Usage::

    rhapsody-cli element add --type TYPE [--name NAME | --bulk FILE] [--path PATH]

Arguments:

- ``--type`` (required): Element type (class, actor, package, ...)
- ``--name``: Name of single element (required if --bulk not provided)
- ``--bulk``: Path to items file (required if --name not provided)
- ``--path``: Target container path using "/" or "\" format (default: Root)

Examples:

- Single element: ``rhapsody-cli element add --type class --name MyClass --path pkg/subpkg``
- Bulk from file: ``rhapsody-cli element add --type class --bulk items.txt --path pkg``
```

#### 3. `docs/cli-command-reference.rst`

**Update Summary Table:**

| Command | Flags | Purpose |
|---------|-------|---------|
| `add` | `--type`, `--name`, `--bulk`, `--path` | Add single or bulk elements |
| `view` | `--path` | View element with multi-level path support |
| `query` | `--path`, `--recursive`, `[PATTERN]` | Query with recursive traversal |
| `delete` | `--path`, `--recursive`, `--force` | Delete with optional recursive + safety |

---

## Success Criteria

✅ All four actions support multi-level paths (`/` or `\` separators)  
✅ Bulk add creates multiple items from file with error reporting  
✅ Recursive query lists full hierarchies with full paths  
✅ Recursive delete includes safety confirmation & `--force` override  
✅ PathResolver is pure, testable logic with >90% coverage  
✅ All existing tests pass; new tests achieve >80% coverage  
✅ Sphinx documentation includes examples for all new features  
✅ Error messages are clear, actionable, and include suggestions  

---

## Known Limitations & Future Work

**Out of Scope (Future Enhancements):**
- Support for additional element types beyond class, actor, package (can be added later)
- Element property modification on creation (attributes, stereotypes) — covered in separate CLI enhancement
- Batch query with complex filters (regex patterns, property matching) — future feature
- Undo/rollback for bulk operations — requires transaction support

**Design Assumptions:**
- Rhapsody projects have a well-defined hierarchy (no circular references)
- Element names are unique within their parent container
- Windows `\` and Unix `/` separators should be normalized transparently

---

## Implementation Order

1. **Phase 1:** Create `PathResolver` utility + comprehensive unit tests
2. **Phase 2:** Update `ElementAddAction` for multi-level paths + single bulk add
3. **Phase 3:** Update `ElementQueryAction` for recursive query
4. **Phase 4:** Update `ElementDeleteAction` for recursive delete + safety
5. **Phase 5:** Update `ElementViewAction` for multi-level paths
6. **Phase 6:** Write Sphinx documentation updates
7. **Phase 7:** Integration testing + final verification

---

## References

- **Current Element CLI:** `src/rhapsody_cli/commands/element_command.py`, `src/rhapsody_cli/actions/element_action.py`
- **Test Infrastructure:** `tests/unit/actions/`, `tests/fakes.py`
- **Documentation:** `docs/user-guide/`, `docs/api-reference/`
- **Code Guidelines:** `docs/CODE_GUIDELINES.md` (TDD, class-based actions, error handling)
