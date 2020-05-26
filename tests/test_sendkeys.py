from easyprocess import EasyProcess
from pykeyboard import PyKeyboard
from pyscreenshot import grab
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.imgutil import getbbox

VISIBLE = 0


def test_zenity():
    with SmartDisplay() as disp:
        with EasyProcess("zenity --warning"):
            disp.waitgrab()
            k = PyKeyboard()
            k.tap_key(k.enter_key)
            assert not getbbox(grab())

        with EasyProcess("zenity --warning"):
            disp.waitgrab()
            k.tap_key(k.enter_key)
            assert not getbbox(grab())

        with EasyProcess("zenity --warning"):
            disp.waitgrab()
            k.tap_key(" ")
            assert not getbbox(grab())

        with EasyProcess("zenity --warning"):
            disp.waitgrab()
            k.tap_key("x")
            assert getbbox(grab())


# def test_gcalctool1():
#     with SmartDisplay() as disp:
#         with EasyProcess("gnome-calculator"):
#             disp.waitgrab()
#             focus_wnd()
#             k = PyKeyboard()
#             k.press_keys([k.control_key, "q"])
#             sleep(1)
#             assert not getbbox(grab())
