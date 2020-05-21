"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. click first button, print return code
4. click second button, print return code
"""
from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse
from easyprocess import EasyProcess
from pyvirtualdisplay import Display
from time import sleep


def click_button_get_return_code(which_button):
    with EasyProcess("zenity --question") as p:
        sleep(1)
        rectangles = discover_buttons()
        PyMouse().click(*rectangles[which_button].center)
        return p.wait().return_code


def main():
    with Display():
        print(click_button_get_return_code(0))
        print(click_button_get_return_code(1))


if __name__ == "__main__":
    main()
