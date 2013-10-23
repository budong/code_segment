#!/usr/local/python2.7/bin/python2.7

class Kls(object):
    no_list = 0
    
    def __init__(self):
        Kls.no_list = Kls.no_list + 1

    @classmethod
    def get_no_of_instance(cls_obj):
        return cls_obj.no_list

ik1 = Kls()
ik2 = Kls()

print ik1.get_no_of_instance()
print ik2.get_no_of_instance()
