from tornado import websocket, web, ioloop
import json

cl = []

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

app = web.Application([
    (r'/', IndexHandler),
    (r'/ws', SocketHandler),
    (r'/(favico.ico)', web.StaticFileHandler, {path: '../'})
])

if __name__ == '__main__':
    app.listen(8888)
    ioloop.IOLoop.instance().start()