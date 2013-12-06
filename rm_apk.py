#!/usr/bin/env python
import os
import shutil

file = open('/root/sbin/delsoft.txt','r')
log = open('/tmp/rm_soft.log','w')
for dir in file:
    dir = dir.strip('\r\n')
    if len(dir) > 48:
        #print len(dir)
        shutil.rmtree(dir,True,None)
        log.write("Rm %s \n" % dir)

file.close()
log.close()
