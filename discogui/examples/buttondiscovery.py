"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. print rectangles
4. draw red rectangles on screenshot
"""
from time import sleep

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from pyscreenshot import grab
from pyvirtualdisplay import Display

from discogui.buttons import discover_buttons
from discogui.draw import draw_indexed_rect_list
from discogui.imgutil import autocrop


@entrypoint
def main():
    with Display(visible=0):
        with EasyProcess("zenity --question"):
            sleep(1)
            img = grab()
            rectangles = discover_buttons()
            print(rectangles)

    img = draw_indexed_rect_list(img, rectangles)
    img = autocrop(img)

    # display results
    img.show()
