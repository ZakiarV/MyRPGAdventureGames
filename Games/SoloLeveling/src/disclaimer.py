from Games.Tools.wrap_text import wrap_text
from Games.Tools.wait import wait
from Games.Tools.read_json_file import read_json_file


def disclaimer():
    info = read_json_file("disclaimer.json")
    print(wrap_text(info["text"]))
    wait(info["wait"])
