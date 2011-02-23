from logging import DEBUG
from path import path
from tempfile import mkdtemp, gettempdir
from discogui.draw import draw_indexed_rect_list
import logging

log = logging.getLogger(__name__)

img_dir = None
img_ind = 0
CROP_RECT = None

def set_crop_rect(rct):
    global CROP_RECT
    CROP_RECT = rct
    
def img_log(im, text):
    '''
    save the image in a temp folder for debugging.
    '''
    if not log.isEnabledFor(DEBUG):
        return
    global img_dir
    global img_ind
    if not img_dir:
        root = path(gettempdir()) / 'img_log'
        if not root.exists():
            root.makedirs()
        img_dir = path(mkdtemp(prefix='img_debug_', suffix='', dir=root))
    if CROP_RECT:
        im = im.crop(CROP_RECT)
    fname = str(img_dir / str(img_ind) + '_' + text + '.png')
    im.save(fname)
    log.debug('image was saved:' + fname)
    img_ind += 1

def img_log_rects(img, rcts, text):
    '''
    1. draw rectangles on image
    2. save image
    '''
    if not log.isEnabledFor(DEBUG):
        return
    img2 = draw_indexed_rect_list(img, rcts)
    img_log(img2, text + '_with_rects')
