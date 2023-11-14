from abc import abstractmethod, ABC


class ConfigurationManager(ABC):
    def __init__(self, path: str) -> None:
        self.path = path

    @abstractmethod
    def get_config(self) -> dict:
        pass
