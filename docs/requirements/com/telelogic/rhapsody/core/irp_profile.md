## SWR_ELEM_00054: IRPProfile Wrapper

**ID:** SWR_ELEM_00054
**Title:** IRPProfile is an inheritance-only wrapper registered for the Profile meta class
**Status:** Implemented
**Priority:** Low
**Description:**
The `IRPProfile` JavaDoc interface represents a profile extending `IRPPackage`.
It declares no owned members; all behavior is inherited from `IRPPackage`,
`IRPUnit` and `IRPModelElement`. The Python `IRPProfile` shall extend
`IRPPackage`, register itself for meta class `"Profile"`, and add no duplicate
COM bindings.

The canonical module is
`src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_profile.py`. Unit tests
in the mirrored unit path use only fake COM objects and assert the wrapper
shape and registration. The mirrored integration test creates a real profile
through `IRPProject.add_profile`, asserts it wraps as `IRPProfile`, and deletes
the created profile. Since the interface owns no members, this is a
registration/navigation check rather than owned-behavior coverage. Live
assertions are CI-only on Windows and are unverified in offline runs.
**Implementation:** src/rhapsody_cli/models/com/telelogic/rhapsody/core/irp_profile.py:IRPProfile
**Last Changed:** 2026-11-27
