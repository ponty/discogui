import pymouse
import sys



def PyMouse():
    '''
    wrapper, turn off print coming from Xlib.ext.randr
    '''
    #Quick, turn off printing!
    class dummyStream:
        ''' dummyStream behaves like a stream but does nothing. '''
        def __init__(self): pass
        def write(self, data): pass
        def read(self, data): pass
        def flush(self): pass
        def close(self): pass
    # Copy old print deals
    old = sys.stdout
    # redirect all print deals
    sys.stdout = dummyStream()
    
    #call your verbose function here
    m = pymouse.PyMouse()
    
    #Turn printing back on!
    sys.stdout = old
    
    return m  
