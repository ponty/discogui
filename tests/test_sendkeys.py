from time import sleep

from easyprocess import EasyProcess
from pykeyboard import PyKeyboard
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.imgutil import getbbox, grab

VISIBLE = 0


def test_zenity():
    with SmartDisplay(visible=VISIBLE) as disp:
        with EasyProcess(["zenity", "--warning"]):
            disp.waitgrab()
            k = PyKeyboard()
            k.tap_key(k.enter_key)
            sleep(0.1)  # wait for processing keyboard event
            assert not getbbox(grab())

        with EasyProcess(["zenity", "--warning"]):
            disp.waitgrab()
            k.tap_key(k.enter_key)
            sleep(0.1)  # wait for processing keyboard event
            assert not getbbox(grab())

        with EasyProcess(["zenity", "--warning"]):
            disp.waitgrab()
            k.tap_key(" ")
            sleep(0.1)  # wait for processing keyboard event
            assert not getbbox(grab())

        with EasyProcess(["zenity", "--warning"]):
            disp.waitgrab()
            k.tap_key("x")
            sleep(0.1)  # wait for processing keyboard event
            assert getbbox(grab())


# def test_gcalctool1():
#     with SmartDisplay() as disp:
#         with EasyProcess(["gnome-calculator"]):
#             disp.waitgrab()
#             focus_wnd()
#             k = PyKeyboard()
#             k.press_keys([k.control_key, "q"])
#             sleep(1)
#             assert not getbbox(grab())
