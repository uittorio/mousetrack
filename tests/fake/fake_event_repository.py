from src.domain.keyboard_event import KeyboardEvent
from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


class FakeEventRepository(EventRepository):
    def __init__(self):
        self.mouse_events = []
        self.keyboard_events = []

    def get_mouse_scroll_events(self) -> list[MouseEvent]:
        return self.mouse_events

    def get_keyboard_events(self) -> list[MouseEvent]:
        return self.keyboard_events

    def get_mouse_move_events(self) -> list[MouseEvent]:
        return self.mouse_events

    def get_mouse_click_events(self) -> list[MouseEvent]:
        return self.mouse_events

    def add_mouse_event(self, event: MouseEvent):
        self.mouse_events.append(event)

    def add_keyboard_event(self, event: KeyboardEvent):
        self.keyboard_events.append(event)
