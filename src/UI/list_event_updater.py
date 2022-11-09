import threading
from time import sleep
from typing import TypeVar

from PyQt6.QtCore import QObject, pyqtSignal

Data = TypeVar("Data")


class ListEventUpdater(QObject):
    updated = pyqtSignal(list)

    def __init__(self, get_data):
        self.get_data = get_data
        QObject.__init__(self)

    def updater(self, data: list[Data]):
        self.updated.emit(data)

    def start(self):
        t_thread = threading.Thread(target=self.__start)
        t_thread.daemon = True
        t_thread.start()

    def __start(self):
        while True:
            data: Data = self.get_data()
            self.updater(data)
            sleep(4)
