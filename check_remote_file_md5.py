#!/usr/local/python2.7/bin/python2.7

import requests

proxies = {"http": "http://120.192.81.163:88"}

r = requests.get("http://apk.mumayi.com/2013/08/01/0/1/mumayidianzishichangMumayiMarket_V1.7.2_mumayi_7a9f5.apk", proxies=proxies)

print r.status_code
