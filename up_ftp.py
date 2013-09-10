#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ftplib import FTP 
import os,sys,string,datetime,time  
import socket  

class MY_FTP(object):

    def __init__(self, hostaddr, username, password, remotedir, port=21):
        self.hostaddr = hostaddr  
        self.username = username  
        self.password = password  
        self.remotedir  = remotedir  
        self.port     = port  
        self.ftp      = FTP()  
        self.file_list = []  
        # self.ftp.set_debuglevel(2)  

    def __del__(self):
        self.ftp.close()  
        # self.ftp.set_debuglevel(0)

    def login(self): 
        ftp = self.ftp  
        try:   
            timeout = 60  
            socket.setdefaulttimeout(timeout)  
            ftp.set_pasv(True)  
            print '开始连接到 %s' %(self.hostaddr)  
            ftp.connect(self.hostaddr, self.port)  
            print '成功连接到 %s' %(self.hostaddr)  
            print '开始登录到 %s' %(self.hostaddr)  
            ftp.login(self.username, self.password)  
            print '成功登录到 %s' %(self.hostaddr)  
            debug_print(ftp.getwelcome())  
        except Exception:  
            pass
        try:  
            ftp.cwd(self.remotedir)
        except(Exception):
            pass
        

    def is_same_size(self, localfile, remotefile):
        try:  
            remotefile_size = self.ftp.size(remotefile)  
        except:  
            remotefile_size = -1  
        try:  
            localfile_size = os.path.getsize(localfile)  
        except:  
            localfile_size = -1  
        debug_print('lo:%d  re:%d' %(localfile_size, remotefile_size),)  
        if remotefile_size == localfile_size:  
            return 1  
        else:  
            return 0  

    def upload_file(self, localfile, remotefile):  
        if not os.path.isfile(localfile):  
            return  
        if self.is_same_size(localfile, remotefile):  
            debug_print('跳过[相等]: %s' %localfile)  
            return  
        file_handler = open(localfile, 'rb')  
        self.ftp.storbinary('STOR %s' %remotefile, file_handler)  
        file_handler.close()  
        debug_print('已传送: %s' %localfile)  

    def upload_files(self, localdir='./', remotedir = './'):  
        if not os.path.isdir(localdir):  
            return  
        localnames = os.listdir(localdir)  
        self.ftp.cwd(remotedir)  
        for item in localnames:  
            src = os.path.join(localdir, item)  
            if os.path.isdir(src):  
                try:  
                    self.ftp.mkd(item)  
                except:  
                    debug_print('目录已存在 %s' %item)  
                self.upload_files(src, item)  
            else:  
                self.upload_file(src, item)  
        self.ftp.cwd('..')  
  

def debug_print(s):  
    print (s)  

  
if __name__ == '__main__':  
    hostaddr = '' # ftp地址  
    username = '' # 用户名  
    password = '' # 密码  
    port  =  21   # 端口号   
    rootdir_local  = '/data/logs' # 本地目录  
    rootdir_remote = '/logs'          # 远程目录  
      
    f = MY_FTP(hostaddr, username, password, rootdir_remote, port)  
    f.login()  
    f.upload_files(rootdir_local,rootdir_remote)
      


