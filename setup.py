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


classifiers = [
    # Get more strings from
    # http://www.python.org/pypi?%3Aaction=list_classifiers
    "License :: OSI Approved :: BSD License",
    "Natural Language :: English",
    "Operating System :: OS Independent",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]

install_requires = [
    "pillow",
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
    long_description_content_type="text/x-rst",
    classifiers=classifiers,
    keywords="GUI",
    author="ponty",
    # author_email='',
    url=URL,
    license="BSD",
    packages=PACKAGES,
    install_requires=install_requires,
    # package_data={
    #     NAME: ["py.typed"],
    # },
)
