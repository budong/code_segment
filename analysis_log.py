#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import os
import re
import gzip
from datetime import datetime
from datetime import timedelta

YEAR=datetime.now().strftime('%Y')
MONTH=datetime.now().strftime('%m')
DAY=(datetime.now()-timedelta(days=1)).strftime('%d')
TODAY=(datetime.now()-timedelta(days=1)).strftime('%Y%m%d')

PREFIX_DONE='/data/logs/ananlysis/'
BASE_DIR='/data/logs/rotate/'
DATE_DIR=''.join([YEAR,'/',MONTH,'/',DAY])
LOG_DIR=''.join([BASE_DIR,DATE_DIR])

CHANGE_40X_LOG = ''.join([PREFIX_DONE,'change_40X_log',TODAY,'.log'])
NOT_CHANGE_40X_LOG = ''.join([PREFIX_DONE,'not_change_40X_log',TODAY,'.log'])

CHANGE_50X_LOG = ''.join([PREFIX_DONE,'change_50X_log',TODAY,'.log'])
NOT_CHANGE_50X_LOG = ''.join([PREFIX_DONE,'not_change_50X_log',TODAY,'.log'])

change_40X_log=open('%s' % CHANGE_40X_LOG,'w')
not_change_40X_log=open('%s' % NOT_CHANGE_40X_LOG,'w')

change_50X_log=open('%s' % CHANGE_50X_LOG,'w')
not_change_50X_log=open('%s' % NOT_CHANGE_50X_LOG,'w')

for i in ['00','04','08','12','16','20']:
    ACCESS_LOG_FILE=''.join([LOG_DIR,'/',i,'/','apk.a.log.gz'])
    if os.path.isfile(ACCESS_LOG_FILE):
        with gzip.open('%s' % ACCESS_LOG_FILE,'rb') as access_log_file :
            for line in access_log_file:
                pattern = re.compile(r' ')
                line_list = pattern.split(line)
                http_status = line_list[8]
                if http_status in ['500','501','502','503','504','505']:
                    change_50X_log.write(http_status + ' ' + line_list[0] + ' ' + line_list[3] + ' ' + line_list[6] + '\n')
                    not_change_50X_log.write(line + '\n')
                elif http_status == '404':
                    change_40X_log.write(http_status + ' ' + line_list[0] + ' ' + line_list[3] + ' ' + line_list[6] + '\n')
                    not_change_40X_log.write(line + '\n')

change_40X_log.close()
not_change_40X_log.close()
change_50X_log.close()
not_change_50X_log.close()


