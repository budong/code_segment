#!/usr/bin/env python2.7
#coding: utf-8

import os
import multiprocessing
import hashlib
import itertools

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

#def consumer(input_q):
#    while True:
#        item = input_q.get()
#        #处理项目
#        print (item)
#        #发出信号通知任务完成
#        input_q.task_done()
#
#def producer(sequence,output_q):
#    for item in sequence:
#        #将项目放入队列
#        output_q.put(item)
#
##建立进程
#if __name__ == '__main__':
#    q = multiprocessing.JoinableQueue()
#    #运行使用者进程
#    cons_p1 = multiprocessing.Process(target=consumer,args=(q,))
#    cons_p1.daemon = True
#    cons_p1.start()
#
#    cons_p2 = multiprocessing.Process(target=consumer,args=(q,))
#    cons_p2.daemon = True
#    cons_p2.start()
#
#    #生产项目中。sequence代表要发送给使用者的项目序列
#    #在实践中，这可能是生成器的输出或者通过一些其他方式生产出来
#    def s():
#        sequence = [1,2,3,4]
#        for i in sequence:
#            time.sleep(10)
#            yield i
#    producer(s(),q)
#
#    #等待所有项目被处理
#    q.join()



#def consumer(input_q):
#    while True:
#        item = input_q.get()
#        if item is None:
#            break
#        #处理项目
#        print (item)
#        #关闭
#        print ("Consumer done")
#
#def producer(sequence,output_q):
#    for item in sequence:
#        #把项目放入队列
#        output_q.put(item)
#
#if __name__ == '__main__':
#    q = multiprocessing.Queue()
#    #启动使用者进程
#    cons_q = multiprocessing.Process(target=consumer,args=(q,))
#    cons_q.start()
#
#    #生产项目
#    sequence = [1,2,3,4]
#    producer(sequence,q)
#
#    #在队列上安置标志
#    q.put(None)
#    #等待使用者关闭
#    cons_q.join()


##管道
#import multiprocessing
#
#def consumer(pipe):
#    output_p,input_p = pipe
#    input_p.close()
#    while True:
#        try:
#            item = output_p.recv()
#        except EOFError:
#            break
#        #处理项目
#        print (item)
#    #关闭
#    print ("Consumer done")
#
##生产项目并将其放置到队列上，sequence是代表要处理的可迭代对象
#def producer(sequence,input_p):
#    for item in sequence:
#        #将项目放在队列上
#        input_p.send(item)
#
#if __name__ == '__main__':
#    (output_p,input_p) = multiprocessing.Pipe()
#    #启动使用者进程
#    cons_p = multiprocessing.Process(target=consumer,args=((output_p,input_p),))
#    cons_p.start()
#
#    #关闭生产者中的管道
#    output_p.close()
#
#    #生产项目
#    sequence = [1,2,3,4]
#    producer(sequence,input_p)
#
#    #关闭输入管道，表示完成
#    input_p.close()
#
#    #等待使用者进程关闭
#    cons_p.join()

#def adder(pipe):
#    server_p,client_p = pipe
#    client_p.close()
#    while True:
#        try:
#            x,y = server_p.recv()
#        except EOFError:
#            break
#        result = x + y
#        server_p.send(result)
#    #关闭
#    print("Server done")
#
#if __name__ == '__main__':
#    (server_p,client_p) = multiprocessing.Pipe()
#    #启动服务器进程
#    adder_p = multiprocessing.Process(target=adder,args=((server_p,client_p),))
#    adder_p.start()
#
#    #关闭客户端中的服务器管道
#    server_p.close()
#
#    #在服务器上提出一些请求
#    client_p.send((3,4))
#    print (client_p.recv())
#
#    client_p.send(('Hello','World'))
#    print (client_p.recv())
#
#    #完成。关闭管道
#    client_p.close()
#
#    #等待消费者进程关闭
#    adder_p.join()
#

#BUFSIZE = 8192
#POOLSIZE = 4
#
#def compute_digest(filename):
#    try:
#        f = open(filename,"rb")
#    except IOError:
#        return None
#    digest = hashlib.sha512()
#    while True:
#        chunk = f.read(BUFSIZE)
#        if not chunk: break
#        digest.update(chunk)
#    f.close()
#    return filename,digest.digest()
#
#def md5Checksum(filePath):
#    with open(filePath, 'rb') as fh:
#        m = hashlib.md5()
#        while True:
#            data = fh.read(8192)
#            if not data:
#                break
#            m.update(data)
#        return filePath,m.hexdigest()
#
#def build_digest_map(topdir):
#    digest_pool = multiprocessing.Pool(POOLSIZE)
#    allfiles = (os.path.join(path,name) for path,dirs,files in os.walk(topdir) for name in files)
#    #digest_map = dict(digest_pool.imap_unordered(compute_digest,allfiles,20))
#    digest_map = dict(digest_pool.imap_unordered(md5Checksum,allfiles,20))
#    digest_pool.close()
#    return digest_map
#
#def build_md5_map(topdir):
#    allfiles = (os.path.join(path,name) for path,dirs,files in os.walk(topdir) for name in files)
#    md5_map = map(md5Checksum,allfiles)
#    return md5_map
#    
#
#if __name__ == '__main__':
#    start_time = time.time()
#    digest_map = build_digest_map("/Users/budong/my_workspace/")
#    end_time = time.time()
#    print digest_map
#    #print (len(digest_map)),(end_time - start_time)
#
#    
#    #start_time = time.time()
#    #md5_map = build_md5_map("/usr")
#    #end_time = time.time()
#    #print len(md5_map),(end_time - start_time)

#
#class FloatChannel(object):
#    def __init__(self,maxsize):
#        self.buffer = multiprocessing.RawArray('d',maxsize)
#        self.buffer_len = multiprocessing.Value('i')
#        self.empty = multiprocessing.Semaphore(1)
#        self.full = multiprocessing.Semaphore(0)
#
#    def send(self,values):
#        self.empty.acquire() #只在缓存为空时继续
#        nitems = len(values)
#        self.buffer_len = nitems #设置缓冲区大小
#        self.buffer[:nitems] = values #将值复制到缓冲区
#        self.full.release() #发送信号通知缓冲区已满
#
#    def recv(self):
#        self.full.acquire() #只在缓冲区已满时继续
#        values = self.buffer[:self.buffer_len.value] #复制值
#        self.empty.release() #发信号通知缓冲区为空
#        return values
#
##性能测试。接收多条消息
#def consume_test(count,ch):
#    for i in xrange(count):
#        values = ch.recv()
#        print type(values)
#
##性能测试。发送多条消息
#def produce_test(count,values,ch):
#    for i in xrange(count):
#        ch.send(values)
#
#if __name__ == '__main__':
#    ch = FloatChannel(100000)
#    p = multiprocessing.Process(target=consume_test,args=(1000,ch))
#    p.start()
#
#    values = [float(x) for x in xrange(100000)]
#    produce_test(1000,values,ch)
#    print ('Done')
#    p.join()
#


def watch(d,evt):
    while True:
        evt.wait()
        print (d)
        evt.clear()

if __name__ == '__main__':
    m = multiprocessing.Manager()
    d = m.dict() #Create a shared dict
    evt = m.Event() #Create a shared Event

    #启动监视字典的进程
    p = multiprocessing.Process(target=watch,args=(d,evt))
    p.daemon = True
    p.start()

    #更新字典并通知监视者
    d['foo'] = 42
    evt.set()
    time.sleep(5)

    #更新字典并通知监视者
    d['bar'] = 37
    evt.set()
    time.sleep(5)

    #终止进程和管理器
    p.terminate()
    m.shutdown()

