from abc import ABC
from pylsl import StreamInlet, resolve_stream
from mne_realtime import LSLClient
from mne.io import Info


class LSL(ABC):
    @staticmethod
    def connect(client_info: Info, host_name: str, wait_max: float) -> LSLClient:
        host_id = LSL.__get_host_id(host_name)
        return LSLClient(client_info, host_id, wait_max)

    @staticmethod
    def __get_host_id(host_name: str) -> str:
        # Returns a list of streams that match the given hostname
        streams = resolve_stream("name", host_name, 1)

        # Check if the stream exists
        if len(streams) == 0:
            raise Exception(f"Stream {host_name} not found")

        # Returns the stream id of the stream
        return streams[0].source_id()
