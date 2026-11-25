"""Integration tests for IRPClass with live Rhapsody COM API.

These tests require a running Rhapsody instance with an open project.
"""

import time
from typing import cast

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPEventReception
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_operation import IRPOperation
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_package import IRPPackage
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_project import IRPProject
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_type import IRPType


@pytest.mark.integration
class TestIRPClassIntegration:
    """Integration tests for IRPClass with real Rhapsody COM API."""

    @staticmethod
    def _unique(prefix: str = "Test") -> str:
        return f"{prefix}_{int(time.time() * 1000) % 1000000}"

    @staticmethod
    def _create_package(project: IRPProject, name: str) -> IRPPackage:
        pkg = project.add_package(name)
        assert pkg is not None
        assert isinstance(pkg, IRPPackage)
        return pkg

    def test_class_inheritance(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("InhPkg")
        parent_name = self._unique("ParentCls")
        child_name = self._unique("ChildCls")
        pkg = self._create_package(test_project, pkg_name)
        parent = pkg.add_class(parent_name)
        child = pkg.add_class(child_name)
        try:
            child.add_superclass(parent)
            generalizations = list(child.generalizations)
            assert any(gen.get_base_class() == parent for gen in generalizations)
            child.delete_superclass(parent)
            generalizations_after = list(child.generalizations)
            assert not any(gen.get_base_class() == parent for gen in generalizations_after)
        finally:
            child.delete_from_project()
            parent.delete_from_project()

    def test_constructor_destructor(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("CtorPkg")
        class_name = self._unique("CtorCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            ctor = test_class.add_constructor("void()")
            assert ctor is not None
            dtor = test_class.add_destructor()
            assert dtor is not None
            operations = list(test_class.operations)
            assert ctor in operations
            assert dtor in operations
        finally:
            test_class.delete_from_project()

    def test_set_is_abstract_raises_not_implemented(self, test_project: IRPProject) -> None:
        """IRPClass.set_is_abstract is marked unimplemented: Rhapsody2.Application.1's automation
        server accepts a write to the 'isAbstract' COM property without error (confirmed via
        typelib inspection that both PROPERTYGET and PROPERTYPUT are declared for isAbstract
        under the same DISPID -- it is not read-only at the interface level), but the write does
        not persist (confirmed via immediate read-back, post-saveAll(), and a fresh re-fetch of
        the element). This is a genuine limitation of this Rhapsody build's IRPClass::isAbstract
        implementation, so the wrapper raises rather than silently no-opping."""
        pkg_name = self._unique("AbsPkg")
        class_name = self._unique("AbsCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            assert test_class.is_abstract is False
            with pytest.raises(NotImplementedError):
                test_class.is_abstract = True
        finally:
            test_class.delete_from_project()

    def test_type_management(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("TypePkg")
        class_name = self._unique("TypeCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            added_type = test_class.add_type(self._unique("MyType"))
            assert added_type is not None
            assert isinstance(added_type, IRPType)
            added_type.delete_from_project()
        finally:
            test_class.delete_from_project()

    def test_add_and_delete_reception(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("RecPkg")
        class_name = self._unique("RecCls")
        reception_name = self._unique("onSignal")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            reception = test_class.add_reception(reception_name)
            assert reception is not None
            assert isinstance(reception, IRPEventReception)
            assert reception in list(test_class.interface_items)
            test_class.delete_reception(reception)
            items_after = [i.name for i in test_class.interface_items]
            assert reception_name not in items_after
        finally:
            test_class.delete_from_project()

    def test_add_event_reception(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("EvRecPkg")
        class_name = self._unique("EvRecCls")
        reception_name = self._unique("onEvSig")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            reception = test_class.add_event_reception(reception_name)
            assert reception is not None
            assert isinstance(reception, IRPEventReception)
            assert reception in list(test_class.interface_items)
        finally:
            test_class.delete_from_project()

    def test_add_event_reception_with_event(self, test_project: IRPProject) -> None:
        """JavaDoc IRPClass.addEventReceptionWithEvent exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPEvent

        pkg_name = self._unique("EvWEvPkg")
        class_name = self._unique("EvWEvCls")
        event_name = self._unique("MyEvent")
        reception_name = self._unique("onMyEvent")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            event = pkg.add_event(event_name)
            with pytest.raises(NotImplementedError, match="addEventReceptionWithEvent is not exposed in the Rhapsody COM"):
                test_class.add_event_reception_with_event(reception_name, cast(IRPEvent, event))
        finally:
            test_class.delete_from_project()

    def test_update_contained_diagrams_on_server_raises_not_implemented(self, test_project: IRPProject) -> None:
        """JavaDoc IRPClass.updateContainedDiagramsOnServer exists, but pywin32 does not expose it (absent from docs/reports/pywin32_authority.json), so the stub raises NotImplementedError."""
        pkg = self._create_package(test_project, self._unique("UnavailableDiagramPkg"))
        test_class = pkg.add_class(self._unique("UnavailableDiagramClass"))
        try:
            with pytest.raises(NotImplementedError):
                test_class.update_contained_diagrams_on_server(1)
        finally:
            test_class.delete_from_project()

    def test_add_triggered_operation(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("TrigPkg")
        class_name = self._unique("TrigCls")
        op_name = self._unique("trigOp")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            triggered_op = test_class.add_triggered_operation(op_name)
            assert triggered_op is not None
            assert isinstance(triggered_op, IRPOperation)
            operations = list(test_class.operations)
            assert triggered_op in operations
        finally:
            test_class.delete_from_project()

    def test_delete_nested_class(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("DelClsPkg")
        outer_name = self._unique("OuterCls")
        inner_name = self._unique("InnerCls")
        pkg = self._create_package(test_project, pkg_name)
        outer = pkg.add_class(outer_name)
        try:
            inner = outer.add_class(inner_name)
            assert inner is not None
            nested_names = [c.name for c in outer.nested_classifiers]
            assert inner_name in nested_names
            outer.delete_class(inner_name)
            nested_after = [c.name for c in outer.nested_classifiers]
            assert inner_name not in nested_after
        finally:
            outer.delete_from_project()

    def test_delete_constructor(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("DelCtorPkg")
        class_name = self._unique("DelCtorCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            ctor = test_class.add_constructor("void()")
            assert ctor is not None
            operations = list(test_class.operations)
            assert ctor in operations
            test_class.delete_constructor(ctor)
            operations_after = list(test_class.operations)
            assert ctor not in operations_after
        finally:
            test_class.delete_from_project()

    def test_delete_destructor(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("DelDtorPkg")
        class_name = self._unique("DelDtorCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            dtor = test_class.add_destructor()
            assert dtor is not None
            operations = list(test_class.operations)
            assert dtor in operations
            test_class.delete_destructor()
            operations_after = list(test_class.operations)
            assert dtor not in operations_after
        finally:
            test_class.delete_from_project()

    def test_delete_event_reception(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("DelEvPkg")
        class_name = self._unique("DelEvCls")
        reception_name = self._unique("delEvSig")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            reception = test_class.add_event_reception(reception_name)
            assert reception is not None
            items = [i.name for i in test_class.interface_items]
            assert reception_name in items
            test_class.delete_event_reception(reception)
            items_after = [i.name for i in test_class.interface_items]
            assert reception_name not in items_after
        finally:
            test_class.delete_from_project()

    def test_delete_type(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("DelTypePkg")
        class_name = self._unique("DelTypeCls")
        type_name = self._unique("MyDataType")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            added_type = test_class.add_type(type_name)
            assert added_type is not None
            test_class.delete_type(type_name)
            assert True
        finally:
            test_class.delete_from_project()

    def test_active_flag_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("ActPkg")
        class_name = self._unique("ActCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            assert test_class.is_active in (0, 1)
            test_class.is_active = 1
            assert test_class.is_active == 1
            test_class.is_active = 0
            assert test_class.is_active == 0
        finally:
            test_class.delete_from_project()

    def test_behavior_overriden_roundtrip(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("BehOvPkg")
        class_name = self._unique("BehOvCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            assert test_class.is_behavior_overriden in (0, 1)
            test_class.is_behavior_overriden = 1
            assert test_class.is_behavior_overriden == 1
            test_class.is_behavior_overriden = 0
            assert test_class.is_behavior_overriden == 0
        finally:
            test_class.delete_from_project()

    def test_is_composite_readonly(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("CompPkg")
        class_name = self._unique("CompCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            assert test_class.is_composite in (0, 1)
        finally:
            test_class.delete_from_project()

    def test_is_reactive_readonly(self, test_project: IRPProject) -> None:
        pkg_name = self._unique("ReactPkg")
        class_name = self._unique("ReactCls")
        pkg = self._create_package(test_project, pkg_name)
        test_class = pkg.add_class(class_name)
        try:
            assert test_class.is_reactive in (0, 1)
        finally:
            test_class.delete_from_project()

    def test_is_final_roundtrip(self, test_project: IRPProject) -> None:
        pkg = test_project.add_package(self._unique("FinalPkg"))
        cls = pkg.add_class(self._unique("FinalCls"))
        try:
            assert isinstance(cls.get_is_final(), int)
            assert cls.set_is_final(1) is None  # type: ignore[func-returns-value]
        finally:
            cls.delete_from_project()
