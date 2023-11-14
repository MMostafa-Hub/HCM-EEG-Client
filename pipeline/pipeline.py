from typing import List
from mne import EpochsArray
from .step.step import Step


class Pipeline:
    def __init__(self, steps: List[Step] = None):
        self._pipeline = steps

    def add(self, step: Step) -> "Pipeline":
        self._pipeline.append(step)
        return self

    def __run(self, data: EpochsArray) -> EpochsArray:
        for step in self._pipeline:
            data = step(data)
        return data

    def __call__(self, data: EpochsArray) -> EpochsArray:
        return self.__run(data)

    def __str__(self) -> str:
        return str(self._pipeline)
    