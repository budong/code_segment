#!/usr/bin/env python2.7
#coding: utf-8

import smtplib

fromaddr = 'peiqiang.lee@gmail.com'
toaddr = 'lipeiqiang@mumayi.com'

msg = "This is a test"

username = 'peiqiang.lee@gmail.com'
password = 'lipeiqiang38145'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr,toaddr,msg)
server.quit()
