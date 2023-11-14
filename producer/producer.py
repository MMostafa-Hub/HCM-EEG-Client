from abc import ABC, abstractmethod
import numpy as np
from mne.io import Info
from mne import Annotations


class Producer(ABC):
    @staticmethod
    @abstractmethod
    def save(
        data: np.ndarray,
        measurement_info: Info,
        path: str,
        annotations: Annotations = None,
    ) -> None:
        pass
