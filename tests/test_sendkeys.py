from discogui.imgutil import getbbox, focus_wnd
from pykeyboard import PyKeyboard
from easyprocess import EasyProcess
from pyscreenshot import grab
from pyvirtualdisplay.smartdisplay import SmartDisplay
from unittest import TestCase
import time

VISIBLE = 0


class Test(TestCase):
    def wait(self):
        self.screen.waitgrab()

    def setUp(self):
        self.screen = SmartDisplay(visible=VISIBLE)
        self.screen.start()
        self.p = None

    def tearDown(self):
        self.p.stop()
        self.screen.stop()

    def test_zenity(self):
        self.p = EasyProcess('zenity --warning').start()
        self.wait()
        k = PyKeyboard()
        k.tap_key(k.enter_key)
        self.assertFalse(getbbox(grab()))

        self.p = EasyProcess('zenity --warning').start()
        self.wait()
        k.tap_key(k.enter_key)
        self.assertFalse(getbbox(grab()))

        self.p = EasyProcess('zenity --warning').start()
        self.wait()
        k.tap_key(' ')
        self.assertFalse(getbbox(grab()))

        self.p = EasyProcess('zenity --warning').start()
        self.wait()
        k.tap_key('x')
        self.assertTrue(getbbox(grab()))

    def test_gcalctool1(self):
        self.p = EasyProcess('gnome-calculator').start()
        self.wait()
        focus_wnd()
        k = PyKeyboard()
        k.press_keys([k.control_key,'q'])
        time.sleep(1)
#        img_debug(grab(), 'ctrl+q')
        self.assertFalse(getbbox(grab()))

#    def test_gcalctool2(self):
#        self.p = EasyProcess('gcalctool').start()
#        self.wait()
#        focus_wnd()
#        send_key('alt+c')
# #        img_debug(grab(), 'altc')
#        time.sleep(1)
#        send_key('q')
#        time.sleep(1)
# #        img_debug(grab(), 'q')
#        self.assertFalse(getbbox(grab()))
