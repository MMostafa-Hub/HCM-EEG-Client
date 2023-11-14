from .producer import Producer
import numpy as np
from mne.io import Info, RawArray
from mne import Annotations


class CSVProducer(Producer):
    def save(
        data: np.ndarray,
        measurement_info: Info,
        path: str,
        annotations: Annotations = None,
    ) -> None:
        raw = RawArray(data, measurement_info)
        if annotations:
            raw.set_annotations(annotations)
        raw.to_data_frame().to_csv(path, index=False)
