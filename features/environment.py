from utils.config_loader import load_config

def before_all(context):
    env = context.config.userdata.get("env")
    context.env_config = load_config(env)
