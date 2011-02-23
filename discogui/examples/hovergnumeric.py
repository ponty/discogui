'''
1. start gnumeric on Xvfb with low ersolution
2. discover buttons using :mod:`discogui.hover` module
3. print rectangles
4. draw red rectangles on screenshot
'''
from discogui.draw import draw_indexed_rect_list
from discogui.hover import active_rectangles
from discogui.imgutil import autocrop
from easyprocess import EasyProcess
from pyscreenshot import grab
from pyvirtualdisplay import Display

def main():
    screen = Display(size=(640,480)).start()
    gnumeric= EasyProcess('gnumeric').start().sleep(2)
    
    img = grab()
    rectangles = active_rectangles()
    print rectangles
    
    gnumeric.stop()
    screen.stop()
    
    img = draw_indexed_rect_list(img, rectangles)
    img = autocrop(img)
    
    # display results
    img.show()

if __name__=='__main__':
    main()