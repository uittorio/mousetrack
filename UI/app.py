import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

from UI.read_events import ReadEvents
from port.event_repository import EventRepository


def draw_app(event_repository: EventRepository):
    QQuickWindow.setSceneGraphBackend('software')
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./UI/main.qml')
    read_events = ReadEvents(event_repository)
    engine.rootObjects()[0].setProperty('readEvents', read_events)
    read_events.boot_up()
    sys.exit(app.exec())
