'''
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. click first button, print return code
4. click second button, print return code
'''
from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse
from easyprocess import EasyProcess
from pyvirtualdisplay import Display

def click_button_get_return_code(which_button):
    zenity = EasyProcess('zenity --question').start().sleep(1)
    rectangles = discover_buttons()
    PyMouse().click(*rectangles[which_button].center)
    return zenity.wait().return_code

def main():
    screen = Display().start()
    print click_button_get_return_code(0)
    print click_button_get_return_code(1)
    screen.stop()

if __name__=='__main__':
    main()