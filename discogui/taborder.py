"""
This module search for GUI controls by sending TAB button events
and comparing the image with the original.

.. note::
     It does not work if the GUI changes during the scan.
     (e.g. blinking cursor)

"""

import logging
from time import sleep

from PIL import ImageChops, ImageFilter, ImageStat
from pykeyboard import PyKeyboard  # type: ignore

from discogui.imglog import img_log, img_log_rects
from discogui.imgutil import focus_wnd, getbbox, grab
from discogui.screenrect import ScreenRect

log = logging.getLogger(__name__)


def darker(im1, im2, box):
    """
    im1 is darker than im2 in box -> 0
    im2 is darker than im1 in box -> 1
    """
    # add border, because box is an 'inside box', crop needs 'outside box'
    box = box.add_border(1)

    stat1 = ImageStat.Stat(im1.crop(box))
    stat2 = ImageStat.Stat(im2.crop(box))
    sum1 = sum(stat1.sum)
    sum2 = sum(stat2.sum)
    assert sum1 != sum2, box
    return 0 if sum1 > sum2 else 1


def tab_rectangles():
    """
    Return rectangles found by sending TAB button events.

    Does not work if other parts of screen are changing (e.g. blinking cursor)

    :rtype: rectangles list
    """
    ls = []

    img_orig = focus_wnd()

    im1 = img_orig
    k = PyKeyboard()
    while 1:
        k.tap_key(k.tab_key)
        sleep(0.1)
        im2 = grab()

        img_log(im1, "im1")
        img_log(im2, "im2")

        boxes = tab_rect_pair(im1, im2)
        if not boxes:
            return []
        if len(ls):
            if len(boxes) == 2:
                assert boxes[0] == ls[-1]
            if boxes[-1] in ls:
                break
            ls += [boxes[-1]]
        else:
            # first
            ls += boxes
        im1 = im2

    img_log_rects(img_orig, ls, "img_orig")
    log.debug("rectangles found:%s", ls)
    return ls


def tab_rect_pair(img_orig, im_next):
    """ """
    img_diff = ImageChops.difference(img_orig, im_next)
    img_log(img_diff, "img_diff")

    # can be dotted -> filter + enhance color
    # Problem: close buttons -> filter value sohuld be low
    img_diff_filtered = img_diff.filter(ImageFilter.MaxFilter(3))
    img_diff_filtered = img_diff_filtered.point(lambda x: 255 * bool(x))
    img_log(img_diff_filtered, "img_diff_filtered")

    bbox = getbbox(img_diff)
    if not bbox:
        return None

    def check_edges(horiz):
        if horiz:
            r1 = bbox.left
            r2 = bbox.right
        else:
            r1 = bbox.top
            r2 = bbox.bottom
        ls = []
        for c in range(int(r1), int(r2)):
            if horiz:
                p1 = (c, bbox.top)
                p2 = (c, bbox.bottom)
            else:
                p1 = (bbox.left, c)
                p2 = (bbox.right, c)
            color1 = sum(img_diff_filtered.getpixel(p1))
            color2 = sum(img_diff_filtered.getpixel(p2))
            ls += [int(bool(color1 + color2))]

        if 0 not in ls:
            log.debug("split pos not found")
            return
        i = ls.index(0)
        if i == 0:
            ls.reverse()
            i = ls.index(0)
            i = len(ls) - i - 1
        pos = i + r1
        log.debug("split pos found:%s" % pos)
        if horiz:
            rsegment1 = ScreenRect(0, 0, pos, img_orig.size[1])
            rsegment2 = ScreenRect(pos, 0, img_orig.size[0], img_orig.size[1])
        else:
            rsegment1 = ScreenRect(0, 0, img_orig.size[0], pos)
            rsegment2 = ScreenRect(0, pos, img_orig.size[0], img_orig.size[1])
        box1 = getbbox(img_diff.crop(rsegment1))
        box1.move(rsegment1.topleft)

        box2 = getbbox(img_diff.crop(rsegment2))
        box2.move(rsegment2.topleft)

        return box1, box2

    r = check_edges(0)
    if r is None:
        r = check_edges(1)
    if r is None:
        # in new styles the textbox is not changing
        return [bbox]
    box1, box2 = r
    d1 = darker(img_orig, im_next, box1)
    d2 = darker(img_orig, im_next, box2)
    if d1 == d2:
        log.warning("d1 == d2  %s  %s %s %s", d1, d2, box1, box2)
    if d1 == 1:
        boxes = (box1, box2)
    else:
        boxes = (box2, box1)
    return boxes
