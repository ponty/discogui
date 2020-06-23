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


button discovery on zenity
--------------------------

```py
# discogui/examples/buttondiscovery.py

"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using `discogui.buttons` module
3. print rectangles
4. draw red rectangles on screenshot
"""

from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons
from discogui.draw import draw_indexed_rect_list
from discogui.imgutil import autocrop

with SmartDisplay(visible=0) as disp:
    with EasyProcess(["zenity", "--question"]):
        img = disp.waitgrab(timeout=60, autocrop=False)
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
[ScreenRect((426,415,509,445)), ScreenRect((515,415,598,445))]
```

Image:

![](/doc/gen/zenity-buttons.png)


button discovery on gnumeric
----------------------------

```py
# discogui/examples/hovergnumeric.py

"""
1. start gnumeric on Xvfb with low ersolution
2. discover buttons using `discogui.hover` module
3. print rectangles
4. draw red rectangles on screenshot
"""
from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.draw import draw_indexed_rect_list
from discogui.hover import active_rectangles
from discogui.imgutil import autocrop

with SmartDisplay(size=(640, 480), visible=0) as disp:
    with EasyProcess(["gnumeric"]):
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
[ScreenRect((4,29,38,63)), ScreenRect((39,29,73,63)), ScreenRect((74,29,108,63)), ScreenRect((123,29,157,63)), ScreenRect((158,29,192,63)), ScreenRect((207,29,241,63)), ScreenRect((242,29,276,63)), ScreenRect((277,29,311,63)), ScreenRect((447,29,481,64)), ScreenRect((4,71,103,105)), ScreenRect((104,71,138,105)), ScreenRect((139,71,173,105)), ScreenRect((174,71,208,105)), ScreenRect((223,71,257,105)), ScreenRect((258,71,292,105)), ScreenRect((293,71,327,105)), ScreenRect((328,71,362,105)), ScreenRect((363,71,397,105)), ScreenRect((398,71,432,105)), ScreenRect((447,71,481,106)), ScreenRect((4,113,38,147)), ScreenRect((39,113,73,147)), ScreenRect((74,113,108,147)), ScreenRect((109,113,143,147)), ScreenRect((144,113,178,147)), ScreenRect((179,113,213,147)), ScreenRect((214,113,248,147)), ScreenRect((249,113,283,147)), ScreenRect((284,113,318,147)), ScreenRect((319,113,353,147)), ScreenRect((354,113,388,147)), ScreenRect((389,113,423,147)), ScreenRect((424,113,458,147)), ScreenRect((277,155,311,189)), ScreenRect((57,310,469,316)), ScreenRect((0,322,58,359))]
```


Image:

![](/doc/gen/gnumeric-buttons.png)

button test
-----------

```py
# discogui/examples/clickbutton.py

"""
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using `discogui.buttons` module
3. click first button, print return code
4. click second button, print return code
"""

from easyprocess import EasyProcess
from pyvirtualdisplay.smartdisplay import SmartDisplay

from discogui.buttons import discover_buttons
from discogui.mouse import PyMouse


def click_button_get_return_code(disp, which_button):
    with EasyProcess(["zenity", "--question"]) as p:
        disp.waitgrab(timeout=60)
        rectangles = discover_buttons()
        PyMouse().click(*rectangles[which_button].center)
        return p.wait().return_code


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






