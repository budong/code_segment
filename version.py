#!/usr/bin/env python2.7

def VersionFile(file_spec,vtype='copy'):
    import os,shutil
    if os.path.isfile(file_spec):
        if vtype not in ('copy','rename'):
            raise ValueError,'Unknown vtype %r' % (vtype,)
        n,e = os.path.splitext(file_spec)
        if len(e) == 4 and e[1:].isdigit():
            num = 1 + int(e[1:])
            root = n 
        else:
            num = 0 
            root = file_spec
        for i in xrange(num,100):
            new_file = '%s.%03d' % (root,i)
            if not os.path.exists(new_file):
                if vtype == 'copy':
                    shutil.copy(file_spec,new_file)
                else:
                    os.rename(file_spec,new_file)
                return True
        raise RuntimeError,"Can't%s%r,all names names taken" % (vtype,file_spec)
    return False

if __name__ == '__main__':
    import os
    tfn = '/tmp/test.txt'
    open(tfn,'w').close()
    print VersionFile(tfn)
    print VersionFile(tfn)
    print VersionFile(tfn)
    #for x in ('','.000','.001','.002'):
    #    os.unlink(tfn + x)
    #print VersionFile(tfn)
    #print VersionFile(tfn)


