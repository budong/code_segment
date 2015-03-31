#!/usr/bin/env python2.7
#coding: utf-8

import socket
import httplib
from xml.etree import ElementTree as ET 

IP = [
        '1.1.1.1',
        ]

with open('ip.txt','r') as fh:
    for line in fh:
        line = line.strip('\n')
        IP.append(line)

def get_response(host,url,method="GET"):
    try:
        conn = httplib.HTTPConnection(host)
        conn.request(method,url)
        r = conn.getresponse()
        data = r.read()
    except (httplib.HTTPException, socket.error),e:
        print "Error: %s %s" % (host,e) 
        return False
    finally:
        conn.close()
    return data

def check_xml(data):
    root = ET.fromstring(data)
    find = root.find('allow-http-request-headers-from')
    if find is None:
        return False
    return True

def main():
    for ip in IP:
        data = get_response(ip,'/crossdomain.xml')
        if data:
            if not check_xml(data):
                print 'http://%s/crossdomain.xml not ok' % ip

if __name__ == '__main__':
    main()
