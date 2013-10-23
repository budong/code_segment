#!/usr/local/python2.7/bin/python2.7

class Kls(object):
    def __init__(self,data):
        self.data = data


    def printd(self):
        print(self.data)

    @staticmethod
    def smethod(*arg):
        print('Static:',arg)

    @classmethod
    def cmethod(*arg):
        print('Class:',arg)


ik = Kls(23)
ik.printd()
ik.smethod()
ik.cmethod()
