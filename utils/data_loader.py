import yaml
import os

def load_test_data(filename):
    data_path = os.path.join(os.path.dirname(__file__), "..", "testdata", filename)
    with open(data_path, "r") as file:
        return yaml.safe_load(file)
