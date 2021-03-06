#!/usr/local/python2.7/bin/python2.7
#https://gist.github.com/brianewing/994303
import os, hashlib, urllib2, optparse

def get_remote_md5_sum(url, max_file_size=100*1024*1024):
    remote = urllib2.urlopen(url)
    hash = hashlib.md5()
 
    total_read = 0
    while True:
        data = remote.read(4096)
        #total_read += 4096
 
        if not data or total_read > max_file_size:
            break
 
        hash.update(data)
 
    return hash.hexdigest()
 
if __name__ == '__main__':
    opt = optparse.OptionParser()
    opt.add_option('--url', '-u', default='http://apkd.mumayi.com/2013/08/01/0/1/mumayidianzishichangMumayiMarket_V1.7.2_mumayi_7a9f5.apk')
 
    options, args = opt.parse_args()
    print get_remote_md5_sum(options.url)
