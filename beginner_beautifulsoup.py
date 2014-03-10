#!/usr/bin/env python2.7
#coding: utf-8

from BeautifulSoup import BeautifulSoup
import urllib2
import re

url = urllib2.urlopen("http://python.org")
content = url.read()
soup = BeautifulSoup(content)
#links = soup.findAll("a")

for a in soup.findAll("a",href=True):
    if re.findall('python',a['href']):
        print "Found the url:",a['href']

