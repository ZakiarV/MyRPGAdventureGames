import os


def get_path_to_json_files():
    path = os.path.abspath(os.path.dirname(__file__))
    return path


if __name__ == '__main__':
    print(get_path_to_json_files())