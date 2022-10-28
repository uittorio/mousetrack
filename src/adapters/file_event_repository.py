import json
from time import strftime, gmtime

from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


class FileEventRepository(EventRepository):
    file_storage = "file_storage/events.json"
    data: list[MouseEvent] = []
    test: MouseEvent

    def __init__(self):
        self.__load_data()

    def __load_data(self):
        self.data = self.get()

    def write_mouse_event(self):
        curr_time: str = strftime("%d/%m/%Y-%H:%M:%S", gmtime())
        self.data.append({
            "type": "click",
            "time": curr_time
        })

        with open(self.file_storage, 'w', encoding='utf-8') as f:
            data = json.dumps(self.data, ensure_ascii=False, indent=4)
            f.write(data)

    def get(self) -> list[MouseEvent]:
        try:
            with open(self.file_storage, encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
