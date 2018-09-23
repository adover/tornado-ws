from tornado import websocket, web, ioloop
import json

define('port', default=8888, help='run on the given port', type=int)

cl = []

class Application(web.Application):
    def __init__(self):
        handlers = [
            (r'/', IndexHandler),
            (r'/ws', SocketHandler),
            (r'/(favico.ico)', web.StaticFileHandler, {path: '../'})
        ]

        settings = dict(debug=True)
        web.Application.__init__(self, handlers, **settings)

class IndexHandler(web.RequestHandler):
    def get(self):
        self.render(index.html)

class SocketHandler(websocket.WebsocketHandler):
    def check_origin(self, origin):
        return true 
    
    def open(self):
        if self not in cl:
            cl.append(self)
    
    def close(self):
        if self in cl:
            cl.remove(self)

def main():
    tornado.options.parse_command_line()
    app.listen(options.port)
    ioloop.IOLoop.instance().start()

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/(favico.ico)', web.StaticFileHandler, {path: '../'})
])

if __name__ == '__main__':
    main()