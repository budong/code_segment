#!/usr/local/python2.7/bin/python2.7
# -*- coding:utf8 -*-

import sys
from fabric.api import *

reload(sys)
sys.setdefaultencoding('utf-8')

env.connection_attempts = 3
env.timeout = 60
env.skip_bad_hosts = True
env.parallel = True

env.roledefs = {
        'sdyd':['root@120.192.86.204:2222','root@120.192.85.20:2222','root@120.192.85.21:2222',
                'root@120.192.85.22:2222','root@120.192.85.23:2222','root@120.192.85.18:2222',
                'root@120.192.85.19:2222','root@120.192.81.162:2222','root@120.192.81.163:2222',
                'root@120.192.81.165:2222','root@120.192.81.167:2222'],
        'sxyd':['root@183.203.9.133:12580','root@183.203.9.134:12580','root@183.203.9.135:12580'],
        'lntt':['root@222.33.192.42:2222','root@222.33.192.34:2222','root@222.33.192.36:2222',
                'root@222.33.192.37:2222','root@222.33.192.45:2222','root@222.33.192.55:2222'],
        'lnlt':['root@60.18.146.37:2222','root@60.18.146.38:2222','root@60.18.146.46:2222',
                'root@60.18.146.54:2222'],
        'cqyd':['root@221.180.146.95:2222','root@221.180.146.96:2222','root@221.180.146.97:2222',
                'root@221.180.146.98:2222']
        }

#'root@60.18.146.58:2222'


#@roles('sdyd')
#@roles('sxyd')
#@roles('lntt')
#@roles('lnlt')
#@roles('cqyd')
#@roles('sdyd','sxyd','lntt','lnlt','cqyd')
@roles('sdyd','sxyd','lnlt','cqyd')
def sync_root_sbin():
    #run('/usr/local/python2.7/bin/python2.7  /root/sbin/nginx_purge_cache.py')
    remote_dir = '/root/sbin'
    with cd(remote_dir):
        run('rsync -avzP 120.192.81.164::sbin /root/sbin/')

#@roles('sdyd')
#@roles('sxyd')
#@roles('lntt')
#@roles('lnlt')
#@roles('cqyd')
@roles('sdyd','sxyd','lntt','lnlt','cqyd')
def send_down_pv_to_center():
    run('/bin/sh /root/sbin/host_down_pv_num.sh')
    run('/usr/local/python2.7/bin/python2.7  /root/sbin/nginx_purge_cache.py')

