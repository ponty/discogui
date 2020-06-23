from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.imgutil import grab_no_blink

with SmartDisplay() as disp:
    with EasyProcess(["zenity", "--entry"]) as p:
        disp.waitgrab()
        # sleep(0.6)
        im = grab_no_blink()
        im.save("blink.png")
