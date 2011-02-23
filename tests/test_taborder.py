from discogui.imgutil import EmptyScreenException
from discogui.taborder import tab_rectangles
from easyprocess import EasyProcess
from pyvirtualdisplay import Display
from unittest import TestCase
import time


class Test(TestCase):
    def setUp(self):
        self.screen = Display()
        self.screen.start()
        self.p = None
        
    def tearDown(self):
        self.p.stop()
        self.screen.stop()
        
    def test_empty(self):
        self.p = EasyProcess('zenity --warning').start()
        # wnd is not ready
        self.assertRaises(EmptyScreenException, tab_rectangles)

    def test_zenity(self):
        self.p = EasyProcess('zenity --warning').start()
        time.sleep(0.2)
        ls = tab_rectangles()
        self.assertEquals(len(ls), 2)
        
    def test_notab(self):
        self.p = EasyProcess('xmessage hi').start()
        time.sleep(0.2)
        ls = tab_rectangles()
        self.assertEquals(len(ls), 0)
        
        
    def test_gmessage(self):
        self.p = EasyProcess('gmessage -buttons x,y,z hi').start()
        time.sleep(0.2)
        ls = tab_rectangles()
        self.assertEquals(len(ls), 4)

