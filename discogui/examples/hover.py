"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using mouse hovering: 
    move the mouse in grid positions and check how the screen changes
3. print button rectangle positions
4. draw red rectangles for buttons on screenshot
"""
from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.draw import draw_indexed_rect_list
from discogui.hover import active_rectangles
from discogui.imgutil import autocrop

with SmartDisplay(size=(640, 480), visible=False) as disp:
    with EasyProcess(["zenity", "--question"]):
        img = disp.waitgrab(timeout=60, autocrop=False)
        rectangles = active_rectangles(grid=30)
        print(rectangles)
img = draw_indexed_rect_list(img, rectangles)
img = autocrop(img)

# save results
img.save("hover.png")
