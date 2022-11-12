from datetime import datetime

from pynput import keyboard

from src.domain.event_messages.event_messages import EventMessages


def get_current_time():
    return datetime.timestamp(datetime.now())


def on_press(event_messages: EventMessages):
    def _(key):
        try:
            event_messages.add_keyboard_event({
                "type": "keypressed",
                "time": get_current_time()
            })
        except AttributeError:
            print('special key {0} pressed'.format(
                key))

    return _


def keyboard_event_listener(event_messages: EventMessages):
    listener = keyboard.Listener(
        on_press=on_press(event_messages),
        daemon=True)
    listener.start()
