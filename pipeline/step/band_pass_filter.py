from .step import Step
from mne import EpochsArray


class BandPassFilter(Step):
    def __init__(self, low: float, high: float):
        self.low = low
        self.high = high

    def __call__(self, data: EpochsArray) -> EpochsArray:
        return data.filter(l_freq=self.low, h_freq=self.high)
