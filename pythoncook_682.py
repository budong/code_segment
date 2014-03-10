#!/usr/bin/env python2.7
#coding: utf-8

#def cross_loop(*sequences):
#    if sequences:
#        for x in sequences[0]:
#            for y in cross_loop(sequences[1:]):
#                yield (x,) + y
#        else:
#            yield ()
#
#g =  cross_loop(['a','b'],['c','d'])
#for x in g:
#    print x
#def cross_list(*sequences):
#    result = [[]]
#    for seq in sequences:
#        result = [sublist+[item] for sublist in result for item in seq]
#    return map(tuple,result)
#
#print cross_list(['a','b'],['c','d'])

def cross(*sequences):
    wheels = map(iter,sequences)
    digits = [it.next() for it in wheels]
    while True:
        yield tuple(digits)
        for i in range(len(digits) - 1,-1,-1):
            try:
                digits[i] = wheels[i].next()
                break
            except StopIteration:
                wheels[i] = iter(sequences[i])
                digits[i] = wheels[i].next()
        else:
            break

for x,y,z in  cross(['a','b'],['c','d','e'],['f','g']):
    print x,y,z
