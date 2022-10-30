from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


class EventMessages:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def add_mouse_event(self, event: MouseEvent):
        event_type = event.get('type')
        if event_type == "click":
            self.event_repository.add_mouse_event(event)

        # I would like to only add an event every 2 seconds for scroll and move
        # I would like to add all the click events
        # I would like to write to disk one at the time to avoid too many writes at the same time, like in a queue.
        # I should first use the click events because they have less logic. Consumes all the events and write to disk every second
        # print(event)
