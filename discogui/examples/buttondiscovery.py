"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using `discogui.buttons` module
3. print rectangles
4. draw red rectangles on screenshot
"""

from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons
from discogui.draw import draw_indexed_rect_list
from discogui.imgutil import autocrop

with SmartDisplay(visible=0) as disp:
    with EasyProcess("zenity --question"):
        img = disp.waitgrab(timeout=60)
        rectangles = discover_buttons()
        print(rectangles)

img = draw_indexed_rect_list(img, rectangles)
img = autocrop(img)

# save results
img.save("zenity-buttons.png")
