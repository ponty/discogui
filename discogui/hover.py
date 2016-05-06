'''
This method moves the mouse over a grid, and compare
the image with the original and finds active regions.

.. note::
     It does not work if the GUI changes during the scan.
     (e.g. blinking cursor)

It can be slow if grid is small or the window is large.

'''

from PIL import ImageChops
from discogui.imglog import img_log, img_log_rects
from discogui.imgutil import getbbox, focus_wnd
from discogui.mouse import PyMouse
import logging
import pyscreenshot
from time import sleep


log = logging.getLogger(__name__)
# log = logging


def is_point_active(img_orig, point, mouse=None):
    '''
    Check point on screen:
    1. move mouse over specified point
    2. move mouse to (0,0)

    If screen changes, then returns the bounding rectangle.

    Does not work if other parts of screen are changing (e.g. blinking cursor)

    :rtype: rectangle or None
    '''

    if not mouse:
        mouse = PyMouse()

    log.debug('point:' + str(point))

    mouse.move(point[0], point[1])
    sleep(0.1)
    img_hover = pyscreenshot.grab()
    mouse.move(0, 0)

    # img_log(img_hover, 'img_hover')
    img_log_rects(img_hover, [point + point], 'img_hover')

    img_diff = ImageChops.difference(img_orig, img_hover)
    # enhance color for debug
    img_diff = img_diff.point(lambda x: 255 * bool(x))
    img_log(img_diff, 'img_diff')

    bbox = getbbox(img_diff)
    if bbox:
        # assert bbox.point_inside(point), (bbox, point)
        if not bbox.point_inside(point):
            log.debug('point%s outside box%s' % (point, bbox))
        return bbox


def active_rectangles(grid=30):
    '''
    Return active rectangles found on the specified grid.
    Does not work if other parts of screen are changing (e.g. blinking cursor)

    :rtype: rectangles list
    '''
    mouse = PyMouse()

    img_orig = focus_wnd()
    rct_wnd = getbbox(img_orig)

    ls = []
    for y in xrange(rct_wnd.top + grid / 2, rct_wnd.bottom, grid - grid / 2):
        for x in xrange(rct_wnd.left + grid / 2, rct_wnd.right - grid / 2, grid):
            bbox = is_point_active(img_orig, (x, y), mouse=mouse)
            if bbox and bbox not in ls:
                ls.append(bbox)

    img_log_rects(img_orig, ls, 'img_orig')
    return ls
