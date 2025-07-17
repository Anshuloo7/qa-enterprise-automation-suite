import logging
import os

def setup_logger():
    log_dir = os.path.join(os.path.dirname(__file__), "..", "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "behave.log")

    logger = logging.getLogger("BehaveLogger")
    logger.setLevel(logging.INFO)

    if not logger.handlers:  # Prevent duplicate logs
        handler = logging.FileHandler(log_file)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    return logger
