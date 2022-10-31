from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


class FakeEventRepository(EventRepository):
    def __init__(self):
        self.events = []

    def get_mouse_scroll_events(self) -> list[MouseEvent]:
        pass

    def get_mouse_move_events(self) -> list[MouseEvent]:
        pass

    def get_mouse_click_events(self) -> list[MouseEvent]:
        return self.events

    def add_mouse_event(self, event: MouseEvent):
        self.events.append(event)
        pass
