#!/usr/bin/env python
#coding: utf-8

from __future__ import division
import os
import re
import fnmatch

pattern = re.compile('(\d+\.\w+)')

FILE = os.path.join(os.path.dirname(__file__), "20140610.log")
ALL = 0
NOT_FOUND = 0
VID = {}

fh = open(FILE,"r")
for line in fh:
    ALL = ALL + 1
    if line.split(" ")[9] == '404':
        video = pattern.search(line.split(" ")[7])
        if video:
            video = video.group()
            VID[video] = VID.get(video,1) + 1
        ##print line.split(" ")
        NOT_FOUND = NOT_FOUND + 1

print "ALL: %s" % ALL
print "NOT_FOUND: %s"  % NOT_FOUND
print "404比例: %s" % str(int(NOT_FOUND)/int(ALL))
print "######"
print "video 404文件 次数\n"
V = {}
for k,v in VID.iteritems():
    files = ['*.mp4','*.hlv','*.flv']
    for file in files:
        if fnmatch.fnmatch(k,file):
            #print k,v
            V[v] = k

V_L = sorted(V.items(), key=lambda V:V[0],reverse=True)
for i in V_L:
    print i[0],i[1]
