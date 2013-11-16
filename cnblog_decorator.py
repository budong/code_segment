#!/usr/bin/env python
# -*- coding: utf-8 -*-

###参考：http://www.cnblogs.com/rhcad/archive/2011/12/21/2295507.html

#一：最简单的函数，准备附加额外功能
#def myfunc():
#    print("myfunc() called")

#myfunc()
#myfunc()

#二：使用装饰函数在函数执行前和执行后分别附加额外功能

#def deco(func):
#    print("Before myfunc() called")
#    func()
#    print("After myfunc() called")
#    return func

#myfunc = deco(myfunc)
#
#myfunc()
#myfunc()

#三：使用语法糖@来装饰函数

#@deco
#def myfunc():
#    print("myfunc() called")
#
#myfunc()
#myfunc()

#四：使用内嵌包装函数来确保每次新函数都被调用

#def deco(func):
#    def _deco():
#        print("Before myfunc() called")
#        func()
#        print("After myfunc() called")
#    return _deco


#@deco
#def myfunc():
#    print("myfunc() called")

#myfunc()
#myfunc()

#五：对带参数的函数进行装饰

#def deco(func):
#    def _deco(a,b):
#        print("Before myfunc() called")
#        ret = func(a,b)
#        print("After myfunc() called.result: %s" % ret)
#        return ret
#    return _deco
#
#@deco
#def myfunc(a,b):
#    print("myfunc(%s,%s) called" % (a,b))
#
#myfunc(1,2)
#myfunc(3,4)
#六：对参数数量不确定的函数进行装饰

#def deco(func):
#    def _deco(*args,**kwargs):
#        print("Before %s called" % func.__name__)
#        ret = func(*args,**kwargs)
#        print("After %s called.result: %s" % (func.__name__,ret))
#        return ret
#    return _deco

#@deco
#def myfunc(a,b):
#    print("myfunc(%s,%s) called." % (a,b))
#    return a+b

#@deco
#def myfunc2(a,b,c):
#    print("myfunc2(%s,%s,%s) called." % (a,b,c))
#    return a+b+c

#myfunc(1,2)
#myfunc(3,4)
#
#myfunc2(1,2,3)
#myfunc2(4,5,6)

#七： 让装饰器带参数

#def deco(arg):
#    def _deco(func):
#        def _deco():
#            print("Before %s called [%s]." % (func.__name__,arg))
#            func()
#            print("After %s called [%s]." % (func.__name__,arg))
#        return _deco
#    return _deco
#
#@deco("mymodule")
#def myfunc():
#    print("myfunc() called.")
#
#@deco("module2")
#def myfunc2():
#    print("myfunc2() called")
#
#myfunc()
#myfunc2()

#八：让装饰器带 类 参数

#class locker:
#    def __init__(self):
#        print("locker.__init__() should be not called")
#
#    @staticmethod
#    def acquire():
#        print("locker.acquire() called.(这是静态方法)")
#
#    @staticmethod
#    def release():
#        print("locker.release() called.(不需要对象实例)")
#
#    
#def deco(cls):
#    def _deco(func):
#        def _deco():
#            print("Before %s called [%s]." % (func.__name__,cls))
#            cls.acquire()
#            try:
#                return func()
#            finally:
#                cls.release()
#        return _deco
#    return _deco
#
#@deco(locker)
#def myfunc():
#    print("myfunc() called.")
#
#myfunc()
#myfunc()

#九： 装饰器带类参数，并分拆公共类到其他py文件中，同时演示了对一个函数应用多个装饰器

#'''mylocker.py: 公共类 for 示例9.py'''
#class mylocker:
#    def __init__(self):
#        print("mylocker.__init__() called.")
#         
#    @staticmethod
#    def acquire():
#        print("mylocker.acquire() called.")
#         
#    @staticmethod
#    def unlock():
#        print("  mylocker.unlock() called.")
# 
#class lockerex(mylocker):
#    @staticmethod
#    def acquire():
#        print("lockerex.acquire() called.")
#         
#    @staticmethod
#    def unlock():
#        print("  lockerex.unlock() called.")
# 
#def lockhelper(cls):
#    '''cls 必须实现acquire和release静态方法'''
#    def _deco(func):
#        def __deco(*args, **kwargs):
#            print("before %s called." % func.__name__)
#            cls.acquire()
#            try:
#                return func(*args, **kwargs)
#            finally:
#                cls.unlock()
#        return __deco
#    return _deco
#
#'''示例9: 装饰器带类参数，并分拆公共类到其他py文件中
#同时演示了对一个函数应用多个装饰器'''
#from mylocker import *
# 
#class example:
#    @lockhelper(mylocker)
#    def myfunc(self):
#        print(" myfunc() called.")
# 
#    @lockhelper(mylocker)
#    @lockhelper(lockerex)
#    def myfunc2(self, a, b):
#        print(" myfunc2() called.")
#        return a + b
# 
#if __name__=="__main__":
#    a = example()
#    a.myfunc()
#    print(a.myfunc())
#    print(a.myfunc2(1, 2))
#    print(a.myfunc2(3, 4))
