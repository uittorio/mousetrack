import pytest as pytest

from src.domain.event_messages.event_messages import EventMessages
from src.domain.mouse_event import MouseEvent
from tests.fake.fake_event_repository import FakeEventRepository


@pytest.fixture
def fake_event_repository():
    return FakeEventRepository()


@pytest.fixture
def event_messages(fake_event_repository):
    return EventMessages(fake_event_repository)


def test_adding_one_click_messages(fake_event_repository, event_messages):
    event: MouseEvent = {
        'time': '',
        'type': "click"
    }
    event_messages.add_mouse_event(event)
    assert fake_event_repository.get_mouse_click_events() == [event]


def test_adding_two_click_messages(fake_event_repository, event_messages):
    event: MouseEvent = {
        'time': '',
        'type': "click"
    }
    event_messages.add_mouse_event(event)
    event_messages.add_mouse_event(event)
    assert fake_event_repository.get_mouse_click_events() == [event, event]


def test_adding_one_move_message(fake_event_repository, event_messages):
    event: MouseEvent = {
        'time': '',
        'type': "move"
    }
    event_messages.add_mouse_event(event)
    assert fake_event_repository.get_mouse_click_events() == [event]


def test_adding_two_move_message(fake_event_repository, event_messages):
    first_event: MouseEvent = {
        'time': '30/10/2022-06:25:11',
        'type': "move"
    }

    second_event: MouseEvent = {
        'time': '30/10/2022-06:25:12',
        'type': "move"
    }
    event_messages.add_mouse_event(first_event)
    event_messages.add_mouse_event(second_event)
    assert fake_event_repository.get_mouse_click_events() == [first_event]


def test_adding_a_move_message_after_3_seconds_of_the_first_none(fake_event_repository, event_messages):
    first_event: MouseEvent = {
        'time': '30/10/2022-06:25:11',
        'type': "move"
    }

    second_event: MouseEvent = {
        'time': '30/10/2022-06:26:15',
        'type': "move"
    }
    event_messages.add_mouse_event(first_event)
    event_messages.add_mouse_event(second_event)
    assert fake_event_repository.get_mouse_click_events() == [first_event, second_event]


def test_adding_a_move_message_after_2_seconds_of_the_first_two(fake_event_repository, event_messages):
    first_event: MouseEvent = {
        'time': '30/10/2022-06:25:11',
        'type': "move"
    }

    second_event: MouseEvent = {
        'time': '30/10/2022-06:25:12',
        'type': "move"
    }

    third_event: MouseEvent = {
        'time': '30/10/2022-06:26:14',
        'type': "move"
    }
    event_messages.add_mouse_event(first_event)
    event_messages.add_mouse_event(second_event)
    event_messages.add_mouse_event(third_event)
    assert fake_event_repository.get_mouse_click_events() == [first_event]
