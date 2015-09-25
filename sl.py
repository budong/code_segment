#!/usr/bin/env python2.7
#coding: utf-8

import os
import httplib
import urlparse
import threading
from xml.etree import ElementTree 

VID_FILE = os.path.join(os.path.dirname(__file__), "vid.txt") 
VID_LIST =[item.rstrip("\n") for item in  open(VID_FILE,"r").readlines()]

THREAD_COUNT = 2
LOOP_COUNT = 2


def get_http_data(url,port='80'):
    url_tuple = urlparse.urlsplit(url)
    domain_name = url_tuple.hostname
    if url_tuple.query != '':
        request_uri = ''.join([url_tuple.path,'?',url_tuple.query])
    else:
        request_uri = url_tuple.path
    try:
        conn = httplib.HTTPConnection(domain_name,port)
        conn.request("GET",request_uri)
        r = conn.getresponse()
        data = r.read()
        conn.close()
    except Exception,e:
        print e
    return data

def parse_xml(data):
    URL_ET = ElementTree.XML(data)
    result = URL_ET.find("result").text
    if result == "suee":
        #url = URL_ET.find("durl").find("url").text
        url = URL_ET.find("durl").findall("url")
        return [u.text for u in url]
    else:
        return []

def check_http_status(url,port='80'):
    url_tuple = urlparse.urlsplit(url)
    domain_name = url_tuple.hostname
    if url_tuple.query != '':
        request_uri = ''.join([url_tuple.path,'?',url_tuple.query])
    else:
        request_uri = url_tuple.path
    try:
        conn = httplib.HTTPConnection(domain_name,port)
        conn.request("GET",request_uri)
        r = conn.getresponse()
        conn.close()
    except Exception,e:
        print e
    print r.status
    if r.status == 200:
        return True
    else:
        return None

def main():
    while True:
        for SERVER_URL in VID_LIST:
            SERVER_URL = ''.join(['http://180.149.139.90/v_play.php?vid=',SERVER_URL])
            data = get_http_data(SERVER_URL)
            url = parse_xml(data)
            if url:
                for u in url:
                   check_http_status(u,'8080')

def loop():
    for i in xrange(LOOP_COUNT):
        main()

    
if __name__ == '__main__':
    threads = []
    for i in xrange(THREAD_COUNT):
        threads.append(threading.Thread(target=loop))
    for t in threads:
        t.start()
    for t in threads:
        t.join()
