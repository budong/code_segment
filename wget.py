#!/usr/bin/env python2.7
#coding: utf-8

import sys,urllib
def reporthook(*a): print a

for url in sys.argv[1:]:
    i = url.rfind('/')
    file = url[i+1:]
    print url,"->",file
    urllib.urlretrieve(url,file,reporthook)
