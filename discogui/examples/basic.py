'''
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. print rectangles
'''
from discogui.buttons import discover_buttons
from easyprocess import EasyProcess
from pyvirtualdisplay import Display

def main():
    buttons = Display().wrap(
                    EasyProcess('zenity --question').wrap(
                                          discover_buttons, delay=1))
    print buttons()
    

if __name__ == '__main__':
    main()