#!/usr/bin/env python2.7
#coding: utf-8

#http://www.pythonforbeginners.com/network/python-modules-urllib2-user-agent/

import urllib2

response = urllib2.urlopen("http://www.python.org")
html = response.read()
#print html
print response.geturl()

headers = response.info()
print headers


#import urllib2
#req = urllib2.Request('http://192.168.1.2/')
#req.add_header('User-agent', 'Mozilla 5.10')
#res = urllib2.urlopen(req)
#html = res.read()
