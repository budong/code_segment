#!/usr/bin/env python2.7 

import sys
import socket

#HOST = "www.mumayi.com"
#PORT = 80
#
##create an AF_INET, STREAM socket (TCP)
#try:
#    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#except socket.error,msg:
#    print "Failed to create socket.Error code: " + str(msg[0]) + ' ,Error message: ' + msg[1]
#    sys.exit(1)
#
#try:
#    remote_ip = socket.gethostbyname(HOST)
#except socket.gaierror:
#    print "Hostname could not be resolved,Exiting"
#    sys.exit(1)
#
##connect to remote server 
#s.connect((HOST,PORT))
#
##send some data to remote server
#message = "GET / HTTP/1.1\r\n\r\n"
#
#try:
#    s.sendall(message)
#except socket.error:
#    print "Send failed"
#    sys.exit(1)
#
##receive data
#reply = s.recv(4096)
#
#print reply
#
#
#s.close()


HOST = "127.0.0.1"
PORT = 5004

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
    s.bind((HOST,PORT))
except socket.error,msg:
    print 'Bind faild.Error Code : ' + str(msg[0]) + 'Message ' + msg[1]
    sys.exit(1)
s.listen(10)

conn,addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1])
while 1:
    data = conn.recv(1024)
    reply = 'OK' + data
    if not data:
        break
    conn.sendall(reply)

conn.close()
s.close()

#while 1:
#    conn,addr = s.accept()
#    print 'Connected with ' + addr[0] + ':' + str(addr[1])
#    data = conn.recv(1024)
#    reply = 'OK' + data
#    if not data:
#        break
#    conn.sendall(reply)
#
#conn.close()
#s.close()
