#!/usr/local/python2.7/bin/python2.7
#coding:utf-8

#1.判断一个列表是否为空
a = []
if a:
    print '不为空'
else:
    print '空'

#2.判断一个变量是否存在
#if vars().has_key('s')         #s为变量名

#3.判断一个文件是否存在
#os.path.isfile(path)           #这里的path是全路径

#4.判断一个文件夹是否存在
#os.path.isdir(path)

#结合运用：在python的搜索路径中寻找文件或目录
#for   dirname in sys.path:
#    c=os.path.join(dirname,filename)
#    if os.path.isfile(c): print 'true'
#    if os.path.isdir(c):   print 'is a dir'

#5.open(file)方法
#如果file不带路径，那么默认情况下即为当前路径

