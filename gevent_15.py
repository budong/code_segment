#!/usr/local/python2.7/bin/python2.7

import gevent
from gevent.event import AsyncResult

a = AsyncResult()


def setter():
    '''
    After 3 seconds set the result of a.
    '''
    gevent.sleep(3)
    a.set('Hello!')

def waitter():
    '''
    After 3 seconds the get call will unblock after the setter
    puts a value into the AsyncResult.
    '''
    print(a.get())

gevent.joinall([gevent.spawn(setter),gevent.spawn(waitter)])
