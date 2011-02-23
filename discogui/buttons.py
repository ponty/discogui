'''
Try to find buttons on the window.

1. get controls by :mod:`discogui.taborder`
2. test controls with :mod:`discogui.hover`, if control is active 
        -> it is identified as a button
3. no controls by tab order -> only 1 button on window 
        -> test whole window by :mod:`discogui.hover`  

.. note::
     It does not work if the GUI changes during the scan.
     (e.g. blinking cursor)

'''

from discogui import  hover
from discogui.imglog import  img_log_rects
from discogui.imgutil import  focus_wnd
from discogui.taborder import tab_rectangles
import logging

log = logging.getLogger(__name__)

def discover_buttons(grid=30):
    '''
    try to get buttons by tab order 
    '''
    tab_ls = tab_rectangles()
    
    if not len(tab_ls):
        log.debug('no tab order on window -> full hover test')
        # slow, no tab order
        return hover.active_rectangles(grid=grid)

    img_orig = focus_wnd()

    ls = []
    for x in tab_ls:
        bbox = hover.is_point_active(img_orig, x.center)   
        if bbox:
            ls += [x]
    
    img_log_rects(img_orig, ls, 'img_orig')
    return ls

