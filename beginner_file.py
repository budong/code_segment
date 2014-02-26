#!/usr/bin/env python2.7
#coding: utf-8


#fh = open("/tmp/peiqiang.txt","w")
#fh.write("I am peiqiang\n")
#fh.close()

#fh = open("/tmp/peiqiang.txt","r")
#for line in fh:
#    print line
#fh.close()

#fh = open("/tmp/peiqiang.txt","a")
#fh.write("......\n")
#fh.close()

#fh = open("/tmp/peiqiang.txt","r")
#content = fh.read()
#print content

#fh = open("/tmp/peiqiang.txt","r")
#content1 = fh.readline()
#content2 = fh.readline()
#print content1,content2

#fh = open("/tmp/peiqiang.txt","r")
#content = fh.readlines()
#print content

fh = open("/tmp/peiqiang.txt","w")
lines_of_text = ["a line of text\n","another line of text\n","a third line\n"]
fh.writelines(lines_of_text)

