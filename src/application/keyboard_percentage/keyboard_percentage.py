import math

from src.port.event_repository import EventRepository


class KeyboardPercentage:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def get(self):
        mouse_click = len(self.event_repository.get_mouse_click_events())
        move = len(self.event_repository.get_mouse_move_events())
        scroll = len(self.event_repository.get_mouse_scroll_events())
        keyboard = len(self.event_repository.get_keyboard_events())
        total = mouse_click + move + scroll + keyboard

        # total = mouse_click + keyboard

        if total == 0:
            return 0

        return ((keyboard / total) * 100) / 100
