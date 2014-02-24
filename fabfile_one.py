#!/usr/local/python2.7/bin/python2.7
# -*- coding:utf8 -*-

import sys 
import time
from fabric.api import *

reload(sys)
sys.setdefaultencoding('utf-8')

#ssh 尝试连接的次数
env.connection_attempts = 3 
#不再读取本机的known_hosts,防止出现key变了，发生异常
env.disable_known_hosts = True
#网络超时时间
env.timeout = 60
#跳过有问题的ip
env.skip_bad_hosts = True
#任务并行
#env.parallel = True

env.roledefs = { 
        'sdyd_one':[],
        'sdyd_two':[],
        'sdyd_three':[],
        'sdyd_four':[]
}

@roles('sdyd_one')
def rm_apk_source():
    put("/tmp/apk_list.txt","/usr/local/bin/apk_list.txt")
    run("/bin/sed  's/^/\/bin\/rm -rf \/data\/mumayi\/soft/' /usr/local/bin/apk_list.txt  > /usr/local/bin/apk_list.sh")
    run("/bin/sh /usr/local/bin/apk_list.sh")

@roles('sdyd_two','sdyd_three')
def rm_apk_cache():
    put('/tmp/apk_list.txt','/usr/local/bin/apk_list.txt')
    run('/bin/sh /usr/local/bin/nginx_purge_cache.sh')
    run('/usr/local/nginx/sbin/nginx -s stop')
    time.sleep(3)
    run('/usr/local/nginx/sbin/nginx')

@roles('sdyd_four')
def rm_ats_cache():
    run('/bin/sh /usr/local/bin/rm_cache.sh')

def all():
    execute(rm_apk_source)
    execute(rm_apk_cache)
    execute(rm_ats_cache)
