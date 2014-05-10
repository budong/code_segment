#!/usr/bin/env python

import socket

HOST = ['www.mumayi.com:80','www.baidu.com:80'] 
#HOST = ['127.0.0.1:5004']

def _check_strategy(host,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((host,port))
    except socket.error:
        print "Connect failed"
        return False
    message = "GET / HTTP/1.1\r\n\r\n"
    try:
        s.sendall(message)
    except socket.error:
        print "Send failed"
        return False
    reply = s.recv(1024)
    #if reply != 'OK':
    #    return False
    s.close()
    return True

def update_strategy():
    for item in HOST:
        #print item
        host_port = item.split(':')
        host = host_port[0]
        port = int(host_port[1])
        if _check_strategy(host,port):
            continue
        return False
    return True

if __name__ =='__main__':
    print update_strategy()
