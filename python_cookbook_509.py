#!/usr/bin/env python2.7
#coding: utf-8

import urlparse
import httplib

def httpExists(url):
    host,path = urlparse.urlsplit(url)[1:3]
    if ':' in host:
        #指定了端口，试图使用它
        host,port = host.split(":",1)
        try:
            port = int(port)
        except ValueError:
            print 'invalid port number %r' % (port,)
            return False
    else:
        port = None
    try:
        connection = httplib.HTTPConnection(host,port=port)
        connection.request("HEAD",path)
        resp = connection.getresponse()
        if resp.status == 200:
            found = True
        elif resp.status == 302:
            print url,resp.getheader('location','')
            found = httpExists(urlparse.urljoin(url,resp.getheader('location','')))
        else:
            print "Status %d %s : %s" % (resp.status,resp.reason,url)
    except Exception,e:
        print e.__class__,e,url
        found = False
    return found

def _test():
    import doctest,httpExists
    return doctest.testmod(httpExists)

if __name__ == "__main__":
    #_test()
    print httpExists('http://www.baidu.com/a.html') 
    print httpExists('http://www.mumayi.com/1.html') 
    print httpExists('http://127.0.0.1/1.html') 



