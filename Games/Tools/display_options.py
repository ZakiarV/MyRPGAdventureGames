from .wrap_text import wrap_text


def display_options(options: list):
    for option in options:
        print(f"{option["id"]}: {wrap_text(option["text"], indent=len(f"{option["id"]}: "))[0:-1]}")