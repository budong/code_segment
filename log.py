#!/usr/bin/env python

import re

DICT = {}

f = open("/data/logs/rotate/2013/11/05/04/www.mumayi.com.a.log_bak","r")
w = open("/tmp/dict.txt",'w')
for line in f:
    pattern = re.compile(r' ')
    line_list = pattern.split(line)
    if line_list[6] in DICT:
        try:    
            http_body_sent = int(line_list[9])
        except ValueError:
            http_body_sent = '0'
        DICT[line_list[6]] += http_body_sent
    else:   
        try:    
            http_body_sent = int(line_list[9])
        except ValueError:
            http_body_sent = '0'
        DICT[line_list[6]] = http_body_sent

DICT= sorted(DICT.iteritems(), key=lambda d:d[1], reverse = True) 
w.write(str(DICT))
f.close()
w.close()
