from easyprocess import EasyProcess
from pyscreenshot import grab
from discogui.imgutil import autocrop, focus_wnd
from discogui.sendkeys import send_key_list
from pyvirtualdisplay import Display
import time


def main():
    with Display():
        with EasyProcess('gcalctool'):
            # wait for displaying the window
            time.sleep(1)
            focus_wnd()
            send_key_list(['2', '*', '2', '=', '\n'])
            img = autocrop(grab())

    img.show()

if __name__ == '__main__':
    main()
