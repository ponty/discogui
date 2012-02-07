from discogui.imgutil import getbbox, focus_wnd
from discogui.sendkeys import send_key, send_key_list
from easyprocess import EasyProcess
from pyscreenshot import grab
from pyvirtualdisplay.smartdisplay import SmartDisplay
from unittest import TestCase
import time



class Test(TestCase):
    def wait(self):
        self.screen.waitgrab()
        
    def setUp(self):
        self.screen = SmartDisplay()
        self.screen.start()
        self.p = None
        
    def tearDown(self):
        self.p.stop()
        self.screen.stop()
        
    def test_zenity(self):
        self.p = EasyProcess('zenity --warning').start()
        self.wait()
        send_key('\n')
        self.assertFalse(getbbox(grab()))

        self.p = EasyProcess('zenity --warning').start()
        self.wait()
        send_key_list(['\n'])
        self.assertFalse(getbbox(grab()))

        self.p = EasyProcess('zenity --warning').start()
        self.wait()
        send_key(' ')
        self.assertFalse(getbbox(grab()))
        
        self.p = EasyProcess('zenity --warning').start()
        self.wait()
        send_key('x')
        self.assertTrue(getbbox(grab()))

    def test_gcalctool1(self):
        self.p = EasyProcess('gcalctool').start()
        self.wait()
        focus_wnd()
        send_key('ctrl+q')
        time.sleep(1)
#        img_debug(grab(), 'ctrl+q')
        self.assertFalse(getbbox(grab()))

    def test_gcalctool2(self):
        self.p = EasyProcess('gcalctool').start()
        self.wait()
        focus_wnd()
        send_key('alt+c')
#        img_debug(grab(), 'altc')
        time.sleep(1)
        send_key('q')
        time.sleep(1)
#        img_debug(grab(), 'q')
        self.assertFalse(getbbox(grab()))

