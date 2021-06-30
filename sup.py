from pprint import pprint
from tkinter import filedialog
import os
from pathlib import Path
start = Path('/System/Library/Fonts/Supplemental')

font_dict = {}


def get_fonts():
    font_array = []
    with os.scandir(start) as entries:
        # print(entries)
        for entry in entries:
            if entry.is_file():
                # print(f"{start}/{entry.name}")
                # print(entry.name.split(".")[1])
                font_array.append(entry.name)
    font_array.sort()
    # print(font_array)
    for font in font_array:
        name = font.split(".")[0]
        font_dict[name] = f"{start}/{font}"


get_fonts()
pprint(font_dict)
