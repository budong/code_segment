#!/usr/bin/env python2.7
#coding: utf-8

import socket
port = 8081
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#从给定的端口，从任何发送者，接收UDP数据报
s.bind(("",port))
print "Waiting on port:",port
while True:
    #接收一个数据报(最大到1024个字节）
    data,addr = s.recvfrom(1024)
    print "Received:",data,"from",addr
