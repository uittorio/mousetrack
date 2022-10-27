from pynput import mouse

from port.event_repository import EventRepository


def on_move(x, y):
    print('moving')


def on_click(x, y, button, pressed):
    print('clicking')


def on_scroll(event_data: EventRepository):
    def inner_func(x, y, dx, dy):
        event_data.write_mouse_event()

    return inner_func


def mouse_event_listener(event_repository: EventRepository):
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll(event_repository)) as listener:
        listener.join()
