import sys

from PyQt6.QtCore import QObject
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

from UI.read_events import ReadEvents
from data.event_data_repository import EventRepository


def draw_app(event_repository: EventRepository):
    QQuickWindow.setSceneGraphBackend('software')
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./UI/main.qml')
    back_end = ReadEvents(event_repository)
    engine.rootObjects()[0].setProperty('backend', back_end)
    back_end.boot_up()
    sys.exit(app.exec())
