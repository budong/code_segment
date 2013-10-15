#!/usr/local/python2.7/bin/python2.7

import gevent
from gevent.event import Event

"""
Illustrates the use of events
"""

evt = Event()

def setter():
    '''After 3 seconds,wake all threads waiting on the value of evt'''
    print('A:Hey  wait for me,I have to do something')
    gevent.sleep(3)
    print("ok,I'm done")
    evt.set()

def waitter():
    '''After 3 seconds the get call will unblock'''
    print("I'll wait for you")
    evt.wait() #blocking
    print("It's about time")


def main():
    gevent.joinall([gevent.spawn(setter),
        gevent.spawn(waitter),
        gevent.spawn(waitter),
        gevent.spawn(waitter),
        gevent.spawn(waitter),
        gevent.spawn(waitter),
        ])
if __name__ == '__main__':
    main()



