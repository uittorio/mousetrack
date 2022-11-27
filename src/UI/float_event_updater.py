import threading
from time import sleep

from PyQt6.QtCore import QObject, pyqtSignal


class FloatEventUpdater(QObject):
    updated = pyqtSignal(float)

    def __init__(self, get_data):
        self.get_data = get_data
        QObject.__init__(self)

    def updater(self, data: float):
        self.updated.emit(data)

    def start(self):
        t_thread = threading.Thread(target=self.__start)
        t_thread.daemon = True
        t_thread.start()

    def __start(self):
        while True:
            data: float = self.get_data()
            self.updater(data)
            sleep(4)
