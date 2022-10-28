from time import strftime, gmtime

from pynput import mouse

from src.port.event_repository import EventRepository


def get_current_time():
    return strftime("%d/%m/%Y-%H:%M:%S", gmtime())


def on_move(event_repository: EventRepository):
    def _on_move(x, y):
        event_repository.add_mouse_event({
            "type": "move",
            "time": get_current_time()
        })

    return _on_move


def on_click(event_repository: EventRepository):
    def _on_click(x, y, button, pressed):
        event_repository.add_mouse_event({
            "type": "click",
            "time": get_current_time()
        })

    return _on_click


def on_scroll(event_data: EventRepository):
    def _on_scroll(x, y, dx, dy):
        event_data.add_mouse_event({
            "type": "scroll",
            "time": get_current_time()
        })

    return _on_scroll


def mouse_event_listener(event_repository: EventRepository):
    mouse_listener = mouse.Listener(
        on_move=on_move(event_repository),
        on_click=on_click(event_repository),
        on_scroll=on_scroll(event_repository),
        daemon=True)
    mouse_listener.start()
