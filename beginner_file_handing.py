#!/usr/bin/env python2.7
#coding: utf-8

filename = '/tmp/budong.txt'

#fh = open(filename,'r')
#for line in fh:
#    print line

#print fh.read()
#while True:
#    if not fh.readline():
#        break
#    print fh.readline()

#print fh.readlines()

#fh = open("/tmp/hello.txt","w")
#fh.write("I am budong\n")
#fh.close()


#line_of_text = ["a line of text\n","another line of text\n","a third line\n"]
#fh.writelines(line_of_text)
#fh.close()


fh = open("/tmp/hello.txt","a")
fh.write("Hello World again")
fh.close()



