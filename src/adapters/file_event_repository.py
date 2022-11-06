import json
import os
import sys
from typing import Union, TypeVar

from src.domain.keyboard_event import KeyboardEvent
from src.domain.mouse_event import MouseEvent
from src.port.event_repository import EventRepository


def safe_open_w(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    return open(path, 'w+', encoding='utf-8')


T = TypeVar("T")


def filter_by(events: list[T], event_type: str):
    return list(filter(lambda event: event.get('type') == event_type, events))


def get_file_path():
    file_name = "events.json"
    if hasattr(sys, "_MEIPASS"):
        abs_home = os.path.abspath(os.path.expanduser("~"))
        file_path = os.path.join(abs_home, f".mouse-track", "file_storage")
    else:
        file_path = 'file_storage'
    return os.path.join(file_path, file_name)


class FileEventRepository(EventRepository):
    data: list[MouseEvent] = []

    def __init__(self):
        self.file_storage = get_file_path()
        self.__load_data()

    def add_mouse_event(self, event: MouseEvent):
        self.data.append(event)
        with safe_open_w(self.file_storage) as f:
            data = json.dumps(self.data, ensure_ascii=False, indent=4)
            f.write(data)

    def add_keyboard_event(self, event: KeyboardEvent):
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

    def get_keyboard_events(self) -> list[KeyboardEvent]:
        return filter_by(self.__get(), 'keypressed')

    def __load_data(self):
        self.data = self.__get()

    def __get(self) -> list[Union[MouseEvent, KeyboardEvent]]:
        try:
            with open(self.file_storage, encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
