#!/usr/local/python2.7/bin/python2.7
# -*- coding:utf8 -*-

#env.hosts = ['user1@host1:port1', 'user2@host2.port2']
#env.gateway = 'root@118.26.228.50:2222'
#env.passwords = {'user1@host1:port1': 'password1', 'user2@host2.port2': 'password2'}


import sys
from fabric.api import *

reload(sys)
sys.setdefaultencoding('utf-8')

env.connection_attempts = 3
env.timeout = 60
env.skip_bad_hosts = True
env.parallel = True

env.roledefs = {
        'dxt':['root@124.193.120.170:2222'],}

#env.hosts = [
#'host1',
#'host2'
#]
#env.passwords = {
#    'host1': "pwdofhost1",
#    'host2': "pwdofhost2",
#}
#
#或者
#env.roledefs = {
#'testserver': ['host1', 'host2'],
#'realserver': ['host3', ]
#}
#env.passwords = {
#    'host1': "pwdofhost1",
#    'host2': "pwdofhost2",
#    'host3': "pwdofhost3",
#}

#env.roledefs = {
#        'sdyd':['root@120.192.86.204:2222','root@120.192.85.20:2222','root@120.192.85.21:2222',
#                'root@120.192.85.22:2222','root@120.192.85.23:2222','root@120.192.85.18:2222',
#                'root@120.192.85.19:2222','root@120.192.81.162:2222','root@120.192.81.163:2222',
#                'root@120.192.81.165:2222','root@120.192.81.167:2222'],
#        'sxyd':['root@183.203.9.133:12580','root@183.203.9.134:12580','root@183.203.9.135:12580'],
#        'lntt':['root@222.33.192.42:2222','root@222.33.192.34:2222','root@222.33.192.36:2222',
#                'root@222.33.192.37:2222','root@222.33.192.45:2222','root@222.33.192.55:2222'],
#        'lnlt':['root@60.18.146.37:2222','root@60.18.146.38:2222','root@60.18.146.46:2222',
#                'root@60.18.146.54:2222'],
#        'cqyd':['root@221.180.146.95:2222','root@221.180.146.96:2222','root@221.180.146.97:2222',
#                'root@221.180.146.98:2222']
#        }
#
#'root@60.18.146.58:2222'


#@roles('sdyd')
#@roles('sxyd')
#@roles('lntt')
#@roles('lnlt')
#@roles('cqyd')
#@roles('sdyd','sxyd','lntt','lnlt','cqyd')
#@roles('sdyd','sxyd','lnlt','cqyd')
#def sync_root_sbin():
#    #run('/usr/local/python2.7/bin/python2.7  /root/sbin/nginx_purge_cache.py')
#    remote_dir = '/root/sbin'
#    with cd(remote_dir):
#        run('rsync -avzP 120.192.81.164::sbin /root/sbin/')
#
#@roles('sdyd')
#@roles('sxyd')
#@roles('lntt')
#@roles('lnlt')
#@roles('cqyd')
#@roles('sdyd','sxyd','lntt','lnlt','cqyd')
#def send_down_pv_to_center():
#    run('/bin/sh /root/sbin/host_down_pv_num.sh')
#    run('/usr/local/python2.7/bin/python2.7  /root/sbin/nginx_purge_cache.py')
#

@roles('dxt')
def host_type():
    run('uname -s')

@roles('dxt')
def host_df():
    run('df -h')

@roles('dxt')
def upload():
    #在远端机器上建立目录
    run('mkdir /home/src')
    #上传文件
    put('/root/code_segment','/home/src')

@roles('dxt')
def download():
    #将远端的/hom/test下载到本地/home
    get('/home/test','/home')

def ls_local():
    local('ls')


@roles('dxt')
def touch_file():
    remote_dir = '/home/test'
    with cd(remote_dir):
        run('touch d')

@roles('dxt')
def stop_nginx():
    run('/usr/local/nginx/sbin/nginx -s stop')


@roles('dxt')
def start_nginx():
    run('/usr/local/nginx/sbin/nginx')
@roles('dxt')
def run_test():
    run('sh /root/sbin/test.sh')


def uptime():
    local('uptime')

def hello1():
    print("Hello world!")

def hello2(name="world"):
    print("Hello %s!" % name)

