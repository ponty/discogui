from easyprocess import EasyProcess
from pyscreenshot import grab
from discogui.imgutil import autocrop, focus_wnd
from pykeyboard import PyKeyboard
from pyvirtualdisplay import Display
from time import sleep
from entrypoint2 import entrypoint

CALCULATORS = """
gnome-calculator
gcalctool
"""


def find_calculator():
    for calc in CALCULATORS.strip().splitlines():
        if EasyProcess([calc, "-h"]).call().return_code == 0:
            return calc
    raise ValueError("no calculator found!")


@entrypoint
def main():
    with Display(visible=0):
        with EasyProcess(find_calculator()):
            # wait for displaying the window
            sleep(0.5)
            focus_wnd()
            k = PyKeyboard()
            k.type_string("2*2=")
            k.tap_key(k.enter_key)
            sleep(0.5)
            img = autocrop(grab())

    img.show()

