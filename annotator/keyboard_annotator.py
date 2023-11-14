from pynput.keyboard._win32 import KeyCode
from pynput.keyboard import Key, Listener
from .annotator import Annotator
from datetime import datetime
from typing import Dict


class KeyboardAnnotator(Annotator):
    def __init__(self, config: Dict[str, str]):
        super().__init__(config)
        self.timer: datetime = 0

        # The last pressed key to avoid double presses
        self.last_pressed_key = None

        # Create a dictionary that maps the keyboard keys to the description
        self.keyboard_mapping: dict = {}
        for key, value in config.items():
            if len(key) == 1:
                self.keyboard_mapping[key.lower()] = value
            else:
                self.keyboard_mapping[getattr(Key, key.lower())] = value

        # Create a listener for the keyboard
        with Listener(on_press=self.on_press, on_release=self.on_release) as listener:
            listener.join()

    def on_press(self, key: KeyCode):
        key = key.char if hasattr(key, "char") else key
        if key not in self.keyboard_mapping:
            return

        # Check if the key is the same as the last pressed key
        if key == self.last_pressed_key:
            return

        self.last_pressed_key = key
        self.timer = datetime.now()
        self.onset.append(self.timer.second)
        self.description.append(self.keyboard_mapping.get(key))

        # print the key press for debugging
        print(f"Started: {self.keyboard_mapping.get(key)}")

    def on_release(self, key):
        # stop the listener
        if key == Key.esc:
            return False

        # Check if the key is in the mapping
        key = key.char if hasattr(key, "char") else key
        if key not in self.keyboard_mapping:
            return

        # set the duration of the pressed key
        self.duration.append((datetime.now() - self.timer).seconds)

        # reset the last pressed key
        self.last_pressed_key = None

        # print the key release for debugging
        print(f"Stopped: {self.keyboard_mapping.get(key)}")
