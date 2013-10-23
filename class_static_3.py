#!/usr/local/python2.7/bin/python2.7

def iget_no_of_instance(ins_obj):
    return ins_obj.__class__.no_list

class Kls(object):
    no_list = 0
    
    def __init__(self):
        Kls.no_list = Kls.no_list + 1

ik1 = Kls()
ik2 = Kls()
ik3 = Kls()
print iget_no_of_instance(ik1)
