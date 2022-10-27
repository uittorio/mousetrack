import json
import threading
from time import sleep

from PyQt6.QtCore import QObject, pyqtSignal

from port.event_repository import EventRepository


class ReadEvents(QObject):
    updated = pyqtSignal(list, arguments=['updater'])

    def __init__(self, event_data_repository: EventRepository):
        self.event_data_repository = event_data_repository
        QObject.__init__(self)

    def updater(self, events):
        self.updated.emit(events)

    def boot_up(self):
        t_thread = threading.Thread(target=self._boot_up)
        t_thread.daemon = True
        t_thread.start()

    def _boot_up(self):
        while True:
            try:
                events = self.event_data_repository.get()
                self.updater(events)
            except FileNotFoundError:
                print("problem finding the file")
            sleep(4)
