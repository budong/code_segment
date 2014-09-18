#!/usr/local/python2.7/bin/python2.7
# -*- coding:utf8 -*-

import sys
from os.path import dirname, abspath

import xlrd

reload(sys)
sys.setdefaultencoding('utf-8')
PREFIX = dirname(abspath(__file__))


data = xlrd.open_workbook('/root/sbin/mumayi.xls')
table = data.sheets()[0] 
col_5=table.col_values(5)
with open('%s/data.txt' % PREFIX,'a') as file:
    for col in col_5:
        file.write(col+'\n')

#参考地址：http://www.cnblogs.com/lhj588/archive/2012/01/06/2314181.html
#http://www.gocalf.com/blog/python-read-write-excel.html
