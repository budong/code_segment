#!/usr/local/python/bin/python2.7
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

#notexistfile = open('/tmp/not_exist_2.txt','w')
rightfile = open('/tmp/right_10.txt','w')
wrongfile = open('/tmp/wrong_10.txt','w')

with open('/root/src/wrong_id_md5_path_6.txt','r') as reader:
    for line in reader:
        line = line.split(',')
        if len(line) == 3: 
            id = line[0].strip()
            md5 = line[1].strip()
            filepath =  line[2].strip('\n')
            filepath = filepath.strip()
            filepath = filepath.strip('"')
            ALL += 1
            fullfilepath = ''.join(['/data/mumayi/soft/',filepath])
            print id
            if os.path.isfile(fullfilepath):
                rightmd5 = md5Checksum(fullfilepath)
                if md5 == rightmd5:
                    COUNT += 1
                    rightfile.write('%s\n' % filepath)
                else:
                    DATA.append((id,md5,filepath))
                    wrongfile.write('%s,\n' % id)
                    #wrongfile.write('%s,%s,%s\n' % (id,md5,filepath))
            else:
                DATA.append((id,md5,filepath))
                wrongfile.write('%s,\n' % id)
                #notexistfile.write('%s\n' % filepath)
rightfile.close()
wrongfile.close()

print "总共：%s" % ALL
print "正确：%s" % COUNT
print "错误：%s" % (ALL - COUNT)
#data = [("a",'1'),('b','1')]
writer = csv.writer(file('/tmp/wrong_id_md5_path_10.txt','wb'))
writer.writerows(DATA)
