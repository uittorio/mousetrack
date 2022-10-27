from pynput import mouse

from data.eventdata import EventData
from updater.updater import TimerUpdater


def on_move(x, y):
    print('moving')


def on_click(x, y, button, pressed):
    print('clicking')

    # if not pressed:
    #     # Stop listener
    #     return False


def on_scroll(event_data: EventData):
    def inner_func(x, y, dx, dy):
        event_data.writeMouseEvent()

    return inner_func

def mouse_event_listener(event_data: EventData):
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll(event_data)) as listener:
        listener.join()
