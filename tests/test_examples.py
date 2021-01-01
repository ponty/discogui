import sys
from tempfile import TemporaryDirectory

from easyprocess import EasyProcess

py = sys.executable

stdout_taborder = "[ScreenRect((4"
stdout_hover = "[ScreenRect((2"
stdout_clickbutton = """1
0"""


def run_mod(mod, cwd, stdout=None):
    p = EasyProcess([py, "-m", mod], cwd=cwd).call()
    assert p.return_code == 0
    if stdout:
        assert p.stdout.startswith(stdout)


def test_examples():
    with TemporaryDirectory() as tmpdirname:
        run_mod("discogui.examples.taborder", tmpdirname, stdout_taborder)
        run_mod("discogui.examples.hover", tmpdirname, stdout_hover)
        run_mod("discogui.examples.clickbutton", tmpdirname, stdout_clickbutton)
