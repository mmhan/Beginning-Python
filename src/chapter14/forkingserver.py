from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler

class Server(ForkingMixIn, TCPServer):
    '''
    Looks like forking is not supported in windows.
    '''
    pass

class Handler(StreamRequestHandler):
    def handle(self):
        addr =self.request.getpeername()
        print "Got connection from", addr
        self.wfile.write("Thank you for connecting")
        
server = Server(('', 1234), Handler)
server.serve_forever()