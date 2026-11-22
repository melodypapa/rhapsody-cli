"""Tests for rhapsody_cli.elements.actor.RPActor."""

from typing import cast

import pytest

from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_classifier import IRPClassifier
from rhapsody_cli.models.com.telelogic.rhapsody.core.irp_model_element import IRPModelElement
from rhapsody_cli.models.core import AbstractRPModelElement
from rhapsody_cli.models.elements.classifiers import RPActor
from rhapsody_cli.models.elements.interactions import RPEvent
from tests.unit.models.fakes import make_fake_element


def test_actor_is_a_classifier() -> None:
    fake = make_fake_element("Actor", properties={"name": "Driver"})
    actor = RPActor(fake)

    assert isinstance(actor, IRPClassifier)
    assert actor.get_name() == "Driver"


def test_actor_add_event_reception_with_event_wraps_result() -> None:
    fake = make_fake_element("Actor")
    event = make_fake_element("Event", properties={"name": "Start"})
    reception = make_fake_element("EventReception", properties={"name": "onStart"})
    fake.addEventReceptionWithEvent.return_value = reception
    actor = RPActor(fake)

    with pytest.raises(NotImplementedError):
        actor.add_event_reception_with_event("onStart", cast(RPEvent, IRPModelElement(event)))


def test_actor_get_is_behavior_overridden_delegates_to_com() -> None:
    fake = make_fake_element("Actor", getIsBehaviorOverriden=1)
    actor = RPActor(fake)

    assert actor.get_is_behavior_overriden() is True


def test_actor_set_is_behavior_overridden_delegates_to_com() -> None:
    fake = make_fake_element("Actor")
    actor = RPActor(fake)

    actor.set_is_behavior_overriden(False)

    fake.setIsBehaviorOverriden.assert_called_once_with(0)


def test_actor_update_contained_diagrams_on_server_delegates_to_com() -> None:
    fake = make_fake_element("Actor")
    actor = RPActor(fake)

    actor.update_contained_diagrams_on_server()

    fake.updateContainedDiagramsOnServer.assert_called_once_with()


def test_actor_is_registered_for_meta_class_actor() -> None:
    fake = make_fake_element("Actor", properties={"name": "Driver"})

    wrapped = AbstractRPModelElement.wrap(fake)

    assert isinstance(wrapped, RPActor)
