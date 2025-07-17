from utils.config_loader import load_config
from utils.data_loader import load_test_data

def before_all(context):
    env = context.config.userdata.get("env")
    context.env_config = load_config(env)

def before_scenario(context, scenario):
    # Load all required test data once per scenario
    context.test_data = {
        "payments": load_test_data("payments.yaml"),
    }
