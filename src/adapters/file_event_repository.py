import json
import os

from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


def safe_open_w(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w+', encoding='utf-8')


class FileEventRepository(EventRepository):
    file_storage = "file_storage/events.json"
    data: list[MouseEvent] = []
    test: MouseEvent

    def __init__(self):
        self.__load_data()

    def __load_data(self):
        self.data = self.get()

    def add_mouse_event(self, event: MouseEvent):
        self.data.append(event)
        with safe_open_w(self.file_storage) as f:
            data = json.dumps(self.data, ensure_ascii=False, indent=4)
            f.write(data)

    def get(self) -> list[MouseEvent]:
        try:
            with open(self.file_storage, encoding='utf-8') as f:
                print("mmmm")
                return json.load(f)
        except FileNotFoundError:
            return []
