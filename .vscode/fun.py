from colorama import init, Fore, Style
from cursor import hide, show

init()

dic = ["RED", "BLACK", "BLUE", "YELLOW", "GREEN", "WHITE", ""]

for color_name in dic:
    color = getattr(Fore, color_name)
    # print(type(color))
    print(f"{color}{color_name}")
