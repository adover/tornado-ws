#!/usr/bin/env python3
from tornado import websocket, web, ioloop
from tornado.options import define, options

define('port', default=8888, help='run on the given port', type=int)

cl = []

class Application(web.Application):
    """
    :param web.Application: 
    """
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/ws', SocketHandler),
            (r'/(favico.ico)', web.StaticFileHandler, {'path': '../'})
        ]

        settings = dict(debug=True)
        web.Application.__init__(self, handlers, **settings)

class IndexHandler(web.RequestHandler):
    """
    :param web.RequestHandler: 
    """
    def get(self):
        self.render('index.html')

class SocketHandler(websocket.WebSocketHandler):
    """
    :param websocket.WebSocketHandler: 
    """
    def check_origin(self, origin):
        return True 
    
    def open(self):
        if self not in cl:
            cl.append(self)
    
    def close(self):
        if self in cl:
            cl.remove(self)

def main():
    options.parse_command_line()
    app = Application()
    app.listen(options.port)
    ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()