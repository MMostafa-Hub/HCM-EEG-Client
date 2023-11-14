from configuration_manager.yaml import YamlConfigurationManager
from annotator.keyboard_annotator import KeyboardAnnotator
from pipeline.pipeline_builder import PipelineBuilder
from producer.csv import CSVProducer
from connector.lsl import LSL
from mne import create_info
import numpy as np
import sys


def main(config_path: str, output_path: str):
    # Get the configuration from the yaml file
    config = YamlConfigurationManager(config_path).get_config()

    # config for the LSL client and measurement info
    host_name = config["host_name"]
    ch_names = config["ch_names"]
    ch_types = config["ch_types"]
    sfreq = config["sfreq"]
    timeout = config["timeout"]

    # Create the measurement info
    measurement_info = create_info(ch_names, sfreq, ch_types)

    # Create a LSL client
    lsl_client = LSL(measurement_info, host_name, timeout)

    # Create the preprocessing pipeline
    preprocessing_pipeline_config = config["preprocessing_pipeline"]
    preprocessing_pipeline = PipelineBuilder(preprocessing_pipeline_config).build()

    # Array to store the eeg data
    eeg_array = np.array([], dtype=np.float64)
    
    with lsl_client.connect() as client:
        annotator = KeyboardAnnotator(config["keyboard_mapping"])
        # Todo: Create the visualization
        try:
            while True:
                # getting the data from lsl server
                epoch = client.get_data_as_epoch()

                # apply the preprocessing pipeline
                epoch = preprocessing_pipeline(epoch)

                # Todo: Update the visualization

                # append the preprocessed data to the eeg array
                eeg_array = np.append(eeg_array, epoch.get_data())
        except KeyboardInterrupt:
            # save the eeg array to a csv file
            CSVProducer.save(
                eeg_array,
                measurement_info,
                output_path,
                annotation=annotator.get_annotations(),
            )


if __name__ == "__main__":
    main(*sys.argv[1:])
