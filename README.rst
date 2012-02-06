``discogui`` discovers GUI elements

Links:
 * home: https://github.com/ponty/discogui
 * documentation: http://ponty.github.com/discogui


Features:
 * python module
 * works on Linux
 * does not depend on Accessibility technologies
 * toolkit independent
 * only  basic tests on very simple GUI
 * GUI should be displayed on Xvfb or Xephyr
 * slow
 
Known problems:
 - Python 3 is not supported

Possible applications:
 * GUI unit-testing
 * automatic GUI control

Basic usage
============
::

    from discogui.buttons import discover_buttons
    from easyprocess import EasyProcess
    from pyvirtualdisplay import Display
    with Display():
        with EasyProcess('zenity --question') as p:   
            p.sleep(1)         
            buttons = discover_buttons()
    print buttons


Installation
============

General
--------

 * install Xvfb_ and Xephyr_
 * install Xlib
 * install scrot
 * install PIL_
 * install xdotool
 * install pip_
 * install latest PyMouse and the program::

    # as root
    pip install https://github.com/pepijndevos/PyMouse/zipball/master
    pip install discogui

Ubuntu
----------
::

    sudo apt-get install python-pip
    sudo apt-get install xvfb
    sudo apt-get install xserver-xephyr
    sudo apt-get install python-xlib
    sudo apt-get install scrot
    sudo apt-get install python-imaging
    sudo apt-get install xdotool

    # PyPI version of PyMouse is too old, this is the latest
    sudo pip install https://github.com/pepijndevos/PyMouse/zipball/master

    sudo pip install discogui

Uninstall
----------
::

    # as root
    pip uninstall discogui


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _Xvfb: http://en.wikipedia.org/wiki/Xvfb
.. _Xephyr: http://en.wikipedia.org/wiki/Xephyr
.. _PIL: http://www.pythonware.com/library/pil/







