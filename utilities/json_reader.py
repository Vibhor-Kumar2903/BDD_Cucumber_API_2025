from utilities.logger import *
import json
import os


# def json_reader(file_name):
#     logger.info(f"\nReading json file.....")
#     base_dir = os.path.dirname(os.path.abspath(__file__))  # directory where this .py file lives
#     file_path = os.path.join(base_dir, "data", file_name)
#     logger.info(f"File path : {file_path}")
#
#     if not os.path.exists(file_path):
#         raise FileNotFoundError(f"\nFile not found: {file_path}")
#
#     logger.info(f"\nJSON file exists, preparing the payload .....")
#     with open(file_path, "r", encoding="utf-8") as json_file:
#         payload = json.load(json_file)
#         logger.info(payload)
#     return payload

# root_dir = "../api/payloads/activities/"
# file_name = "post_activities.json" # Given file is named as.

def get_json_data(root_directory, json_file_name):
    logger.info("\n1. Loading JSON from a from a file.")
    base_dir = os.path.dirname(os.path.abspath(__file__))

    json_file_path = os.path.join(base_dir, root_directory, json_file_name)
    logger.info(f"\nFile path : {json_file_path}")

    with open(json_file_path, "r") as j_file:
        data = json.load(j_file)

    return data

# print(get_json_data(root_dir,file_name))