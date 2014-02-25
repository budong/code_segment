#!/usr/bin/env python2.7
#coding: utf-8

import os

items = os.listdir("/root")

newlist = []
for names in items:
    if names.endswith(".log"):
            newlist.append(names)

print newlist
