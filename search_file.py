#!/usr/bin/env python2.7

import os

def search_file(filename,search_path,pathsep=os.pathsep):
    for path in search_path.split(pathsep):
        candidate = os.path.join(path,filename)
        if os.path.isfile(candidate):
            return os.path.abspath(candidate)
        return None


if __name__ == '__main__':
    search_path = '/bin' + os.pathsep + '/usr/bin'
    find_file = search_file('ls',search_path)
    if find_file:
        print "File 'ls' found at %s" % find_file
    else:
        print "File 'ls' not found"
