#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

class List(object):
    def unique(self,list):
        start = time.time()
        result = []
        for i in list:
            if i not in result:
                result.append(i)
        stop = time.time()
        print 'Used: ' + str(stop - start) + ' 秒'
        return result

    def unique_better(self,list,idfun=None):
        start = time.time()
        if idfun == None:
            def idfun(x): return x
        seen = {}
        result = []
        for item in list:
            marker = idfun(item)
            if marker in seen: continue
            seen[marker] = 1
            result.append(item)
        stop = time.time()
        print 'Used: ' + str(stop - start) + ' 秒'
        return result
if __name__ == '__main__':
    list = List()
    a = ['b','b','d','d','c','c']
    print '不太明白这道题的意思:'
    print '第一种是我自己想到的，第二种是网上找的。'
    print 'One:'
    print list.unique(a)
    print 'Two:'
    print list.unique_better(a)
    print '更多资料：http://www.peterbe.com/plog/uniqifiers-benchmark'
