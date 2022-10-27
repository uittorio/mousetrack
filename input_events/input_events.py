from pynput import mouse

from updater.updater import TimerUpdater


def on_move(x, y):
    print('moving')


def on_click(x, y, button, pressed):
    print('clicking')

    # if not pressed:
    #     # Stop listener
    #     return False


def on_scroll(timer_updater: TimerUpdater):
    def inner_func(x, y, dx, dy):
        timer_updater.updateTime()

    return inner_func

def mouse_event_listener(timer_updater: TimerUpdater):
    with mouse.Listener(
            on_move=on_move,
            on_click=on_click,
            on_scroll=on_scroll(timer_updater)) as listener:
        listener.join()
