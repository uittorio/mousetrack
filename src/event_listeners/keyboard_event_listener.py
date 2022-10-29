from pynput import keyboard


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


def keyboard_event_listener():
    listener = keyboard.Listener(
        on_press=on_press,
        on_release=on_release,
        daemon=True)
    listener.start()
