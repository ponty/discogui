from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons


def test_zenity():
    with SmartDisplay(visible=0) as d:
        with EasyProcess(["zenity", "--warning"]):
            d.waitgrab()
            ls = discover_buttons()
            assert len(ls) == 1


def test_notab():
    with SmartDisplay(visible=0) as d:
        with EasyProcess(["xmessage", "-buttons", "x,y,z", "hi"]):
            d.waitgrab()
            ls = discover_buttons(grid=10)
            assert len(ls) == 3


def test_gmessage():
    with SmartDisplay(visible=0) as d:
        with EasyProcess(["gmessage", "-buttons", "x,y,z", "hi"]):
            d.waitgrab()
            ls = discover_buttons()
            assert len(ls) == 3
