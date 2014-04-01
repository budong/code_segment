#!/usr/bin/env python2.7
#coding: utf-8

import multiprocessing
import time

#进程

#def clock(interval):
#    while True:
#        print ("The time is %s" % time.ctime())
#        time.sleep(interval)
#
#if __name__ == '__main__':
#    p = multiprocessing.Process(target=clock,args=(15,))
#    p.start()

#class ClockProcess(multiprocessing.Process):
#    def __init__(self,interval):
#        multiprocessing.Process.__init__(self)
#        self.interval = interval
#
#    def run(self):
#        while True:
#            print ("The time is %s" % time.ctime())
#            time.sleep(self.interval)
#
#if __name__ == '__main__':
#    p = ClockProcess(10)
#    p.start()

#进程间通信

def consumer(input_q):
    while True:
        item = input_q.get()
        #处理项目
        print (item)
        #发出信号通知任务完成
        input_q.task_done()

def producer(sequence,output_q):
    for item in sequence:
        #将项目放入队列
        output_q.put(item)

#建立进程
if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()
    #运行使用者进程
    cons_p = multiprocessing.Process(target=consumer,args=(q,))
    cons_p.daemon = True
    cons_p.start()

    #生产项目中。sequence代表要发送给使用者的项目序列
    #在实践中，这可能是生成器的输出或者通过一些其他方式生产出来
    sequence = [1,2,3,4]
    producer(sequence,q)

    #等待所有项目被处理
    q.join()

