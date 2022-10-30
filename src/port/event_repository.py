from src.domain.mouse_event import MouseEvent
from abc import ABC, abstractmethod


class EventRepository(ABC):
    @abstractmethod
    def add_mouse_event(self, event: MouseEvent): pass

    @abstractmethod
    def get_mouse_click_events(self) -> list[MouseEvent]: pass

    @abstractmethod
    def get_mouse_scroll_events(self) -> list[MouseEvent]: pass

    @abstractmethod
    def get_mouse_move_events(self) -> list[MouseEvent]: pass

