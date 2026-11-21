"""Tests for rhapsody_cli.models.elements.values.model_values classes."""

from rhapsody_cli.models.core import AbstractRPModelElement, IRPCollection, IRPModelElement
from rhapsody_cli.models.elements.values import (
    RPInstanceSlot,
    RPInstanceSpecification,
    RPInstanceValue,
    RPLiteralSpecification,
    RPValueSpecification,
)
from tests.unit.models.fakes import make_fake_collection, make_fake_element


class TestRPInstanceSlot:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("InstanceSlot", properties={"name": "Slot1"})
        slot = RPInstanceSlot(fake)
        assert isinstance(slot, IRPModelElement)
        assert slot.get_name() == "Slot1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("InstanceSlot", properties={"name": "Slot1"})
        wrapped = AbstractRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPInstanceSlot)

    def test_add_element_value_delegates_and_wraps(self) -> None:
        fake = make_fake_element("InstanceSlot")
        val = make_fake_element("Class", properties={"name": "Cls1"})
        result = make_fake_element("InstanceValue", properties={"name": "IV1"})
        fake.addElementValue.return_value = result
        slot = RPInstanceSlot(fake)
        wrapped = slot.add_element_value(IRPModelElement(val))
        assert wrapped.get_name() == "IV1"
        fake.addElementValue.assert_called_once_with(val)

    def test_add_string_value_delegates_and_wraps(self) -> None:
        fake = make_fake_element("InstanceSlot")
        result = make_fake_element("LiteralSpecification", properties={"name": "LS1"})
        fake.addStringValue.return_value = result
        slot = RPInstanceSlot(fake)
        wrapped = slot.add_string_value("hello")
        assert wrapped.get_name() == "LS1"
        fake.addStringValue.assert_called_once_with("hello")

    def test_get_slot_property_wraps_result(self) -> None:
        fake = make_fake_element("InstanceSlot")
        prop = make_fake_element("Attribute", properties={"name": "attr1"})
        fake.getSlotProperty.return_value = prop
        slot = RPInstanceSlot(fake)
        wrapped = slot.get_slot_property()
        assert wrapped is not None and wrapped.get_name() == "attr1"

    def test_get_values_returns_collection(self) -> None:
        fake = make_fake_element("InstanceSlot")
        v = make_fake_element("InstanceValue", properties={"name": "v1"})
        fake.getValues.return_value = make_fake_collection([v])
        slot = RPInstanceSlot(fake)
        result = slot.get_values()
        assert isinstance(result, IRPCollection)

    def test_set_slot_property_delegates(self) -> None:
        fake = make_fake_element("InstanceSlot")
        prop = make_fake_element("Attribute", properties={"name": "attr1"})
        fake.setSlotProperty.return_value = None
        slot = RPInstanceSlot(fake)
        slot.set_slot_property(IRPModelElement(prop))
        fake.setSlotProperty.assert_called_once_with(prop)


class TestRPInstanceSpecification:
    def test_is_model_element(self) -> None:
        fake = make_fake_element("InstanceSpecification", properties={"name": "IS1"})
        spec = RPInstanceSpecification(fake)
        assert isinstance(spec, IRPModelElement)
        assert spec.get_name() == "IS1"

    def test_is_registered(self) -> None:
        fake = make_fake_element("InstanceSpecification", properties={"name": "IS1"})
        wrapped = AbstractRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPInstanceSpecification)

    def test_add_instance_slot_delegates_and_wraps(self) -> None:
        fake = make_fake_element("InstanceSpecification")
        prop = make_fake_element("Attribute", properties={"name": "attr1"})
        slot = make_fake_element("InstanceSlot", properties={"name": "s1"})
        fake.addInstanceSlot.return_value = slot
        spec = RPInstanceSpecification(fake)
        wrapped = spec.add_instance_slot("s1", IRPModelElement(prop))
        assert wrapped.get_name() == "s1"
        fake.addInstanceSlot.assert_called_once_with("s1", prop)

    def test_get_classifier_wraps_result(self) -> None:
        fake = make_fake_element("InstanceSpecification")
        clf = make_fake_element("Class", properties={"name": "C1"})
        fake.getClassifier.return_value = clf
        spec = RPInstanceSpecification(fake)
        wrapped = spec.get_classifier()
        assert wrapped.get_name() == "C1"

    def test_get_instance_slots_returns_collection(self) -> None:
        fake = make_fake_element("InstanceSpecification")
        s = make_fake_element("InstanceSlot", properties={"name": "s1"})
        fake.getInstanceSlots.return_value = make_fake_collection([s])
        spec = RPInstanceSpecification(fake)
        result = spec.get_instance_slots()
        assert isinstance(result, IRPCollection)

    def test_is_root_instance_specification_returns_int(self) -> None:
        fake = make_fake_element("InstanceSpecification", isRootInstanceSpecification=True)
        spec = RPInstanceSpecification(fake)
        assert spec.is_root_instance_specification() == 1

    def test_populate_slots_delegates(self) -> None:
        fake = make_fake_element("InstanceSpecification")
        fake.populateSlots.return_value = None
        spec = RPInstanceSpecification(fake)
        spec.populate_slots()
        fake.populateSlots.assert_called_once_with()

    def test_set_classifier_delegates(self) -> None:
        from rhapsody_cli.models.elements.classifiers import RPClassifier

        fake = make_fake_element("InstanceSpecification")
        clf = make_fake_element("Class", properties={"name": "C1"})
        fake.setClassifier.return_value = None
        spec = RPInstanceSpecification(fake)
        spec.set_classifier(RPClassifier(clf))
        fake.setClassifier.assert_called_once_with(clf)


class TestRPInstanceValue:
    def test_is_registered(self) -> None:
        fake = make_fake_element("InstanceValue", properties={"name": "IV1"})
        wrapped = AbstractRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPInstanceValue)

    def test_get_value_wraps_result(self) -> None:
        fake = make_fake_element("InstanceValue")
        val = make_fake_element("Class", properties={"name": "C1"})
        fake.getValue.return_value = val
        iv = RPInstanceValue(fake)
        wrapped = iv.get_value()
        assert wrapped is not None and wrapped.get_name() == "C1"

    def test_set_value_delegates(self) -> None:
        fake = make_fake_element("InstanceValue")
        val = make_fake_element("Class", properties={"name": "C1"})
        fake.setValue.return_value = None
        iv = RPInstanceValue(fake)
        iv.set_value(IRPModelElement(val))
        fake.setValue.assert_called_once_with(val)


class TestRPLiteralSpecification:
    def test_is_registered(self) -> None:
        fake = make_fake_element("LiteralSpecification", properties={"name": "LS1"})
        wrapped = AbstractRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPLiteralSpecification)

    def test_get_value_returns_string(self) -> None:
        fake = make_fake_element("LiteralSpecification", getValue="hello")
        ls = RPLiteralSpecification(fake)
        assert ls.get_value() == "hello"

    def test_set_value_delegates(self) -> None:
        fake = make_fake_element("LiteralSpecification")
        ls = RPLiteralSpecification(fake)
        ls.set_value("hello")
        fake.setValue.assert_called_once_with("hello")


class TestRPValueSpecification:
    def test_is_registered(self) -> None:
        fake = make_fake_element("ValueSpecification", properties={"name": "VS1"})
        wrapped = AbstractRPModelElement.wrap(fake)
        assert isinstance(wrapped, RPValueSpecification)

    def test_can_be_instantiated(self) -> None:
        fake = make_fake_element("ValueSpecification", properties={"name": "VS1"})
        vs = RPValueSpecification(fake)
        assert vs.get_name() == "VS1"
