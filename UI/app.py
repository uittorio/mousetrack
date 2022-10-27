import sys
import threading
from time import strftime, gmtime, sleep

from PyQt6.QtCore import QObject, pyqtSignal
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow

from updater.updater import TimerUpdater


def draw_app(back_end: TimerUpdater):
    QQuickWindow.setSceneGraphBackend('software')
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('./UI/main.qml')
    engine.rootObjects()[0].setProperty('backend', back_end)
    sys.exit(app.exec())
