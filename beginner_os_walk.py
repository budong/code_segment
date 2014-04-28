#!/usr/bin/env python2.7
#coding: utf-8

import os
from os.path import join,getsize

for root,dirs,files in os.walk("/Users/budong/Downloads/my_project/sina"):
    print "root :",root
    print "dirs :",dirs
    print "files :",files

    #print root,"consumes",
    #print sum([getsize(join(root,name)) for name in files]),
    #print "bytes in",len(files),"non-directory files"

import fnmatch

#rootpath = '/home'
#pattern = '*.mp3'

#for root,dirs,files in os.walk(rootpath):
#    for filename in fnmatch.filter(files,pattern):
#        print(os.path.join(root,filename))

#images = ['*.jpg', '*.jpeg', '*.png', '*.tif', '*.tiff']
#matches = []
#
#for root,dirnames,filenames in os.walk(rootpath):
#    for extensions in images:
#        for filename in fnmatch.filter(filenames,extensions):
#            matches.append(os.path.join(root,filename))
#
#print matches
