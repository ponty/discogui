"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using `discogui.buttons` module
3. click first button, print return code
4. click second button, print return code
"""

from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse


def click_button_get_return_code(disp, which_button):
    with EasyProcess(["zenity", "--question"]) as p:
        disp.waitgrab(timeout=60)
        rectangles = discover_buttons()
        PyMouse().click(*rectangles[which_button].center)
        return p.wait().return_code


with SmartDisplay() as disp:
    print(click_button_get_return_code(disp, 0))
with SmartDisplay() as disp:
    print(click_button_get_return_code(disp, 1))
