import json
import threading
from time import sleep

from PyQt6.QtCore import QObject, pyqtSignal

from domain.mouse_event import MouseEvent
from port.event_repository import EventRepository


class ReadEvents(QObject):
    updated = pyqtSignal(list, arguments=['updater'])

    def __init__(self, event_data_repository: EventRepository):
        self.event_data_repository = event_data_repository
        QObject.__init__(self)

    def updater(self, events: list[MouseEvent]):
        self.updated.emit(events)

    def read(self):
        t_thread = threading.Thread(target=self.__read)
        t_thread.daemon = True
        t_thread.start()

    def __read(self):
        while True:
            try:
                events: list[MouseEvent] = self.event_data_repository.get()
                self.updater(events)
            except FileNotFoundError:
                print("problem finding the file")
            sleep(4)
