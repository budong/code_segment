#!/usr/local/python2.7/bin/python2.7

def get_no_of_instances(cls_obj):
    return cls_obj.no_list

class Kls(object):
    no_list = 0
    
    def __init__(self):
        Kls.no_list = Kls.no_list + 1

ik1 = Kls()
ik2 = Kls()
ik3 = Kls()
print(get_no_of_instances(Kls))
