#!/usr/bin/env python
# -*- utf-8 -*-

#This is a example of mysqldb

import sys
import time
import MySQLdb 
reload(sys)
sys.setdefaultencoding('utf-8')

class OperateMysql(object):
    def create(self):
        try:
            conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',port=3306)
            cursor = conn.cursor()
            cursor.execute('create database if not exists blog')
            conn.select_db('blog')
            cursor.execute('create table Blog(id int,user_id varchar(100),title varchar(100),create_time int)')
            values = [
                (1,'user_1','title-1',time.mktime(time.strptime('2013-02-04 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (2,'user_1','title-2',time.mktime(time.strptime('2013-02-05 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (3,'user_1','title-3',time.mktime(time.strptime('2013-02-06 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (4,'user_1','title-4',time.mktime(time.strptime('2013-02-07 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (5,'user_1','title-5',time.mktime(time.strptime('2013-02-08 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (6,'user_1','title-6',time.mktime(time.strptime('2013-02-09 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (7,'user_2','title-1',time.mktime(time.strptime('2013-02-04 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (8,'user_2','title-2',time.mktime(time.strptime('2013-02-05 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (9,'user_2','title-3',time.mktime(time.strptime('2013-02-06 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (10,'user_2','title-4',time.mktime(time.strptime('2013-02-07 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (11,'user_2','title-5',time.mktime(time.strptime('2013-02-08 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (12,'user_3','title-1',time.mktime(time.strptime('2013-02-04 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (13,'user_3','title-2',time.mktime(time.strptime('2013-02-05 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (14,'user_3','title-3',time.mktime(time.strptime('2013-02-06 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (15,'user_3','title-4',time.mktime(time.strptime('2013-02-07 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (16,'user_4','title-1',time.mktime(time.strptime('2013-02-04 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (17,'user_4','title-2',time.mktime(time.strptime('2013-02-05 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (18,'user_4','title-3',time.mktime(time.strptime('2013-02-06 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (19,'user_5','title-1',time.mktime(time.strptime('2013-02-04 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (20,'user_5','title-2',time.mktime(time.strptime('2013-02-05 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (21,'user_6','title-1',time.mktime(time.strptime('2013-02-09 18:10:00','%Y-%m-%d %H:%M:%S'))),
                (22,'user_7','title-1',time.mktime(time.strptime('2013-02-10 18:10:00','%Y-%m-%d %H:%M:%S')))
                    ]
            cursor.executemany('insert into Blog values(%s,%s,%s,%s)',values)
            conn.commit()
            cursor.close()
            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0],e.args[1])
    def select(self):
        try:
            conn = MySQLdb.connect(host='localhost',user='root',passwd='123456',db='blog',port=3306)
            cursor = conn.cursor()
            count = cursor.execute(\
                    'select user_id from Blog\
                    where year(from_unixtime(create_time))=year(now())\
                    and week(from_unixtime(create_time))=week(now())\
                    group by user_id order by count(title) desc limit 5')
            results = cursor.fetchall()
            for r in results:
                print r
            conn.commit()
            cursor.close()
            conn.close()
        except MySQLdb.Error,e:
            print "Mysql Error %d: %s" % (e.args[0],e.args[1])
if __name__ == '__main__':
    om = OperateMysql()
    om.create()
    om.select()


