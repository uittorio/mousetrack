from datetime import datetime
from typing import Literal, Union

import pytest as pytest

from src.application.keyboard_percentage.keyboard_percentage import KeyboardPercentage
from src.domain.event_messages.event_messages import EventMessages
from src.domain.keyboard_event import KeyboardEvent
from src.domain.mouse_event import MouseEvent
from tests.fake.fake_event_repository import FakeEventRepository


@pytest.fixture
def fake_event_repository():
    return FakeEventRepository()


@pytest.fixture
def keyboard_events(fake_event_repository):
    return KeyboardPercentage(fake_event_repository)


def test_return_0_when_no_events(fake_event_repository, keyboard_events):
    assert keyboard_events.get() == 0


def create_event(event_type: str) -> Union[KeyboardEvent, MouseEvent]:
    iso_date = datetime.fromisoformat("2022-10-30T06:25:11")
    return {
        'time': datetime.timestamp(iso_date),
        'type': event_type
    }


def test_return_1_when_there_are_only_keyboard_events(fake_event_repository, keyboard_events):
    event = create_event("keypressed")
    fake_event_repository.add_keyboard_event(event)
    assert keyboard_events.get() == 1


def test_return_05_when_theres_is_one_mouse_and_one_keyboard(fake_event_repository, keyboard_events):
    event = create_event("keypressed")
    mouse_event = create_event("click")
    fake_event_repository.add_keyboard_event(event)
    fake_event_repository.add_mouse_event(mouse_event)
    assert keyboard_events.get() == 0.5
