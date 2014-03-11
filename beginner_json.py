#!/usr/bin/env python2.7
#coding: utf-8


import json
import urllib2

#url = 'http://xmlso.mumayi.com/v16/indexnew.php'
#data = json.load(urllib2.urlopen(url))
#print data

data = [ { 'Hola':'Hello', 'Hoi':"Hello", 'noun':"hello" } ]
print data

json_encoded = json.dumps(data)
print json_encoded

decode_data = json.loads(json_encoded)
print decode_data

decode_data[0]['name'] = 'budong'
print decode_data
print json.dumps(decode_data)
