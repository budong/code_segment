#!/usr/bin/env python2.7
#coding: utf-8

import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost',6666))
sock.listen(5)
while True:
    connection,address = sock.accept()
    try:
        buf = connection.recv(1024)
        if buf=='show&131045249':
            connection.send('1.1.1.1/a.html,2.2.2.2/b.html')
    except socket.timeout:
        print 'time out' 
    connection.close() 
