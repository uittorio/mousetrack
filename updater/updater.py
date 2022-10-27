from time import strftime, gmtime

from PyQt6.QtCore import QObject, pyqtSignal


class TimerUpdater(QObject):
    updated = pyqtSignal(str, arguments=['updater'])

    def __init__(self):
        QObject.__init__(self)

    def updater(self, curr_time):
        self.updated.emit(curr_time)


    # t_thread = threading.Thread(target=self._bootUp)
    # t_thread.daemon = True
    # t_thread.start()

    def updateTime(self):
        curr_time = strftime("%H:%M:%S", gmtime())
        self.updater(curr_time)
