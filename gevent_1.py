#!/usr/local/python2.7/bin/python2.7

import gevent

def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')

def bar():
    print('Running in bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

gevent.joinall([gevent.spawn(foo),gevent.spawn(bar),])
