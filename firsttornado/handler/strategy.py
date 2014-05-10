#!/usr/bin/env python
#coding: utf-8

import tornado.web
from base import *
from lib.sinasocket import update_strategy

import json
import re

def do_strategy(strategy):
    cdn_strategy = []
    for i in range(len(strategy)):
        item = strategy[i]
        key = ''.join(['keys[',str(i),']'])
        key_name = ''.join(['vals[',str(i),'][name]']) 
        key_weight = ''.join(['vals[',str(i),'][weight]'])
        length = len(item[key_weight])
        region_id,sp_id = tuple(item[key][0].split(','))
        name = ','.join(item[key_name][0:length])
        weight = ','.join(item[key_weight][0:length])
        cdn_strategy.append((name,weight,sp_id,region_id))
    return cdn_strategy

class StrategyIndexHandler(BaseHandler):
    '''调度策略CDN_strategy首页'''
    @tornado.web.authenticated
    def get(self):
        cdn_strategy = self.db.query("select CDN_sp.sp_id,CDN_sp.sp_name,CDN_region.region_id,CDN_region.region_name,CDN_strategy.idc_list,CDN_strategy.weight from CDN_strategy inner join CDN_sp on CDN_strategy.sp=CDN_sp.sp_id inner join CDN_region  on CDN_strategy.region=CDN_region.region_id")

        cdn_idc = self.db.query("SELECT *  FROM `CDN_idc`")
        idc_dict = {}
        for item in cdn_idc:
            idc_dict[str(item.idc_id)] = item.idc_name

        for item in cdn_strategy:
            idc_list_id = item['idc_list'].split(',')
            idc_list_name = [idc_dict.get(i,'-') for i in idc_list_id]
            weight_list = item['weight'].split(',')
            idc_weight = zip(idc_list_name,weight_list)
            item['idc_weight'] = idc_weight

        self.render("strategy.html",cdn_strategy=cdn_strategy)

class StrategyQueryHandler(BaseHandler):
    '''CDN_strategy,根据ISP和REGION的id，显示相应页面'''
    @tornado.web.authenticated
    def get(self):
        cdn_region = self.db.query("SELECT * FROM `CDN_region`")
        cdn_sp = self.db.query("SELECT * FROM `CDN_sp`")
        self.render("strategy-query.html",cdn_region=cdn_region,cdn_sp=cdn_sp)

    @tornado.web.authenticated
    def post(self):
        sp_id = self.get_argument('sp_id')
        region_id = self.get_argument('region_id')
        self.redirect(''.join(["/strategy/edit/",str(region_id),"/",str(sp_id)]))

class StrategyEditHandler(BaseHandler):
    '''CDN_strategy,修改idc_list'''
    @tornado.web.authenticated
    def get(self,region_id,sp_id):
        if sp_id == 'all' and region_id == 'all':
            cdn_strategy = self.db.query("select CDN_sp.sp_id,CDN_sp.sp_name,CDN_region.region_id,CDN_region.region_name,CDN_strategy.idc_list,CDN_strategy.weight from CDN_strategy inner join CDN_sp on CDN_strategy.sp=CDN_sp.sp_id inner join CDN_region  on CDN_strategy.region=CDN_region.region_id")
        elif sp_id == 'all' and region_id !='all':
            cdn_strategy = self.db.query("select CDN_sp.sp_id,CDN_sp.sp_name,CDN_region.region_id,CDN_region.region_name,CDN_strategy.idc_list,CDN_strategy.weight from CDN_strategy inner join CDN_sp on CDN_strategy.sp=CDN_sp.sp_id inner join CDN_region  on CDN_strategy.region=CDN_region.region_id where CDN_strategy.region=%s" % int(region_id))
        elif sp_id != 'all' and region_id == 'all':
            cdn_strategy = self.db.query("select CDN_sp.sp_id,CDN_sp.sp_name,CDN_region.region_id,CDN_region.region_name,CDN_strategy.idc_list,CDN_strategy.weight from CDN_strategy inner join CDN_sp on CDN_strategy.sp=CDN_sp.sp_id inner join CDN_region  on CDN_strategy.region=CDN_region.region_id where CDN_strategy.sp=%s" % int(sp_id))
        elif sp_id != 'all' and region_id != 'all':
            cdn_strategy = self.db.query("select CDN_sp.sp_id,CDN_sp.sp_name,CDN_region.region_id,CDN_region.region_name,CDN_strategy.idc_list,CDN_strategy.weight from CDN_strategy inner join CDN_sp on CDN_strategy.sp=CDN_sp.sp_id inner join CDN_region  on CDN_strategy.region=CDN_region.region_id where CDN_strategy.sp=%s and CDN_strategy.region=%s" % (int(sp_id),int(region_id)))

        cdn_idc = self.db.query("SELECT *  FROM `CDN_idc`")
        idc_dict = {}
        for item in cdn_idc:
            idc_dict[str(item.idc_id)] = item.idc_name

        for item in cdn_strategy:
            idc_list_id = item['idc_list'].split(',')
            idc_list_name = [idc_dict.get(i,'-') for i in idc_list_id]
            weight_list = item['weight'].split(',')
            idc_weight = zip(idc_list_name,weight_list)
            config_index = len(idc_weight) + 1
            item['idc_weight'] = idc_weight
            item['config_index'] = config_index

        config_index = [i['config_index'] for  i in cdn_strategy]
        self.render("strategy-edit.html",cdn_strategy=cdn_strategy,config_index=config_index,cdn_idc=cdn_idc)

    @tornado.web.authenticated
    def post(self,region_id,sp_id):
        user_post_data = self.request.arguments
        #self.write(user_post_data)
        #将相同的调度分为一组
        length = int(user_post_data['length'][0])
        strategy = []
        for i in range(length):
            strategy_dic = {}
            key = ''.join(['keys[',str(i),']'])
            key_name = ''.join(['vals[',str(i),'][name]'])
            key_weight = ''.join(['vals[',str(i),'][weight]'])
            strategy_dic[key] = user_post_data[key]
            strategy_dic[key_name] = user_post_data[key_name]
            strategy_dic[key_weight] = user_post_data[key_weight]
            strategy.append(strategy_dic)

        #pattern = re.compile(r'([\d+])')
        #strategy = []
        #for i in range(length):
        #    strategy_dic = {}
        #    for k,v in user_post_data.iteritems():
        #        index = pattern.search(k)
        #        if index:
        #            if index.group() == str(i):
        #                strategy_dic[k] = v
        #    strategy.append(strategy_dic)

        #self.write(json.dumps(strategy))
        cdn_strategy = do_strategy(strategy) 
        for strategy in cdn_strategy:
            self.db.execute("UPDATE `CDN_strategy` SET `idc_list`=%s,`weight`=%s  where sp=%s and region=%s",strategy[0],strategy[1],strategy[2],strategy[3])
        if update_strategy():
            self.redirect(''.join(["/strategy/edit/",region_id,"/",sp_id]))
        else:
            self.write('未能更新策略，请重新提交')


class StrategyDeleteHandler(BaseHandler):
    '''CDN_strategy,根据ISP和REGION的id，删除一条调度策略'''
    @tornado.web.authenticated
    def get(self,region_id,sp_id):
        cdn_strategy = self.db.get("select CDN_sp.sp_id,CDN_sp.sp_name,CDN_region.region_id,CDN_region.region_name,CDN_strategy.idc_list,CDN_strategy.weight from CDN_strategy inner join CDN_sp on CDN_strategy.sp=CDN_sp.sp_id inner join CDN_region  on CDN_strategy.region=CDN_region.region_id where CDN_strategy.sp=%s and CDN_strategy.region=%s" % (int(sp_id),int(region_id)))

        cdn_idc = self.db.query("SELECT *  FROM `CDN_idc`")
        idc_dict = {}
        for item in cdn_idc:
            idc_dict[str(item.idc_id)] = item.idc_name

        idc_list_id = cdn_strategy['idc_list'].split(',')
        idc_list_name = [idc_dict.get(i,'-') for i in idc_list_id]
        weight_list = cdn_strategy['weight'].split(',')
        idc_weight = zip(idc_list_name,weight_list)
        cdn_strategy['idc_weight'] = idc_weight

        self.render("strategy-delete.html",cdn_strategy=cdn_strategy)

    @tornado.web.authenticated
    def post(self,region_id,sp_id):
        value = self.get_argument('delstrategy')
        if value == "yes":
            self.db.execute("DELETE FROM `CDN_strategy` WHERE `region`=%s and `sp`=%s" % (int(region_id),int(sp_id)))
        if update_strategy():
            self.redirect("/")
        else:
            self.write('未能更新策略，请重新提交')

class StrategyAddHandler(BaseHandler):
    '''CDN_strategy,增加一条调度'''
    @tornado.web.authenticated
    def get(self):
        cdn_region = self.db.query("SELECT * FROM `CDN_region`")
        cdn_sp = self.db.query("SELECT * FROM `CDN_sp`")
        cdn_idc = self.db.query("SELECT * FROM `CDN_idc`")
        self.render("strategy-add.html",cdn_region=cdn_region,cdn_sp=cdn_sp,cdn_idc=cdn_idc)

    @tornado.web.authenticated
    def post(self):
        #self.write(self.request.arguments)
        region_id = self.get_argument('region_id')
        sp_id = self.get_argument('sp_id')
        name = self.get_arguments('vals[0][name]')
        weight = self.get_arguments('vals[0][weight]')
        length = len(weight)
        idc_list = ','.join(name[0:length])
        weight = ','.join(weight)
        self.write(json.dumps(idc_list) + json.dumps(weight))
        self.db.execute("INSERT INTO `CDN_strategy`(`sp`, `region`, `idc_list`, `weight`) VALUES (%s,%s,'%s','%s')" % (int(sp_id),int(region_id),idc_list,weight)) 
        if update_strategy():
            self.redirect(''.join(["/strategy/edit/",str(region_id),"/",str(sp_id)]))
        else:
            self.write('未能更新策略，请重新提交')
