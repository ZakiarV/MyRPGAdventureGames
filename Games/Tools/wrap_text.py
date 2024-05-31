import os
import sys
import textwrap


def get_terminal_size():
    if sys.prefix == sys.base_prefix:
        columns, rows = os.get_terminal_size()
    else:
        columns, rows = 80, 24
    return columns, rows


def wrap_text(text, width=70, indent=0):
    if sys.prefix == sys.base_prefix:
        width = get_terminal_size()[0]
        wrapped_text = textwrap.wrap(text, width - indent)
    else:
        wrapped_text = textwrap.wrap(text, width - indent)
    indent_text = []
    for index, line in enumerate(wrapped_text):
        if index == 0:
            indent_text.append(f"{line}\n")
        else:
            indent_text.append(f"{' ' * indent}{line}\n")
    final_text = "".join(indent_text)
    return final_text
