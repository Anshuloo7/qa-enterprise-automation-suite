from utils.config_loader import load_config
from utils.data_loader import load_test_data
from utils.logger_setup import setup_logger

def before_all(context):
    # Setup logger
    context.logger = setup_logger()
    context.logger.info("=== Test Execution Started ===")

    # Load environment config
    env = context.config.userdata.get("env")
    context.env_config = load_config(env)
    context.logger.info(f"Running tests in environment: {env or 'default'}")

def before_scenario(context, scenario):
    # Load all required test data
    context.test_data = {
        "payments": load_test_data("payments.yaml"),
    }
    context.logger.info(f"Starting scenario: {scenario.name}")

def after_scenario(context, scenario):
    context.logger.info(f"Scenario '{scenario.name}' - Status: {scenario.status}")

def after_all(context):
    context.logger.info("=== Test Execution Completed ===")
