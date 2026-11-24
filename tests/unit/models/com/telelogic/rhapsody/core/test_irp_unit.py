"""Unit tests for the canonical IRPUnit wrapper."""

import re
from pathlib import Path

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import AddToModelMode, IRPUnit
from rhapsody_cli.models.com.telelogic.rhapsody.core import irp_unit as irp_unit_module
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_collection import IRPCollection
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_collection, make_fake_element


def test_unit_save_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    unit.save()

    fake.save.assert_called_once_with(0)


def test_unit_filename_uses_pywin32_filename_property() -> None:
    fake = make_fake_element("Package", properties={"filename": "Model/Foo.sbs"})
    unit = IRPUnit(fake)

    assert unit.filename == "Model/Foo.sbs"
    fake.getFilename.assert_not_called()


def test_unit_set_filename_uses_pywin32_filename_property() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    unit.filename = "Model/Bar.sbs"

    assert fake.filename == "Model/Bar.sbs"
    fake.setFilename.assert_not_called()


def test_unit_is_read_only_delegates_to_com() -> None:
    fake = make_fake_element("Package", isReadOnly=1)
    unit = IRPUnit(fake)

    assert unit.is_read_only() is True


def test_unit_set_read_only_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    unit.set_read_only(True)

    fake.setReadOnly.assert_called_once_with(1)


def test_unit_is_a_model_element() -> None:
    fake = make_fake_element("Package", properties={"name": "MyPkg"})
    unit = IRPUnit(fake)

    assert isinstance(unit, IRPModelElement)
    assert unit.name == "MyPkg"


def test_add_to_model_mode_constants_match_java_api() -> None:
    assert int(AddToModelMode.AS_REFERENCE) == 0
    assert int(AddToModelMode.AS_UNIT_WITH_COPY) == 1
    assert int(AddToModelMode.AS_UNIT_WITHOUT_COPY) == 2
    # IntEnum is int-compatible so callers can compare raw COM ints directly.
    assert AddToModelMode.AS_REFERENCE == 0  # type: ignore[comparison-overlap]


def test_unit_copy_to_another_project_unwraps_parent_and_wraps_result() -> None:
    parent = IRPModelElement(make_fake_element("Project"))
    copied_fake = make_fake_element("Package", properties={"name": "Copied"})
    fake = make_fake_element("Package", copyToAnotherProject=copied_fake)
    unit = IRPUnit(fake)

    result = unit.copy_to_another_project(parent)

    assert isinstance(result, IRPModelElement)
    assert result.name == "Copied"
    fake.copyToAnotherProject.assert_called_once_with(parent._com)


def test_unit_get_add_to_model_mode_returns_int() -> None:
    fake = make_fake_element("Package", getAddToModelMode=2)
    unit = IRPUnit(fake)

    assert unit.get_add_to_model_mode() == 2


def test_unit_cm_header_uses_pywin32_cmheader_property() -> None:
    fake = make_fake_element("Package", properties={"CMHeader": "// CM header"})
    unit = IRPUnit(fake)

    assert unit.cm_header == "// CM header"
    fake.getCMHeader.assert_not_called()


def test_unit_set_cm_header_uses_pywin32_cmheader_property() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    unit.cm_header = "// CM header"

    assert fake.CMHeader == "// CM header"
    fake.setCMHeader.assert_not_called()


def test_unit_get_cm_state_returns_int() -> None:
    fake = make_fake_element("Package", getCMState=1)
    unit = IRPUnit(fake)

    assert unit.get_cm_state() == 1


def test_unit_current_directory_uses_pywin32_property() -> None:
    fake = make_fake_element("Package", properties={"currentDirectory": "C:\\proj"})
    unit = IRPUnit(fake)

    assert unit.current_directory == "C:\\proj"
    fake.getCurrentDirectory.assert_not_called()


def test_unit_include_in_next_load_uses_pywin32_property() -> None:
    fake = make_fake_element("Package", properties={"includeInNextLoad": 1})
    unit = IRPUnit(fake)

    assert unit.include_in_next_load == 1
    fake.getIncludeInNextLoad.assert_not_called()


def test_unit_is_stub_uses_pywin32_property() -> None:
    fake = make_fake_element("Package", properties={"isStub": 0})
    unit = IRPUnit(fake)

    assert unit.is_stub == 0
    fake.getIsStub.assert_not_called()


def test_unit_get_language_returns_str() -> None:
    fake = make_fake_element("Package", getLanguage="C++")
    unit = IRPUnit(fake)

    assert unit.get_language() == "C++"


def test_unit_get_last_modified_time_returns_str() -> None:
    fake = make_fake_element("Package", getLastModifiedTime="20250731T120000")
    unit = IRPUnit(fake)

    assert unit.get_last_modified_time() == "20250731T120000"


def test_unit_get_nested_save_units_returns_collection() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Package", getNestedSaveUnits=coll)
    unit = IRPUnit(fake)

    result = unit.get_nested_save_units()

    assert isinstance(result, IRPCollection)


def test_unit_get_nested_save_units_count_returns_int() -> None:
    fake = make_fake_element("Package", getNestedSaveUnitsCount=3)
    unit = IRPUnit(fake)

    assert unit.get_nested_save_units_count() == 3


def test_unit_structure_diagrams_uses_pywin32_property() -> None:
    coll = make_fake_collection([])
    fake = make_fake_element("Package", properties={"structureDiagrams": coll})
    unit = IRPUnit(fake)

    result = unit.structure_diagrams

    assert isinstance(result, IRPCollection)
    fake.getStructureDiagrams.assert_not_called()


def test_unit_get_unit_path_raises_not_implemented_without_com_dispatch() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    with pytest.raises(NotImplementedError):
        unit.get_unit_path(1)

    fake.getUnitPath.assert_not_called()


def test_unit_is_reference_unit_returns_int() -> None:
    fake = make_fake_element("Package", isReferenceUnit=1)
    unit = IRPUnit(fake)

    assert unit.is_reference_unit() == 1
    fake.isReferenceUnit.assert_called_once_with()


def test_unit_is_separate_save_unit_returns_int() -> None:
    fake = make_fake_element("Package", isSeparateSaveUnit=0)
    unit = IRPUnit(fake)

    assert unit.is_separate_save_unit() == 0
    fake.isSeparateSaveUnit.assert_called_once_with()


def test_unit_load_passes_flag_and_wraps_result() -> None:
    loaded_fake = make_fake_element("Package", properties={"name": "Loaded"})
    fake = make_fake_element("Package", load=loaded_fake)
    unit = IRPUnit(fake)

    result = unit.load(1)

    assert isinstance(result, IRPModelElement)
    assert result.name == "Loaded"
    fake.load.assert_called_once_with(1)


def test_unit_move_to_another_project_leave_a_reference_unwraps_parent_and_wraps_result() -> None:
    parent = IRPModelElement(make_fake_element("Project"))
    moved_fake = make_fake_element("Package", properties={"name": "Moved"})
    fake = make_fake_element("Package", moveToAnotherProjectLeaveAReference=moved_fake)
    unit = IRPUnit(fake)

    result = unit.move_to_another_project_leave_a_reference(parent)

    assert isinstance(result, IRPModelElement)
    assert result.name == "Moved"
    fake.moveToAnotherProjectLeaveAReference.assert_called_once_with(parent._com)


def test_unit_reference_to_another_project_unwraps_parent_and_wraps_result() -> None:
    parent = IRPModelElement(make_fake_element("Project"))
    ref_fake = make_fake_element("Package", properties={"name": "Ref"})
    fake = make_fake_element("Package", referenceToAnotherProject=ref_fake)
    unit = IRPUnit(fake)

    result = unit.reference_to_another_project(parent)

    assert isinstance(result, IRPModelElement)
    assert result.name == "Ref"
    fake.referenceToAnotherProject.assert_called_once_with(parent._com)


def test_unit_set_include_in_next_load_uses_pywin32_property() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    unit.include_in_next_load = 1

    assert fake.includeInNextLoad == 1
    fake.setIncludeInNextLoad.assert_not_called()


def test_unit_set_language_passes_language_and_recursive_flag() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    unit.set_language("cpp", 0)

    fake.setLanguage.assert_called_once_with("cpp", 0)


def test_unit_set_separate_save_unit_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    unit.set_separate_save_unit(1)

    fake.setSeparateSaveUnit.assert_called_once_with(1)


def test_unit_set_unit_path_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    unit.set_unit_path("C:\\proj\\new")

    fake.setUnitPath.assert_called_once_with("C:\\proj\\new")


def test_unit_unload_delegates_to_com() -> None:
    fake = make_fake_element("Package")
    unit = IRPUnit(fake)

    unit.unload()

    fake.unload.assert_called_once_with()


def test_irp_unit_uses_no_legacy_dual_binding_helpers() -> None:
    """IRPUnit's own methods call exactly one pywin32 member — no name probing."""
    import ast as _ast

    source = Path(irp_unit_module.__file__).read_text(encoding="utf-8")
    tree = _ast.parse(source)
    unit_cls = next(node for node in tree.body if isinstance(node, _ast.ClassDef) and node.name == "IRPUnit")
    offenders: list[str] = []
    for fn in unit_cls.body:
        if not isinstance(fn, _ast.FunctionDef):
            continue
        for sub in _ast.walk(fn):
            if isinstance(sub, _ast.Call) and isinstance(sub.func, _ast.Attribute):
                if sub.func.attr in ("_get_method_or_property", "_set_method_or_property"):
                    offenders.append(f"IRPUnit.{fn.name}:{sub.lineno}:legacy-helper")
            if isinstance(sub, _ast.Call) and isinstance(sub.func, _ast.Name) and sub.func.id == "hasattr":
                offenders.append(f"IRPUnit.{fn.name}:{sub.lineno}:hasattr-probe")
    assert offenders == []


def test_irp_unit_module_uses_future_annotations_and_unquoted_type_references() -> None:
    """The synced wrapper uses future annotations with unquoted type references."""
    source = Path(irp_unit_module.__file__).read_text(encoding="utf-8")

    assert "from __future__ import annotations" in source
    assert re.search(r'cast\("', source) is None
    assert re.search(r'(-> |: )"[A-Z][A-Za-z]*"', source) is None
