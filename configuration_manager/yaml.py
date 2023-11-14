from .configuration_manager import ConfigurationManager
import yaml


class YamlConfigurationManager(ConfigurationManager):
    def __init__(self, path: str) -> None:
        super().__init__(path)

    def get_config(self) -> dict:
        with open(self.path, "r") as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)
    