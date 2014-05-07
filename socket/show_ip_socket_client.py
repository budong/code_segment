#!/usr/bin/env python2.7
#coding: utf-8

import socket
import urlparse
import httplib

def parse_url(url):
    url_tuple = urlparse.urlsplit(url)
    netloc = url_tuple.netloc
    if url_tuple.query:
        request_uri = ''.join([url_tuple.path,'?',url_tuple.query])
    else:
        request_uri = url_tuple.path
    return (netloc,request_uri)

def get_http_data_and_status(netloc,request_uri):
    try:
        conn = httplib.HTTPConnection(netloc)
        conn.request("GET",request_uri)
        r = conn.getresponse()
        status = r.status
        data = r.read()
    except (httplib.HTTPException, socket.error),e:
        print "Error: %s" % e
    finally:
        conn.close()
    return (status,data)

def socket_data():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect(("localhost",6666))
    s.sendto("show&131045249",("localhost",6666))
    resp,addr = s.recvfrom(1024)
    return resp

netloc,request_uri = parse_url('http://localhost:8000/gs?vid=131045249&status=221.236.31.41')
s,d = get_http_data_and_status(netloc,request_uri)
r = socket_data()
print d,r
