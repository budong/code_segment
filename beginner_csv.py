#!/usr/bin/env python2.7
#coding: utf-8

import csv 

#with open('/tmp/csv.txt','rb') as fh:
#    reader = csv.reader(fh)
#    for row in reader:
#        print row

ifile = open('/tmp/csv.txt','rb')
reader = csv.reader(ifile)

ofile = open('/tmp/csv.csv','wb')
writer = csv.writer(ofile,delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for row in reader:
    print row
    writer.writerow(row)


ifile.close()
ofile.close()
