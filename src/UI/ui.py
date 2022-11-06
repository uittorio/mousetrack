import os
import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

from src.UI.event_updater import EventUpdater
from src.port.event_repository import EventRepository


class UI:
    def __init__(self, event_repository: EventRepository):
        QQuickWindow.setSceneGraphBackend('software')
        self.event_repository = event_repository
        self.app = QGuiApplication(sys.argv)
        self.engine = QQmlApplicationEngine()

    def draw(self):
        self.engine.quit.connect(self.app.quit)
        absolute_path = os.path.dirname(__file__)

        self.engine.load(absolute_path + '/components/main.qml')
        click_events_updater = EventUpdater(self.event_repository.get_mouse_click_events)
        scroll_events_updater = EventUpdater(self.event_repository.get_mouse_scroll_events)
        move_event_updater = EventUpdater(self.event_repository.get_mouse_move_events)
        applicationObject = self.engine.rootObjects()[0]
        applicationObject.setProperty('clickEventsUpdater', click_events_updater)
        applicationObject.setProperty('scrollEventsUpdater', scroll_events_updater)
        applicationObject.setProperty('moveEventsUpdater', move_event_updater)
        click_events_updater.start()
        scroll_events_updater.start()
        move_event_updater.start()
        sys.exit(self.app.exec())
