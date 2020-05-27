Experimental Python library for discovering GUI elements.

Links:
 * home: https://github.com/ponty/discogui
 * PYPI: https://pypi.python.org/pypi/discogui

[![Build Status](https://travis-ci.org/ponty/discogui.svg?branch=master)](https://travis-ci.org/ponty/discogui)

Features:
 * python module
 * works on Linux
 * does not depend on Accessibility technologies
 * toolkit independent
 * only basic tests on very simple GUI
 * GUI should be displayed on Xvfb or Xephyr
 
Possible applications:
 * automatic GUI testing
 * automatic GUI control

Installation::
    
```console
$ sudo apt install xvfb
$ python3 -m pip install discogui
```

Usage
=====

basic
-----

```py
# discogui/examples/basic.py

"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. print rectangles
"""

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons


@entrypoint
def main():
    with SmartDisplay(visible=0) as disp:
        with EasyProcess("zenity --question"):
            disp.waitgrab(timeout=60)
            buttons = discover_buttons()
    print(buttons)

```     
    
<!-- embedme doc/gen/python3_-m_discogui.examples.basic.txt -->
Run it:
```console
$ python3 -m discogui.examples.basic
[ScreenRect((427,416,510,446)), ScreenRect((516,416,599,446))]
```

button discovery on zenity
--------------------------

```py
# discogui/examples/buttondiscovery.py

"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. print rectangles
4. draw red rectangles on screenshot
"""

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons
from discogui.draw import draw_indexed_rect_list
from discogui.imgutil import autocrop


@entrypoint
def main():
    with SmartDisplay(visible=0) as disp:
        with EasyProcess("zenity --question"):
            img = disp.waitgrab(timeout=60)
            rectangles = discover_buttons()
            print(rectangles)

    img = draw_indexed_rect_list(img, rectangles)
    img = autocrop(img)

    # save results
    img.save("zenity-buttons.png")

```

<!-- embedme doc/gen/python3_-m_discogui.examples.buttondiscovery.txt -->
Run it:
```console
$ python3 -m discogui.examples.buttondiscovery
[ScreenRect((427,416,510,446)), ScreenRect((516,416,599,446))]
```

Image:

![](/doc/gen/zenity-buttons.png)


button discovery on gnumeric
----------------------------

```py
# discogui/examples/hovergnumeric.py

"""
1. start gnumeric on Xvfb with low ersolution
2. discover buttons using :mod:`discogui.hover` module
3. print rectangles
4. draw red rectangles on screenshot
"""
from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.draw import draw_indexed_rect_list
from discogui.hover import active_rectangles
from discogui.imgutil import autocrop


@entrypoint
def main():
    with SmartDisplay(size=(640, 480), visible=0) as disp:
        with EasyProcess("gnumeric"):
            img = disp.waitgrab(timeout=60)
            rectangles = active_rectangles()
            print(rectangles)
    img = draw_indexed_rect_list(img, rectangles)
    img = autocrop(img)

    # save results
    img.save("gnumeric-buttons.png")

```

<!-- embedme doc/gen/python3_-m_discogui.examples.hovergnumeric.txt -->
Run it:
```console
$ python3 -m discogui.examples.hovergnumeric
[ScreenRect((5,30,39,64)), ScreenRect((40,30,74,64)), ScreenRect((75,30,109,64)), ScreenRect((124,30,158,64)), ScreenRect((159,30,193,64)), ScreenRect((208,30,242,64)), ScreenRect((243,30,277,64)), ScreenRect((278,30,312,64)), ScreenRect((448,30,482,65)), ScreenRect((5,72,104,106)), ScreenRect((105,72,139,106)), ScreenRect((140,72,174,106)), ScreenRect((175,72,209,106)), ScreenRect((224,72,258,106)), ScreenRect((259,72,293,106)), ScreenRect((294,72,328,106)), ScreenRect((329,72,363,106)), ScreenRect((364,72,398,106)), ScreenRect((399,72,433,106)), ScreenRect((448,72,482,107)), ScreenRect((5,114,39,148)), ScreenRect((40,114,74,148)), ScreenRect((75,114,109,148)), ScreenRect((110,114,144,148)), ScreenRect((145,114,179,148)), ScreenRect((180,114,214,148)), ScreenRect((215,114,249,148)), ScreenRect((250,114,284,148)), ScreenRect((285,114,319,148)), ScreenRect((320,114,354,148)), ScreenRect((355,114,389,148)), ScreenRect((390,114,424,148)), ScreenRect((425,114,459,148)), ScreenRect((278,156,312,190)), ScreenRect((5,311,470,317)), ScreenRect((1,323,59,360))]
```


Image:

![](/doc/gen/gnumeric-buttons.png)

button test
-----------

```py
# discogui/examples/clickbutton.py

"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. click first button, print return code
4. click second button, print return code
"""

from easyprocess import EasyProcess
from entrypoint2 import entrypoint
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse


def click_button_get_return_code(disp, which_button):
    with EasyProcess("zenity --question") as p:
        disp.waitgrab(timeout=60)
        rectangles = discover_buttons()
        PyMouse().click(*rectangles[which_button].center)
        return p.wait().return_code


@entrypoint
def main():
    with SmartDisplay() as disp:
        print(click_button_get_return_code(disp, 0))
    with SmartDisplay() as disp:
        print(click_button_get_return_code(disp, 1))

```

<!-- embedme doc/gen/python3_-m_discogui.examples.clickbutton.txt -->
Run it:
```console
$ python3 -m discogui.examples.clickbutton
1
0
```






