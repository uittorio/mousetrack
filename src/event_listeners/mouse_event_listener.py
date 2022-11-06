from datetime import datetime

from pynput import mouse

from src.domain.event_messages.event_messages import EventMessages


def get_current_time():
    return datetime.timestamp(datetime.now())


def on_move(event_messages: EventMessages):
    def _(x, y):
        event_messages.add_mouse_event({
            "type": "move",
            "time": get_current_time()
        })

    return _


def on_click(event_messages: EventMessages):
    def _(x, y, button, pressed):
        if pressed:
            event_messages.add_mouse_event({
                "type": "click",
                "time": get_current_time()
            })

    return _


def on_scroll(event_messages: EventMessages):
    def _(x, y, dx, dy):
        event_messages.add_mouse_event({
            "type": "scroll",
            "time": get_current_time()
        })

    return _


def mouse_event_listener(event_messages: EventMessages):
    mouse_listener = mouse.Listener(
        on_move=on_move(event_messages),
        on_click=on_click(event_messages),
        on_scroll=on_scroll(event_messages),
        daemon=True)
    mouse_listener.start()
