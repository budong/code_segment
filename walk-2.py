#!/usr/bin/env python
#coding: utf-8

import os
import re
import sqlite3

TRANSMIT_CONFIG = '/data1/vod/transmitd/transmitd_config.ini'
PATTERN = re.compile('(disk=)(.*)')

def _produce_dir():
    '''generate cache data directory'''
    fh = open(TRANSMIT_CONFIG,'r')
    try:
        for line in fh:
            line_re = PATTERN.match(line)
            if line_re:
                disk_string = line_re.groups()[1]
                disk_string = disk_string.strip(' ')
                disk_list = disk_string.split(',')
                return disk_list
    finally:
        fh.close()

def _check_vid(directory,vid):
    '''check file's vid whether in sqlitedb '''
    db_file = ''.join([directory,'/sina_vod.db'])
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("select * from video where vid=%s" % vid)
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    return False

def _check_file(name):
     '''check whether filename contan "." and vid is digit'''
     name = name.split('.')
     if len(name) != 2:
         return False
     vid = name[0]
     if not vid.isdigit():
         return False
     return vid

def delete_file(directory):
    '''delete file which vid not in sqlitedb'''
    data_dir = ''.join([directory,'/t'])
    for root,dirs,files in os.walk(data_dir):
        for file in files:
            absolute_file = os.path.join(root,file)
            if _check_file(file):
                vid = _check_file(file)
                if not _check_vid(directory,vid):
                    print 'Delete file %s ' % absolute_file
                    #os.remove(absolute_file)
            else:
                print 'Delete file %s ' % absolute_file
                #os.remove(absolute_file)
        
if __name__ == '__main__':
    DIR_LIST = _produce_dir()
    for dir in DIR_LIST: 
        delete_file(dir)
