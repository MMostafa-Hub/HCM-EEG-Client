from typing import Any, List, Dict
from .pipeline import Pipeline
from .step.band_pass_filter import BandPassFilter
from .step.band_stop_filter import BandStopFilter
from .step.high_pass_filter import HighPassFilter
from .step.low_pass_filter import LowPassFilter
from .step.step import Step


class PipelineBuilder:
    def __init__(self, steps_config: List[Dict[str, Any]]):
        step_dict = {
            "band_pass": BandPassFilter,
            "band_stop": BandStopFilter,
            "high_pass": HighPassFilter,
            "low_pass": LowPassFilter,
        }
        steps: List[Step] = []
        for step_config in steps_config:
            for key, value in step_config.items():
                step = step_dict[key](*value)
            steps.append(step)

        self._pipeline = Pipeline(steps)

    def build(self) -> Pipeline:
        return self._pipeline
