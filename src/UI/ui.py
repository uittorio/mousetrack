import os
import sys

from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtWidgets import QApplication

from src.UI.float_event_updater import FloatEventUpdater
from src.UI.list_event_updater import ListEventUpdater
from src.application.keyboard_percentage.keyboard_percentage import KeyboardPercentage
from src.port.event_repository import EventRepository

class UI:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository
        self.app = QApplication(sys.argv)
        self.engine = QQmlApplicationEngine()
        self.keyboard_events = KeyboardPercentage(self.event_repository)

    def draw(self):
        self.engine.quit.connect(self.app.quit)
        absolute_path = os.path.dirname(__file__)

        self.engine.load(absolute_path + '/components/main.qml')
        click_events_updater = ListEventUpdater(self.event_repository.get_mouse_click_events)
        scroll_events_updater = ListEventUpdater(self.event_repository.get_mouse_scroll_events)
        move_event_updater = ListEventUpdater(self.event_repository.get_mouse_move_events)
        keyboard_event_updater = ListEventUpdater(self.event_repository.get_keyboard_events)
        keyboard_events_updater = FloatEventUpdater(self.keyboard_events.get)
        applicationObject = self.engine.rootObjects()[0]
        applicationObject.setProperty('clickEventsUpdater', click_events_updater)
        applicationObject.setProperty('scrollEventsUpdater', scroll_events_updater)
        applicationObject.setProperty('moveEventsUpdater', move_event_updater)
        applicationObject.setProperty('keyboardEventsUpdater', keyboard_event_updater)
        applicationObject.setProperty('percentageKeyboardEvents', keyboard_events_updater)
        click_events_updater.start()
        scroll_events_updater.start()
        move_event_updater.start()
        keyboard_event_updater.start()
        keyboard_events_updater.start()
        sys.exit(self.app.exec())
