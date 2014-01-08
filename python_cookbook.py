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

判断文件以什么结尾：
In [35]: from itertools import imap

In [36]: def anyTrue(predicate,sequence):
   ....:     return True in imap(predicate,sequence)
   ....: 

In [37]: def endsWith(s,*endings):
   ....:     return anyTrue(s.endswith,endings)
   ....: 

In [38]: import os

In [39]: for filename in os.listdir('.'):
   ....:     if endsWith(filename,'.txt'):
   ....:         print filename
   ....:         
xml.txt
peiqiang.txt



文件迭代对象，这个牛逼：
In [82]: for num,line in enumerate(open('data.txt','r')):
       ....:     print num,line
          ....:     
              0 /2013/04/17/30/309271/jiakaokemuyi_V3.5_mumayi_fd325.apk

              1 /2013/04/09/30/305188/duliangdanweihuansuanqi_V1.0_mumayi_f9d78.apk

              2 /2013/04/17/30/309276/jiakaokemusan_V3.0_mumayi_cce8f.apk

              3 /2013/04/01/30/301439/jinshutanceqi_V1.3.6_mumayi_a95b8.apk

              4 /2013/04/09/30/305188/duliangdanweihuansuanqi_V1.0_mumayi_f9d78.apk

              5 /2013/04/16/30/308441/huanghuatanceqi_V4.4_mumayi_f02b7.apk
