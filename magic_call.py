#!/usr/local/python2.7/bin/python2.7

#http://blog.csdn.net/sasoritattoo/article/details/9422019
#http://www.cnblogs.com/lovemo1314/archive/2011/04/29/2032871.html
#https://pycoders-weekly-chinese.readthedocs.org/en/latest/issue6/a-guide-to-pythons-magic-methods.html

class Animal(object):
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs
        self.stomach = []

    def __call__(self,food):
        self.stomach.append(food)

    def poop(self):
        if len(self.stomach) > 0:
            return self.stomach.pop(0)

    def __str__(self):
        return "A animal named %s" % (self.name)

cow = Animal('king',4)
dog = Animal('flopp',4)
print "we have 2 animales a cow name %s and dog named %s" % (cow.name,dog.name)
print cow

#give food to cow
cow('gras')
print cow.stomach

#give food to dog
dog('bone')
dog('beef')
print dog.stomach

#what comes inn most come out
print cow.poop()
print cow.stomach

print dog.poop()
print dog.stomach
