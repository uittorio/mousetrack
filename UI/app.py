import sys
import threading
from time import strftime, gmtime, sleep

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

from UI.read_events import ReadEvents


def draw_app():
    QQuickWindow.setSceneGraphBackend('software')
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./UI/main.qml')
    back_end = ReadEvents()
    engine.rootObjects()[0].setProperty('backend', back_end)
    back_end.boot_up()
    sys.exit(app.exec())
