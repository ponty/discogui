from discogui.buttons import discover_buttons
from easyprocess import EasyProcess
from nose.tools import eq_
from pyvirtualdisplay.smartdisplay import SmartDisplay


def test_zenity():
    with SmartDisplay(visible=0) as d:
        with EasyProcess('zenity --warning') as p:
            d.waitgrab()
            ls = discover_buttons()
            eq_(len(ls), 1)


def test_notab():
    with SmartDisplay(visible=0) as d:
        with EasyProcess('xmessage -buttons x,y,z hi') as p:
            d.waitgrab()
            ls = discover_buttons(grid=10)
            eq_(len(ls), 3)


def test_gmessage():
    with SmartDisplay(visible=0) as d:
        with EasyProcess('gmessage -buttons x,y,z hi') as p:
            d.waitgrab()
            ls = discover_buttons()
            eq_(len(ls), 3)
