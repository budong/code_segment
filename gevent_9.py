#!/usr/local/python2.7/bin/python2.7

import gevent
import signal

def run_forever():
    gevent.sleep(1000)

if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT,gevent.shutdown)
    thread = gevent.spawn(run_forever)
    thread.join()
