'''
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. print rectangles
'''
from discogui.buttons import discover_buttons
from easyprocess import EasyProcess
from pyvirtualdisplay import Display


def main():
    with Display(visible=0):
        with EasyProcess('zenity --question') as p:
            p.sleep(5)
            buttons = discover_buttons()
    print( buttons )


if __name__ == '__main__':
    main()
