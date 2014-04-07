#!/usr/bin/env python2.7
#coding: utf-8

import time
import threading
import string
from Queue import Queue
#from queue import Queue

#def worker():
#    print "worker"
#    time.sleep(1)
#    return True

#if __name__ == '__main__':
#    for i in xrange(5):
#        worker()

#for i in xrange(5):
#    t = threading.Thread(target=worker)
#    t.start()
#
#print "Current has %d threads" % (threading.activeCount() - 1)

#threads = []
#for i in xrange(5):
#    t = threading.Thread(target=worker)
#    threads.append(t)
#    t.start
#
#for item in threading.enumerate():
#    print item
#
#print
#
#for item in threads:
#    print item


#t = threading.Thread(target=worker)
#t.setDaemon(True)
#t.start()
#print "Haha"

#def thread_main(a):
#    global count,mutex
#    #获得线程名
#    threadname = threading.currentThread().getName()
#    for x in xrange(0,int(a)):
#        #取得锁
#        mutex.acquire()
#        count = count + 1
#        #释放锁
#        mutex.release()
#        print threadname,x,count
#        #time.sleep(1)
#
#def main(num):
#    global count,mutex
#    threads = []
#
#    count = 1
#    #创建一个锁
#    mutex = threading.Lock()
#    #先创建线程对象
#    for x in range(0,num):
#        threads.append(threading.Thread(target=thread_main,args=(10,)))
#    #启动所有线程
#    for t in threads:
#        t.start()
#    #主线程中等待所有子线程退出
#    for t in threads:
#        t.join()
#
#if __name__ == '__main__':
#    num = 4
#    #创建4个线程
#    main(4)
#

#class Test(threading.Thread):
#    def __init__(self,num):
#        threading.Thread.__init__(self)
#        self._run_num = num
#
#    def run(self):
#        global count,mutex
#        threadname = threading.currentThread().getName()
#
#        for x in xrange(0,int(self._run_num)):
#            mutex.acquire()
#            count = count + 1
#            mutex.release()
#            print threadname,x,count,'\n'
#            #time.sleep(1)
#
#if __name__ == '__main__':
#    global count,mutex
#    threads = []
#    num = 4
#    count = 3
#    #创建锁
#    mutex = threading.Lock()
#    #创建线程对象
#    for x in range(0,num):
#        threads.append(Test(10))
#    #启动线程
#    for t in threads:
#        t.start()
#    #等待子线程结束
#    for t in threads:
#        t.join()
#
#    #print t.join.__doc__
#    #print 'end'
#    print 'count:',count


#def doWaiting():
#    print 'start waiting:',time.strftime('%H:%M:%S')
#    time.sleep(3)
#    print 'stop waitting:',time.strftime('%H:%M:%S')
#
#thread1 = threading.Thread(target=doWaiting)
#thread1.start()
#time.sleep(1)
#print 'start join'
#thread1.join()
#print 'end join'


#def clock(interval):
#    while True:
#        print ("The time is %s" % time.ctime())
#        time.sleep(interval)
#
#if __name__ == '__main__':
#    threads = []
#    for x in xrange(0,4):
#        threads.append(threading.Thread(target=clock,args=(3,)))
#    for t in threads:
#        t.start()
#    for t in threads:
#        t.join()
#

#class ClockThread(threading.Thread):
#    def __init__(self,interval):
#        threading.Thread.__init__(self)
#        self.daemon = True
#        self.interval = interval
#
#    def run(self):
#        while True:
#            print ("The time is %s" % time.ctime())
#            time.sleep(self.interval)
#
#if __name__ == '__main__':
#    threads = []
#    for x in xrange(0,3):
#        threads.append(ClockThread(3))
#    for t in threads:
#        t.start()
#    for t in threads:
#        t.join()

class WorkerThread(threading.Thread):
    def __init__(self,*args,**kwargs):
        threading.Thread.__init__(self,*args,**kwargs)
        self.input_queue = Queue()
    def send(self,item):
        self.input_queue.put(item)
    def close(self):
        self.input_queue.put(None)
        self.input_queue.join()
    def run(self):
        while True:
            item = self.input_queue.get()
            if item is None:
                break
            print (item)
            self.input_queue.task_done()
        self.input_queue.task_done()
        return

if __name__ == '__main__':
    w = WorkerThread()
    w.start()
    w.send("hello")
    w.send("world")
    w.close()


