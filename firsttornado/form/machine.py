#!/usr/bin/env python
# coding=utf-8

from wtforms import TextField, validators
from lib.forms import Form

class MachineEditForm(Form):
    host = TextField('host',[validators.Required(),validators.IPAddress(message = "公网IP:无效的IP地址")])
    max_bandwidth = TextField('max_bandwidth',[validators.Required(),validators.Regexp("^[0-9]*$",message ="服务器最大带宽:必须是数字")])
    use_bandwidth = TextField('use_bandwidth',[validators.Required(),validators.Regexp("^[0-9]*$",message ="服务器使用带宽:必须是数字")])
    total_disk = TextField('total_disk',[validators.Required(),validators.Regexp("^[0-9]*$",message ="服务器最大磁盘:必须是数字")])
    use_disk = TextField('use_disk',[validators.Required(),validators.Regexp("^[0-9]*$",message ="服务器使用磁盘:必须是数字")])
    save_disk = TextField('save_disk',[validators.Required(),validators.Regexp("^[0-9]*$",message ="服务器固化磁盘:必须是数字")])
