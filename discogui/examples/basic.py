"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using `discogui.buttons` module
3. print rectangles
"""

from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons

with SmartDisplay(visible=0) as disp:
    with EasyProcess("zenity --question"):
        disp.waitgrab(timeout=60)
        buttons = discover_buttons()
print(buttons)
