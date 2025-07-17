import yaml
import os

def load_config(env=None):
    config_path = os.path.join(os.path.dirname(__file__), "..", "config", "config.yaml")
    with open(config_path, "r") as file:
        config_data = yaml.safe_load(file)

    if env is None:
        env = config_data.get("default")

    return config_data["environments"].get(env)