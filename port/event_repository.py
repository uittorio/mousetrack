from domain.event import Event
from abc import ABC, abstractmethod


class EventRepository(ABC):
    @abstractmethod
    def write_mouse_event(self): pass

    @abstractmethod
    def get(self) -> list[Event]: pass

