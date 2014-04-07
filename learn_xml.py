#!/usr/bin/env python2.7
#coding: utf-8

#http://docs.python.org/2/library/xml.etree.elementtree.html

import xml.etree.ElementTree as ET
#tree = ET.parse('/Users/budong/code_segment/example_xml.txt')
#root = tree.getroot()
#print root

with open('/Users/budong/code_segment/example_xml.txt') as fh:
    data = fh.read()

root = ET.fromstring(data)
print root
