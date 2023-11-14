from abc import ABC, abstractmethod
from typing import Dict, List
from mne import Annotations, EpochsArray


class Annotator(ABC):
    def __init__(self, config: Dict):
        self._config = config
        self.onset = []  # in seconds
        self.duration = []  # in seconds
        self.description: List[str] = []

    def add(self, onset: float, duration: float, description: str):
        self.onset.append(onset)
        self.duration.append(duration)
        self.description.append(description)

    def get_annotations(self) -> Annotations:
        return Annotations(
            onset=self.onset, duration=self.duration, description=self.description
        )
