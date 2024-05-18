import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(name, log_file, level=logging.INFO):
    """
    Configures and returns a logger with a rotating file handler.

    Parameters:
    - name: Name of the logger.
    - log_file: Path to the log file.
    - level: Logging level (e.g., logging.INFO, logging.ERROR).

    Returns:
    - Configured logger.
    """
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    log_directory = os.path.dirname(log_file)
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)

    handler = RotatingFileHandler(log_file, maxBytes=10000, backupCount=5)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


app_logger = setup_logger('app_logger', 'logs/app.log', level=logging.INFO)
