import threading

from UI.app import draw_app
from input_events.input_events import mouse_event_listener


def main():
    t1 = threading.Thread(target=mouse_event_listener, args=())
    t1.start()
    draw_app()


main()
