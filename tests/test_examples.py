import sys

from backports.tempfile import TemporaryDirectory
from easyprocess import EasyProcess

py = sys.executable

stdout_taborder = "[ScreenRect((425,415,510,445)), ScreenRect((514,415,599,445))]"
stdout_hover = "[ScreenRect((233,271,318,302)), ScreenRect((322,271,407,302))]"
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
