#!/usr/bin/env python2.7
#coding: utf-8

#http://code.google.com/p/pywhois/
#http://www.pythonforbeginners.com/dns/using-pywhois
#pip install python-whois


import whois
data = raw_input("Enter a domain: ")
w = whois.whois(data)
print w

