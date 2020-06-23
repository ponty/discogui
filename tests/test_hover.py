from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.hover import active_rectangles


def test_zenity():
    with SmartDisplay() as disp:
        with EasyProcess(["zenity", "--warning"]):
            disp.waitgrab()
            ls = active_rectangles()
            assert len(ls) == 1


def test_notab():
    with SmartDisplay() as disp:
        with EasyProcess(["xmessage", "-buttons", "x,y,z", "hi"]):
            disp.waitgrab()
            ls = active_rectangles(grid=10)
            assert len(ls) == 3


def test_gmessage():
    with SmartDisplay() as disp:
        with EasyProcess(["gmessage", "-buttons", "x,y,z", "hi"]):
            disp.waitgrab()
            ls = active_rectangles()
            assert len(ls) == 3
