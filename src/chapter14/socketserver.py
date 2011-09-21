from SocketServer import TCPServer, StreamRequestHandler

class Handler(StreamRequestHandler):
    '''
    Socket server version of simple server from server.py
    '''
    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')
        
server = TCPServer(('', 1234), Handler)
server.serve_forever()