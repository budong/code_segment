#!/usr/local/python2.7/bin/python2.7

import gevent.monkey
gevent.monkey.patch_socket()

import gevent
import urllib2
import simplejson as json

def fetch(pid):
    response = urllib2.urlopen('http://xmlso.mumayi.com/v16/indexnew.php')
    result = response.read()
    json_result = json.loads(result)
    title = json_result['11']['title']
    
    print('Process %s: %s' % (pid,title))
    return json_result['11']['title']

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch,i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()
print('Asynchronous:')
asynchronous()

