from typing import Dict
from .annotator import Annotator
from datetime import datetime
from pynput.keyboard import Key, Listener


class KeyboardAnnotator(Annotator):
    def __init__(self, config: Dict[str, str]):
        super().__init__(config)
        self.timer: datetime = 0

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

    def on_press(self, key):
        self.timer = datetime.now()
        self.onset.append(self.timer.second)
        self.description.append(self.keyboard_mapping[key])

    def on_release(self, key):
        self.duration.append(datetime.now().second - self.timer.second)
