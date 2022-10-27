import json
from time import strftime, gmtime

from port.event_repository import EventRepository


class FileEventRepository(EventRepository):
    file_storage = "file_storage/events.json"

    def __init__(self):
        self.data = []
        self.__load_data()

    def __load_data(self):
        data = self.get()
        self.data = data

    def write_mouse_event(self):
        curr_time: str = strftime("%d/%m/%Y-%H:%M:%S", gmtime())
        self.data.append({
            "type": "MouseEvent",
            "time": curr_time
        })

        with open(self.file_storage, 'w', encoding='utf-8') as f:
            data = json.dumps(self.data, ensure_ascii=False, indent=4)
            f.write(data)

    def get(self) -> list:
        try:
            with open(self.file_storage, encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
