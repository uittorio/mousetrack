from src.domain.mouse_event import MouseEvent
from abc import ABC, abstractmethod


class EventRepository(ABC):
    @abstractmethod
    def add_mouse_event(self, event: MouseEvent): pass

    @abstractmethod
    def get(self) -> list[MouseEvent]: pass

