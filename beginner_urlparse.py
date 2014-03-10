#!/usr/bin/env python2.7
#coding: utf-8

import urlparse

url = "http://python.org"
domain = urlparse.urlsplit(url)[1].split(':')[0]
print "The domain name of the url is: ",domain
