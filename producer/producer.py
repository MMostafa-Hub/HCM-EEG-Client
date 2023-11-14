from abc import ABC, abstractmethod
import numpy as np
from mne.io import Info


class Producer(ABC):
    @staticmethod
    @abstractmethod
    def save(data: np.array, measurement_info: Info, path: str):
        pass
