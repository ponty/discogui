"""
1. start gnumeric on Xvfb with low ersolution
2. discover buttons using :mod:`discogui.hover` module
3. print rectangles
4. draw red rectangles on screenshot
"""
from discogui.draw import draw_indexed_rect_list
from discogui.hover import active_rectangles
from discogui.imgutil import autocrop
from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay
from entrypoint2 import entrypoint


@entrypoint
def main():
    with SmartDisplay(size=(640, 480), visible=0) as disp:
        with EasyProcess("gnumeric"):
            img = disp.waitgrab(timeout=60)
            rectangles = active_rectangles()
            print(rectangles)
    img = draw_indexed_rect_list(img, rectangles)
    img = autocrop(img)

    # display results
    img.show()



