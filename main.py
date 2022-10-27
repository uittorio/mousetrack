import threading

from UI.app import draw_app
from data.event_data_repository import EventRepository
from input_events.input_events import mouse_event_listener


def main():
    event_repository = EventRepository()

    t1 = threading.Thread(target=mouse_event_listener, args=[event_repository], daemon=True)
    t1.start()

    draw_app(event_repository)


main()
