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

2.反转字符串
In [38]: my
Out[38]: 'I am lee'

In [39]: ''.join(reversed(re.split(r'(\s)',my)))
Out[39]: 'lee am I'

In [40]: my[::-1]
Out[40]: 'eel ma I'


3.string.maketrans string.maketrans
In [1]: import string

In [2]: help(string.maketrans)


In [3]: s = 'abcdefg-1234567'

In [4]: table=string.maketrans("","")

In [5]: s.translate(table)
Out[5]: 'abcdefg-1234567'

In [6]: s.translate(table,'abc123')
Out[6]: 'defg-4567'

In [7]: table=string.maketrans('abc','ABC')

In [8]: s.translate(table)
Out[8]: 'ABCdefg-1234567'

In [9]: s.translate(table,'ab123')
Out[9]: 'Cdefg-4567'

