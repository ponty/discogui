import sys

from backports.tempfile import TemporaryDirectory
from easyprocess import EasyProcess

py = sys.executable

stdout_taborder = "[ScreenRect((425,413,510,447)), ScreenRect((514,413,599,447))]"
stdout_hover = "[ScreenRect((233,269,318,304)), ScreenRect((322,269,407,304))]"
stdout_clickbutton = """1
0"""


def run_mod(mod, cwd, stdout=None):
    p = EasyProcess([py, "-m", mod], cwd=cwd).call()
    assert p.return_code == 0
    if stdout:
        assert p.stdout == stdout


def test_examples():
    with TemporaryDirectory() as tmpdirname:
        run_mod("discogui.examples.taborder", tmpdirname, stdout_taborder)
        run_mod("discogui.examples.hover", tmpdirname, stdout_hover)
        run_mod("discogui.examples.clickbutton", tmpdirname, stdout_clickbutton)
