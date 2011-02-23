from easyprocess import EasyProcess
from unittest import TestCase
from discogui.hover import active_rectangles
from discogui.imgutil import EmptyScreenException
from pyvirtualdisplay import Display
import time


class Test(TestCase):
    def setUp(self):
        self.screen = Display()
        self.screen.start()

        
    def tearDown(self):
        self.p.stop()
        self.screen.stop()
        
    def test_empty(self):
        self.p = EasyProcess('zenity --warning').start()
        # wnd is not ready
        #time.sleep(0.2)
        self.assertRaises(EmptyScreenException, active_rectangles)
        
    def test_zenity(self):
        self.p = EasyProcess('zenity --warning').start()
        time.sleep(0.2)
        ls = active_rectangles()
        self.assertEquals(len(ls), 1)
        
    def test_notab(self):
        self.p = EasyProcess('xmessage -buttons x,y,z hi').start()
        time.sleep(0.2)
        ls = active_rectangles(grid=10)
        self.assertEquals(len(ls), 3)
        
        
    def test_gmessage(self):
        self.p = EasyProcess('gmessage -buttons x,y,z hi').start()
        time.sleep(0.2)
        ls = active_rectangles()
        self.assertEquals(len(ls), 3)

