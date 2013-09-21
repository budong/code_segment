#!/usr/local/python2.7/bin/python2.7
# -*- coding:utf8 -*-

#pip install python-memcached

import memcache
mc = memcache.Client(['127.0.0.1:11211'],debug=True)
mc.set('name','budongzhenren',60)
print mc.get('name')
mc.delete('name')

