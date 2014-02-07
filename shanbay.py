#!/usr/local/python2.7/bin/python2.7
# -*- coding: utf-8 -*-

import re

line_pattern = re.compile(r' ')
word_pattern = re.compile(r'[a-z]+')
file = open("/root/sbin/danci.txt","r")
list = file.readlines()
print list
#with open("/root/sbin/danci.txt","r") as file:
#    for line in file:
#        print line
