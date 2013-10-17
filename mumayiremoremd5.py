#!/usr/local/python2.7/bin/python2.7
import os
import hashlib
import urllib2

from os.path import dirname,abspath

PREFIX = dirname(abspath(__file__))
IP_LIST = []
URI_LIST = [] 
URL_LIST = []

def get_remote_md5_sum(url):
    remote = urllib2.urlopen(url)

    hash = hashlib.md5()
 
    while True:
        data = remote.read(4096)
        if not data:
            break
        hash.update(data)
 
    return hash.hexdigest()
 

def get_remote_url():
    with open('%s/ip.txt' % PREFIX,'r') as ipfile:
        for line in ipfile:
            line = line.split('\n')[0] 
            IP_LIST.append(line)

    with open('%s/uri.txt' % PREFIX,'r') as urifile:
        for line in urifile:
            line = line.split('\n')[0]
            URI_LIST.append(line)

    for ip in IP_LIST:
        for uri in URI_LIST:
            URL_LIST.append(''.join(['http://',ip,uri]))

    return URL_LIST



with open('%s/md5.txt' % PREFIX,'w') as md5file:
    for url in get_remote_url(): 
        print url
        md5 = get_remote_md5_sum(url)
        md5file.write(url + ' ' + md5)
