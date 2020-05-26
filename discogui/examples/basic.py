"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. print rectangles
"""
from time import sleep

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from pyvirtualdisplay import Display
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons


@entrypoint
def main():
    with SmartDisplay(visible=0) as disp:
        with EasyProcess("zenity --question"):
            disp.waitgrab(timeout=60)
            buttons = discover_buttons()
    print(buttons)
