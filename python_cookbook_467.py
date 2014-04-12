#!/usr/bin/env python2.7
#coding: utf-8

import socket,ftplib

def isFTPSiteUp(site):
    try:
        ftplib.FTP(site).quit()
    except socket.error:
        return False
    else:
        return True

def filterFTPsites(sites):
    return [site for site in sites if isFTPSiteUp(site)]

f = filterFTPsites(['120.192.81.163','120.192.81.167','120.192.81.1'])
print f
