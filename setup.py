import os.path

from setuptools import setup

NAME = "discogui"

# get __version__
__version__ = None
exec(open(os.path.join(NAME, "about.py")).read())
VERSION = __version__

URL = "https://github.com/ponty/discogui"
DESCRIPTION = "GUI discovery"
LONG_DESCRIPTION = """Experimental Python library for discovering GUI elements.

Documentation: https://github.com/ponty/discogui/tree/"""
LONG_DESCRIPTION += VERSION
PACKAGES = [
    "discogui",
    "discogui.examples",
]


# extra = {}
# if sys.version_info >= (3,):
#     extra["use_2to3"] = True
#     extra["use_2to3_exclude_fixers"] = ["lib2to3.fixes.fix_import"]

classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
]

install_requires = [
    "pillow",
    "path.py",
    "PyUserInput",
    "PyScreenshot",
    "easyprocess",
    "pyvirtualdisplay",
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=classifiers,
    keywords="GUI",
    author="ponty",
    # author_email='',
    url=URL,
    license="BSD",
    packages=PACKAGES,
    install_requires=install_requires,
)
