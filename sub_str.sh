#!/bin/bash
#截取字符串
#资料：http://zhangwei20086.blog.163.com/blog/static/23055718201222945133958/

var="1234567890"
#echo ${var:3:2}

sub=`expr substr "$var" 1 2`
#echo $sub

#echo $var|cut -c 1-2

