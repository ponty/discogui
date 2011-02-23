from unittest import TestCase
from discogui.screenrect import ScreenRect


class Test(TestCase):
    def test(self):
        self.assertEqual( ScreenRect(1,2,3,4), ScreenRect(1,2,3,4))
        self.assertNotEqual( ScreenRect(1,2,3,5), ScreenRect(1,2,3,4))
        
        
        self.assertTrue(ScreenRect(1,2,3,4).point_inside((2,3)))
        self.assertFalse(ScreenRect(1,2,3,4).point_inside((2,5)))

        # point on edge -> True
        self.assertTrue(ScreenRect(1,2,3,4).point_inside((1,2)))
        
        
        
        
        
        
        
                