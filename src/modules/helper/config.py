import yaml
from yaml import SafeLoader

class Config():
    def __init__(self):

        with open("config.yaml", "r") as file:
            self.config = yaml.load(file, Loader=SafeLoader)

            # Set the Build version & icon
            self.build_version = "2.0"

            self.link_to_boost = self.config["link_to_boost"]
            self.proxies_file = self.config["proxies_file"]
            self.threads = self.config["threads"]