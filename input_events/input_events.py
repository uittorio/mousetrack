from pynput import mouse


def on_move(x, y):
    print('moving')


def on_click(x, y, button, pressed):
    print('clicking')
    # if not pressed:
    #     # Stop listener
    #     return False


def on_scroll(x, y, dx, dy):
    print('scrolling')

def mouse_event_listener():
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll) as listener:
        listener.join()
