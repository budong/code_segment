#!/usr/bin/env python2.7
#coding: utf-8

import smtplib
from email.Message import Message 

fromaddr = 'peiqiang.lee@gmail.com'
toaddr = 'lipeiqiang@mumayi.com'

#msg = "test\ntest"

msg = Message()
msg['Subject'] = 'subject'
msg['From'] = fromaddr
msg['To'] = toaddr
msg.set_payload('mail content')
msg =  msg.as_string()

username = 'peiqiang.lee@gmail.com'
password = 'password'

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr,toaddr,msg)
server.quit()
