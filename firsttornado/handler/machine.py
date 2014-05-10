#!/usr/bin/env python
#coding: utf-8

import tornado.web
from base import *
from form.machine import *

class MachineIndexHandler(BaseHandler):
    'CDN_machine,所有服务器信息'
    @tornado.web.authenticated
    def get(self):
        cdn_machine = self.db.query("select machine_id,CDN_machine.idc_id,host,total_disk,use_disk,save_disk,CDN_machine.max_bandwidth as machine_max_bandwidth,CDN_machine.use_bandwidth as machine_use_bandwidth,idc_name,CDN_idc.max_bandwidth as idc_max_bandwidth from CDN_machine inner join CDN_idc on CDN_machine.idc_id=CDN_idc.idc_id order by CDN_machine.idc_id asc")
        self.render('machine.html',cdn_machine=cdn_machine)

class MachineAddHandler(BaseHandler):
    'CDN_machine,增加一台服务器'
    @tornado.web.authenticated
    def get(self):
        cdn_idc = self.db.query("SELECT * FROM `CDN_idc`")
        self.render('machine-add.html',cdn_idc=cdn_idc)

    @tornado.web.authenticated
    def post(self):
        args = ['idc_id','host','max_bandwidth','use_bandwidth','total_disk','use_disk','save_disk']
        values = {}
        for key in args:
            values[key] = self.get_argument(key,None)
        machine_id = self.db.execute("INSERT INTO `CDN_machine`(`idc_id`, `host`, `total_disk`, `use_disk`, `save_disk`, `max_bandwidth`, `use_bandwidth`) VALUES (%s,'%s',%s,%s,%s,%s,%s)" % (int(values['idc_id']),values['host'],int(values['total_disk']),int(values['use_disk']),int(values['save_disk']),int(values['max_bandwidth']),int(values['use_bandwidth'])))
        self.redirect(''.join(["/machine/edit/",str(machine_id)]))

class MachineEditHandler(BaseHandler):
    'CDN_machine,编辑服务器信息'
    @tornado.web.authenticated
    def get(self,machine_id,template_variables = {"form": None}):
        cdn_machine = self.db.get("SELECT * FROM `CDN_machine` WHERE `machine_id`=%s" % int(machine_id))
        self.render('machine-edit.html',cdn_machine=cdn_machine,**template_variables)

    @tornado.web.authenticated
    def post(self,machine_id):
        args = ['machine_id','host','max_bandwidth','use_bandwidth','total_disk','use_disk','save_disk']
        values = {}
        for key in args:
            values[key] = self.get_argument(key,None)

        #validate the fields
        form = MachineEditForm(self)

        if not form.validate():
            self.get(machine_id,{"form": form})
            return 
        self.db.execute("UPDATE `CDN_machine` SET `host`='%s',`total_disk`=%s,`use_disk`=%s,`save_disk`=%s,`max_bandwidth`=%s,`use_bandwidth`=%s WHERE `machine_id`=%s" % (values['host'],values['total_disk'],values['use_disk'],values['save_disk'],values['max_bandwidth'],values['use_bandwidth'],int(machine_id)))
        self.redirect(''.join(["/machine/edit/",machine_id]))

class MachineDeleteHandler(BaseHandler):
    'CDN_machine,删除服务器'
    @tornado.web.authenticated
    def get(self,machine_id):
        cdn_machine = self.db.get("SELECT * FROM `CDN_machine` WHERE `machine_id`=%s" % int(machine_id))
        self.render('machine-delete.html',cdn_machine=cdn_machine)

    @tornado.web.authenticated
    def post(self,machine_id):
        value = self.get_argument("delidc")
        idc_id = self.get_argument("idc_id")
        if value == "yes":
            self.db.execute("DELETE FROM `CDN_machine` WHERE `machine_id`=%s" % int(machine_id))
        self.redirect(''.join(["/idc/",idc_id]))
