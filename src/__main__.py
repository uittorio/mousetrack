from src.UI.ui import UI
from src.adapters.file_event_repository import FileEventRepository
from src.domain.event_messages.event_messages import EventMessages
from src.event_listeners.keyboard_event_listener import keyboard_event_listener
from src.event_listeners.mouse_event_listener import mouse_event_listener


def main():
    event_repository = FileEventRepository()
    event_messages = EventMessages(event_repository)

    ui = UI(event_repository)
    mouse_event_listener(event_messages)
    keyboard_event_listener(event_messages)
    ui.draw()
