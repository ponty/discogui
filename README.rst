``discogui`` discovers GUI elements

 * python module
 * works on Linux
 * does not depend on Accessibility technologies
 * toolkit independent
 * only  basic tests on very simple GUI
 * GUI should be displayed on Xvfb or Xephyr
 * slow
 
home: https://github.com/ponty/discogui

documentation: http://ponty.github.com/discogui

Possible applications:
 * GUI unit-testing
 * automatic GUI control

Basic usage
============
::

    from discogui.buttons import discover_buttons
    from easyprocess import EasyProcess
    from pyvirtualdisplay import Display
    buttons = Display().wrap(
                EasyProcess('zenity --question').wrap(
                    discover_buttons, delay=1))
    print buttons()


Installation
============

General
--------

 * install Xvfb_ and Xephyr_
 * install Xlib
 * install scrot
 * install PIL_
 * install xdotool
 * install setuptools_
 * install latest PyMouse and the program::

    # as root
    easy_install https://github.com/pepijndevos/PyMouse/zipball/master
    easy_install discogui

Ubuntu
----------
::

    sudo apt-get install python-setuptools
    sudo apt-get install xvfb
    sudo apt-get install xserver-xephyr
    sudo apt-get install python-xlib
    sudo apt-get install scrot
    sudo apt-get install python-imaging
    sudo apt-get install xdotool

    # PyPI version of PyMouse is too old, this is the latest
    sudo easy_install https://github.com/pepijndevos/PyMouse/zipball/master

    sudo easy_install discogui

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







