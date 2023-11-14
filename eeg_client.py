from mne import create_info
from configuration_manager.yaml import YamlConfigurationManager
from producer.csv import CSVProducer
import numpy as np
import sys

def main(config_path: str, output_path: str):
    # Get the configuration from the yaml file
    config = YamlConfigurationManager(config_path).get_config()

    host_name = config["host_name"]
    ch_names = config["ch_names"]
    ch_types = config["ch_types"]
    sfreq = config["sfreq"]
    timeout = config["timeout"]

    preprocessing_pipeline = config["preprocessing_pipeline"]

    CSVProducer.save(eeg_array, measurement_info, output_path)


if __name__ == "__main__":
    main(*sys.argv[1:])
