#!/usr/bin/env python
#coding: utf-8

import os.path
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import unicodedata

import handler.user
import handler.strategy
import handler.idc
import handler.machine
import handler.address

from tornado.options import define, options

#Development
define("port", default=8888, help="run on the given port", type=int)
define("mysql_host", default="127.0.0.1:3306", help="database host")
define("mysql_database", default="cdndb_1", help="database name")
define("mysql_user", default="root", help="database user")
define("mysql_password", default="budong", help="database password")

#Production
#define("port", default=8888, help="run on the given port", type=int)
#define("mysql_host", default="172.16.139.89:3302", help="database host")
#define("mysql_database", default="cdndb_1", help="database name")
#define("mysql_user", default="cdn", help="database user")
#define("mysql_password", default="cdn", help="database password")

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r'/login',handler.user.LoginHandler),
            (r'/logout',handler.user.LogoutHandler),
            (r"/", handler.strategy.StrategyIndexHandler),
            (r"/strategy/query",handler.strategy.StrategyQueryHandler),
            (r"/strategy/edit/(\w+)/(\w+)", handler.strategy.StrategyEditHandler),
            (r"/strategy/delete/(\d+)/(\d+)", handler.strategy.StrategyDeleteHandler),
            (r"/strategy/add", handler.strategy.StrategyAddHandler),
            (r"/idc", handler.idc.IdcIndexHandler),
            (r"/idc/([0-9]+)", handler.idc.IdcDetailHandler),
            (r"/idc/add", handler.idc.IdcAddHandler),
            (r"/idc/edit/([0-9]+)", handler.idc.IdcEditHandler),
            (r"/idc/delete/([0-9]+)", handler.idc.IdcDeleteHandler),
            (r"/machine", handler.machine.MachineIndexHandler),
            (r"/machine/add", handler.machine.MachineAddHandler),
            (r"/machine/edit/([0-9]+)", handler.machine.MachineEditHandler),
            (r"/machine/delete/([0-9]+)", handler.machine.MachineDeleteHandler),
            (r"/querycdn", handler.address.QueryCdnHandler),
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            login_url="/login",
            debug=True,
        )
        tornado.web.Application.__init__(self, handlers, **settings)

        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host=options.mysql_host, database=options.mysql_database,
            user=options.mysql_user, password=options.mysql_password)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    #http_server.listen(options.port,address='172.16.139.87')
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
