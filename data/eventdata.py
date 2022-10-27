import json
from datetime import time
from time import strftime, gmtime


class EventData:
    def __init__(self):
        self.data = []

    def loadData(self):
        try:
            with open("data/eventData.json", encoding='utf-8') as f:
                self.data = json.load(f)
                print(self.data)
        except FileNotFoundError:
            print("Creating the file for the first time")

    def writeMouseEvent(self):
        curr_time: str = strftime("%H:%M:%S", gmtime())
        self.data.append({
            "type": "MouseEvent",
            "time": curr_time
        })

        with open('data/eventData.json', 'w', encoding='utf-8') as f:
            data = json.dumps(self.data, ensure_ascii=False, indent=4)
            f.write(data)


