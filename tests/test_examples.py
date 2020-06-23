import sys

from backports.tempfile import TemporaryDirectory
from easyprocess import EasyProcess

py = sys.executable

# stdout_buttondiscovery = (
#     "[ScreenRect((426,415,509,445)), ScreenRect((515,415,598,445))]"
# )

# stdout_hovergnumeric = "[ScreenRect((4,26,34,57)), ScreenRect((35,26,65,57)), ScreenRect((66,26,96,57)), ScreenRect((111,26,141,57)), ScreenRect((142,26,172,57)), ScreenRect((187,26,217,57)), ScreenRect((218,26,248,57)), ScreenRect((249,26,279,57)), ScreenRect((4,58,99,89)), ScreenRect((100,58,130,89)), ScreenRect((131,58,161,89)), ScreenRect((162,58,192,89)), ScreenRect((207,58,237,89)), ScreenRect((238,58,268,89)), ScreenRect((269,58,299,89)), ScreenRect((300,58,330,89)), ScreenRect((331,58,361,89)), ScreenRect((362,58,392,89)), ScreenRect((407,58,437,89)), ScreenRect((4,90,34,121)), ScreenRect((35,90,65,121)), ScreenRect((66,90,96,121)), ScreenRect((97,90,127,121)), ScreenRect((128,90,158,121)), ScreenRect((159,90,189,121)), ScreenRect((190,90,220,121)), ScreenRect((221,90,251,121)), ScreenRect((252,90,282,121)), ScreenRect((283,90,313,121)), ScreenRect((314,90,344,121)), ScreenRect((345,90,375,121)), ScreenRect((376,90,406,121)), ScreenRect((265,123,295,154)), ScreenRect((57,311,465,317))]"

stdout_clickbutton = """1
0"""


def run_mod(mod, cwd, stdout=None):
    p = EasyProcess([py, "-m", mod], cwd=cwd).call()
    assert p.return_code == 0
    if stdout:
        assert p.stdout == stdout


def test_examples():
    with TemporaryDirectory() as tmpdirname:
        run_mod("discogui.examples.buttondiscovery", tmpdirname,)
        run_mod("discogui.examples.hovergnumeric", tmpdirname)
        run_mod("discogui.examples.clickbutton", tmpdirname, stdout_clickbutton)
