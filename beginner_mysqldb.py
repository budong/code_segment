#!/usr/bin/env python2.7
#coding: utf-8

import MySQLdb

connection = MySQLdb.connect(host='localhost',user='root',passwd='mumayi',db='android')
cursor = connection.cursor()

#list the tables in demo
sql = "show tables;"


#execute the sql
cursor.execute(sql)
response = cursor.fetchall()

loop through the response and print table names
for row in response:
    print row
