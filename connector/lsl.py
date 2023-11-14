from abc import ABC
from pylsl import resolve_byprop
from mne_realtime import LSLClient
from mne.io import Info


class LSL(ABC):
    def __init__(self, client_info: Info, host_name: str, timeout: float = 1) -> None:
        self.timeout = timeout
        self.client_info = client_info
        self.host_id = self.__get_host_id(host_name)

    def connect(self) -> LSLClient:
        return LSLClient(self.client_info, self.host_id, self.timeout)

    def __get_host_id(self, host_name: str) -> str:
        # Returns a list of streams that match the given hostname
        streams = resolve_byprop("name", host_name, timeout=self.timeout)
        
        # Check if the stream exists
        if len(streams) == 0:
            raise Exception(f"stream {host_name} not found")

        # Returns the stream id of the stream
        return streams[0].source_id()
