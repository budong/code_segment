#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import re

LOG_FILE='/data/logs/ananlysis/change_50X_log20130501.log'

with open('%s' % LOG_FILE,'rb') as log_file:
    hour_dic = {}
    count = 0
    for line in log_file:
        pattern=re.compile(r' ')
        line_list=pattern.split(line)
        hour_pattern=re.compile(r'((.*)2013:([0-9]+):([0-9]+):([0-9]+))')
        hour = hour_pattern.match(line_list[2])
        hour =  hour.group(3)       
        if hour in hour_dic:
            hour_dic[hour] = hour_dic[hour] + 1
        else:
            hour_dic[hour] = 1
    print "小时" + ' ' + "次数"
    for i in hour_dic:
        count = count + hour_dic[i]
        print i,hour_dic[i]
    print "共" + ' ' + str(count)
        
