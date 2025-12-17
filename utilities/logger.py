import logging
import allure


# -------------------------------------------
# Create a global logger object
# -------------------------------------------
logger = logging.getLogger("BehaveLogger")
logger.setLevel(logging.DEBUG)   # Capture all levels


# -------------------------------------------
# Console Handler
# -------------------------------------------
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
console_handler.setFormatter(formatter)


# -------------------------------------------
# File Handler (Optional)
# Stores logs in logs/test.log
# -------------------------------------------
# file_handler = logging.FileHandler("logs/test.log", mode="a")
# file_handler.setLevel(logging.DEBUG)
# file_handler.setFormatter(formatter)


# -------------------------------------------
# Attach handlers to logger (avoid duplicates)
# -------------------------------------------
# if not logger.handlers:
#     logger.addHandler(console_handler)
#     logger.addHandler(file_handler)


# ------------------------------------------------
# Wrapper to automatically send logs to Allure
# ------------------------------------------------
def _attach_to_allure(level, message):
    """
    Internal helper to attach logs to Allure in a clean way.
    """
    try:
        allure.attach(
            message,
            name=f"{level.upper()}",
            attachment_type=allure.attachment_type.TEXT
        )
    except:
        # Allure may not be active for some runs
        pass


# -------------------------------------------
# Override logging methods to also log to Allure
# -------------------------------------------
original_info = logger.info
original_debug = logger.debug
original_warning = logger.warning
original_error = logger.error
original_critical = logger.critical


def info(message):
    original_info(message)
    _attach_to_allure("info", message)


def debug(message):
    original_debug(message)
    _attach_to_allure("debug", message)


def warning(message):
    original_warning(message)
    _attach_to_allure("warning", message)


def error(message):
    original_error(message)
    _attach_to_allure("error", message)


def critical(message):
    original_critical(message)
    _attach_to_allure("critical", message)


# Assign new methods to logger
logger.info = info
logger.debug = debug
logger.warning = warning
logger.error = error
logger.critical = critical
