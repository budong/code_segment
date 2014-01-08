#!/usr/bin/env python2.7

import random

NUM = [ i for i in xrange(10) ]
file = open('/tmp/name_num.txt','w')

while 1:
    if NUM:
        name = raw_input("Input your name:")
    else:
        break
    number = random.choice(NUM)
    print '%s:%s' % (name,number)
    file.write('%s:%s\n' % (name,number))
    NUM.remove(number)

file.close()
