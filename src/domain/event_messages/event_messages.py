from datetime import datetime, timedelta

from src.domain.keyboard_event import KeyboardEvent
from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


def is_event_3_seconds_after_previous(event: MouseEvent, previous_event: MouseEvent):
    time = event.get('time')
    previous_event_time = previous_event.get('time')
    date = datetime.fromtimestamp(time)
    previous_event_date = datetime.fromtimestamp(previous_event_time)

    return date > (previous_event_date + timedelta(seconds=3))


class EventMessages:
    def __init__(self, event_repository: EventRepository):
        self.last_move_event = None
        self.last_scroll_event = None
        self.event_repository = event_repository

    def add_mouse_event(self, event: MouseEvent):
        event_type = event.get('type')
        if event_type == "click":
            self.event_repository.add_mouse_event(event)

        if event_type == "scroll":
            if self.last_scroll_event is None:
                self.event_repository.add_mouse_event(event)
                self.last_scroll_event = event
            else:
                if is_event_3_seconds_after_previous(event, self.last_scroll_event):
                    self.event_repository.add_mouse_event(event)
                    self.last_scroll_event = event

        if event_type == "move":
            if self.last_move_event is None:
                self.event_repository.add_mouse_event(event)
                self.last_move_event = event
            else:
                if is_event_3_seconds_after_previous(event, self.last_move_event):
                    self.event_repository.add_mouse_event(event)
                    self.last_move_event = event

    def add_keyboard_event(self, event: KeyboardEvent):
        event_type = event.get('type')
        if event_type == "keypressed":
            self.event_repository.add_keyboard_event(event)
