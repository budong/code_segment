#!/usr/bin/env python
#coding: utf-8

import tornado.web
from base import *

import json

class IdcIndexHandler(BaseHandler):
    '''CDN_idc首页，显示所有idc简要信息'''
    @tornado.web.authenticated
    def get(self):
        total = {}
        cdn_idc = self.db.query("select CDN_idc.idc_id,CDN_idc.idc_name,CDN_idc.domain,CDN_idc.max_bandwidth as idc_max_bandwidth,sum(total_disk) as idc_total_disk,sum(use_disk) as idc_use_disk,sum(save_disk) as idc_save_disk,sum(CDN_machine.max_bandwidth) as machine_max_bandwidth,sum(use_bandwidth) as machine_use_bandwidth from CDN_idc left join CDN_machine on CDN_idc.idc_id=CDN_machine.idc_id group by idc_name")
        for idc in cdn_idc:
            if idc['idc_max_bandwidth'] is not None:
                total['idc_max_bandwidth'] = total.setdefault('idc_max_bandwidth',0) + idc['idc_max_bandwidth']
            if idc['idc_save_disk'] is not None:
                total['idc_save_disk'] = total.setdefault('idc_save_disk',0) + idc['idc_save_disk']
            if idc['idc_total_disk'] is not None:
                total['idc_total_disk'] = total.setdefault('idc_total_disk',0) + idc['idc_total_disk']
            if idc['idc_use_disk'] is not None:
                total['idc_use_disk'] = total.setdefault('idc_use_disk',0) + idc['idc_use_disk']
            if idc['machine_max_bandwidth'] is not None:
                total['machine_max_bandwidth'] = total.setdefault('machine_max_bandwidth',0) + idc['machine_max_bandwidth']
            if idc['machine_use_bandwidth'] is not None:
                total['machine_use_bandwidth'] = total.setdefault('machine_use_bandwidth',0) + idc['machine_use_bandwidth']
        self.render('idc.html',cdn_idc=cdn_idc,total=total)

class IdcDetailHandler(BaseHandler):
    '''CDN_idc，显示idc详细信息,如包含哪些服务器'''
    @tornado.web.authenticated
    def get(self,idc_id):
        idc_machine = self.db.query("SELECT machine_id,CDN_machine.idc_id,host,total_disk,use_disk,save_disk,CDN_machine.max_bandwidth,use_bandwidth,idc_name FROM `CDN_machine` inner join `CDN_idc` on CDN_machine.idc_id=CDN_idc.idc_id where CDN_machine.idc_id=%s" % int(idc_id))
        self.render('idc-machine.html',idc_machine=idc_machine)

class IdcAddHandler(BaseHandler):
    '''CDN_idc，增加一个idc'''
    @tornado.web.authenticated
    def get(self):
        self.render('idc-add.html')

    @tornado.web.authenticated
    def post(self):
        args = ['idc_name','idc_bw','domain']
        values = {}
        for key in args:
            values[key] = self.get_argument(key,None)
        self.db.execute("INSERT INTO `CDN_idc`(`idc_name`, `max_bandwidth`,`domain`) VALUES ('%s',%s,'%s')" % (values['idc_name'],int(values['idc_bw']),values['domain']))
        self.redirect("/idc")

class IdcEditHandler(BaseHandler):
    '''CDN_idc，编辑idc信息'''
    @tornado.web.authenticated
    def get(self,idc_id):
        cdn_idc = self.db.get("SELECT * FROM `CDN_idc` WHERE `idc_id`=%s" % int(idc_id))
        self.render('idc-edit.html',cdn_idc=cdn_idc)

    @tornado.web.authenticated
    def post(self,idc_id):
        args = ['idc_name','idc_bw','domain']
        values = {}
        for key in args:
            values[key] = self.get_argument(key,None)
        self.db.execute("UPDATE `CDN_idc` SET `max_bandwidth`=%s,`domain`='%s' WHERE `idc_name`='%s'" % (int(values['idc_bw']),values['domain'],values['idc_name']))
        self.redirect(''.join(["/idc/edit/",idc_id]))

class IdcDeleteHandler(BaseHandler):
    '''CDN_idc，删除idc信息
    同时删除这个idc下的服务器信息'''
    @tornado.web.authenticated
    def get(self,idc_id):
        cdn_idc = self.db.get("SELECT * FROM `CDN_idc` WHERE `idc_id`=%s" % int(idc_id))
        self.render('idc-delete.html',cdn_idc=cdn_idc)

    @tornado.web.authenticated
    def post(self,idc_id):
        value = self.get_argument("delidc")
        if value == "yes":
            self.db.execute("DELETE FROM `CDN_idc` WHERE `idc_id`=%s" % int(idc_id))
            self.db.execute("DELETE FROM `CDN_machine` WHERE `idc_id`=%s" % int(idc_id))
        self.redirect("/idc")
