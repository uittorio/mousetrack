from datetime import datetime
from typing import Literal, Union

import pytest as pytest

from src.domain.event_messages.event_messages import EventMessages
from src.domain.keyboard_event import KeyboardEvent
from src.domain.mouse_event import MouseEvent
from tests.fake.fake_event_repository import FakeEventRepository


@pytest.fixture
def fake_event_repository():
    return FakeEventRepository()


@pytest.fixture
def event_messages(fake_event_repository):
    return EventMessages(fake_event_repository)


def mouse_event(event_type: Union[Literal["click"], Literal["scroll"], Literal["move"]], iso_date: str) -> MouseEvent:
    iso_date = datetime.fromisoformat(iso_date)
    return {
        'time': datetime.timestamp(iso_date),
        'type': event_type
    }


def keyboard_event(event_type: Union[Literal["keypressed"]], iso_date: str) -> KeyboardEvent:
    iso_date = datetime.fromisoformat(iso_date)
    return {
        'time': datetime.timestamp(iso_date),
        'type': event_type
    }


def test_adding_one_click_message(fake_event_repository, event_messages):
    event = mouse_event("click", "2022-10-30T06:25:11")
    event_messages.add_mouse_event(event)
    assert fake_event_repository.get_mouse_click_events() == [event]


def test_adding_two_click_messages(fake_event_repository, event_messages):
    event = mouse_event("click", "2022-10-30T06:25:11")
    event_messages.add_mouse_event(event)
    event_messages.add_mouse_event(event)
    assert fake_event_repository.get_mouse_click_events() == [event, event]


def test_adding_one_move_message(fake_event_repository, event_messages):
    event = mouse_event("move", "2022-10-30T06:25:11")
    event_messages.add_mouse_event(event)
    assert fake_event_repository.get_mouse_move_events() == [event]


def test_adding_two_move_message(fake_event_repository, event_messages):
    first_event = mouse_event("move", "2022-10-30T06:25:11")
    second_event = mouse_event("move", "2022-10-30T06:25:12")
    event_messages.add_mouse_event(first_event)
    event_messages.add_mouse_event(second_event)
    assert fake_event_repository.get_mouse_move_events() == [first_event]


def test_adding_a_move_message_after_3_seconds_of_the_first_none(fake_event_repository, event_messages):
    first_event = mouse_event("move", "2022-10-30T06:25:11")
    second_event = mouse_event("move", "2022-10-30T06:25:15")

    event_messages.add_mouse_event(first_event)
    event_messages.add_mouse_event(second_event)
    assert fake_event_repository.get_mouse_move_events() == [first_event, second_event]


def test_adding_a_move_message_after_2_seconds_of_the_first_two(fake_event_repository, event_messages):
    first_event = mouse_event("move", "2022-10-30T06:25:11")
    second_event = mouse_event("move", "2022-10-30T06:25:12")
    third_event = mouse_event("move", "2022-10-30T06:25:14")
    event_messages.add_mouse_event(first_event)
    event_messages.add_mouse_event(second_event)
    event_messages.add_mouse_event(third_event)
    assert fake_event_repository.get_mouse_move_events() == [first_event]


def test_adding_a_move_message_after_4_seconds_of_the_first_one_on_the_next_minute(fake_event_repository,
                                                                                   event_messages):
    first_event = mouse_event("move", "2022-10-30T06:25:59")
    second_event = mouse_event("move", "2022-10-30T06:26:04")

    event_messages.add_mouse_event(first_event)
    event_messages.add_mouse_event(second_event)
    assert fake_event_repository.get_mouse_move_events() == [first_event, second_event]


def test_adding_one_keyboard_message(fake_event_repository, event_messages):
    event = keyboard_event("keypressed", "2022-10-30T06:25:11")
    event_messages.add_keyboard_event(event)
    assert fake_event_repository.get_keyboard_events() == [event]
