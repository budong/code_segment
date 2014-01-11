#!/usr/bin/env python2.7

import os,itertools

def all_equal(elements):
    first_element = elements[0]
    for other_element in elements[1:]:
        if other_element != first_element: return False
    return True

def common_prefix(*sequences):
    if not sequences: return [],[]
    common = []
    for elements in itertools.izip(*sequences):
        if not all_equal(elements): break
        common.append(elements[0])
    return common,[ sequence[len(common):] for sequence in sequences]

def relpath(p1,p2,sep=os.path.sep,pardir=os.path.pardir):
    common,(u1,u2) = common_prefix(p1.split(sep),p2.split(sep))
    if not common:
        return p2
    return sep.join([pardir]*len(u1) + u2)

def test(p1,p2,sep=os.path.sep):
    print "from",p1,"to",p2,"->",relpath(p1,p2,sep)

if __name__ == '__main__':
    #test('/home/www','/data/peiqiang/test','/')
    #test('/home/www','/home/www/test','/')
    test('/home/www/test','/home/www','/')
    #test('/home/www','/home/www','/')
