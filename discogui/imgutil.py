from discogui import imglog
from discogui.mouse import PyMouse
from discogui.screenrect import ScreenRect
import pyscreenshot

def getbbox(img, outside=False):
    '''
    Get bounding box.
    PIL getbbox() is not symmetrical on left/right.
    
    outside=0 -> box contains edges
    outside=1 -> box does not contain edges
    
    :param img: PIL image
    :param outside: bool
    :rtype: ScreenRect
    '''
    bbox = img.getbbox()
    if bbox:
        bbox = ScreenRect(bbox)
        if outside:
            bbox.left -= 1
            bbox.top -= 1
        else:
            bbox.right += 1
            bbox.bottom += 1
        return bbox

def autocrop(img, outside=False):
    box = getbbox(img, outside=outside)
    if box:
        img = img.crop(box)
    return img
        
class EmptyScreenException(Exception):
    pass

def focus_wnd():
    '''
    move mouse over window to get focus
    '''
    rct_wnd = getbbox(pyscreenshot.grab())
    if not rct_wnd:
        raise EmptyScreenException('Empty screen!')

    imglog.set_crop_rect(rct_wnd)

    # init window focus
    mouse = PyMouse()
    mouse.move(*rct_wnd.topleft)

    img_orig = pyscreenshot.grab()
    imglog.img_log(img_orig, 'img_orig')
    return img_orig
    
    
