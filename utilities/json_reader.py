from utilities.logger import *
import json
import os


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

