import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import threading
import concurrent.futures
import hashlib, binascii

from tornado import autoreload
from tornado.options import define, options
from tornado import gen

import settings

define("port", default=1337, help="")
settings.init()

class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[
            (r'/OrgHome', IndexHandler),
            (r'/OrgHome/(.*)', tornado.web.StaticFileHandler, {'path': 'templates'}),
            (r'/OrgHome/css/(.*)', tornado.web.StaticFileHandler, {'path': 'css'})
        ],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True,
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    ioloop = tornado.ioloop.IOLoop().instance()
    autoreload.start(ioloop)
    ioloop.start()
