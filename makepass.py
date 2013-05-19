#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""产生随机密码"""

from random import choice
import string

def GenPasswd(length=8,chars=string.letters+string.digits):
    return ''.join([choice(chars) for i in range(length)])

for i in range(6):
    print GenPasswd(12)
