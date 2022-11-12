from src.domain.keyboard_event import KeyboardEvent
from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


class FakeEventRepository(EventRepository):
    def __init__(self):
        self.mouse_click_events = []
        self.mouse_move_events = []
        self.mouse_scroll_events = []
        self.keyboard_events = []

    def get_mouse_scroll_events(self) -> list[MouseEvent]:
        return self.mouse_scroll_events

    def get_keyboard_events(self) -> list[KeyboardEvent]:
        return self.keyboard_events

    def get_mouse_move_events(self) -> list[MouseEvent]:
        return self.mouse_move_events

    def get_mouse_click_events(self) -> list[MouseEvent]:
        return self.mouse_click_events

    def add_mouse_event(self, event: MouseEvent):
        if event.get("type") == "click":
            self.mouse_click_events.append(event)

        if event.get("type") == "move":
            self.mouse_move_events.append(event)

        if event.get("type") == "scroll":
            self.mouse_scroll_events.append(event)

    def add_keyboard_event(self, event: KeyboardEvent):
        self.keyboard_events.append(event)
