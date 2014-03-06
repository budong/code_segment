#!/usr/local/python2.7/bin/python2.7
#coding: utf-8

import collections

#print collections.Counter(['a','b','c','a','b','b'])
#print collections.Counter({'a':2,'b':3,'c':1})
#print collections.Counter(a=2,b=3,c=1)

#c = collections.Counter()
#print 'initial:',c
#
#c.update('abcdaab')
#print 'Sequence:',c
#
#c.update({'a':1,'d':5})
#print 'Dict:',c
#
#for letter in 'abcde':
#    print '%s: %d' % (letter,c[letter])

#c = collections.Counter('extremely')
#c['z'] = 0
#print c
#print list(c.elements())

#c = collections.Counter()
#with open("/usr/share/dict/words","r") as fh:
#    for line in fh:
#        c.update(line.rstrip().lower())
#
#print "Most common:"
#for letter,count in c.most_common(3):
#    print "%s: %7d" % (letter,count)

#c1 = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
#c2 = collections.Counter('alphabet')
#
#print "C1:",c1
#print "C2:",c2
#
#print "\nCombined counts:"
#print c1 + c2
#
#print "\nSubstraction:"
#print c1 - c2
#
#print "\nIntersection (taking positive minimums):"
#print c1 & c2
#
#print "\nUnion (taking maximums):"
#print c1 | c2
#

cnt = collections.Counter()
for word in  ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt['word'] += 1

print cnt

print collections.Counter({'blue': 3, 'red': 2, 'green': 1})

