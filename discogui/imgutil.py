import time
from time import sleep

import pyscreenshot
from PIL import ImageChops

from discogui import imglog
from discogui.mouse import PyMouse
from discogui.screenrect import ScreenRect


def getbbox(img, outside=False):
    """
    Get bounding box.
    PIL getbbox() was not symmetrical on left/right.
    It is OK in latest version.

    outside=0 -> box contains edges
    outside=1 -> box does not contain edges

    :param img: PIL image
    :param outside: bool
    :rtype: ScreenRect
    """
    bbox = img.getbbox()
    if bbox:
        bbox = ScreenRect(bbox)
        if outside:
            bbox = bbox.add_border()
        #     bbox.left -= 1
        #     bbox.top -= 1
        # else:
        #     bbox.right += 1
        #     bbox.bottom += 1
        return bbox


def autocrop(img, outside=False):
    box = getbbox(img, outside=outside)
    if box:
        img = img.crop(box)
    return img


class EmptyScreenException(Exception):
    pass


def focus_wnd():
    """
    move mouse over window to get focus
    """
    rct_wnd = getbbox(grab())
    if not rct_wnd:
        raise EmptyScreenException("Empty screen!")

    imglog.set_crop_rect(rct_wnd)

    # init window focus
    mouse = PyMouse()
    mouse.move(*rct_wnd.topleft)

    # time to take effect
    # gmessage fails without this
    sleep(0.3)

    img_orig = grab()
    imglog.img_log(img_orig, "img_orig")
    return img_orig


def grab():
    return pyscreenshot.grab(childprocess=True)


def _grab_and_sleep(blink_time):
    start = time.time()
    im = grab()
    dt = time.time() - start
    t = blink_time / 4 - dt
    assert t > 0
    # while t < 0:
    #     t += blink_time
    sleep(t)
    return im


def grab_no_blink(blink_time=1.2, crop=True):
    # find at least one frame with caret on and one with caret off
    lsim = [_grab_and_sleep(blink_time) for _ in range(4)]
    im = img_list_min(lsim)
    if crop:
        im = autocrop(im)
    return im


def img_eq(im1, im2):
    diff = ImageChops.difference(im1, im2)
    bbox = diff.getbbox()
    print(diff.getbbox())
    return bbox is None


def img_list_min(ls):
    imref = ls[0]
    for im in ls[1:]:
        diffabs = ImageChops.difference(imref, im)
        bbox = diffabs.getbbox()
        if bbox:
            diff = ImageChops.subtract(imref, im)
            if img_eq(diffabs, diff):
                return im
            else:
                return imref
    return imref
