#!/usr/local/python2.7/bin/python2.7

from gevent import sleep
from gevent.pool import Pool
from gevent.coros import BoundedSemaphore

sem = BoundedSemaphore(2)

def worker1(n):
    sem.acquire()
    print('Worker  %i acquired semapore' % n)
    sleep(2)
    sem.release()
    print('Worker %i released semaphore' % n)

def worker2(n):
    with sem:
        print('Worker %i acquired semaphore' % n)
        sleep(2)
    print('Worker %i released semaphore' % n)

pool = Pool()
pool.map(worker1,xrange(0,2))
pool.map(worker2,xrange(3,6))
