#!/usr/bin/env python2.7

def AddSysPath(new_path):
    import sys,os
    if not os.path.exists(new_path): return -1
    if sys.platform == 'win32':
        new_path = new_path.lower()
    for x in sys.path:
        x = os.path.abspath(x)
        if sys.platform == 'win32':
            x = x.lower()
        if new_path in (x,x + os.sep):
            return 0

    sys.path.append(new_path)
    return 1

if __name__ == '__main__':
    import sys
    print "Before:"
    for x in sys.path: print x
    if sys.platform == 'win32':
        pass
    else:
        print AddSysPath('/tmp')
    print 'After:'
    for x in sys.path: print x
