import threading
from time import sleep

from PyQt6.QtCore import QObject, pyqtSignal

from src.domain.mouse_event import MouseEvent


class EventUpdater(QObject):
    updated = pyqtSignal(list, arguments=['updater'])

    def __init__(self, get_mouse_events):
        self.get_mouse_events = get_mouse_events
        QObject.__init__(self)

    def updater(self, events: list[MouseEvent]):
        self.updated.emit(events)

    def start(self):
        t_thread = threading.Thread(target=self.__start)
        t_thread.daemon = True
        t_thread.start()

    def __start(self):
        while True:
            try:
                events: list[MouseEvent] = self.get_mouse_events()
                self.updater(events)
            except FileNotFoundError:
                print("problem finding the file")
            sleep(4)
