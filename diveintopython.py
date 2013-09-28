1.这个列表解析比较好玩，做个标记
params={"server":"mpilgrim","database":"master","uid":"sa","pwd":"secret"}
";".join(["%s=%s" % (k, v) for k, v in params.items()])

2.查看python的搜索路径
import sys
sys.path
sys.path.append('/home/')

3.list方法，以前没注意
li = ['a','b','c']
li.extend(['d','e','f'])

li = ['a','b','c']
li.append(['d','e','f'])

li = [1,2,3,4]
li = [elem*2 for elem in li]

[mapping-expression for element in source-list if filter-expression]
li = ["a", "mpilgrim", "foo", "b", "c", "b", "d", "d"]
[elem for elem in li if len(elem) > 1]  
[elem for elem in li if elem != "b"]         
[elem for elem in li if li.count(elem) == 1]

map

4.访问内置变量
from __builtin__ import *

5.
callable(object) 判断一个对象是否可调用
getattr(object,method) 得到一个函数的引用

import statsout
def output(data,format="text")
    output_function = getattr(statsout,"output_%s" % format,statsout.output_text)
    return output_function(data)

6.and or 的比较返回值
>>> 'a' and 'b'         
'b'
>>> 'a' or 'b'          
'a'


>>> a = ""
>>> b = "second"
>>> (1 and [a] or [b])[0] 
''

7.lambda
>>> g = lambda x: x*2  
>>> g(3)


8.显示调用父类__init__
class FileInfo(UserDict):
    "store file metadata"
    def __init__(self, filename=None):
        UserDict.__init__(self)        
        self["name"] = filename  


9.有些意思，逗号分隔
os.path.splitext('/root/src/T-Shirt.mp3')[1].upper()[1:]
'MP3'

10.python 私有函数
如果一个 Python 函数，类方法，或属性的名字以两个下划线开始（但不是结束），它是私有的；其它所有的都是公有的。
__setitem__  前后都是两个下划线，是专用方法

11.os目录路径相加
import os
os.path.join("c:\\music\\ap\\", "mahadeva.mp3") 

os.path.split('/root/code_segment/diveintopython.py')
('/root/code_segment', 'diveintopython.py')

(filepath,filename) = os.path.split('/root/code_segment/diveintopython.py')
(shortname,extension) = os.path.splitext(filename)

[f for f in os.listdir(dirname) if os.path.isfile(os.path.join(dirname,f))]
[f for f in os.listdir(dirname) if os.path.isdir(os.path.join(dirname,f))]

import glob
glob.glob('c:\\music\\_singles\\*.mp3')

12.爬虫下载网页
import urllib
sock = urllib.urlopen("url")
htmlsource = sock.read()
sock.close()
print htmlsource

13.命名空间
locals()
globals()
