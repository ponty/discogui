from discogui.imgutil import EmptyScreenException
from discogui.taborder import tab_rectangles
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

    # def test_empty(self):
    #    self.p = EasyProcess('zenity --warning').start()
        # wnd is not ready
    #    self.assertRaises(EmptyScreenException, tab_rectangles)

#    def test_zenity(self):
#        self.p = EasyProcess('zenity --warning').start()
#        self.wait()
#        ls = tab_rectangles()
#        self.assertEquals(len(ls), 2)

    def test_notab(self):
        self.p = EasyProcess('xmessage hi').start()
        self.wait()
        ls = tab_rectangles()
        self.assertEquals(len(ls), 0)

    def test_gmessage(self):
        self.p = EasyProcess('gmessage -buttons x,y,z hi').start()
        self.wait()
        ls = tab_rectangles()
        self.assertEquals(len(ls), 4)
