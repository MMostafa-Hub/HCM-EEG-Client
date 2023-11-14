from abc import ABC, abstractmethod
from mne import EpochsArray


class Step(ABC):
    @abstractmethod
    def __call__(self, data: EpochsArray) -> EpochsArray:
        pass
