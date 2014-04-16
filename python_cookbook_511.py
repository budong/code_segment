#!/usr/bin/env python2.7
#coding: utf-8

import urllib
def isContentType(URLorFile,contentType='text'):
    '''判断URL(urllib.urlopen访问的伪文件对象) 是否是要求的类型（默认为文本)'''
    try:
        if isinstance(URLorFile,str):
            thefile = urllib.urlopen(URLorFile)
        else:
            thefile = URLorFile
        result = thefile.info().getmaintype() == contentType.lower()
        if thefile is not URLorFile:
            thefile.close()
    except IOError:
        result = False #如果我们无法打开它，它什么类型也不是
    return result

print isContentType('http://42qu.cc/budong')
