``discogui`` discovers GUI elements

Links:
 * home: https://github.com/ponty/discogui
 * documentation: http://discogui.readthedocs.org
 * PYPI: https://pypi.python.org/pypi/discogui

|Travis| |Coveralls| |Latest Version| |Supported Python versions| |License| |Downloads| |Code Health| |Documentation|

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
===========
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
-------

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

Ubuntu 14.04
------------
::

    sudo apt-get install python-pip xvfb python-xlib scrot python-pil xdotool
    sudo pip install https://github.com/pepijndevos/PyMouse/zipball/master
    sudo pip install discogui

Uninstall
---------
::

    # as root
    pip uninstall discogui


.. _setuptools: http://peak.telecommunity.com/DevCenter/EasyInstall
.. _pip: http://pip.openplans.org/
.. _Xvfb: http://en.wikipedia.org/wiki/Xvfb
.. _Xephyr: http://en.wikipedia.org/wiki/Xephyr
.. _PIL: http://www.pythonware.com/library/pil/


.. |Travis| image:: http://img.shields.io/travis/ponty/discogui.svg
   :target: https://travis-ci.org/ponty/discogui/
.. |Coveralls| image:: http://img.shields.io/coveralls/ponty/discogui/master.svg
   :target: https://coveralls.io/r/ponty/discogui/
.. |Latest Version| image:: https://img.shields.io/pypi/v/discogui.svg
   :target: https://pypi.python.org/pypi/discogui/
.. |Supported Python versions| image:: https://img.shields.io/pypi/pyversions/discogui.svg
   :target: https://pypi.python.org/pypi/discogui/
.. |License| image:: https://img.shields.io/pypi/l/discogui.svg
   :target: https://pypi.python.org/pypi/discogui/
.. |Downloads| image:: https://img.shields.io/pypi/dm/discogui.svg
   :target: https://pypi.python.org/pypi/discogui/
.. |Code Health| image:: https://landscape.io/github/ponty/discogui/master/landscape.svg?style=flat
   :target: https://landscape.io/github/ponty/discogui/master
.. |Documentation| image:: https://readthedocs.org/projects/discogui/badge/?version=latest
   :target: https://readthedocs.org/projects/discogui/?badge=latest






