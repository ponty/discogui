'''
simple xdotool wrapper.

There is no easy linux Sendkeys modul, 
I have found this tools:
 * `SendKeys<http://www.rutherfurd.net/python/sendkeys/>`
       - windows only
 * xmacro, xdotool, xaut
       - no python interface
 * `xautomation<http://sourceforge.net/projects/xautomation/>`
          - Python library to automate X11
          - hard to install
 * `pykey<http://www.shallowsky.com/software/crikey/pykey-0.1>`
          - no setup      

This  module is used until crossplatform Sendkey modul is developed.
'''    

from easyprocess import EasyProcess
import time

EasyProcess('xdotool --version').check()

MODIFIERS = [
  "alt",
  "ctrl",
  "control",
  "meta",
  "super",
  "shift",
]

tmp = dict([
  ("Return", '\n',),
  ("ampersand", '&',),
  ("apostrophe", '\'',),
  ("asciicircum", '^',),
  ("asciitilde", '~',),
  ("asterisk", '*',),
  ("at", '@',),
  ("backslash", '\\',),
  ("bar", '|',),
  ("braceleft", '(',),
  ("braceright", ')',),
  ("bracketleft", '[',),
  ("bracketright", ']',),
  ("colon", ':',),
  ("comma", ',',),
  ("dollar", '$',),
  ("equal", '=',),
  ("exclam", '!',),
  ("grave", '`',),
  ("greater", '>',),
  ("less", '<',),
  ("minus", '-',),
  ("numbersign", '#',),
  ("parenleft", '(',),
  ("parenright", ')',),
  ("percent", '%',),
  ("period", '.',),
  ("plus", '+',),
  ("question", '?',),
  ("quotedbl", '"',),
  ("semicolon", ';',),
  ("slash", '/',),
  ("space", ' ',),
  ("Tab", '\t',),
  ("underscore", '_',),
  ("Escape", '\x1b',),
        ])

#inverted dict
XDOTOOL_KEY_MAP = dict([[v, k] for k, v in tmp.items()])

def send_key(key):
    '''
    send one key
    '''    
    x=key
    modifier = ''
    for m in MODIFIERS:
        if x.startswith(m):
            x = x.replace(m + '+', '')
            modifier = m + '+'
            break
    x = XDOTOOL_KEY_MAP.get(x, x)
    x = modifier + x
    EasyProcess(cmd=["xdotool", 'key', x ]).call()

def send_key_list(keys, pause=0.05):
    '''
    send more keys
    
    :param pause: The number of seconds to wait between sending each key or key combination. (float)
    '''    
    for x in keys:
        time.sleep(pause)
        send_key(x)

def _test():
    send_key_list(['alt+f'])

if __name__ == '__main__':
    _test()  
   
