import json
from datetime import time
from time import strftime, gmtime


class EventRepository:
    def __init__(self):
        self.data = []
        self.__load_data()

    def __load_data(self):
        try:
            data = self.get()
            self.data = data
        except FileNotFoundError:
            print("Creating the file for the first time")

    def write_mouse_event(self):
        curr_time: str = strftime("%d/%m/%Y-%H:%M:%S", gmtime())
        self.data.append({
            "type": "MouseEvent",
            "time": curr_time
        })

        with open('data/eventData.json', 'w', encoding='utf-8') as f:
            data = json.dumps(self.data, ensure_ascii=False, indent=4)
            f.write(data)

    def get(self):
        with open("data/eventData.json", encoding='utf-8') as f:
            return json.load(f)


