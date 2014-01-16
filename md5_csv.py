#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import csv 
import hashlib

ALL = 0
COUNT = 0
DATA = []

def md5Checksum(filePath):
    with open(filePath, 'rb') as fh: 
        m = hashlib.md5()
        while True:
            data = fh.read(8192)
            if not data:
                break
            m.update(data)
        return m.hexdigest()

rightfile = open('/tmp/right.txt','w')
wrongfile = open('/tmp/wrong.txt','w')

reader = csv.reader(file('/root/sbin/bgp163bothwpq.txt','rb'))
for id,md5,filepath in reader:
    ALL += 1
    fullfilepath = ''.join(['/data/mumayi/soft/',filepath])
    if os.path.isfile(fullfilepath):
        rightmd5 = md5Checksum(fullfilepath)
        if md5 == rightmd5:
            COUNT += 1
            rightfile.write('%s\n' % filepath)
        else:
            DATA.append((id,md5,filepath))
            wrongfile.write('%s,\n' % id)
    else:
        DATA.append((id,md5,filepath))
        wrongfile.write('%s,\n' % id)
rightfile.close()
wrongfile.close()

print "总共：%s" % ALL
print "正确：%s" % COUNT
#data = [("a",'1'),('b','1')]
writer = csv.writer(file('/tmp/bgp163bothwpq.txt','wb'))
writer.writerows(DATA)
