import logging
from logging import DEBUG
from pathlib import Path
from tempfile import gettempdir, mkdtemp

from discogui.draw import draw_indexed_rect_list

log = logging.getLogger(__name__)

img_dir = None
img_ind = 0
CROP_RECT = None


def set_crop_rect(rct):
    global CROP_RECT
    CROP_RECT = rct


def img_log(im, text):
    """
    save the image in a temp folder for debugging.
    """
    if not log.isEnabledFor(DEBUG):
        return
    global img_dir
    global img_ind
    if not img_dir:
        root = Path(gettempdir()) / "img_log"
        root.mkdir(exist_ok=True)
        img_dir = Path(mkdtemp(prefix="img_debug_", suffix="", dir=root))
    if CROP_RECT:
        im = im.crop(CROP_RECT)
    fname = str(img_dir / (str(img_ind) + "_" + text + ".png"))
    im.save(fname)
    log.debug("image was saved: " + fname)
    img_ind += 1


def img_log_rects(img, rcts, text):
    """
    1. draw rectangles on image
    2. save image
    """
    if not log.isEnabledFor(DEBUG):
        return
    img2 = draw_indexed_rect_list(img, rcts)
    img_log(img2, text + "_with_rects")
