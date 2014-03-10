#!/usr/bin/env python2.7
#coding: utf-8

s = ['a111','b222','c333','d444','e555']

found = False

for c in s:
    if c.startswith("c"):
        found = True
        print u"发现c开头的项"
        break

if not found:
    print u"没有发现c开头的项"

for c in s:
    if c.startswith("c"):
        print u"发现c开头的项"
        break
else:
    print u"没有发现c开头的项"
