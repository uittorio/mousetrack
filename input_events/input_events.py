from pynput import mouse, keyboard

from port.event_repository import EventRepository


def on_move(x, y):
    print('moving')


def on_click(x, y, button, pressed):
    print('clicking')


def on_press(key):
    try:
        print('alphanumeric key {0} pressed'.format(
            key.char))
    except AttributeError:
        print('special key {0} pressed'.format(
            key))


def on_release(key):
    print('{0} released'.format(
        key))


def on_scroll(event_data: EventRepository):
    def _on_scroll(x, y, dx, dy):
        event_data.write_mouse_event()

    return _on_scroll


def mouse_event_listener(event_repository: EventRepository):
    mouseListener = mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll(event_repository))

    # keyboardListener = keyboard.Listener(
    #     on_press=on_press,
    #     on_release=on_release
    # )

    # keyboardListener.start();
    mouseListener.start()
