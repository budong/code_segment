#!/usr/bin/env python
#coding: utf-8

import os
import sys
import fnmatch
import sqlite3

if len(sys.argv) < 2:
    print 'No parameter specified.'
    sys.exit()

if sys.argv[1].startswith('--'):
    option = sys.argv[1][2:]
    if option == 'help':
        print '''
            ./walk.py /data1 /data2
              '''
    else:
        print 'Unknow option.'

DIR_LIST = sys.argv[1:]

def _check_vid(directory,vid):
    db_file = ''.join([directory,'/sina_vod.db'])
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute("select * from video where vid=%s" % vid)
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    return False


def check_file():
    patterns = ['*.hlv','*.flv','*.mp4','*.3gp']
    for directory in DIR_LIST:
        #data_dir = ''.join([directory,'/t'])
        #for root,dirs,files in os.walk(data_dir):
        for root,dirs,files in os.walk(directory):
            for extensions in patterns:
                for file in fnmatch.filter(files,extensions):
                    absolute_file = os.path.join(root,file)
                    vid = file.split(".")[0]
                    if not _check_vid(directory,vid):
                        print 'Delete file %s ' % absolute_file
                        #os.remove(absolute_file)
        
if __name__ == '__main__':
    check_file()
