#!/usr/bin/env python2.7

import smtplib
from email.Message import Message 

mail_server = 'smtp.163.com'
mail_server_port = 25
from_addr = 'sias_peiqiang@163.com'
to_addr = 'lipeiqiang@mumayi.com'


from_header = 'From: %s\r\n' % from_addr
to_header = 'To: %s \r\n ' % to_addr 
subject_header = 'Subject: nothing intersting'

body = 'This is a not-very-intersting email.'
email_message = '%s\n%s%s\n\n%s' % (subject_header,from_header,to_header,body)

msg = Message()
msg['Subject'] = 'subject'
msg['From'] = from_addr
msg['To'] = to_addr
msg.set_payload('mail content')
msg =  msg.as_string()

s = smtplib.SMTP(mail_server,mail_server_port)
s.set_debuglevel(1)
s.starttls()
s.login("sias_peiqiang@163.com","password")
#s.sendmail(from_addr,to_addr,email_message)
s.sendmail(from_addr,to_addr,msg)
s.quit()
