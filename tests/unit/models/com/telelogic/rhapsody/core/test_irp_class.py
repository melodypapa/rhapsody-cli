"""Unit tests for rhapsody_cli.models.com.telelogic.rhapsody.core.IRPClass."""

from pathlib import Path
from typing import cast
from unittest.mock import MagicMock

import pytest

import rhapsody_cli.models.com.telelogic.rhapsody.core.irp_class as irp_class_module
from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass
from rhapsody_cli.models.core import AbstractRPModelElement, IRPModelElement
from rhapsody_cli.models.elements.classifiers import RPClassifier
from rhapsody_cli.models.elements.classifiers.model_operation import RPOperation
from rhapsody_cli.models.elements.interactions.model_interactions import RPEvent, RPEventReception
from tests.unit.models.fakes import make_fake_element


def test_class_is_a_classifier() -> None:
    fake = make_fake_element("Class", properties={"name": "Widget"})
    klass = IRPClass(fake)

    assert isinstance(klass, RPClassifier)
    assert klass.get_name() == "Widget"


def test_class_add_superclass_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    base = make_fake_element("Class", properties={"name": "Base"})
    klass = IRPClass(fake)

    klass.add_superclass(IRPClass(base))

    fake.addSuperclass.assert_called_once_with(base)


def test_class_add_constructor_wraps_result() -> None:
    fake = make_fake_element("Class")
    ctor = make_fake_element("Operation", properties={"name": "Widget"})
    fake.addConstructor.return_value = ctor
    klass = IRPClass(fake)

    result = klass.add_constructor("int x")

    fake.addConstructor.assert_called_once_with("int x")
    assert result.get_name() == "Widget"


def test_class_add_destructor_wraps_result() -> None:
    fake = make_fake_element("Class")
    dtor = make_fake_element("Operation", properties={"name": "~Widget"})
    fake.addDestructor.return_value = dtor
    klass = IRPClass(fake)

    result = klass.add_destructor()

    fake.addDestructor.assert_called_once_with()
    assert result.get_name() == "~Widget"


def test_class_is_abstract_property_reads_pywin32_property() -> None:
    fake = MagicMock(spec=["isAbstract"])
    fake.isAbstract = 1
    klass = IRPClass(fake)

    assert klass.is_abstract is True


def test_class_add_class_nested_wraps_result() -> None:
    fake = make_fake_element("Class")
    nested = make_fake_element("Class", properties={"name": "Inner"})
    fake.addClass.return_value = nested
    klass = IRPClass(fake)

    result = klass.add_class("Inner")

    fake.addClass.assert_called_once_with("Inner")
    assert result.get_name() == "Inner"


def test_class_is_registered_for_meta_class_class() -> None:
    fake = make_fake_element("Class", properties={"name": "Widget"})

    wrapped = AbstractRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPClass)


def test_class_add_event_reception_wraps_result() -> None:
    fake = make_fake_element("Class")
    reception = make_fake_element("EventReception", properties={"name": "onEvent"})
    fake.addEventReception.return_value = reception
    klass = IRPClass(fake)

    result = klass.add_event_reception("onEvent")

    fake.addEventReception.assert_called_once_with("onEvent")
    assert result.get_name() == "onEvent"


def test_class_add_event_reception_with_event_unwraps_and_wraps() -> None:
    fake = make_fake_element("Class")
    event = make_fake_element("Event", properties={"name": "Tick"})
    reception = make_fake_element("EventReception", properties={"name": "onTick"})
    fake.addEventReceptionWithEvent.return_value = reception
    klass = IRPClass(fake)

    with pytest.raises(NotImplementedError):
        wrapped_event = AbstractRPModelElement.wrap(event)
        klass.add_event_reception_with_event("onTick", cast(RPEvent, wrapped_event))


def test_class_add_link_unwraps_all_args_and_wraps_result() -> None:
    fake = make_fake_element("Class")
    from_part = make_fake_element("Instance", properties={"name": "p1"})
    to_part = make_fake_element("Instance", properties={"name": "p2"})
    assoc = make_fake_element("Relation", properties={"name": "r1"})
    from_port = make_fake_element("Port", properties={"name": "port1"})
    to_port = make_fake_element("Port", properties={"name": "port2"})
    link = make_fake_element("Link", properties={"name": "link1"})
    fake.addLink.return_value = link
    klass = IRPClass(fake)

    result = klass.add_link(
        cast(IRPModelElement, AbstractRPModelElement.wrap(from_part)),
        cast(IRPModelElement, AbstractRPModelElement.wrap(to_part)),
        cast(IRPModelElement, AbstractRPModelElement.wrap(assoc)),
        cast(IRPModelElement, AbstractRPModelElement.wrap(from_port)),
        cast(IRPModelElement, AbstractRPModelElement.wrap(to_port)),
    )

    fake.addLink.assert_called_once_with(from_part, to_part, assoc, from_port, to_port)
    assert result.get_name() == "link1"


def test_class_add_link_to_part_via_port_unwraps_and_wraps() -> None:
    fake = make_fake_element("Class")
    to_part = make_fake_element("Instance", properties={"name": "p1"})
    part_port = make_fake_element("Instance", properties={"name": "pp"})
    class_port = make_fake_element("Instance", properties={"name": "cp"})
    assoc = make_fake_element("Relation", properties={"name": "r1"})
    link = make_fake_element("Link", properties={"name": "link1"})
    fake.addLinkToPartViaPort.return_value = link
    klass = IRPClass(fake)

    result = klass.add_link_to_part_via_port(
        cast(IRPModelElement, AbstractRPModelElement.wrap(to_part)),
        cast(IRPModelElement, AbstractRPModelElement.wrap(part_port)),
        cast(IRPModelElement, AbstractRPModelElement.wrap(class_port)),
        cast(IRPModelElement, AbstractRPModelElement.wrap(assoc)),
    )

    fake.addLinkToPartViaPort.assert_called_once_with(to_part, part_port, class_port, assoc)
    assert result.get_name() == "link1"


def test_class_add_reception_wraps_result() -> None:
    fake = make_fake_element("Class")
    reception = make_fake_element("EventReception", properties={"name": "onSignal"})
    fake.addReception.return_value = reception
    klass = IRPClass(fake)

    result = klass.add_reception("onSignal")

    fake.addReception.assert_called_once_with("onSignal")
    assert result.get_name() == "onSignal"


def test_class_add_triggered_operation_wraps_result() -> None:
    fake = make_fake_element("Class")
    op = make_fake_element("Operation", properties={"name": "handle"})
    fake.addTriggeredOperation.return_value = op
    klass = IRPClass(fake)

    result = klass.add_triggered_operation("handle")

    fake.addTriggeredOperation.assert_called_once_with("handle")
    assert result.get_name() == "handle"


def test_class_add_type_wraps_result() -> None:
    fake = make_fake_element("Class")
    typ = make_fake_element("Type", properties={"name": "Color"})
    fake.addType.return_value = typ
    klass = IRPClass(fake)

    result = klass.add_type("Color")

    fake.addType.assert_called_once_with("Color")
    assert result.get_name() == "Color"


def test_class_delete_class_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    klass = IRPClass(fake)

    klass.delete_class("Inner")

    fake.deleteClass.assert_called_once_with("Inner")


def test_class_delete_constructor_unwraps_arg() -> None:
    fake = make_fake_element("Class")
    ctor = make_fake_element("Operation", properties={"name": "Widget"})
    klass = IRPClass(fake)

    wrapped_ctor = AbstractRPModelElement.wrap(ctor)
    klass.delete_constructor(cast(RPOperation, wrapped_ctor))

    fake.deleteConstructor.assert_called_once_with(ctor)


def test_class_delete_destructor_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    klass = IRPClass(fake)

    klass.delete_destructor()

    fake.deleteDestructor.assert_called_once_with()


def test_class_delete_event_reception_unwraps_arg() -> None:
    fake = make_fake_element("Class")
    reception = make_fake_element("EventReception", properties={"name": "onEvent"})
    klass = IRPClass(fake)

    wrapped_reception = AbstractRPModelElement.wrap(reception)
    klass.delete_event_reception(cast(RPEventReception, wrapped_reception))

    fake.deleteEventReception.assert_called_once_with(reception)


def test_class_delete_reception_unwraps_arg() -> None:
    fake = make_fake_element("Class")
    reception = make_fake_element("EventReception", properties={"name": "onSignal"})
    klass = IRPClass(fake)

    wrapped_reception = AbstractRPModelElement.wrap(reception)
    klass.delete_reception(cast(RPEventReception, wrapped_reception))

    fake.deleteReception.assert_called_once_with(reception)


def test_class_delete_superclass_unwraps_arg() -> None:
    fake = make_fake_element("Class")
    base = make_fake_element("Class", properties={"name": "Base"})
    klass = IRPClass(fake)

    klass.delete_superclass(IRPClass(base))

    fake.deleteSuperclass.assert_called_once_with(base)


def test_class_delete_type_delegates_to_com() -> None:
    fake = make_fake_element("Class")
    klass = IRPClass(fake)

    klass.delete_type("Color")

    fake.deleteType.assert_called_once_with("Color")


def test_class_is_active_property_reads_pywin32_property() -> None:
    fake = MagicMock(spec=["isActive"])
    fake.isActive = 1
    klass = IRPClass(fake)

    assert klass.is_active == 1


def test_class_is_behavior_overriden_property_reads_pywin32_property() -> None:
    fake = MagicMock(spec=["isBehaviorOverriden"])
    fake.isBehaviorOverriden = 0
    klass = IRPClass(fake)

    assert klass.is_behavior_overriden == 0


def test_class_is_composite_property_reads_pywin32_property() -> None:
    fake = MagicMock(spec=["isComposite"])
    fake.isComposite = 1
    klass = IRPClass(fake)

    assert klass.is_composite == 1


def test_class_get_is_final_calls_pywin32_method() -> None:
    fake = MagicMock(spec=["getIsFinal"])
    fake.getIsFinal.return_value = 0
    klass = IRPClass(fake)

    assert klass.get_is_final() == 0
    fake.getIsFinal.assert_called_once_with()


def test_class_is_reactive_property_reads_pywin32_property() -> None:
    fake = MagicMock(spec=["isReactive"])
    fake.isReactive = 1
    klass = IRPClass(fake)

    assert klass.is_reactive == 1


def test_class_is_abstract_setter_raises_not_implemented() -> None:
    fake = make_fake_element("Class")
    klass = IRPClass(fake)

    with pytest.raises(NotImplementedError):
        klass.is_abstract = True

    fake.setIsAbstract.assert_not_called()


def test_class_is_active_setter_writes_pywin32_property() -> None:
    fake = make_fake_element("Class")
    klass = IRPClass(fake)

    klass.is_active = 0

    assert fake.isActive == 0


def test_class_is_behavior_overriden_setter_writes_pywin32_property() -> None:
    fake = make_fake_element("Class")
    klass = IRPClass(fake)

    klass.is_behavior_overriden = 1

    assert fake.isBehaviorOverriden == 1


def test_class_set_is_final_calls_pywin32_method() -> None:
    fake = MagicMock(spec=["setIsFinal"])
    klass = IRPClass(fake)

    klass.set_is_final(1)

    fake.setIsFinal.assert_called_once_with(1)


def test_class_does_not_expose_unavailable_server_diagram_update() -> None:
    assert not hasattr(IRPClass, "update_contained_diagrams_on_server")


def test_class_module_has_no_legacy_dual_binding_helpers() -> None:
    source = Path(irp_class_module.__file__).read_text(encoding="utf-8")

    assert "_get_method_or_property" not in source
    assert "_set_method_or_property" not in source


def test_class_canonical_package_exports_same_class() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass as PackageRPClass

    assert PackageRPClass is IRPClass


def test_class_canonical_module_registers_wrapper() -> None:
    from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPClass as CanonicalRPClass

    fake = make_fake_element("Class")

    assert isinstance(AbstractRPModelElement.wrap(fake), CanonicalRPClass)
