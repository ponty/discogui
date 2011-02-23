'''
1. start zenity Yes/No dialog on Xvfb
2. discover buttons using :mod:`discogui.buttons` module
3. print rectangles
4. draw red rectangles on screenshot
'''
from easyprocess import EasyProcess
from pyscreenshot import grab
from discogui.buttons import discover_buttons
from discogui.draw import draw_indexed_rect_list
from discogui.imgutil import autocrop
from pyvirtualdisplay import Display

def main():
    screen = Display().start()
    zenity= EasyProcess('zenity --question').start().sleep(1)
    
    img = grab()
    rectangles = discover_buttons()
    print rectangles
    
    zenity.stop()
    screen.stop()
    
    img = draw_indexed_rect_list(img, rectangles)
    img = autocrop(img)
    
    # display results
    img.show()

if __name__=='__main__':
    main()    