#!/usr/local/python2.7/bin/python2.7
#http://www.libaoyin.com/2013/08/06/pyhton-staticmethod-classmethod/

class Kls(object):
    def __init__(self,data):
        self.data = data

    def printd(self):
        print(self.data)

ik1 = Kls('arun')
ik2 = Kls('seema')

ik1.printd()
ik2.printd()

