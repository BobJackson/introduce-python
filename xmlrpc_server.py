from xmlrpc.server import SimpleXMLRPCServer


def double(x):
    return x * 2


server = SimpleXMLRPCServer(('localhost', 6789))
server.register_function(double, 'double')
server.serve_forever()
