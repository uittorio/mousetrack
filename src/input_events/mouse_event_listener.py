from pynput import keyboard, mouse

from src.port.event_repository import EventRepository


def on_move(x, y):
    print('moving')


def on_click(x, y, button, pressed):
    print('clicking')


def on_scroll(event_data: EventRepository):
    def _on_scroll(x, y, dx, dy):
        event_data.write_mouse_event()

    return _on_scroll


def mouse_event_listener(event_repository: EventRepository):
    mouse_listener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll(event_repository),
        daemon=True)
    mouse_listener.start()
