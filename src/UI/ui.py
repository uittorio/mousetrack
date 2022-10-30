import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

from src.UI.mouse_click_events_updater import MouseClickEventsUpdater
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
        click_events_updater = MouseClickEventsUpdater(self.event_repository)
        self.engine.rootObjects()[0].setProperty('clickEventsUpdater', click_events_updater)
        click_events_updater.read()
        sys.exit(self.app.exec())
