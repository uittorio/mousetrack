import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

from src.UI.read_events import ReadEvents
from src.port.event_repository import EventRepository


class UI:
    def __init__(self, event_repository: EventRepository):
        QQuickWindow.setSceneGraphBackend('software')
        self.event_repository = event_repository
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

    def draw(self):
        self.engine.quit.connect(self.app.quit)
        self.engine.load('./UI/main.qml')
        read_events = ReadEvents(self.event_repository)
        self.engine.rootObjects()[0].setProperty('clickEvents', read_events)
        read_events.read()
        sys.exit(self.app.exec())
