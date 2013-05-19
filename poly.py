#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""什么是多态"""

class Person(object):
    def __init__(self,age):
        self.age = age
    def dream(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Boy(Person):
    def dream(self):
        return '我想当个科学家，发明很多很多东西...'

class Student(Person):
    def dream(self):
        return '我要好好学习，考上一个好大学...'

class Adult(Person):
    def dream(self):
        return '我想做一份自己喜欢的工作，敲敲代码就是一件幸福的事...'

if __name__ == '__main__':
    boy = Boy('boy')
    student = Student('student')
    adult = Adult('adult')

    print '什么是多态，首先让我想到的是：'
    print "1 + 1 = 2" + "\n" + "'a' + 'b' = 'ab'" + '\n'

    print '然后我再到stackoverflow一打听,原来多态也可以是这样:'
    print ''
    print "当我还是个小"+ boy.age + "时，'梦想'："
    print boy.dream() 
    print '' 
    print "当我还是个" + student.age + "时,'梦想':"
    print student.dream()
    print ''
    print "当我成为一个" + adult.age + "时，'梦想':"
    print adult.dream()

    print ''
    print "我想 '多态' 也就是随时可以拥有 '梦想' 吧..."
    print '参考资料：'
    print 'http://en.wikipedia.org/wiki/Polymorphism_in_object-oriented_programming'
    print 'http://stackoverflow.com/questions/2835793/how-does-polymorphism-work-in-python'
    print 'http://stackoverflow.com/questions/3724110/practical-example-of-polymorphism'
    
