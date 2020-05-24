import logging
import os

from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

import cog

FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
logging.basicConfig(level=logging.DEBUG, format=FORMAT)


def screenshot(cmd, fname):
    logging.info("%s %s", cmd, fname)
    fpath = "docs/_img/%s" % fname
    if os.path.exists(fpath):
        os.remove(fpath)
    with SmartDisplay(visible=0, bgcolor="black") as disp:
        with EasyProcess(cmd):
            img = disp.waitgrab(timeout=5 * 60)
            img.save(fpath)
            cog.outl(".. image:: _img/%s" % fname)
