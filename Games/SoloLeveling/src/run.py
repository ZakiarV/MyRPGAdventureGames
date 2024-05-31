from .disclaimer import disclaimer
from Games.Tools.wrap_text import wrap_text
from Games.Tools.read_json_file import read_json_file
from Games.Tools.display_options import display_options


def run():
    info = read_json_file("run.json")
    print(wrap_text(info["text"]))
    display_options(info["options"])
