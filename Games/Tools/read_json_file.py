import json
from Games.SoloLeveling.ConfigFiles.get_path_to_json_files import get_path_to_json_files


def read_json_file(file_name):
    with open(f"{get_path_to_json_files()}/src/{file_name}", 'r') as file:
        data = json.load(file)
    return data
