#!/usr/bin/env python2.7
#coding: utf-8

import socket
port = 8081
host = "localhost"
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.sendto("Holy Guido!It's working.",(host,port))
