from .step import Step
from mne import EpochsArray


class HighPassFilter(Step):
    def __init__(self, freq: float):
        self.freq = freq

    def __call__(self, data: EpochsArray) -> EpochsArray:
        return data.filter(l_freq=self.freq)
