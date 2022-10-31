from datetime import datetime

from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


class EventMessages:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository
        self.added_events = []

    def add_mouse_event(self, event: MouseEvent):
        event_type = event.get('type')
        if event_type == "click":
            self.event_repository.add_mouse_event(event)

        if event_type == "scroll":
            self.event_repository.add_mouse_event(event)

        if event_type == "move":
            move_events = self.__search_move_elements()

            if len(move_events) == 0:
                self.event_repository.add_mouse_event(event)
                self.added_events.append(event)
            else:
                first_element = move_events[0]
                first_element_time = first_element.get('time')

                time = event.get('time')
                date = datetime.strptime(time, "%d/%m/%Y-%H:%M:%S")

                first_element_date = datetime.strptime(first_element_time, "%d/%m/%Y-%H:%M:%S")

                if date.second > first_element_date.second + 3:
                    self.event_repository.add_mouse_event(event)
                    self.added_events.append(event)
                    self.added_events.clear()

    def __search_move_elements(self):
        return list(filter(lambda event: event.get('type') == "move", self.added_events))
