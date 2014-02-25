#!/usr/bin/env python2.7
#coding: utf-8

import os
from os.path import join,getsize

for root,dirs,files in os.walk("/var/log"):
    #print "root :",root
    #print "dirs :",dirs
    #print "files :",files

    print root,"consumes",
    print sum([getsize(join(root,name)) for name in files]),
    print "bytes in",len(files),"non-directory files"
