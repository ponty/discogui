import glob
import logging
import os
from pathlib import Path

from easyprocess import EasyProcess
from entrypoint2 import entrypoint

commands = [
    "python3 -m discogui.examples.taborder",
    "python3 -m discogui.examples.hover",
    "python3 -m discogui.examples.clickbutton",
]


def empty_dir(dir):
    files = glob.glob(os.path.join(dir, "*"))
    for f in files:
        os.remove(f)


@entrypoint
def main():
    gendir = Path(__file__).absolute().parent / "gen"
    logging.info("gendir: %s", gendir)
    gendir.mkdir(exist_ok=True)
    empty_dir(gendir)
    pls = []
    try:
        os.chdir("gen")
        for cmd in commands:
            # with SmartDisplay() as disp:
            logging.info("cmd: %s", cmd)
            fname_base = cmd.replace(" ", "_")
            fname = fname_base + ".txt"
            logging.info("cmd: %s", cmd)
            print("file name: %s" % fname)
            with open(fname, "w") as f:
                f.write("$ " + cmd + "\n")
                p = EasyProcess(cmd).call()
                f.write(p.stdout)
                f.write(p.stderr)
                pls += [p]
    finally:
        os.chdir("..")
        for p in pls:
            p.stop()
    embedme = EasyProcess(["embedme", "../README.md"])
    embedme.call()
    print(embedme.stdout)
    assert embedme.return_code == 0
    assert "but file does not exist" not in embedme.stdout
