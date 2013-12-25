1.字符串对齐
In [1]: print '|','hej'.ljust(20),'|','hej'.rjust(20),'|','hej'.center(20),'|'
| hej                  |                  hej |         hej          |

In [3]: print 'hej'.center(20,'+')
++++++++hej+++++++++

2.map
In [10]: mystr='abc'

In [11]: map(ord,mystr)
Out[11]: [97, 98, 99]

3.ord,chr,str
In [12]: print ord('a')
97

In [13]: print chr(97)
a

In [15]: print str(97)
97
