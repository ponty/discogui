from time import sleep

from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.imgutil import grab_no_blink, img_eq


def blink(sleep_time):
    with SmartDisplay() as disp:
        with EasyProcess(["zenity", "--entry"]):
            disp.waitgrab()
            sleep(sleep_time)
            return grab_no_blink()


def test_blink():
    im1 = blink(0)
    im2 = blink(0.6)
    assert img_eq(im1, im2)


def test_noblink():
    with SmartDisplay() as disp:
        with EasyProcess(["zenity", "--info", "--text", "hi"]):
            disp.waitgrab()
            assert grab_no_blink()
