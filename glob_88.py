#!/usr/bin/env python2.7

import glob,os

def all_files(pattern,search_path,pathsep=os.pathsep):
    for path in search_path.split(pathsep):
        for match in glob.glob(os.path.join(path,pattern)):
            yield match

print list(all_files('*.py',os.environ['PATH']))
for match in  all_files('*.py',os.environ['PATH']):
    print match

#if __name__ == '__main__':
#    import sys
#    if len(sys.argv) !=2 or sys.argv[1].startswith('-'):
#        print 'Use: %s <pattern>' % sys.argv[0]
#        sys.exit(1)
#    matches = list(all_files(sys.argv[1],os.environ['PATH']))
#    print '%d match:' % len(matches)
#    for match in matches:
#        print match
