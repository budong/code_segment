#!/usr/bin/env python2.7
#coding: utf-8

import time

def u1():
    print 'start u1'
    time.sleep(20)
    print 'end u1'

def u2():
    print 'start u2'
    time.sleep(20)
    with open('/tmp/u2.txt','w') as file:
        file.write('u2\n')
    print 'end u2'

if __name__ == '__main__':
    u1()
    u2()
