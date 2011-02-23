from easyprocess import EasyProcess
from pyscreenshot import grab
from discogui.imgutil import autocrop, focus_wnd
from discogui.sendkeys import send_key_list
from pyvirtualdisplay import Display
import time


def main():
    screen = Display()
    screen.start()
    
    gcalctool = EasyProcess('gcalctool').start()
    
    # wait for displaying the window
    time.sleep(0.2)
    
    focus_wnd()
    
    send_key_list(['2', '*', '2', '=', '\n'])
    
    img = autocrop(grab())
    
    gcalctool.stop()
    screen.stop()
    
    # after stopping screen!
    img.show()

if __name__=='__main__':
    main()