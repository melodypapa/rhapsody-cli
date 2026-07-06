"""Tests for the public py_rhapsody package API surface."""

from __future__ import annotations

import py_rhapsody
from py_rhapsody._core import wrap
from tests.fakes import make_fake_element


def test_rhapsody_application_is_exported() -> None:
    assert py_rhapsody.RhapsodyApplication is not None


def test_exceptions_are_exported() -> None:
    assert py_rhapsody.RhapsodyConnectionError is not None
    assert py_rhapsody.RhapsodyRuntimeException is not None


def test_importing_package_registers_all_core_element_wrappers() -> None:
    for meta_class, expected_name in [
        ("Project", "RPProject"),
        ("Package", "RPPackage"),
        ("Class", "RPClass"),
        ("Attribute", "RPAttribute"),
        ("Operation", "RPOperation"),
        ("Actor", "RPActor"),
        ("UseCase", "RPUseCase"),
        ("Instance", "RPInstance"),
        ("Statechart", "RPStatechart"),
        ("Requirement", "RPRequirement"),
        ("ActivityDiagram", "RPDiagram"),
    ]:
        fake = make_fake_element(meta_class, getName="X")
        wrapped = wrap(fake)
        assert type(wrapped).__name__ == expected_name, meta_class
