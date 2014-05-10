#!/usr/bin/env python
#coding: utf-8

import tornado.web
from base import *

class LoginHandler(BaseHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        getusername = self.get_argument("username")
        getpassword = self.get_argument("password")
        cdn_users = self.db.get("SELECT `name`, `password` FROM `CDN_users` WHERE `name`='%s'" % getusername)
        if cdn_users is not None:
            if cdn_users['name'] == getusername and cdn_users['password'] == getpassword:
                self.set_secure_cookie("user", self.get_argument("username"))
                self.redirect("/")
            else:
                self.redirect("/login")
        else:
            self.redirect("/login")

class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user")
        self.redirect(self.get_argument("next", "/"))
