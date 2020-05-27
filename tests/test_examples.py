import sys

from backports.tempfile import TemporaryDirectory
from easyprocess import EasyProcess

py = sys.executable


def run_mod(mod, cwd):
    p = EasyProcess([py, "-m", mod], cwd=cwd).call()
    assert p.return_code == 0


def test_examples():
    with TemporaryDirectory() as tmpdirname:
        run_mod("discogui.examples.buttondiscovery", tmpdirname)
        run_mod("discogui.examples.hovergnumeric", tmpdirname)
        run_mod("discogui.examples.clickbutton", tmpdirname)
