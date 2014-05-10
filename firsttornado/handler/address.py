#!/usr/bin/env python
#coding: utf-8

import urlparse
import tornado.web
from base import *

class QueryCdnHandler(BaseHandler):
    '''查询cdn调度结果'''
    def parse_url(self,url):
        url_tuple = urlparse.urlsplit(url)
        netloc = url_tuple.netloc
        if url_tuple.query:
            request_uri = ''.join([url_tuple.path,'?',url_tuple.query])
        else:
            request_uri = url_tuple.path
        return (netloc,request_uri)

    def get_http_data_and_status(self,netloc,request_uri):
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

    def query_sp_region_name(self,sp_id,region_id):
        sp = self.db.get("SELECT `sp_name` FROM `CDN_sp` WHERE `sp_id`=%s" % int(sp_id))
        region = self.db.get("SELECT `region_name` FROM `CDN_region` WHERE `region_id`=%s" % int(region_id))
        return (sp['sp_name'],region['region_name'])

    def query_cdn(self,vid,ip,port=6666):
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((ip,port))
        s.sendto("show&%s" % vid,(ip,port))
        resp,addr = s.recvfrom(1024)
        s.close()
        return resp

    @tornado.web.authenticated
    def get(self):
        self.render('querycdn.html',error='')

    @tornado.web.authenticated
    def post(self):
        fields = ['vid','ip']
        values = {}
        for key in fields:
            values[key] = self.get_argument(key,None)
        url = ''.join(['http://180.149.139.89:8080/master/gs?vid=',values['vid'],'&status=',values['ip']])
        if values['vid'] and values['ip']:
            netloc,request_uri = self.parse_url(url)
            status,data = self.get_http_data_and_status(netloc,request_uri)
            data_list = data.split("|")
            sp_name,region_name = self.query_sp_region_name(data_list[0],data_list[1])
            resp = self.query_cdn(vid=values['vid'],ip=data_list[2])
            resp_list = resp.splitlines()
            #self.write(json.dumps(resp))
            self.render('querycdnresult.html',results=resp_list,sp_name=sp_name,region_name=region_name,client_ip=data_list[2])
        else:
            self.render('querycdn.html',error="你输入的信息有误，请重新输入")
