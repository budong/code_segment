#!/usr/local/python2.7/bin/python2.7

from gevent.pool import Pool

class SocketPool(object):

    def __init__(self):
        self.pool = Pool(100)
        self.pool.start()

    def listen(self,socket):
        while True:
            socket.recv()

    def add_hander(self,socket):
        if self.pool.full():
            raise Exception("A maximum pool size")
        else:
            self.pool.spawn(self.listen,socket)

    def shutdown(self):
        self.pool.kill()




