import threading
from time import strftime, gmtime

from UI.app import draw_app
from input_events.input_events import mouse_event_listener


def main():
    # t1 = threading.Thread(target=mouse_event_listener, args=())
    # t1.start()
    curr_time = strftime("%H:%M:%S", gmtime())

    draw_app(curr_time)


main()
