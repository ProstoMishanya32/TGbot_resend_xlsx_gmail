# - *- coding: utf- 8 - *-
import time, os, traceback
from datetime import datetime, timedelta

# Удаление отступов у текста
def ded(get_text: str):
    if get_text is not None:
        split_text = get_text.split("\n")
        if split_text[0] == "": split_text.pop(0)
        if split_text[-1] == "": split_text.pop(-1)
        save_text = []

        for text in split_text:
            while text.startswith(" "):
                text = text[1:]

            save_text.append(text)
        get_text = "\n".join(save_text)

    return get_text

def get_real_time():
    time = datetime.now().strftime("%D  %H:%M:%S")
    return time
