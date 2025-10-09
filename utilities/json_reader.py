from utilities.logger import get_logger
import json
import os

logger = get_logger()

def json_reader(file_name):
    logger.info(f"\nReading json file.....")
    base_dir = os.path.dirname(os.path.abspath(__file__))  # directory where this .py file lives
    file_path = os.path.join(base_dir, "data", file_name)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"\nFile not found: {file_path}")

    logger.info(f"\nJSON file exists, preparing the payload .....")
    with open(file_path, "r", encoding="utf-8") as json_file:
        payload = json.load(json_file)
        logger.info(payload)
    return payload

