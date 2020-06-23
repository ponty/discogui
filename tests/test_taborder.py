from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.taborder import tab_rectangles


def test_notab():
    with SmartDisplay() as disp:
        with EasyProcess(["xmessage", "hi"]):
            disp.waitgrab()
            ls = tab_rectangles()
            assert len(ls) == 0


def test_gmessage():
    with SmartDisplay() as disp:
        with EasyProcess(["gmessage", "-buttons", "x,y,z", "hi"]):
            disp.waitgrab()
            ls = tab_rectangles()
            assert len(ls) == 4
