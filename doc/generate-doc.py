import logging
import os

from easyprocess import EasyProcess
from entrypoint2 import entrypoint

from pyvirtualdisplay.smartdisplay import SmartDisplay

# (cmd,grab,background)
commands = [
    "python3 -m discogui.examples.basic",
    "python3 -m discogui.examples.buttondiscovery",
    "python3 -m discogui.examples.hovergnumeric",
    "python3 -m discogui.examples.clickbutton",
]


@entrypoint
def main():
    pls = []
    try:
        os.chdir("gen")
        for cmd in commands:
            with SmartDisplay() as disp:
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
    embedme = EasyProcess(["npx", "embedme", "../README.md"])
    embedme.call()
    print(embedme.stdout)
    assert embedme.return_code == 0
    assert not "but file does not exist" in embedme.stdout
