import logging
import os

def setup_logger(name, log_file, level=logging.INFO):
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    handler = logging.FileHandler(log_file)

    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # VERY IMPORTANT: avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(handler)

    return logger
