from easyprocess import EasyProcess
from pyscreenshot import grab
from discogui.imgutil import autocrop, focus_wnd
from discogui.sendkeys import send_key_list
from pyvirtualdisplay import Display
import time

CALCULATORS = '''
gnome-calculator
gcalctool
'''


def find_calculator():
    for calc in CALCULATORS.strip().splitlines():
        if EasyProcess([calc, '-h']).call().return_code == 0:
            return calc
    raise ValueError('no calculator found!')


def main():
    with Display(visible=0):
        with EasyProcess(find_calculator()):
            # wait for displaying the window
            time.sleep(0.5)
            focus_wnd()
            send_key_list(['2', '*', '2', '=', '\n'])
            time.sleep(0.5)
            img = autocrop(grab())

    img.show()

if __name__ == '__main__':
    main()
