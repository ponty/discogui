from discogui.buttons import discover_buttons
from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay
from unittest import TestCase


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
        
        
#    def test_empty(self):
#        self.p = EasyProcess('zenity --warning').start()
#        # wnd is not ready
#        #time.sleep(0.2)
#        self.assertRaises(EmptyScreenException, discover_buttons)
        
    def test_zenity(self):
        self.p = EasyProcess('zenity --warning').start()
        self.wait()
        ls = discover_buttons()
        self.assertEquals(len(ls), 1)
        
    def test_notab(self):
        self.p = EasyProcess('xmessage -buttons x,y,z hi').start()
        self.wait()
        ls = discover_buttons(grid=10)
        self.assertEquals(len(ls), 3)
        
        
    def test_gmessage(self):
        self.p = EasyProcess('gmessage -buttons x,y,z hi').start()
        self.wait()
        ls = discover_buttons()
        self.assertEquals(len(ls), 3)

