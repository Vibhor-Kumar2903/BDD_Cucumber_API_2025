from datetime import datetime
import os
import allure
import logging

# Singleton logger instance
LOGGER = None

def get_logger(name="RobotLogger", log_level=logging.INFO):
    """
    Returns a logger instance that logs to both console and file.
    Logs are also attached to Allure reports automatically.
    """
    global LOGGER
    if LOGGER:
        return LOGGER

    # Create logs directory if not present
    log_dir = os.path.join(os.getcwd(), "Logs")
    os.makedirs(log_dir, exist_ok=True)

    # Create a timestamped log file
    log_file = os.path.join(log_dir, f"test_run_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

    # Configure logger
    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # File Handler
    file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    # Add Allure step logging hook
    def allure_hook(message, level="INFO"):
        """Attach log entries to Allure report."""
        with allure.step(f"[{level}] {message}"):
            allure.attach(message, name=f"{level} Log", attachment_type=allure.attachment_type.TEXT)

    # Monkey patch logger methods to also log to Allure
    def _log_with_allure(level_func, level_name):
        def wrapper(msg, *args, **kwargs):
            message = str(msg)
            level_func(message, *args, **kwargs)
            allure_hook(message, level_name)
        return wrapper

    logger.info = _log_with_allure(logger.info, "INFO")
    logger.warning = _log_with_allure(logger.warning, "WARNING")
    logger.error = _log_with_allure(logger.error, "ERROR")
    logger.debug = _log_with_allure(logger.debug, "DEBUG")

    LOGGER = logger
    return LOGGER
