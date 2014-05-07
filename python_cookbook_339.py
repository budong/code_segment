#!/usr/bin/env python2.7
#coding: utf-8

def wrap_callable(any_callable,before,after):
    '''用before/after调用将任何可调用体封装起来'''
    def _wrapped(*a,**kw):
        before()
        try:
            return any_callable(*a,**kw)
        finally:
            after()
    #只针对python 2.4: _wrapped.__name__ = any_callable__name__
    return _wrapped

import inspect
class GenericWrapper(object):
    #'''将对象的所有方法用before/after调用封装起来'''
#    def __init__(self,obj,before,after,ignore=()):
#        #我们必须设置__dict__来绕过__setattr__;因此，
#        #我们需要重现带下划线的名字
#        #we need to reproduce the name-mangling for double-underscores
#        classname = 'GenericWrapper'
#        self.__dict__['_%s__methods' % classname] = {}
#        self.__dict__['_%s__obj' % classname] = obj
#        for name,method in inspect.getmembers(obj,inspect.ismethod):
#            if name not in ignore and method not in ignore:
#                self.__methods[name] = wrap_callable(method,before,after)

        def print_self(self):
            print self.__dict__

        def __getattr__(self,name):
            try:
                return self.__methods(name)
            except KeyError:
                return getattr(self.__obj,name)
        def __setattr__(self,name,value):
            setattr(self.__obj,name,value)

class SynchronizedObject(GenericWrapper):
    '''封装一个对象及其所有的方法，支持同步'''
    def __init__(self,obj,ignore=(),lock=None):
        if lock is None:
            import threading
            lock = threading.RLock()
            GenericWrapper.__init__(self,obj,lock.acquire,lock.release,ignore)

if __name__ == '__main__':
    import threading
    import time
    class Dummy(object):
        def foo(self):
            print 'hello from foo'
            time.sleep(1)
        def bar(self):
            print 'hello from bar'
        def baaz(self):
            print 'hello from baaz'
    g = GenericWrapper()
    g.print_self()
    #tw = SynchronizedObject(Dummy(),ignore=['baaz'])
    #threading.Thread(target=tw.foo).start()
    #time.sleep(0.1)
    #threading.Thread(target=tw.bar).start()
    #time.sleep(0.1)
    #threading.Thread(target=tw.baaz).start()

