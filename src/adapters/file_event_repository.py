import json
import os

from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


def safe_open_w(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w+', encoding='utf-8')


def filter_by(events: list[MouseEvent], event_type: str):
    return list(filter(lambda event: event.get('type') == event_type, events))


class FileEventRepository(EventRepository):
    file_storage = "file_storage/events.json"
    data: list[MouseEvent] = []

    def __init__(self):
        self.__load_data()

    def add_mouse_event(self, event: MouseEvent):
        self.data.append(event)
        with safe_open_w(self.file_storage) as f:
            data = json.dumps(self.data, ensure_ascii=False, indent=4)
            f.write(data)

    def get_mouse_click_events(self) -> list[MouseEvent]:
        return filter_by(self.__get(), 'click')

    def get_mouse_scroll_events(self) -> list[MouseEvent]:
        return filter_by(self.__get(), 'scroll')

    def get_mouse_move_events(self) -> list[MouseEvent]:
        return filter_by(self.__get(), 'move')

    def __load_data(self):
        self.data = self.__get()

    def __get(self) -> list[MouseEvent]:
        try:
            with open(self.file_storage, encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
