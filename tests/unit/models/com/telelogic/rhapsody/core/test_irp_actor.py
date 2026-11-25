"""Tests for rhapsody_cli.elements.actor.IRPActor."""

from typing import cast

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core import IRPActor, IRPEvent
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from tests.unit.models.fakes import make_fake_element


def test_actor_is_a_classifier() -> None:
    fake = make_fake_element("Actor", properties={"name": "Driver"})
    actor = IRPActor(fake)

    assert isinstance(actor, IRPClassifier)
    assert actor.name == "Driver"


def test_actor_add_event_reception_with_event_wraps_result() -> None:
    fake = make_fake_element("Actor")
    event = make_fake_element("Event", properties={"name": "Start"})
    reception = make_fake_element("EventReception", properties={"name": "onStart"})
    fake.addEventReceptionWithEvent.return_value = reception
    actor = IRPActor(fake)

    with pytest.raises(NotImplementedError):
        actor.add_event_reception_with_event("onStart", cast(IRPEvent, IRPModelElement(event)))

    fake.addEventReceptionWithEvent.assert_not_called()


def test_actor_is_behavior_overridden_property_reads_and_writes_com_property() -> None:
    fake = make_fake_element("Actor", properties={"isBehaviorOverriden": 0})
    actor = IRPActor(fake)

    assert actor.is_behavior_overriden is False

    actor.is_behavior_overriden = True

    assert fake.isBehaviorOverriden == 1
    assert actor.is_behavior_overriden is True

    actor.is_behavior_overriden = False

    assert fake.isBehaviorOverriden == 0
    assert actor.is_behavior_overriden is False


def test_actor_update_contained_diagrams_on_server_is_documented_unavailable() -> None:
    fake = make_fake_element("Actor")
    actor = IRPActor(fake)

    with pytest.raises(NotImplementedError):
        actor.update_contained_diagrams_on_server(0)

    fake.updateContainedDiagramsOnServer.assert_not_called()


def test_actor_is_registered_for_meta_class_actor() -> None:
    fake = make_fake_element("Actor", properties={"name": "Driver"})

    wrapped = IRPModelElement.wrap(fake)

    assert isinstance(wrapped, IRPActor)
