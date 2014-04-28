#!/usr/bin/env python
#coding: utf-8

import sqlite3

#连接数据库文件
#如果数据库文件不存在，就新建一个，如果存在则打开此文件
conn = sqlite3.connect('/tmp/budong.db')

#获取游标
curs = conn.cursor()

'''
#创建表格
curs.execute("create table stocks (date text, trans text, symbol text,  qty real, price real)")

#插入数据
curs.execute("insert into stocks values('2006-01-15','BUoY','RHATd',100,35.14)")

#将变动保存到数据库文件，如果没有执行此语句，则前面的insert 语句操作不会被保存
conn.commit()
'''

#得到所有的记录
curs.execute("select * from stocks")
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names,row):
        print '%s: %s' % pair
    print

#r = curs.execute("select * from stocks")
#print r.fetchall()

#关闭连接
conn.close()
